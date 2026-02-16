#!/usr/bin/env python3
"""
Pre-render Dataview queries to static markdown tables for Quartz.
Runs after rsync, before git commit. Replaces ```dataview blocks
in-place within the Quartz content/ directory (never touches the vault).
"""

import os, re, yaml, sys
from pathlib import Path
from collections import defaultdict

CONTENT_DIR = Path(__file__).parent / "content"
ASSETS_DIR = CONTENT_DIR / "assets"
COMPANIES_DIR = CONTENT_DIR / "companies"

# ── Load all asset metadata ──────────────────────────────────────────

def load_assets():
    assets = []
    for f in sorted(ASSETS_DIR.glob("*.md")):
        if f.name == "TEMPLATE.md":
            continue
        text = f.read_text(errors="replace")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except:
            continue
        meta["_file"] = f.stem
        meta["_filename"] = f.name
        # normalize list fields to strings for display
        for k, v in meta.items():
            if isinstance(v, list):
                meta[k] = ", ".join(str(x) for x in v)
            elif v is None:
                meta[k] = ""
            else:
                meta[k] = str(v)
        assets.append(meta)
    return assets

# ── Dataview query parser & executor ─────────────────────────────────

STAGE_ORDER = {
    "Approved": 0, "NDA Filed": 1, "Phase 3": 2, "Phase 2/3": 3,
    "Phase 2b": 4, "Phase 2": 5, "Phase 1/2": 6, "Phase 1b": 7,
    "Phase 1": 8, "IND-enabling": 9, "Preclinical": 10,
    "Discovery": 11, "Research": 12, "Commercial": 13,
}

def sort_key(val, field="stage"):
    if field == "stage":
        return STAGE_ORDER.get(val, 99)
    return val.lower() if isinstance(val, str) else str(val)

def matches_where(asset, where_clause):
    """Simple evaluator for common Dataview WHERE patterns."""
    if not where_clause:
        return True

    clause = where_clause.strip()

    # Handle AND
    if " AND " in clause:
        parts = clause.split(" AND ")
        return all(matches_where(asset, p.strip()) for p in parts)

    # Handle OR
    if " OR " in clause:
        parts = clause.split(" OR ")
        return any(matches_where(asset, p.strip()) for p in parts)

    # Parenthesized group - strip outer parens
    if clause.startswith("(") and clause.endswith(")"):
        return matches_where(asset, clause[1:-1])

    # field = "value"
    m = re.match(r'(\w+)\s*=\s*"([^"]*)"', clause)
    if m:
        return asset.get(m.group(1), "") == m.group(2)

    # field != "value" / field != null
    m = re.match(r'(\w+)\s*!=\s*"([^"]*)"', clause)
    if m:
        return asset.get(m.group(1), "") != m.group(2)
    m = re.match(r'(\w+)\s*!=\s*null', clause)
    if m:
        return bool(asset.get(m.group(1), ""))

    # contains(field, "value")
    m = re.match(r'contains\((\w+),\s*"([^"]*)"\)', clause)
    if m:
        return m.group(2).lower() in asset.get(m.group(1), "").lower()

    # file.name != "xxx"
    m = re.match(r'file\.name\s*!=\s*"([^"]*)"', clause)
    if m:
        return asset.get("_filename", "") != m.group(1)

    # status = "Active" style already handled above, catch-all
    return True

def parse_query(query_text):
    """Parse a Dataview TABLE query into structured components."""
    lines = query_text.strip().split("\n")

    # Detect TABLE WITHOUT ID vs TABLE
    full = " ".join(l.strip() for l in lines)

    without_id = "TABLE WITHOUT ID" in full

    # Extract columns
    col_match = re.search(
        r"TABLE(?:\s+WITHOUT\s+ID)?\s+(.*?)\s+FROM\s+",
        full, re.IGNORECASE | re.DOTALL
    )
    if not col_match:
        return None

    cols_raw = col_match.group(1)
    columns = []
    # Split columns respecting parentheses nesting
    parts = []
    depth = 0
    current = []
    for ch in cols_raw:
        if ch == '(':
            depth += 1
            current.append(ch)
        elif ch == ')':
            depth -= 1
            current.append(ch)
        elif ch == ',' and depth == 0:
            parts.append(''.join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append(''.join(current).strip())

    for part in parts:
        part = part.strip().rstrip(",")
        if not part:
            continue
        m = re.match(r'(.+?)\s+AS\s+"([^"]+)"', part, re.IGNORECASE)
        if m:
            columns.append((m.group(1).strip(), m.group(2)))
        elif part:
            columns.append((part.strip(), part.strip()))

    # FROM
    from_match = re.search(r'FROM\s+"([^"]+)"', full)
    from_path = from_match.group(1) if from_match else ""

    # WHERE
    where_match = re.search(r"WHERE\s+(.*?)(?:\s+SORT|\s+GROUP|\s*$)", full, re.IGNORECASE)
    where_clause = where_match.group(1).strip() if where_match else ""

    # GROUP BY (parse before SORT since SORT can follow GROUP BY)
    group_match = re.search(r"GROUP\s+BY\s+(\w+)", full, re.IGNORECASE)
    group_by = group_match.group(1) if group_match else None

    # SORT (can appear before or after GROUP BY)
    sort_match = re.search(r"SORT\s+(.*?)$", full, re.IGNORECASE)
    sort_clause = sort_match.group(1).strip() if sort_match else ""
    # Clean trailing GROUP BY if SORT appears before it
    sort_clause = re.sub(r"\s+GROUP\s+BY\s+\w+.*$", "", sort_clause, flags=re.IGNORECASE).strip()

    return {
        "without_id": without_id,
        "columns": columns,
        "from": from_path,
        "where": where_clause,
        "sort": sort_clause,
        "group_by": group_by,
    }

def execute_query(parsed, assets, current_file=""):
    """Execute a parsed query against asset data, return markdown table."""
    if not parsed:
        return None

    # Filter by FROM path
    if "companies" in parsed["from"]:
        return None  # Skip company queries for now

    # Filter by WHERE
    filtered = [a for a in assets if matches_where(a, parsed["where"])]

    # GROUP BY
    if parsed["group_by"]:
        return execute_grouped_query(parsed, filtered)

    # SORT
    if parsed["sort"]:
        sort_parts = parsed["sort"].split(",")
        first_sort = sort_parts[0].strip()
        desc = "DESC" in first_sort.upper()
        field = first_sort.split()[0].strip()

        # Handle confidence_rating sort
        if field == "confidence_rating":
            def conf_key(a):
                c = a.get("confidence_rating", "0/10")
                try:
                    return int(c.split("/")[0])
                except:
                    return 0
            filtered.sort(key=conf_key, reverse=not desc)
        elif field in ("stage",):
            filtered.sort(key=lambda a: sort_key(a.get(field, ""), field), reverse=desc)
        else:
            filtered.sort(key=lambda a: a.get(field, "").lower(), reverse=desc)

        # Secondary sort
        if "choice(stage" in parsed["sort"]:
            filtered.sort(key=lambda a: STAGE_ORDER.get(a.get("stage", ""), 99))

    if not filtered:
        return "*No results*"

    # Build table
    cols = parsed["columns"]
    header_fields = []
    header_names = []

    if not parsed["without_id"]:
        header_fields.insert(0, "_file")
        header_names.insert(0, "File")

    for field, name in cols:
        header_fields.append(field)
        header_names.append(name)

    lines = []
    lines.append("| " + " | ".join(header_names) + " |")
    lines.append("| " + " | ".join("---" for _ in header_names) + " |")

    for a in filtered:
        row = []
        for f in header_fields:
            if f == "_file":
                row.append(f'[[{a["_file"]}]]')
            else:
                val = a.get(f, "")
                # Truncate long values
                if len(val) > 80:
                    val = val[:77] + "..."
                row.append(val.replace("|", "/"))
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)

def execute_grouped_query(parsed, filtered):
    """Handle GROUP BY queries."""
    group_field = parsed["group_by"]
    groups = defaultdict(list)
    for a in filtered:
        key = a.get(group_field, "Unknown")
        groups[key].append(a)

    cols = parsed["columns"]
    lines = []

    # Build header from column definitions
    header_names = []
    for field_expr, name in cols:
        header_names.append(name)

    lines.append("| " + " | ".join(header_names) + " |")
    lines.append("| " + " | ".join("---" for _ in header_names) + " |")

    # Sort groups
    if group_field == "stage" or "choice(stage" in parsed.get("sort", ""):
        sorted_groups = sorted(groups.items(), key=lambda x: STAGE_ORDER.get(x[0], 99))
    elif group_field == "thesis_cluster":
        sorted_groups = sorted(groups.items(), key=lambda x: (-len(x[1]), x[0]))
    else:
        sorted_groups = sorted(groups.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, members in sorted_groups:
        row = []
        for field_expr, name in cols:
            if field_expr.strip() == group_field:
                row.append(key)
            elif "length(rows)" in field_expr:
                row.append(str(len(members)))
            elif "length(filter" in field_expr and "Active" in field_expr:
                active = sum(1 for m in members if m.get("status", "") == "Active")
                row.append(str(active))
            else:
                row.append(key)
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)

# ── Process all files ────────────────────────────────────────────────

def process_file(fpath, assets):
    text = fpath.read_text(errors="replace")

    def replace_block(m):
        query_text = m.group(1).strip()
        parsed = parse_query(query_text)
        if not parsed:
            # Can't parse — leave a comment
            return f"<!-- Dataview query (install Dataview plugin in Obsidian to render) -->\n\n*Static rendering not available for this query.*"

        result = execute_query(parsed, assets, fpath.stem)
        if result is None:
            return f"<!-- Dataview query -->\n\n*View in Obsidian with Dataview plugin for dynamic results.*"
        return result

    new_text = re.sub(r"```dataview\n(.*?)```", replace_block, text, flags=re.DOTALL)

    # Also handle inline dataviewjs
    new_text = re.sub(
        r"`\$=.*?`",
        lambda m: f"`{len(assets)} assets`" if "length" in m.group() else m.group(),
        new_text
    )

    if new_text != text:
        fpath.write_text(new_text)
        return True
    return False

def main():
    print("Loading assets...")
    assets = load_assets()
    print(f"Loaded {len(assets)} assets")

    count = 0
    for fpath in sorted(CONTENT_DIR.rglob("*.md")):
        if process_file(fpath, assets):
            count += 1
            print(f"  Rendered: {fpath.relative_to(CONTENT_DIR)}")

    print(f"\nPre-rendered Dataview in {count} files")

if __name__ == "__main__":
    main()
