# Style, Structure & Linking Audit — deals/ Folder

**Auditor:** style-auditor agent
**Date:** 2026-02-26
**Scope:** All 29 files in `pd-pipeline-research/deals/`
**Method:** Read first 30 lines of every file + grep all wikilinks + glob assets/ and companies/

---

## SUMMARY SCORECARD

| Category | Status | Severity |
|----------|--------|----------|
| Naming convention | 6 files non-standard | MEDIUM |
| YAML frontmatter | 28 of 29 files missing | HIGH |
| LLM preamble artifacts | 15 files have "Now I have..." opener | MEDIUM |
| Wikilinks to assets/ | 0 of 26 deal files link to assets | HIGH |
| Wikilinks to companies/ | 0 of 26 deal files link to companies | HIGH |
| Cross-links with PD-Deal-Summary | All 26 deal files represented; all links resolve | CLEAN |
| Internal structure | Consistent (EXEC SUMMARY → PHASE 1 → ...) | CLEAN |
| Missing asset notes | 3 assets have no note | LOW |
| Missing company notes | 3 companies have no note | LOW |

---

## 1. NAMING CONVENTIONS

**Standard pattern:** `Company-Target-Deal-Analysis.md` (Title-Case, hyphens, Deal-Analysis suffix)

### Files with incorrect naming — rename required:

| Current filename | Problem | Recommended name |
|-----------------|---------|-----------------|
| `Lilly-ABL Bio Deal Analysis.md` | Spaces instead of hyphens | `Lilly-ABL-Bio-Grabody-B-Deal-Analysis.md` |
| `minzasolmin-failure-analysis.md` | Drug-name-first; all-lowercase; "failure-analysis" suffix | `Novartis-UCB-Minzasolmin-Failure-Analysis.md` |
| `deal-analysis-novartis-arrowhead-aro-snca.md` | Prefix-based pattern; all-lowercase | `Novartis-Arrowhead-ARO-SNCA-Deal-Analysis.md` |
| `BIAL-Pariceract-Deep-Dive.md` | "Deep-Dive" suffix instead of "Deal-Analysis" | `BIAL-Pariceract-Deal-Analysis.md` |

### Files missing "Deal-" in suffix (minor, lower priority):

| Current filename | Problem | Recommended name |
|-----------------|---------|-----------------|
| `Bayer-BlueRock-Cell-Therapy-Analysis.md` | Missing "Deal-" | `Bayer-BlueRock-Cell-Therapy-Deal-Analysis.md` |
| `Sumitomo-Raguneprocel-Analysis.md` | Missing "Deal-" | `Sumitomo-Raguneprocel-Deal-Analysis.md` |

### PD-Deal-Summary.md wikilink that needs updating after rename:
- Row 4 links `[[Lilly-ABL Bio Deal Analysis]]` — spaces in wikilink, needs to be updated after rename
- Row 5 links `[[deal-analysis-novartis-arrowhead-aro-snca]]` — needs update after rename

### Files following standard pattern (no action needed):
AbbVie-Cerevel, Biogen-Denali, GSK-ABL-Bio, Merck-Valo, Neurocrine-Voyager-GBA1, AbbVie-Mitokinin, Insilico-Hygtia-NLRP3, Aspen-Neuroscience, AbbVie-Capsida, Biogen-Alectos-GBA2, Lilly-Prevail, Lilly-Ventyx-NLRP3, Biohaven-Highlightll-TYK2, Capsida-Lilly, Roche-Prothena, Neuron23, Kenai-Therapeutics, MeiraGTx-Hologen, GSK-Vesalius, Sanofi-ABL-Bio

---

## 2. YAML FRONTMATTER

**Standard:** Minimum `tags:` and `date:` fields in YAML block.

### Only file WITH valid frontmatter:
- `PD-Deal-Summary.md` ✓ (has `tags: [pd-pipeline, deals, summary]` and `date: 2026-02-23`)

### Files MISSING YAML frontmatter — all 26 deal analysis files + 2 meta files:

**With inline Obsidian tags (partial mitigation, but no YAML):**
- `minzasolmin-failure-analysis.md` — has `#deal-analysis #alpha-synuclein #failure-case` inline
- `deal-analysis-novartis-arrowhead-aro-snca.md` — has `#deal-analysis #alpha-synuclein #RNAi`
- `GSK-ABL-Bio-Deal-Analysis.md` — has `#deal-analysis #parkinson`
- `AbbVie-Mitokinin-Deal-Analysis.md` — has `#deal-analysis #mitochondria #disease-modification`
- `FINAL-PD-Deal-Landscape-Report.md` — has `#meta-synthesis #deal-sourcing #parkinson #final-report`

**With no tags at all (22 files):**
All remaining deal analysis files, plus `FACT-CHECK-AUDIT.md`.

### Recommended frontmatter template for deal files:
```yaml
---
tags: [pd-pipeline, deals, deal-analysis, <thesis-cluster>]
date: 2026-02-14
companies: [<Acquirer>, <Target>]
asset: <drug-name>
cluster: <alpha-synuclein|genetic-pd|bbb-platform|neuroinflammation|mitophagy|cell-therapy|symptomatic|ai-discovery>
deal_value: <$XM upfront / $XB total>
status: <active|terminated|deprioritized>
---
```

---

## 3. LLM PREAMBLE ARTIFACTS

15 deal files open with an LLM process artifact on line 1 that should be deleted. These are internal reasoning traces captured as file content.

### Files with preamble to delete (line 1 contents):

| File | Line 1 text |
|------|------------|
| `AbbVie-Cerevel-Deal-Analysis.md` | "Now I have comprehensive data. Let me compile the deep-dive analysis." |
| `Biogen-Denali-LRRK2-Deal-Analysis.md` | "Now I have gathered comprehensive information. Let me compile..." |
| `Sanofi-ABL-Bio-Deal-Analysis.md` | "Now I have comprehensive information. Let me compile..." |
| `Biogen-Alectos-GBA2-Deal-Analysis.md` | "Now I have comprehensive information. Let me create a detailed..." |
| `Lilly-Prevail-Deal-Analysis.md` | "Now I have comprehensive data. Let me compile the deep-dive research report..." |
| `Lilly-Ventyx-NLRP3-Deal-Analysis.md` | "Perfect. I have comprehensive data from my web searches. Now I'll compile..." |
| `AbbVie-Capsida-Deal-Analysis.md` | "Perfect. Now I have comprehensive data. Let me compile the deep due-diligence analysis..." |
| `Bayer-BlueRock-Cell-Therapy-Analysis.md` | "Now let me compile this comprehensive research into a detailed due-diligence report." |
| `Capsida-Lilly-Deal-Analysis.md` | "Now let me compile this comprehensive research into a structured deep due-diligence report." |
| `Sumitomo-Raguneprocel-Analysis.md` | "Now I have comprehensive data to write the deep due-diligence analysis. Let me create the final report." |
| `Roche-Prothena-Deal-Analysis.md` | "Perfect. Now I have comprehensive information. Let me compile this into a thorough due diligence report..." |
| `Neuron23-Deal-Analysis.md` | "Now I have comprehensive data. Let me compile my deep due diligence analysis." |
| `Kenai-Therapeutics-Deal-Analysis.md` | "Perfect. Now I have comprehensive data. Let me compile a thorough deep-dive analysis..." |
| `MeiraGTx-Hologen-Deal-Analysis.md` | "Perfect. Now I have comprehensive information. Let me compile the deep due-diligence analysis." |
| `GSK-Vesalius-Deal-Analysis.md` | "Now I have comprehensive information to provide a thorough analysis. Let me compile..." |

**Fix:** Delete line 1 (and following blank line 2 if present) from each of these files.

---

## 4. WIKILINKS TO ASSETS/

**Finding: Zero of 26 deal analysis files contain wikilinks to assets/**

All deal files are written as standalone documents using external URLs only. None link to the parallel asset notes in `assets/`.

### Assets that EXIST and should be linked (add to each file's References section):

| Deal File | Add link | Asset file confirmed |
|-----------|----------|---------------------|
| `AbbVie-Cerevel-Deal-Analysis` | `[[tavapadon]]` | `assets/tavapadon.md` ✓ |
| `Biogen-Denali-LRRK2-Deal-Analysis` | `[[biib122]]` | `assets/biib122.md` ✓ |
| `minzasolmin-failure-analysis` | `[[minzasolmin]]` | `assets/minzasolmin.md` ✓ |
| `Roche-Prothena-Deal-Analysis` | `[[prasinezumab]]` | `assets/prasinezumab.md` ✓ |
| `BIAL-Pariceract-Deep-Dive` | `[[pariceract]]` | `assets/pariceract.md` ✓ |
| `Bayer-BlueRock-Cell-Therapy-Analysis` | `[[bemdaneprocel]]` | `assets/bemdaneprocel.md` ✓ |
| `Aspen-Neuroscience-Deal-Analysis` | `[[anpd001]]` | `assets/anpd001.md` ✓ |
| `Neurocrine-Voyager-GBA1-Deal-Analysis` | `[[gba1-voyager]]` | `assets/gba1-voyager.md` ✓ |
| `deal-analysis-novartis-arrowhead-aro-snca` | `[[aro-snca]]` | `assets/aro-snca.md` ✓ |
| `Biohaven-Highlightll-TYK2-Deal-Analysis` | `[[bhv-8000]]` | `assets/bhv-8000.md` ✓ |
| `Insilico-Hygtia-NLRP3-Deal-Analysis` | `[[ism8969]]` | `assets/ism8969.md` ✓ |
| `Lilly-Prevail-Deal-Analysis` | `[[pr001]]` | `assets/pr001.md` ✓ |
| `Capsida-Lilly-Deal-Analysis` | `[[cap-003]]` | `assets/cap-003.md` ✓ |
| `Lilly-ABL Bio Deal Analysis` | `[[abl301]]` (ABL Bio's clinical asset) | `assets/abl301.md` ✓ |
| `Sanofi-ABL-Bio-Deal-Analysis` | `[[abl301]]` | `assets/abl301.md` ✓ |
| `Lilly-Ventyx-NLRP3-Deal-Analysis` | `[[vtx3232]]` | `assets/vtx3232.md` ✓ |
| `Sumitomo-Raguneprocel-Analysis` | `[[raguneprocel]]` | `assets/raguneprocel.md` ✓ |
| `MeiraGTx-Hologen-Deal-Analysis` | `[[aav-gad]]` | `assets/aav-gad.md` ✓ |
| `Merck-Valo-Deal-Analysis` | `[[valo-merck]]` | `assets/valo-merck.md` ✓ |
| `GSK-Vesalius-Deal-Analysis` | `[[vesalius-gsk]]` | `assets/vesalius-gsk.md` ✓ |
| `Kenai-Therapeutics-Deal-Analysis` | `[[rndp-001]]` | `assets/rndp-001.md` ✓ |

### Assets that NEED TO BE CREATED before linking:

| Deal File | Missing asset | Notes |
|-----------|--------------|-------|
| `AbbVie-Mitokinin-Deal-Analysis` | `assets/abbv-1088.md` | Drug formerly MTK458; PINK1 activator |
| `Biogen-Alectos-GBA2-Deal-Analysis` | `assets/al01811.md` | GBA2 inhibitor; preclinical |
| `Neuron23-Deal-Analysis` | `assets/neu-411.md` | LRRK2 inhibitor; Phase 2 NEULARK |

### Platform deals (no single drug asset — link to platform description):
- `AbbVie-Capsida-Deal-Analysis` — platform deal; no single asset note needed
- `GSK-ABL-Bio-Deal-Analysis` — platform deal; no single asset note needed

---

## 5. WIKILINKS TO COMPANIES/

**Finding: Zero of 26 deal analysis files contain wikilinks to companies/**

### Companies that EXIST for all deal parties:

All major pharma acquirers have company notes:
- `companies/abbvie.md`, `companies/biogen.md`, `companies/eli-lilly.md`, `companies/gsk.md`, `companies/novartis.md`, `companies/roche.md`, `companies/sanofi.md`, `companies/ucb.md` — all confirmed ✓

All deal targets/partners have company notes:
- `companies/cerevel-therapeutics.md`, `companies/denali-therapeutics.md`, `companies/prothena.md`, `companies/bial.md`, `companies/bayer.md`, `companies/bluerock-therapeutics.md`, `companies/aspen-neuroscience.md`, `companies/neurocrine-biosciences.md`, `companies/arrowhead-pharmaceuticals.md`, `companies/biohaven.md`, `companies/hangzhou-highlightll-pharma.md`, `companies/insilico-medicine.md`, `companies/hygtia-therapeutics.md`, `companies/prevail-therapeutics.md`, `companies/capsida-biotherapeutics.md`, `companies/abl-bio.md`, `companies/ventyx-biosciences.md`, `companies/sumitomo-pharma.md`, `companies/meiragtx.md`, `companies/hologen.md`, `companies/merck-kgaa.md`, `companies/valo-health.md`, `companies/vesalius-therapeutics.md`, `companies/kenai-therapeutics.md`, `companies/neuron23.md`, `companies/voyager-therapeutics.md` — all confirmed ✓

### Companies that NEED TO BE CREATED:

| Deal File | Missing company note | Notes |
|-----------|---------------------|-------|
| `AbbVie-Mitokinin-Deal-Analysis` | `companies/mitokinin.md` | Acquired company (Oct 2023) |
| `Biogen-Alectos-GBA2-Deal-Analysis` | `companies/alectos-therapeutics.md` | Licensed company |
| `BIAL-Pariceract-Deep-Dive` | `companies/lysosomal-therapeutics.md` | Acquired company (Oct 2020) |

### Recommended approach for adding company links:
Add a `## See Also` section at the end of each deal file:
```markdown
## See Also
- [[CompanyA]] — acquirer
- [[CompanyB]] — target
- [[asset-name]] — lead drug
- [[PD-Deal-Summary]] — master deal table
```

---

## 6. CROSS-LINKS WITH PD-DEAL-SUMMARY.MD

**Finding: All 26 deal files appear in the summary table. All wikilinks resolve to real files.**

### Summary table coverage — COMPLETE:
Every deal analysis file is linked from `PD-Deal-Summary.md` rows 1–26. ✓

### Links that require updating after renaming:
- Row 4: `[[Lilly-ABL Bio Deal Analysis]]` → update to `[[Lilly-ABL-Bio-Grabody-B-Deal-Analysis]]` after rename
- Row 5: `[[deal-analysis-novartis-arrowhead-aro-snca]]` → update to `[[Novartis-Arrowhead-ARO-SNCA-Deal-Analysis]]` after rename

### Other summary-file links — all resolve:
- `[[FINAL-PD-Deal-Landscape-Report]]` → `FINAL-PD-Deal-Landscape-Report.md` ✓
- `[[master-pd-pipeline|Master PD Pipeline]]` → `consolidated/master-pd-pipeline.md` ✓

---

## 7. INTERNAL STRUCTURE

**Finding: Structure is largely consistent across all 26 deal files.**

### Standard structure (present in all files):
1. # Title heading
2. Deal metadata block (Date, Value, Asset, Analyst)
3. `## Executive Summary` (or `## EXECUTIVE SUMMARY`)
4. `## PHASE 1: DEEP DIVE` with subsections (Scientific Foundation, Asset Quality, Deal Terms)
5. Additional PHASE 2/3 sections (competitive analysis, investment verdict, etc.)

### Minor structural inconsistencies:
- **Heading capitalization varies:** Some use `# DEEP DUE-DILIGENCE:` (all caps), others use `# Deep Due-Diligence:`, others `# Company/Company Deal Name`. Not a functional problem, but inconsistent.
- **No `## References` or `## See Also` section** in any deal file — this is where wikilinks to assets/ and companies/ should go (see §4 and §5).
- **Date metadata format varies:** Some use bold `**Date:** February 14, 2026`, others just plain text — minor.

### Files with non-standard structural openers (preamble artifacts — see §3):
15 files open with LLM process text before the actual `#` heading. These need the first 1-2 lines deleted.

---

## PRIORITIZED FIX LIST

### P1 — Do first (high impact, systematic):
1. **Remove LLM preamble** from 15 files (line 1 deletion per file listed in §3)
2. **Add YAML frontmatter** to all 26 deal analysis files (use template in §2)
3. **Update PD-Deal-Summary.md** wikilinks after renames (rows 4 and 5)

### P2 — Naming fixes (require file renames + summary table updates):
4. Rename `Lilly-ABL Bio Deal Analysis.md` → `Lilly-ABL-Bio-Grabody-B-Deal-Analysis.md`
5. Rename `deal-analysis-novartis-arrowhead-aro-snca.md` → `Novartis-Arrowhead-ARO-SNCA-Deal-Analysis.md`
6. Rename `BIAL-Pariceract-Deep-Dive.md` → `BIAL-Pariceract-Deal-Analysis.md`
7. Rename `minzasolmin-failure-analysis.md` → `Novartis-UCB-Minzasolmin-Failure-Analysis.md`
8. Rename `Bayer-BlueRock-Cell-Therapy-Analysis.md` → `Bayer-BlueRock-Cell-Therapy-Deal-Analysis.md` *(lower priority)*
9. Rename `Sumitomo-Raguneprocel-Analysis.md` → `Sumitomo-Raguneprocel-Deal-Analysis.md` *(lower priority)*

### P3 — Wikilink additions (add See Also sections to each file):
10. Add `## See Also` block with asset + company wikilinks to all 26 deal files (asset links per §4, company links per §5)
11. Create missing asset notes: `assets/abbv-1088.md`, `assets/al01811.md`, `assets/neu-411.md`
12. Create missing company notes: `companies/mitokinin.md`, `companies/alectos-therapeutics.md`, `companies/lysosomal-therapeutics.md`

---

*Audit completed 2026-02-26. All file existence checks performed via Glob/Bash. Wikilink inventory via Grep. File content via Read (first 30 lines per file).*
