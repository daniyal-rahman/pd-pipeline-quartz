# FACT-CHECK AUDIT: PD Deal Analysis Files

**Audit Date:** February 23, 2026
**Auditor:** Claude (claude-sonnet-4-6)
**Scope:** 15 deal analysis files in `/deals/` folder
**Method:** File reading + web search verification of key claims

---

## SUMMARY TABLE

| File | Issues Found | Severity | Action Needed |
|------|-------------|----------|---------------|
| AbbVie-Cerevel-Deal-Analysis.md | 3 | LOW | Minor corrections |
| Neurocrine-Voyager-GBA1-Deal-Analysis.md | 2 | LOW | Clarification needed |
| GSK-ABL-Bio-Deal-Analysis.md | 2 | MEDIUM | Currency/value correction |
| deal-analysis-novartis-arrowhead-aro-snca.md | 2 | LOW | Minor corrections |
| Biogen-Denali-LRRK2-Deal-Analysis.md | 2 | LOW | Minor corrections |
| FINAL-PD-Deal-Landscape-Report.md | 4 | MEDIUM | Several corrections needed |
| Lilly-Ventyx-NLRP3-Deal-Analysis.md | 1 | LOW | One date note |
| Lilly-Prevail-Deal-Analysis.md | 2 | HIGH | NCT error + acquisition price framing |
| Bayer-BlueRock-Cell-Therapy-Analysis.md | 2 | LOW-MEDIUM | Year/NCT corrections |
| BIAL-Pariceract-Deep-Dive.md | 1 | LOW | Minor enrollment discrepancy |
| Roche-Prothena-Deal-Analysis.md | 1 | LOW | Prothena stock figure |
| AbbVie-Mitokinin-Deal-Analysis.md | 1 | LOW | Minor deal-date note |
| Capsida-Lilly-Deal-Analysis.md | 1 | LOW | Deal total vs upfront |
| Biogen-Alectos-GBA2-Deal-Analysis.md | 0 | CLEAN | No factual errors found |
| Sanofi-ABL-Bio-Deal-Analysis.md | 1 | LOW | Deal date correction |

**Overall quality: HIGH.** Most files are factually solid. The one HIGH-severity issue is in Lilly-Prevail (self-acknowledged NCT error that needs correction, not just flagging). Currency conversion ambiguity in GSK-ABL-Bio is the main MEDIUM issue.

---

## DETAILED PER-FILE FINDINGS

---

### 1. AbbVie-Cerevel-Deal-Analysis.md

**Deal economics verified:**
- $8.7B acquisition at $45/share — CONFIRMED via AbbVie press release (August 1, 2024 closing)
- Emraclidine EMPOWER failure — CONFIRMED November 11, 2024
- 12% stock drop, ~$40B market cap loss — CONFIRMED by multiple sources (BioSpace, BioPharma Dive)
- $3.5B impairment charge — PLAUSIBLE but not independently verified; consistent with $8.7B deal for two key assets where the non-PD lead (emraclidine) failed
- NDA submitted September 26, 2025 — CONFIRMED via AbbVie press release

**Clinical trial claims:**
- TEMPO-3: 507 patients, 27 weeks, adjunctive therapy — CONSISTENT with public data
- TEMPO-1/-2 results: -9.7, -10.2, -9.1 vs. +1.8 (placebo) — CONSISTENT with published trial summaries
- TEMPO-3: +1.1 hours ON time — CONSISTENT

**Issues found:**

**ISSUE 1 (LOW):** The file describes the acquisition as completing "August 2024" without specifying the date. The acquisition ANNOUNCED December 6, 2023 and COMPLETED August 1, 2024. No inaccuracy per se, but framing is slightly ambiguous — some readers might think the deal was announced in August 2024.

**ISSUE 2 (LOW):** Mitokinin deal stated as "$110M + $545M milestones." This is correct for total potential deal value ($655M). The file also separately states total as "$655M" in the analysis body. No arithmetic error, just verify consistency across uses.

**ISSUE 3 (LOW):** Aliada acquisition price stated as "$1.4B December 2024." This is consistent with public sources. No error.

**Action:** No corrections required. Minor clarification that the Cerevel deal was *announced* December 2023 and *completed* August 2024 could be added for precision.

---

### 2. Neurocrine-Voyager-GBA1-Deal-Analysis.md

**Deal economics verified:**
- Deal date January 9, 2023 — CONFIRMED
- $175M upfront ($136M cash + $39M equity at 50% premium) — CONFIRMED exactly via GlobalNewsWire press release
- $985M GBA1 development milestones — CONFIRMED (if Voyager declines its cost/profit share option)
- "Up to $4.4B total" — NEEDS EXPLANATION (see Issue 1 below)

**Issues found:**

**ISSUE 1 (LOW):** The file states a total deal value of "$4.4B." The verified components are: $175M upfront + up to $985M development milestones (GBA1) + potential commercial milestones + royalties (low double-digit to 20% US; high single-digit to mid-teens ex-US). The three additional CNS programs each have separate milestone structures. The $4.4B figure appears to be the aggregate across all four programs (GBA1 + 3 additional CNS targets) and/or includes commercial milestones not broken out in the press release. This total is **not independently verifiable** from the press release alone. The file should note that $4.4B is an aggregate estimate across all programs, not solely the GBA1 program.

**ISSUE 2 (LOW):** The file states "May 2025: Neurocrine returned 2 of 3 additional CNS programs to Voyager." This is confirmed by FierceBiotech ("Neurocrine hands back 2 CNS gene therapy programs to Voyager"). No error here, but the file could note which programs were returned (the two undisclosed rare CNS targets, keeping the GBA1 program and one other).

**Action:** Add a note clarifying that $4.4B is aggregate across all 4 programs. No corrections needed otherwise.

---

### 3. GSK-ABL-Bio-Deal-Analysis.md

**Deal economics verified:**
- Deal announced April 6, 2025 — CONFIRMED
- ABL Bio press release terms: £38.5M upfront + £38.6M near-term = £77.1M total upfront/near-term; up to £2.075B milestones — CONFIRMED

**Issues found:**

**ISSUE 1 (MEDIUM):** The file states the upfront as "$50M" and total milestones as "up to $2.8B." These are USD conversions of the GBP-denominated deal. Verified conversion: £38.5M upfront ≈ $49.5M (approximately $50M — CORRECT). Total milestones £2.075B ≈ $2.75B at approximately $1.33/£ exchange rate at time of deal. Multiple sources (FierceBiotech headline: "$2.5B pact"; Inside Precision Medicine: "$2.5B"; GeneEngineering News: "$2.75B+"; Korean sources: "$2.8B") report different USD figures. The file's "$2.8B" figure is on the high end but defensible depending on exchange rate used. The FierceBiotech "$2.5B" headline appears to be an approximation using a lower GBP/USD rate.

**Recommended correction:** Note in the file that the deal is denominated in GBP (£2.075B milestone maximum) and that USD equivalents vary by source ($2.5B–$2.8B depending on exchange rate used). The file should not present $2.8B as a precise figure — it is a conversion.

**ISSUE 2 (LOW):** The file notes the FierceBiotech URL title says "$2.5B pact" vs. the file's stated $2.8B. The file itself flags this discrepancy. No action needed beyond the note already present. The underlying facts are correct — just a currency conversion variance.

**Action:** Add a note that deal is in GBP and USD equivalent varies by source. The "$2.8B" is defensible but higher-end.

---

### 4. deal-analysis-novartis-arrowhead-aro-snca.md

**Deal economics verified:**
- Deal date September 2, 2025 — CONFIRMED via Arrowhead press release
- $200M upfront — CONFIRMED
- Up to $2B in milestones — CONFIRMED
- Total $2.2B — CONFIRMED ($200M + $2B = $2.2B; correct arithmetic)
- Royalties: "tiered royalties" — CONFIRMED; the file says "low double digits" which is consistent with standard range

**Clinical trial claims:**
- Minzasolmin ORCHESTRA: December 16, 2024, 450+ patients, 18 months, early-stage PD — CONFIRMED. (Note: actual enrollment was 496 patients, not "450+" — file's "450+" is technically correct as a lower bound but imprecise)
- LIGHTHOUSE terminated June 2023 — CONFIRMED
- ION464 discontinued February 12, 2025 — CONFIRMED (same date as BIIB094 via Biogen press release)

**Issues found:**

**ISSUE 1 (LOW):** ORCHESTRA enrollment stated as "450+ patients." Verified enrollment was 496 patients. "450+" is not wrong (it's a lower bound), but "approximately 500 patients" or "496 patients" would be more precise.

**ISSUE 2 (LOW):** The file states the Novartis-Argo deal was "$5.2B ($160M upfront)" for cardiovascular RNAi. This is cited for comparison purposes only. This figure is consistent with public reports and is not a PD-specific claim requiring verification.

**Action:** Update ORCHESTRA enrollment from "450+" to "496" for precision.

---

### 5. Biogen-Denali-LRRK2-Deal-Analysis.md

**Deal economics verified:**
- Deal: $560M cash + $465M equity — CONFIRMED exactly via GlobalNewsWire press release
- Equity at $34.94/share, 13.3M shares — CONFIRMED
- Total upfront: $1.025B — CONFIRMED ($560M + $465M)
- Up to $1.125B milestones — CONFIRMED
- Total $2.15B — CONFIRMED ($1.025B + $1.125B = $2.15B; correct arithmetic)

**Clinical trial claims:**
- LIGHTHOUSE terminated June 2023 — CONFIRMED. Reason: "complexity and long timeline with anticipated completion in 2031" — CONFIRMED word-for-word in Biogen press release
- LUMA: 640-650 patients, Phase 2b — CONFIRMED (NeurologyLive reports 650 participants, 113 sites; file says 640-650 / 98 centers — slight discrepancy in site count: 98 vs 113)
- BEACON Phase 2a: ~50 LRRK2-PD patients, first patient December 2024 — CONFIRMED via Denali/Biogen press release
- BIIB094 (ION859) discontinued February 2025 — CONFIRMED

**Issues found:**

**ISSUE 1 (LOW):** LUMA site count: file says "98 centers" but NeurologyLive/ClinicalTrials.gov reports 113 sites. The 98 figure may reflect the number of sites at an earlier point in enrollment. Not a material error but worth updating.

**ISSUE 2 (LOW):** The file states Phase 1/1b showed "80-87% reduction in p-Rab10." This is consistent with published Phase 1 data (NEJM 2023 paper). No error.

**Action:** Update LUMA site count from "98 centers" to "113 sites."

---

### 6. FINAL-PD-Deal-Landscape-Report.md

**Issues found:**

**ISSUE 1 (MEDIUM):** LUMA readout cited as "March 2026." This is consistent with ClinicalTrials.gov completion date of March 2026. However, "readout" and "estimated completion" are different — top-line data typically follows trial completion by several months. The March 2026 date is the trial's estimated primary completion date; actual data disclosure will likely be mid-to-late 2026. The file should clarify: "estimated trial completion March 2026; top-line data expected H2 2026."

**ISSUE 2 (MEDIUM):** The report states Capsida's first patient (CAP-002) "died." The Capsida-Lilly file does not mention this. The AbbVie-Mitokinin file references "Capsida AbbVie exercised option (January 2025) → $40M payment" and notes the IND clearance was for CAP-003 (not CAP-002). CAP-002 is the AbbVie program (for an undisclosed neurodegenerative target), separate from CAP-003 (the Lilly/Prevail GBA-PD program). The claim that a CAP-002 patient died is unverified in the deal analysis files and was not confirmed by web searches. This claim needs sourcing. If unsourced, it should be removed or flagged as unverified.

**ISSUE 3 (LOW):** The report cites two different alpha-syn SAA sensitivity figures in different sections: "87.7% sensitivity" in one section and "86% sensitivity" in another. These are not necessarily contradictory (different studies, different populations), but the lack of attribution to specific studies is unclear. Should add study citations to disambiguate.

**ISSUE 4 (LOW):** The report lists Sanofi's ROFN (right of first negotiation) investment in Ventyx as context for the Lilly deal. The Lilly-Ventyx file states Sanofi invested "$27M at $3.82/share September 2024." This is consistent with public records. The Final Report does not state this incorrectly — it's just a cross-reference point.

**Action:**
- Clarify LUMA readout timing (trial completion ≠ data release)
- Source or remove the CAP-002 patient death claim
- Add citations for the two different SAA sensitivity figures

---

### 7. Lilly-Ventyx-NLRP3-Deal-Analysis.md

**Deal economics verified:**
- Lilly acquired Ventyx January 7, 2026 — CONFIRMED (announcement date; transaction expected to close H1 2026)
- $1.2B at $14.00/share — CONFIRMED
- 62% premium — CONFIRMED (62% to 30-day VWAP ending January 5, 2026)
- Sanofi ROFN investment $27M at $3.82/share September 2024 — CONSISTENT with public records

**Clinical trial claims:**
- VTX3232 Phase 2a: N=10, 28-day, open-label, 40mg oral daily — CONSISTENT with published interim data
- MDS-UPDRS Part III: -5.2 points (p=0.0054) — CONSISTENT with reported data
- MDS-UPDRS Part I: -2.4 (p=0.0118), Part II: -2.7 (p=0.0471) — CONSISTENT
- CSF drug levels exceeded IC90 — CONSISTENT

**Issues found:**

**ISSUE 1 (LOW):** The file states the deal was announced January 7, 2026 and describes it as an "acquisition." Technically, the definitive agreement was signed January 7, 2026, but the acquisition has not yet closed as of February 23, 2026 (pending stockholder approval and regulatory clearance). The file correctly notes it is expected to close in H1 2026. No factual error, but future readers should note this is a signed agreement, not a completed acquisition.

**Action:** No corrections required. Deal status is accurately described.

---

### 8. Lilly-Prevail-Deal-Analysis.md

**Deal economics verified:**
- Acquisition price: $22.50/share ($880M upfront) + $4.00 CVR ($160M) = $26.50/share total = $1.04B — CONFIRMED by multiple sources
- The file title correctly states "$1.04B" — CONFIRMED

**Issues found:**

**ISSUE 1 (HIGH — requires correction):** The file mentions NCT06944522 in the context of PR001's Phase 3 (exPDite-2) trial. The file itself acknowledges this is an error, noting the NCT is "for bemdaneprocel (BlueRock), NOT PR001." This is correct — NCT06944522 belongs to BlueRock's exPDite-2 bemdaneprocel Phase 3 trial, as confirmed by the Bayer-BlueRock file. The issue is that the wrong NCT number appears in the file body even though the file flags it. The text referencing NCT06944522 for PR001's Phase 3 should be removed entirely, and the PR001 Phase 3 NCT number (if known) should be substituted, or the trial should simply be described without an NCT number if it has not yet been registered.

**ISSUE 2 (LOW):** The file states the acquisition as "$880M upfront" without the CVR structure. While technically accurate that $880M was the upfront cash payment at closing, the full deal was $880M + up to $160M CVR = $1.04B. The title correctly states $1.04B but the body should consistently clarify the structure: $880M cash + $160M CVR.

**Action:**
- Remove the NCT06944522 reference for PR001 (this NCT belongs to bemdaneprocel/BlueRock)
- Clarify the $880M upfront + $160M CVR structure throughout

---

### 9. Bayer-BlueRock-Cell-Therapy-Analysis.md

**Deal economics verified:**
- Bayer owned 40.8% stake, acquired remaining 59.2% for $240M upfront + $360M milestones — CONFIRMED (this deal closed 2019, not 2023 as the file might imply)
- Total valuation: ~$1B — CONFIRMED

**IMPORTANT DATE NOTE:** The Bayer acquisition of BlueRock occurred in 2019, not 2023. The $240M figure and deal structure are confirmed for the 2019 acquisition. The file correctly describes this as Bayer "acquiring the remaining stake" — this is accurate.

**Clinical trial claims:**
- Phase 1 (exPDite): 12 patients (5 low-dose 0.9M cells/putamen, 7 high-dose 2.7M cells/putamen) — CONSISTENT with BioPharma Dive coverage
- 18-month high-dose: -23 points MDS-UPDRS Part III — CONSISTENT with Bayer press releases
- 36-month high-dose: -17.9 points — CONSISTENT
- Zero GID through 36 months — CONSISTENT
- FDA RMAT designation May 2024 — CONSISTENT
- Phase 3 exPDite-2: ~102 patients, first patient September 2025 — CONFIRMED via Bayer press release ("First Parkinson's disease patient treated in BlueRock's pivotal Phase III trial")

**Issues found:**

**ISSUE 1 (LOW-MEDIUM):** NCT06944522 is used for Phase 3 exPDite-2 in this file. This is the CORRECT NCT for BlueRock's bemdaneprocel Phase 3. (The same NCT was incorrectly attributed to Lilly's PR001 in the Prevail file — this Bayer file uses it correctly.)

**ISSUE 2 (LOW):** Bayer $250M Berkeley facility described as opened "October 2023." The Bayer press release confirms a $250M investment commitment in October 2023; whether "opened" vs. "announced" is accurate requires checking, but the $250M figure and timing are correct.

**Action:** Confirm that NCT06944522 for exPDite-2 is the correct registry number (the Lilly-Prevail file must be corrected to remove this NCT, not the Bayer file). No other corrections needed.

---

### 10. BIAL-Pariceract-Deep-Dive.md

**Deal economics verified:**
- BIAL acquired Lysosomal Therapeutics October 2020 for "up to $130M" — CONFIRMED via Business Wire press release. The $130M is milestone-contingent; upfront amount not disclosed in public sources.

**Clinical trial claims:**
- ACTIVATE trial (NCT05819359) — NCT CONFIRMED (NeurologyLive, BioSpace cite this NCT)
- 273 genetically confirmed GBA-PD patients — CONFIRMED
- 85 sites, Europe and North America — CONFIRMED
- 78-week treatment period — CONFIRMED
- First patient May 2023 — CONSISTENT ("First Patient Dosed in Phase 2 ACTIVATE Trial" per NeurologyLive)
- Topline mid-2026 — CONSISTENT (NeurologyLive: "expected to conclude midway through 2026")
- Doses: 10mg vs. 60mg vs. placebo — CONFIRMED

**Issues found:**

**ISSUE 1 (LOW):** The file states "273 patients" enrolled. The BIAL press release on recruitment milestone says the study "met its recruitment goal of more than 230 people." The 273 figure may reflect final enrollment above the initial 230 target. This is internally consistent (273 > 230), but the file should note that 273 is the reported final enrollment, while the recruitment goal was 230+.

**Action:** No corrections required. The enrollment figure of 273 is consistent with public reporting.

---

### 11. Roche-Prothena-Deal-Analysis.md

**Deal economics verified:**
- $30M upfront (2013) — CONFIRMED
- $135M earned to date — CONFIRMED via Prothena SEC filings and press releases
- Up to $620M remaining milestones — CONFIRMED (Phase 3 decision unlocks milestones)
- Double-digit teen royalties — CONFIRMED
- Total ~$755M — CORRECT arithmetic ($30M + $135M + $620M remaining = $785M max; the file's "$755M+" is slightly understated but the $755M+ framing is accurate as a floor)

**Clinical trial claims:**
- PADOVA: N=586, minimum 18 months, missed primary (HR=0.84, p=0.0657) — CONFIRMED via Roche press release December 2024
- Levodopa subgroup: HR=0.79, p=0.0431 (nominal); covariate-adjusted HR=0.76, p=0.0175 — CONSISTENT with Roche data
- 75% of participants on levodopa — CONFIRMED
- Roche advancing to Phase 3: June 2025 — CONFIRMED via Roche press release June 16, 2025
- PASADENA 4-year OLE: Nature Medicine October 2024 — CONFIRMED

**Issues found:**

**ISSUE 1 (LOW):** The file states "Prothena stock +11% on announcement" of Phase 3 advancement. This is consistent with press coverage ("Prothena's Partner Roche to Advance Prasinezumab...") but the exact stock movement percentage should be verified from financial data rather than taken as fact. Not a critical error.

**Action:** No corrections required. Consider sourcing the stock movement figure if used in investment context.

---

### 12. AbbVie-Mitokinin-Deal-Analysis.md

**Deal economics verified:**
- Option exercised October 5, 2023 — CONFIRMED via AbbVie press release
- $110M upfront — CONFIRMED
- Up to $545M milestones — CONFIRMED
- Total $655M — CONFIRMED ($110M + $545M; correct arithmetic)
- Original option: March 2021 — CONFIRMED via PitchBook/PRNewswire
- ABBV-1088 (formerly MTK458) — CONFIRMED

**Scientific claims:**
- MTK458 off-target mitochondrial effects (Science Advances 2024) — CONFIRMED (cited correctly as published data)
- pS65-Ubiquitin as biomarker — CONFIRMED (cited correctly with PMC references)
- MJFF $1M+ in grants — CONSISTENT with MJFF published de-risking stories

**Issues found:**

**ISSUE 1 (LOW):** The file states AbbVie acquired Cerevel for "$8.7B in August 2023" in the strategic rationale section. The Cerevel deal was *announced* December 6, 2023 and *completed* August 1, 2024 (not "August 2023"). The Mitokinin deal closed October 5, 2023 — which was actually *before* the Cerevel announcement. The file's narrative ("AbbVie acquired Cerevel for $8.7B in August 2023 [1 month before Mitokinin close]") is therefore incorrect in two ways: the Cerevel announcement was after the Mitokinin close, and the completion was in 2024. The *announcement* sequence was: Mitokinin (October 2023) → Cerevel announcement (December 2023) → Cerevel close (August 2024). The strategic logic is still sound (AbbVie was building a PD portfolio), but the specific timing claim in parentheses is wrong.

**Action:** Correct the Cerevel timing: "AbbVie acquired Cerevel ($8.7B announced December 2023, completed August 2024), 2 months after the Mitokinin close (October 2023)." The sequencing matters slightly for the strategic narrative.

---

### 13. Capsida-Lilly-Deal-Analysis.md

**Deal economics verified:**
- Lilly-Capsida deal: January 2023 — CONFIRMED (January 4, 2023 per Capsida press release)
- $55M upfront (payment + commitment to financing round) — CONFIRMED via FierceBiotech and Endpoints News
- Up to $685M milestones — CONFIRMED
- Total $740M — CONFIRMED ($55M + $685M = $740M; correct arithmetic)
- AbbVie-Capsida: $80M upfront + $10M equity + up to $665M milestones — CONFIRMED
- AbbVie option exercise January 2025: $40M — CONFIRMED via Capsida press release

**Issues found:**

**ISSUE 1 (LOW):** The file states AbbVie-Capsida deal total as "$665M" and then adds "AbbVie exercised option (January 2025) → $40M payment" which implies the $665M includes this payment. The file also earlier states "$80M upfront, $10M equity, up to $665M milestones across 3 neuro programs + ophthalmology expansion (2023, $70M)." The total deal structure is slightly complex to parse, but no arithmetic errors are present.

**Action:** No corrections required.

---

### 14. Biogen-Alectos-GBA2-Deal-Analysis.md

**Deal economics verified:**
- Deal June 2022 — CONFIRMED via Biogen press release
- $15M upfront — CONFIRMED
- Up to $77.5M development milestones — CONFIRMED
- Up to $630M commercial milestones — CONFIRMED
- Total $722.5M (rounds to $722M) — CONFIRMED
- Backup molecules included — CONFIRMED

**Scientific claims:**
- GBA2 LOF causes SPG46/cerebellar ataxia — CONFIRMED (PMC3567281 cited correctly)
- Miglustat is an FDA-approved GBA2 inhibitor — CONFIRMED (for Niemann-Pick C)
- GT-02287 first-ever CSF substrate reduction December 2025 — CONFIRMED via Gain Therapeutics press release

**Issues found:**

No factual errors identified. The file accurately states the deal terms, correctly identifies the scientific risks (GBA2 LOF diseases), and accurately characterizes the competitive landscape.

**Action:** No corrections required.

---

### 15. Sanofi-ABL-Bio-Deal-Analysis.md

**Deal economics verified:**
- ABL301 deal January 11, 2022 — CONFIRMED
- $75M upfront — CONFIRMED (plus $45M in near-term milestones, not always separately stated)
- Up to $985M total milestones — CONFIRMED
- Deprioritized January 29, 2026 — CONFIRMED (Sanofi Q4 2025 earnings)
- ABL Bio stock -19.5% — CONSISTENT with Korean financial press reporting

**Issues found:**

**ISSUE 1 (LOW):** The Sanofi-ABL-Bio file states the deal date as "January 2022" without specifying January 11. The file summary states "January 2022: $75M upfront, up to $985M milestones, royalties (~$1.06B total)." The $1.06B figure ($75M + $985M) is correct. No material error.

The file also states that GSK's deal with ABL Bio was in "April 2024" — the actual GSK deal was April 2025, not April 2024. However, looking at the file more carefully, the Sanofi-ABL-Bio file states "GSK paid £38.5M upfront, £77.1M near-term, Up to £2.075B ($2.8B) total milestones" and "(PR Newswire, April 2024)." This is an ERROR: the GSK deal was announced April 6, 2025, not April 2024. The Lilly deal was December 2024. The GSK deal postdated the Lilly deal.

**ISSUE 2 (LOW-MEDIUM):** The Sanofi-ABL-Bio file states "GSK (PR Newswire, April 2024)." This date is wrong — the GSK/ABL Bio deal was April 2025. The Lilly deal was December 2024. This matters for the chronological argument in the file about whether GSK/Lilly saw ABL301 Phase 1 data before signing their platform deals. (The Lilly deal in December 2024 was arguably post-Phase 1 data; the GSK deal in April 2025 was definitely post-Phase 1 data.) The file's argument is substantively correct (GSK/Lilly signed after Phase 1), but the April 2024 date for GSK is wrong and should read April 2025.

**Action:** Correct GSK deal date from "April 2024" to "April 2025."

---

## CROSS-FILE CONSISTENCY ISSUES

### A. NCT06944522 Conflict (HIGH)

**Files affected:** Lilly-Prevail-Deal-Analysis.md (incorrect use), Bayer-BlueRock-Cell-Therapy-Analysis.md (correct use)

NCT06944522 is the Phase 3 registration for BlueRock's bemdaneprocel (exPDite-2). It is CORRECTLY cited in the Bayer-BlueRock file. It is INCORRECTLY referenced in the Lilly-Prevail file as if it could apply to PR001, with the file itself noting this is an error. The Lilly-Prevail file needs this NCT removed.

### B. Cerevel Deal Date (LOW)

**Files affected:** AbbVie-Mitokinin-Deal-Analysis.md

The Mitokinin file says Cerevel was acquired "August 2023." Correct: announced December 2023, completed August 2024. The Cerevel file itself correctly states "completed August 2024."

### C. GSK ABL Bio Date (LOW)

**Files affected:** Sanofi-ABL-Bio-Deal-Analysis.md

GSK deal cited as "April 2024" in the Sanofi file — should be April 2025.

### D. Neurocrine-Voyager $4.4B Total (LOW)

**Files affected:** Neurocrine-Voyager-GBA1-Deal-Analysis.md, FINAL-PD-Deal-Landscape-Report.md

The $4.4B total cited in both files is an aggregate across all 4 programs (GBA1 + 3 additional CNS). The GBA1-only total is $175M upfront + $985M development milestones + commercial milestones + royalties. The $4.4B is not verifiable from the press release alone and should be labeled as an "aggregate estimate across all 4 programs."

---

## VERIFIED FACTS (SPOT-CHECKED VIA WEB SEARCH)

The following key claims were confirmed via web search:

| Claim | File | Verification |
|-------|------|-------------|
| AbbVie/Cerevel: $8.7B at $45/share, completed August 1, 2024 | AbbVie-Cerevel | CONFIRMED (AbbVie press release) |
| Emraclidine EMPOWER failure announced November 11, 2024 | AbbVie-Cerevel | CONFIRMED (AbbVie press release) |
| Neurocrine/Voyager: $136M cash + $39M equity at 50% premium, January 9, 2023 | Neurocrine-Voyager | CONFIRMED (GlobalNewsWire) |
| GSK/ABL Bio: £38.5M upfront, up to £2.075B milestones, April 6, 2025 | GSK-ABL-Bio | CONFIRMED (ABL Bio press release) |
| Biogen/Denali: $560M cash + $465M equity = $1.025B upfront, August 2020 | Biogen-Denali | CONFIRMED (GlobalNewsWire) |
| LIGHTHOUSE terminated June 2023, reason: "complexity...completion in 2031" | Biogen-Denali | CONFIRMED (Biogen press release) |
| Novartis/Arrowhead: $200M upfront + up to $2B milestones, September 2, 2025 | Novartis-Arrowhead | CONFIRMED (Arrowhead press release) |
| Minzasolmin ORCHESTRA: 496 patients, failed December 16, 2024 | Novartis-Arrowhead | CONFIRMED (UCB press release) |
| Lilly/Ventyx: $1.2B at $14/share, 62% premium, January 7, 2026 | Lilly-Ventyx | CONFIRMED (Lilly press release) |
| Lilly/Prevail: $880M + $160M CVR = $1.04B, completed January 22, 2021 | Lilly-Prevail | CONFIRMED (Lilly press release) |
| Bayer/BlueRock: $240M + $360M milestones, 40.8% stake pre-existing, 2019 | Bayer-BlueRock | CONFIRMED (FierceBiotech, Bayer) |
| BIAL/LTI: up to $130M, October 1, 2020 | BIAL-Pariceract | CONFIRMED (Business Wire) |
| ACTIVATE trial: NCT05819359, 273 patients, 85 sites, 78 weeks | BIAL-Pariceract | CONFIRMED (NeurologyLive, BioSpace) |
| Roche/Prothena: $30M upfront 2013, $135M earned, up to $620M remaining | Roche-Prothena | CONFIRMED (Prothena IR) |
| AbbVie/Mitokinin: $110M + $545M = $655M, October 5, 2023 | AbbVie-Mitokinin | CONFIRMED (AbbVie press release) |
| Capsida/Lilly: $55M + up to $685M = $740M, January 4, 2023 | Capsida-Lilly | CONFIRMED (Capsida press release) |
| Biogen/Alectos: $15M + $77.5M dev + $630M commercial = $722M, June 2022 | Biogen-Alectos | CONFIRMED (Biogen press release) |
| Sanofi/ABL Bio: $75M upfront + $985M milestones, January 11, 2022 | Sanofi-ABL-Bio | CONFIRMED (ABL Bio press release) |
| Sanofi deprioritized ABL301: January 29, 2026 | Sanofi-ABL-Bio | CONFIRMED (multiple Korean/EU sources) |
| Tavapadon NDA: submitted September 26, 2025 | AbbVie-Cerevel, AbbVie-Mitokinin | CONFIRMED (AbbVie press release) |
| Prasinezumab Phase 3 decision: June 2025 | Roche-Prothena | CONFIRMED (Roche press release June 16, 2025) |
| PADOVA: HR=0.84, p=0.0657; levodopa subgroup HR=0.79, p=0.0431 | Roche-Prothena | CONFIRMED (Roche press release December 2024) |

---

## PRIORITY CORRECTIONS

### Immediate (before using files for investment decisions):

1. **Lilly-Prevail-Deal-Analysis.md:** Remove NCT06944522 from any reference to PR001. This NCT belongs to BlueRock's bemdaneprocel (exPDite-2). If PR001's Phase 3 NCT is known, substitute it.

2. **Sanofi-ABL-Bio-Deal-Analysis.md:** Change "April 2024" to "April 2025" for the GSK/ABL Bio deal date.

3. **AbbVie-Mitokinin-Deal-Analysis.md:** Correct the Cerevel acquisition timing — Mitokinin closed October 2023, Cerevel was announced December 2023 and completed August 2024. The current text says "August 2023" which is wrong for both the announcement and completion dates.

### Low Priority (clarifications, not corrections):

4. **deal-analysis-novartis-arrowhead-aro-snca.md:** Update ORCHESTRA enrollment from "450+" to "496" for precision.

5. **Biogen-Denali-LRRK2-Deal-Analysis.md:** Update LUMA site count from "98 centers" to "113 sites."

6. **Neurocrine-Voyager-GBA1-Deal-Analysis.md / FINAL report:** Add note that $4.4B is aggregate estimate across all 4 programs, not verifiable from the GBA1 press release alone.

7. **GSK-ABL-Bio-Deal-Analysis.md:** Add note that the total milestone value is in GBP (£2.075B); USD equivalents vary from $2.5B to $2.8B by source depending on exchange rate. The $2.8B is a reasonable conversion but should not be stated as precise.

8. **FINAL-PD-Deal-Landscape-Report.md:** Clarify LUMA readout timing (March 2026 = trial completion, not data release; data likely H2 2026). Source or remove the CAP-002 patient death claim.

---

## NOTES ON ANALYTICAL CLAIMS (NOT FACT-CHECKED)

The following are analytical opinions/estimates in the files that are flagged as estimates in the text. These are NOT errors — just noted for completeness:

- Confidence scores (6/10, 7/10, etc.) — editorial judgments, not factual claims
- Peak sales estimates (e.g., Roche "$3B+ peak sales," Mizuho "$532M peak U.S. sales for tavapadon") — analyst estimates, appropriately attributed
- Probability of Phase 3 success estimates — clearly labeled as estimates with reasoning
- Strategic interpretation of deal structures (e.g., "cheap optionality" for Biogen/Alectos) — analytical opinions

These are all fine and consistent with the user's instruction to "not critique writing style or analytical opinions."

---

*Audit completed February 23, 2026. All web searches conducted on this date. Primary sources cited throughout. Claims marked CONSISTENT are plausible and coherent with multiple secondary sources but not verified against official press releases.*
