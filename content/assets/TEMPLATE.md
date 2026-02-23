# PD Asset Note Template

This document specifies how to create atomic notes for PD therapeutic assets. Follow this exactly for consistency across all ~50 notes in this folder.

---

## Prerequisites

- Obsidian with **Dataview** community plugin installed
- All asset notes live in `pd-pipeline-research/assets/`
- Filenames are kebab-case: `prasinezumab.md`, `aro-snca.md`, `biib122.md`

---

## Frontmatter

Every note starts with this YAML block. All fields are required unless marked optional.

```yaml
---
drug_name: "Prasinezumab"
aliases: ["PRX002", "RO7046015"]          # Other names, codes, identifiers
target: "alpha-synuclein (aggregated, C-terminal)"  # Must be consistent across notes sharing a target
mechanism: "short description of how it works"
modality: "Monoclonal antibody"            # Use consistent values (see Modality Values below)
developer: "Prothena"                      # Originator company
company_type: "biotech"                    # big pharma | biotech | startup | academic
publicly_traded: true                      # true | false
ticker: "PRTA"                             # optional — omit if private
partner: "Roche"                           # optional — omit or leave empty if unpartnered
partner_type: "big pharma"                 # optional — big pharma | biotech | academic | ""
stage: "Phase 3"                           # Use consistent values (see Stage Values below)
status: "Active"                           # Active | Discontinued | Terminated | Deprioritized | Failed
patient_population: "Early PD on stable levodopa"
route_of_administration: "IV (monthly infusion)"  # oral | IV | SC | intrathecal | intracranial | inhaled
key_biomarkers: ["neuromelanin MRI", "DaT-SPECT"]
confidence_rating: "6/10"                  # optional — from our analysis, not published
next_catalyst: "PARAISO Phase 3 readout"
catalyst_date: "2027-2028"
thesis_cluster: "alpha-synuclein"          # Use consistent values (see Cluster Values below)
tags: [pd-pipeline]
date: 2026-02-15
---
```

### Controlled Values

Keep these consistent so Dataview queries work across notes.

**Modality values:**
`small molecule` | `monoclonal antibody` | `bispecific antibody` | `siRNA` | `ASO` | `AAV gene therapy` | `cell therapy (ESC)` | `cell therapy (iPSC autologous)` | `cell therapy (iPSC allogeneic)` | `active vaccine` | `peptide vaccine` | `molecular glue` | `kinase activator` | `kinase inhibitor` | `enzyme activator` | `enzyme inhibitor` | `PET tracer` | `platform` | `AI discovery platform`

**Stage values:**
`Discovery` | `Preclinical` | `IND-enabling` | `Phase 1` | `Phase 1b` | `Phase 1/2` | `Phase 2` | `Phase 2b` | `Phase 2/3` | `Phase 3` | `NDA Filed` | `Approved` | `Terminated` | `Discontinued`

**Thesis cluster values:**
`alpha-synuclein` | `genetic-pd` | `bbb-platform` | `neuroinflammation` | `mitophagy` | `cell-therapy` | `symptomatic` | `ai-discovery` | `diagnostics`

**Company type values:**
`big pharma` | `biotech` | `startup` | `academic` | `cro`

---

## Note Structure

### 1. Summary (required)

2-4 sentences. Lead with the conclusion — what matters most about this asset right now. Reference key trials or data points by name so the reader can jump to the Clinical section. Use [[wikilinks]] when referencing other assets.

**Rules:**
- No filler phrasing ("This is an interesting asset...")
- State the company type parenthetically so it's immediately clear: "Roche (big pharma)", "Prothena (biotech, PRTA)"
- Include the if-positive / if-negative decision tree for the next major readout
- Link to other assets when discussing what happens in success/failure scenarios

### 2. Deal Info (conditional)

**Include ONLY if the asset was part of a discrete deal** (acquisition, licensing, partnership). Omit entirely for internally developed programs, academic assets, or assets only mentioned in passing.

```markdown
## Deal Info

| Field | Value |
|-------|-------|
| Partner | Roche |
| Deal Date | 2013 |
| Upfront | $30M |
| Total (Biobucks) | ~$755M |
| Deal Type | Licensing/co-development |
```

Deal Type values: `Acquisition` | `Licensing/co-development` | `Partnership` | `Option deal` | `Internal`

Do NOT include conviction ratio — it can be derived from upfront/total.

### 3. Notes (required)

Split into four subsections. Each uses bullet points — dense, no filler.

#### 3a. Science
- Mechanism of action explained clearly for someone who isn't a specialist
- Key molecular differentiators vs. other approaches to the same target
- Genetic/biological validation for the target (Mendelian, GWAS, functional)
- What makes this approach distinct — use [[wikilinks]] when comparing to other assets
- Open scientific questions specific to this asset

#### 3b. Clinical
One structured block per trial. Format:

```markdown
**{TRIAL NAME} ({Phase})** | {NCT number} | N={enrollment} | {population}
- **Primary endpoint:** {endpoint} → {result with p-value if available}
- **Key secondary:** {findings}
- **Status:** {Completed | Active | Terminated}
- **Interpretation:** 1-2 sentences on what this result means
```

Rules:
- Include ALL known trials, even Phase 1
- NCT numbers where available; "NCT TBD" for announced-but-not-registered trials
- If no trials exist (preclinical asset), write "No clinical trials initiated" and note any IND-enabling studies or NHP data
- Trial names are standard pharma convention (acronyms) — explain them on first use if the acronym has meaning, otherwise just treat as the trial identifier

#### 3c. Financial
- Deal economics: upfront, milestones earned, milestones remaining
- Peak sales estimates with source attribution
- Stock/market reactions to key events
- Comparison to similar deals in the space
- For private companies: last known valuation, total raised, key investors

#### 3d. Competitive
Start with a **Dataview query** that auto-populates competitors:

~~~markdown
*No results*
~~~

The `{TARGET_STRING}` should match what other notes in the same target class use in their `target:` frontmatter field. It only needs to be a substring — `contains()` handles partial matching. For example, `"alpha-synuclein"` will match `"alpha-synuclein (aggregated, C-terminal)"`.

After the Dataview table, add narrative bullets using [[wikilinks]]:
- Key competitive distinctions by modality or approach
- What happens to this asset if key competitors succeed or fail
- Do NOT make static comparative claims like "the only Phase 3 asset" — let the Dataview table show that dynamically

### 4. Analysis (required)

Narrative section — 2-4 paragraphs. This is where analytical judgment goes.

**Rules:**
- Any estimate we generate (probability of success, market sizing, etc.) MUST be explicitly flagged: **"Analytical estimate — [claim]. This is our assessment, not from a published source. The reasoning: ..."**
- Show the reasoning chain for estimates (base rate → adjustments up → adjustments down → net)
- Do NOT use "for deal sourcers" or "sourcing implications" framing
- DO include signal analysis: what does company behavior tell us? What does deal structure reveal?
- DO include the decision tree: if next readout positive → X; if negative → Y
- Use [[wikilinks]] when referencing implications for other assets

### 5. References (required)

Four subsections. Include ALL sources that support claims in the note.

```markdown
## References

### Clinical Trials
- [{Trial name}](https://clinicaltrials.gov/ct2/show/{NCT}) — {NCT number}

### Key Publications
- [{Title} | {Journal} ({Date})]({URL})

### Press Releases & Filings
- [{Title} ({Date})]({URL})

### Regulatory & Market
- [{Title} | {Source}]({URL})
```

Rules:
- Every factual claim in Notes should be traceable to a reference
- If a reference section is empty (e.g., no clinical trials for a preclinical asset), omit that subsection
- URLs from the source deal analysis files should be carried over — don't drop them
- For assets with thin source material (mentioned in passing in synthesis files), include what's available and note "Limited source material — requires primary research"

---

## Source Files

Each asset note should be built from the relevant deal analysis and/or synthesis file. The source mapping:

| Source file pattern | Contains |
|---|---|
| `*-Deal-Analysis.md` | Deep analysis with URLs, trial data, financials |
| `*-Deep-Dive.md` | Same as above |
| `*-Analysis.md` | Same as above |
| `synthesis-*.md` | Cross-deal patterns, competitor mentions, thinner per-asset data |
| `FINAL-PD-Deal-Landscape-Report.md` | Landscape-level context, competitor mentions |

For assets that were the PRIMARY subject of a deal analysis file, that file is the main source (rich data, many URLs).

For assets only MENTIONED in other analyses or synthesis files, data will be thinner. Extract what's available and flag gaps.

---

## Wikilink Conventions

- Link to other asset notes by their filename (without .md): `[[prasinezumab]]`, `[[aro-snca]]`
- Use display text when the filename isn't reader-friendly: `[[aro-snca|ARO-SNCA]]`, `[[biib122|BIIB122]]`
- Link on first mention in each section, not every mention
- When discussing target classes broadly, link to the most representative asset: `[[pariceract|GBA1 targets]]`, `[[biib122|LRRK2 targets]]`

---

## Example

See `prasinezumab.md` in this folder as the reference implementation.
