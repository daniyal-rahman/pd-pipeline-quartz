# Deals Fact-Check: Batch 2
**Auditor:** factchecker-2
**Date:** 2026-02-26
**Scope:** 13 deal analysis files (rows 14–26 of PD-Deal-Summary.md) + FINAL-PD-Deal-Landscape-Report.md cross-reference
**Prior batch:** FACT-CHECK-AUDIT.md (Feb 23, 2026) — 15 files already reviewed; findings below do not duplicate batch 1

---

## Summary

| Severity | Count | Files Affected |
|----------|-------|----------------|
| MEDIUM | 3 | PD-Deal-Summary.md (rows 16, 19, 24) |
| LOW | 2 | GSK-Vesalius-Deal-Analysis.md, BIAL-Pariceract-Deep-Dive.md |
| CLEAN | 8 | Biogen-Alectos, Capsida-Lilly, Aspen-Neuroscience, Neuron23, Kenai, Merck-Valo, Sumitomo-Raguneprocel, AbbVie-Mitokinin |
| Already flagged in batch 1 | — | See FACT-CHECK-AUDIT.md |

---

## MEDIUM Issues

### M1 — AbbVie/Capsida deal date wrong in master summary
**File:** `deals/PD-Deal-Summary.md`, row 16
**Claim:** Year = "2022"
**Correct:** April 2021 (initial CNS collaboration); February 2023 (ophthalmology expansion)
**Source:** AbbVie-Capsida-Deal-Analysis.md ("2021: Initial CNS collaboration, $90M upfront for 3 neurodegeneration targets"); confirmed by web search (April 2021 press releases)
**Note:** The deal row likely refers to the initial deal, which is 2021, not 2022. The ophthalmology expansion was February 2023 but that is a separate event. PD-relevant collaboration is the 2021 CNS deal.
**Action:** Correct row 16 year from "2022" → "2021" in PD-Deal-Summary.md

---

### M2 — MeiraGTx/Hologen deal date wrong in master summary
**File:** `deals/PD-Deal-Summary.md`, row 19
**Claim:** Year = "2024"
**Correct:** March 13, 2025
**Source:** Web search confirmed GlobeNewswire / NASDAQ press releases dated March 13, 2025. MeiraGTx-Hologen-Deal-Analysis.md body also references deal as 2025.
**Action:** Correct row 19 year from "2024" → "2025" in PD-Deal-Summary.md

---

### M3 — Insilico/Hygtia deal date wrong in master summary
**File:** `deals/PD-Deal-Summary.md`, row 24
**Claim:** Year = "2024"
**Correct:** January 20, 2026
**Source:** Insilico-Hygtia-NLRP3-Deal-Analysis.md explicitly states: "Insilico Hong Kong IPO: December 30, 2025; ISM8969 deal announced January 20, 2026 (3 weeks after IPO)." Hygtia was founded August 2025 — it could not have done a deal in 2024. No web search needed; file body is self-consistent.
**Action:** Correct row 24 year from "2024" → "2026" in PD-Deal-Summary.md

---

## LOW Issues

### L1 — GSK-Vesalius internal cross-reference table: ABL Bio deal date wrong
**File:** `deals/GSK-Vesalius-Deal-Analysis.md`
**Claim:** Competitive landscape / deal comparison table lists GSK/ABL Bio deal as "Dec 2024"
**Correct:** April 6, 2025
**Source:** FACT-CHECK-AUDIT.md (batch 1) already established the GSK/ABL Bio deal date as April 2025. PD-Deal-Summary.md row 1 footnote [^2] confirms correction. The GSK-Vesalius file appears to use an older internal placeholder date.
**Action:** Update cross-reference table in GSK-Vesalius file: "Dec 2024" → "April 2025" for ABL Bio deal entry

---

### L2 — BIAL-Pariceract competitive landscape: GT-02287 data date wrong
**File:** `deals/BIAL-Pariceract-Deep-Dive.md`
**Claim:** Competitive landscape section cites GT-02287 CSF data as "Dec 2024"
**Correct:** December 18, 2025
**Source:** Web search confirmed Gain Therapeutics CSF GluSph data announcement via GlobeNewswire dated December 18, 2025.
**Action:** Update BIAL file: "Dec 2024" → "Dec 2025" for GT-02287 CSF GluSph biomarker data

---

## FINAL-PD-Deal-Landscape-Report.md Cross-Reference

**Scope:** Cross-checked batch 2 deal data against Section I (Executive Summary), Section II.1 (Science Rankings), and Section III.3 (Conviction Table) in first 200 lines.

**Findings:**

1. **MeiraGTx/Hologen conviction ratio** (Section III.3): Shows "$200M / $430M = 46.5%" — arithmetic correct ✓. Deal value consistent with individual file ✓.

2. **Insilico/Hygtia deal** in report: Listed with correct deal value ($66M total) ✓. Deal date in report body not verified in the 200-line preview — given row 24 master table error (M3 above), this may cascade into report as well if report pulls from master table.

3. **GSK/ABL Bio conviction ratio**: Shows "1.8% ($50M/$2.8B)" — batch 1 already flagged $2.8B as likely overstated (should be ~$2.5B). With corrected denominator, conviction = ~2.0%. This is a minor downstream effect of the batch 1 issue, not a new finding.

4. **No new issues found** in batch 2 deal sections of FINAL report beyond items already in FACT-CHECK-AUDIT.md.

---

## Files Reviewed — No New Issues

| Row | Deal | Status | Notes |
|-----|------|--------|-------|
| 14 | Capsida/Lilly | CLEAN (batch 1) | $55M upfront, $740M total, Jan 2023 ✓ |
| 15 | Biogen/Alectos | CLEAN (batch 1) | $15M upfront, $722.5M total, Jun 2022 ✓ |
| 17 | AbbVie/Mitokinin | Batch 1 LOW | Cerevel timing error previously flagged |
| 20 | Aspen Neuroscience | CLEAN | $115M Series C, Nov 2025, $340M total ✓ |
| 22 | Neuron23 | CLEAN | $96.5M Series D, Jun 2025, NEULARK NCT06680830 ✓ |
| 23 | Kenai Therapeutics | CLEAN | $90M ($82M Series A + $8M CIRM), Feb 2024 ✓ |
| 25 | Merck/Valo | CLEAN | $3B+ headline, announced Nov 20, 2025 ✓ |
| 26 | Sumitomo/Raguneprocel | CLEAN | Japan filing Aug 2025, RACTHERA Dec 2024, Nature Apr 2025 ✓ |

---

## Corrections Needed in PD-Deal-Summary.md

```
Row 16: Year "2022" → "2021"
Row 19: Year "2024" → "2025"
Row 24: Year "2024" → "2026"
```

## Corrections Needed in Individual Deal Files

```
GSK-Vesalius-Deal-Analysis.md: ABL Bio deal date in cross-reference table "Dec 2024" → "April 2025"
BIAL-Pariceract-Deep-Dive.md: GT-02287 CSF data date "Dec 2024" → "Dec 2025"
```

---

## Methodology

- Read all 13 deal files in full (large files read via preview + file output)
- Cross-referenced deal values, dates, and clinical claims against PD-Deal-Summary.md master table
- Verified 3 dates via web search: MeiraGTx/Hologen deal date (March 13, 2025 ✓), GT-02287 CSF data date (December 18, 2025 ✓), AbbVie/Capsida initial deal (April 2021 ✓)
- Did not re-check issues already documented in FACT-CHECK-AUDIT.md (batch 1)
- Partial review of FINAL-PD-Deal-Landscape-Report.md (first 200 lines; sections I, II.1, III.3)
