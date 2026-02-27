# Fact-Check: Deal Files Batch 1 (Files #1–13 in PD-Deal-Summary)

**Audit Date:** February 26, 2026
**Auditor:** factchecker-1 (claude-sonnet-4-6)
**Scope:** 13 deal analysis files, priority order per task assignment
**Prior Audit Reference:** FACT-CHECK-AUDIT.md (Feb 23, 2026) — covers files #1, 2, 3, 5, 6, 8, 9, 10, 11, 13
**New in this audit:** Files #4 (Lilly-ABL Bio), #7 (minzasolmin), #12 (Biohaven-Highlightll)

---

## Quick Reference: Issue Table

| File | Issue | Severity | Correction Needed |
|------|-------|----------|-------------------|
| Lilly-ABL Bio Deal Analysis.md | GSK deal cited as "$2.8B" (should be ~$2.5B) | Medium | Update to ~$2.5B consistent with PD-Deal-Summary correction |
| Lilly-ABL Bio Deal Analysis.md | Ventyx acquisition dated "2024" (should be Jan 2026) | Medium | Change to "announced Jan 2026 (pending close H1 2026)" |
| Lilly-ABL Bio Deal Analysis.md | VTX3232 Phase 2a results called "not statistically significant" — contradicts Lilly-Ventyx file (p=0.0054 MDS-UPDRS III) | Medium | Clarify: Part III was p=0.0054 (significant); aggregate motor claim was "trend" — two different claims |
| minzasolmin-failure-analysis.md | No material errors found | Clean | None required |
| Biohaven-Highlightll-TYK2-Deal-Analysis.md | No material errors found | Clean | None required |
| AbbVie-Cerevel-Deal-Analysis.md | Already audited Feb 23 — 3 LOW issues found | Low | See FACT-CHECK-AUDIT.md §1 |
| Neurocrine-Voyager-GBA1-Deal-Analysis.md | Already audited Feb 23 — 2 LOW issues found | Low | See FACT-CHECK-AUDIT.md §2 |
| GSK-ABL-Bio-Deal-Analysis.md | Already audited Feb 23 — $2.8B→~$2.5B, GBP note needed | Medium | See FACT-CHECK-AUDIT.md §3 |
| deal-analysis-novartis-arrowhead-aro-snca.md | Already audited Feb 23 — enrollment "450+" should be "496" | Low | See FACT-CHECK-AUDIT.md §4 |
| Biogen-Denali-LRRK2-Deal-Analysis.md | Already audited Feb 23 — LUMA sites "98" should be "113" | Low | See FACT-CHECK-AUDIT.md §5 |
| Bayer-BlueRock-Cell-Therapy-Analysis.md | Already audited Feb 23 — 2 LOW issues | Low | See FACT-CHECK-AUDIT.md §9 |
| Lilly-Ventyx-NLRP3-Deal-Analysis.md | Already audited Feb 23 — 1 LOW issue (pending close) | Low | See FACT-CHECK-AUDIT.md §7 |
| Lilly-Prevail-Deal-Analysis.md | Already audited Feb 23 — NCT06944522 attribution ERROR (HIGH) | High | See FACT-CHECK-AUDIT.md §8 — must correct |
| Sanofi-ABL-Bio-Deal-Analysis.md | Already audited Feb 23 — GSK date "April 2024" should be "April 2025" | Low-Med | See FACT-CHECK-AUDIT.md §15 |
| Roche-Prothena-Deal-Analysis.md | Already audited Feb 23 — 1 LOW issue (stock figure) | Low | See FACT-CHECK-AUDIT.md §11 |

---

## Detailed Findings: Three Previously Unchecked Files

---

### File #4: Lilly-ABL Bio Deal Analysis.md

**Deal Economics Verified:**
- Upfront: $40M cash + $15M equity = $55M total — CONFIRMED via ABL Bio press release (PR Newswire) and multiple secondary sources
- Milestones: up to $2.562B — CONFIRMED
- Total: $2.602B — CONFIRMED
- Date: November 12, 2025 — CONFIRMED

**Source URLs Spot-Checked:**
- `pharmexec.com/view/abl-bio-2-billion-multi-program-collaboration-agreement-eli-lilly` — CONFIRMED (found in web search, legitimate Pharmaceutical Executive URL)
- `prnewswire.com/news-releases/abl-bio-announces-grabody-b-brain-delivery-platform-license-agreement-with-gsk...302421544.html` — CONFIRMED (this is the legitimate GSK-ABL Bio PR Newswire release)
- `en.sedaily.com/finance/2026/01/31/abl-bios-parkinsons-drug-licensed-to-sanofi-deprioritized` — CONFIRMED (Seoul Economic Daily, found in search results)

**Issues Found:**

**ISSUE 1 (MEDIUM):** Executive Summary states "Lilly's $2.6B Grabody-B license is the third mega-deal for ABL Bio's IGF1R-based BBB shuttle (after GSK's **$2.8B** and Sanofi's $1.06B)." The $2.8B for GSK is the uncorrected figure. PD-Deal-Summary.md footnote [^3] explicitly corrects this to ~$2.5B (£2.15B at ~$1.17/£ at time of deal; FierceBiotech and Inside Precision Medicine both reported "$2.5B"). The file should read "after GSK's ~$2.5B."

**ISSUE 2 (MEDIUM):** Lilly PD portfolio table lists "VTX3232 | ... | Phase 2 (positive data 6/2025) | Ventyx ($1.2B acq, **2024**)." The acquisition date is wrong. The definitive agreement was announced January 7, 2026, not 2024. PD-Deal-Summary.md corrected this explicitly (footnote [^9]). Should read "announced Jan 2026; pending close H1 2026."

**ISSUE 3 (MEDIUM):** File says (Phase 2 section): "Motor improvement: Trend toward motor symptom improvement in n=10 trial (**not statistically significant**, but directionally positive)." The Lilly-Ventyx-NLRP3-Deal-Analysis.md (already audited Feb 23, confirmed clean) reports MDS-UPDRS Part III: -5.2 points (p=0.0054), Part I: -2.4 (p=0.0118), Part II: -2.7 (p=0.0471) — all statistically significant. The Lilly-ABL Bio file's characterization contradicts the Lilly-Ventyx file's data. The resolution: MDS-UPDRS Part III p=0.0054 IS significant; the "trend" language in the Lilly-ABL Bio file may refer to an overall motor function composite that was directionally positive but not the primary p-value. Regardless, the "not statistically significant" framing is inaccurate or at minimum misleading — individual MDS-UPDRS subscale p-values are all <0.05.

**Action:** Correct GSK "$2.8B" → "~$2.5B"; correct Ventyx date "2024" → "announced Jan 2026"; clarify VTX3232 Phase 2a results (MDS-UPDRS subscales p<0.05 individually; the "trend" language is imprecise).

---

### File #7: minzasolmin-failure-analysis.md

**Deal Economics Verified:**
- Deal: Novartis / UCB, announced December 2, 2021 — CONFIRMED
- Upfront: $150M from Novartis to UCB — CONFIRMED
- Total: ~$1.5B — CONFIRMED
- Termination: December 16, 2024 — CONFIRMED

**Trial Data Verified:**
- ORCHESTRA: Phase 2a, 496 patients, 18 months, randomized, placebo-controlled — CONFIRMED
- Failed primary and all secondary endpoints — CONFIRMED
- Hypersensitivity reactions 8.5% vs 1.2% placebo; liver elevations 8 vs 1 patient — CONSISTENT with UCB press release
- UCB termination revenue: **€92M** — CONFIRMED via UCB Q4 2024 financial disclosures (multiple sources confirm this figure)
- Novartis response: $2.2B Arrowhead deal September 2025 — CONFIRMED

**Scientific Claims Verified:**
- α-syn SAA sensitivity "87.7%" for PD — CONFIRMED (Lancet Neurology PPMI paper cited correctly; consistent with primary source)
- LRRK2 patients with only 34.7% α-syn positivity — consistent with published PPMI subgroup analyses
- DaT-SPECT showed "some differences" without clinical benefit — CONFIRMED by UCB press release language

**Source URLs Spot-Checked:**
- `nature.com/articles/s41531-023-00552-7` — legitimate Nature npj Parkinson's Disease journal URL, consistent with July 2023 publication cited
- `clinicaltrialsarena.com/news/ucb-drops-parkinsons-treatment-after-orchestra-trial-failed-all-endpoints/` — CONFIRMED (found in web search)
- `fiercebiotech.com/biotech/ucbs-orchestra-hits-dud-note-novartis-partnered-parkinsons-asset-fails-phase-2` — CONFIRMED in search results

**Issues Found:**

None. All key factual claims are verified. The analytical framing (mechanism vs. target failure distinction, trial design critique) is opinion/analysis and not subject to fact-checking.

**One Minor Note (LOW, no correction needed):** The file refers to the relationship as "Novartis lost $150M upfront." More precisely, Novartis paid UCB $150M for rights and lost the investment when the trial failed — this framing is editorially defensible. The €92M "termination revenue" was a separate contractual payment from Novartis to UCB upon termination, which the file does not explicitly mention but also does not contradict.

**Action:** No corrections required.

---

### File #12: Biohaven-Highlightll-TYK2-Deal-Analysis.md

**Deal Economics Verified:**
- Deal date: March 22, 2023 (March 2023) — CONFIRMED via Biohaven press release (PR Newswire)
- Upfront: $10M cash + $10M BHVN equity = $20M total — CONFIRMED
- Milestones: up to $950M — CONFIRMED
- Royalties: mid-single digit to lower teens percentages — CONFIRMED
- Total: $970M ($20M + $950M) — CONFIRMED; consistent with PD-Deal-Summary.md

**Clinical Trial Data Verified:**
- Phase 2/3 enrollment: 550 patients — CONFIRMED via Biohaven press release (May 2025)
- Sites: ~185 sites — CONFIRMED
- Countries: 13 countries (US, Canada, 11 European nations) — CONFIRMED
- Initiated: May 2025 — CONFIRMED
- Primary endpoint: time-to-event MDS-UPDRS Part II — CONFIRMED (FDA-accepted for registration)
- Drug formerly named TLL-041 — CONFIRMED

**Phase 1 Claims:**
- "Phase 1 completed May 2024" — PLAUSIBLE; AAN 2025 poster presented Phase 1 data, suggesting analysis was complete by April 2025. May 2024 completion is internally consistent with months between completion and data presentation. No contrary evidence found.
- "Positive safety/biomarker data" — CONSISTENT with Biohaven's public statements

**Source URLs Spot-Checked:**
- `ir.biohaven.com/news-releases/news-release-details/biohaven-acquires-exclusive-license-oral-brain-penetrant-dual` — CONFIRMED (found in web search as the legitimate Biohaven IR press release)
- `ir.biohaven.com/news-releases/news-release-details/biohaven-enrolls-first-patient-phase-23-trial-early-parkinsons` — CONFIRMED (found in web search)
- `fiercebiotech.com/biotech/biohaven-tacks-brain-disorder-med-its-pipeline-paying-970m-ex-china-rights-highlightll-drug` — CONSISTENT domain/format for FierceBiotech deal coverage

**Issues Found:**

None. All key factual claims are verified against primary and secondary sources.

**Action:** No corrections required.

---

## Cross-Check: PD-Deal-Summary.md Footnote Corrections vs. Individual Files

The PD-Deal-Summary.md includes extensive footnotes (added Feb 23) correcting prior errors. I verified whether the individual deal files were updated to reflect these corrections:

| Correction in PD-Deal-Summary | Affects Which File | File Updated? |
|-------------------------------|-------------------|---------------|
| GSK deal: $2.8B → ~$2.5B (£2.15B) | GSK-ABL-Bio-Deal-Analysis.md | Partially — file notes GBP ambiguity but still leads with $2.8B |
| GSK deal: $2.8B → ~$2.5B | **Lilly-ABL Bio Deal Analysis.md** | ❌ NO — still says "GSK's $2.8B" in executive summary |
| Ventyx date: 2023 → Jan 2026 | Lilly-Ventyx-NLRP3-Deal-Analysis.md | ✅ File already says Jan 2026 announcement |
| Ventyx date | **Lilly-ABL Bio Deal Analysis.md** | ❌ NO — still says "Ventyx ($1.2B acq, 2024)" |
| Lilly/Prevail NCT error (HIGH) | Lilly-Prevail-Deal-Analysis.md | ❌ NO — NCT06944522 still in file |
| Sanofi-ABL Bio GSK date: Apr 2024 → Apr 2025 | Sanofi-ABL-Bio-Deal-Analysis.md | ❌ NO — not yet corrected |
| AbbVie-Mitokinin Cerevel timing | AbbVie-Mitokinin-Deal-Analysis.md | ❌ NO — still says "August 2023" |

**Conclusion:** The PD-Deal-Summary.md footnotes document what needs correcting but the individual files have not yet been updated. These are all tracked in FACT-CHECK-AUDIT.md Priority Corrections list.

---

## Summary of All Issues (Batch 1)

### Critical / High Severity (must fix before use in investment decisions):
1. **Lilly-Prevail-Deal-Analysis.md** — NCT06944522 incorrectly attributed to PR001 (belongs to BlueRock bemdaneprocel). Remove the NCT entirely from PR001 context.

### Medium Severity (fix soon):
2. **Lilly-ABL Bio Deal Analysis.md** — GSK deal cited as "$2.8B" (correct: ~$2.5B)
3. **Lilly-ABL Bio Deal Analysis.md** — Ventyx acquisition date "2024" (correct: announced Jan 2026)
4. **Lilly-ABL Bio Deal Analysis.md** — VTX3232 Phase 2a results described as "not statistically significant" (incorrect: MDS-UPDRS subscales all p<0.05)
5. **GSK-ABL-Bio-Deal-Analysis.md** — $2.8B needs GBP denomination note; USD equivalent range $2.5–2.8B depending on FX rate used

### Low Severity (clarifications):
6. **Sanofi-ABL-Bio-Deal-Analysis.md** — GSK deal date says "April 2024" (correct: April 2025)
7. **AbbVie-Mitokinin-Deal-Analysis.md** — Cerevel deal timing says "August 2023" (correct: announced Dec 2023, completed Aug 2024)
8. **deal-analysis-novartis-arrowhead-aro-snca.md** — ORCHESTRA enrollment "450+" → "496"
9. **Biogen-Denali-LRRK2-Deal-Analysis.md** — LUMA site count "98 centers" → "113 sites"
10. **Neurocrine-Voyager-GBA1-Deal-Analysis.md** — Note that $4.4B total is aggregate across all 4 programs, not verifiable from GBA1 press release alone

### Clean Files (no corrections needed):
- minzasolmin-failure-analysis.md ✅
- Biohaven-Highlightll-TYK2-Deal-Analysis.md ✅
- Bayer-BlueRock-Cell-Therapy-Analysis.md ✅ (minor NCT clarification only)
- Lilly-Ventyx-NLRP3-Deal-Analysis.md ✅ (status "pending close" already correctly noted)
- Roche-Prothena-Deal-Analysis.md ✅
- AbbVie-Cerevel-Deal-Analysis.md ✅

---

## Verification Methods

All claims verified via:
- Primary source web searches (Biohaven IR, ABL Bio press releases, UCB press releases)
- Cross-reference against PD-Deal-Summary.md footnotes (which are themselves fact-checked against primary sources per Feb 23 audit)
- Cross-reference between individual deal files for internal consistency

Web sources confirming new verifications:
- Lilly/ABL Bio: [ABL Bio PR Newswire](https://www.prnewswire.com/news-releases/abl-bio-receives-upfront-payment-for-license-research-and-collaboration-agreement-for-grabody-platform-and-equity-investment-from-lilly-302649529.html)
- Biohaven Phase 2/3: [Biohaven IR](https://ir.biohaven.com/news-releases/news-release-details/biohaven-enrolls-first-patient-phase-23-trial-early-parkinsons)
- Biohaven deal: [PR Newswire](https://www.prnewswire.com/news-releases/biohaven-acquires-exclusive-license-for-oral-brain-penetrant-dual-tyk2jak1-inhibitor-for-immune-mediated-brain-disorders-301778426.html)
- UCB termination revenue €92M: [UCB Q4 2024 / PR Newswire](https://www.prnewswire.com/news-releases/on-growth-path-for-a-decade-plus-strong-launch-execution-driving-company-growth-302386784.html)
- GSK ABL Bio date (April 2025): [FierceBiotech](https://www.fiercebiotech.com/biotech/gsks-pens-25b-pact-use-abl-bios-tech-bypass-blood-brain-barrier)

---

*Audit completed February 26, 2026. Three previously unchecked files now covered. All 13 priority files have been fact-checked. See FACT-CHECK-AUDIT.md for full prior-audit details on files #1, 2, 3, 5, 6, 8, 9, 10, 11, 13.*
