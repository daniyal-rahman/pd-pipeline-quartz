---
drug_name: "UX-DA001"
aliases: []
target: "dopaminergic neuron replacement"
mechanism: "Autologous iPSC-derived midbrain dopaminergic neural precursor cells reprogrammed from patient peripheral blood, transplanted into putamen via stereotactic surgery"
modality: "cell therapy (iPSC autologous)"
developer: "UniXell Biotechnology"
company_type: "startup"
publicly_traded: false
stage: "Phase 1"
status: "Active"
patient_population: "Moderate to severe PD with motor fluctuations"
route_of_administration: "intracranial (stereotactic injection)"
key_biomarkers: ["18F-FP-CIT PET (dopamine transporter)", "MDS-UPDRS Part III", "ON/OFF time diary"]
confidence_rating: "4/10"
next_catalyst: "Phase 1 multi-patient safety/efficacy data"
catalyst_date: "2026-2027"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# UX-DA001

## Summary

UX-DA001 is China's first registration-directed autologous iPSC-derived cell therapy for Parkinson's disease, developed by UniXell Biotechnology (startup, private, Shanghai). First patient dosed March 2025 at Ruijin Hospital; 6-month data presented at MDS Congress (October 2025) showed a 21-point MDS-UPDRS Part III improvement in OFF state (>45% improvement), 3.6 fewer daily OFF hours, and PET evidence of graft survival with increasing dopamine transporter signal — all without immunosuppression. UX-DA001 holds dual IND approval (NMPA December 2024, FDA February 2025), positioning UniXell for parallel China/US development. The key differentiator from [[anpd001|ANPD001]] (Aspen Neuroscience) is the blood-derived reprogramming source (peripheral blood vs. skin biopsy) and the China-first regulatory strategy. If multi-patient Phase 1 data replicate the single-patient signal, UniXell becomes a serious contender alongside [[anpd001]] in the autologous iPSC space and a potential China-based partner for global pharma; if results attenuate or safety issues emerge with additional patients, the autologous iPSC thesis narrows back to [[anpd001]] alone and the field tilts further toward allogeneic approaches like [[bemdaneprocel]].

## Notes

### Science
- Patient peripheral blood mononuclear cells are reprogrammed into iPSCs, then differentiated into midbrain dopaminergic neural precursor cells (human midbrain DA-NPCs) and transplanted into the putamen via minimally invasive stereotactic surgery
- Autologous approach eliminates immunosuppression requirement — a significant advantage over allogeneic competitors like [[bemdaneprocel]] (ESC-derived, requires chronic immunosuppression)
- Uses peripheral blood as the cell source, unlike [[anpd001|ANPD001]] which derives iPSCs from skin biopsy fibroblasts — blood draws are less invasive and potentially more scalable
- Built on four proprietary technology platforms: (1) iPSC reprogramming, (2) stem cell differentiation, (3) SISBAR lineage tracing technology for quality control, and (4) high-precision gene editing
- SISBAR lineage tracing is a distinguishing feature — allows tracking of cell lineage during differentiation, potentially reducing off-target cell populations in the graft
- The core scientific question for all iPSC-derived cell therapies remains: do transplanted DA neurons survive long-term, integrate into host circuitry, and maintain dopamine release without tumorigenesis or graft-induced dyskinesia?
- Autologous iPSC manufacturing requires weeks per patient batch — the fundamental scalability challenge shared with [[anpd001]]

### Clinical

**Phase 1 (China)** | NCT06778265 | N=TBD (first patient dosed) | Moderate to severe PD
- **Primary endpoint:** Safety, tolerability, and preliminary efficacy
- **First patient (6-month data, MDS Congress Oct 2025):**
  - Female patient with moderate-to-severe PD on four anti-PD medications with significant motor fluctuations
  - MDS-UPDRS Part III: improved 21 points in OFF state, 9 points in ON state (>45% improvement in both)
  - Daily OFF time reduced by 3.6 hours; ON time without dyskinesia increased by 3.3 hours
  - 18F-FP-CIT PET: consecutively increased uptake in bilateral putamen — objective evidence of dopamine transporter expression, cell survival, and functional integration
  - Non-motor symptoms improved on NMSS and PDQ-39 quality of life scales
  - No serious adverse events; no cell-related adverse events
- **Status:** Active, enrolling
- **Interpretation:** Single-patient data only — promising but must be contextualized. The 21-point OFF improvement exceeds the 8-10 point MCID for MDS-UPDRS III and is comparable to deep brain stimulation effects. PET evidence of graft integration is the strongest signal. Multi-patient data are required to assess reproducibility and distinguish drug effect from placebo/surgical effect.

**US IND** | NCT TBD | FDA IND cleared February 2025
- **Status:** IND approved; US trial site(s) and enrollment timeline not yet disclosed
- **Interpretation:** Dual China/US IND is unusual for a Chinese startup and signals intent for global registration, not just a China-only asset

### Financial
- **Funding:** Multiple rounds from notable Chinese and international investors including Hillhouse Capital, CDH Investments, Fosun Group, Sherpa Healthcare Partners, TF Capital, Tianshi Capital, KSCY Holding Group, Chinese Academy of Sciences Venture Capital, PDVC, Tasly Capital, and Tencent Investment (~14 known investors total)
- **Total raised:** Not publicly disclosed; investor roster suggests total funding in the range of $50-150M based on comparable Chinese cell therapy companies
- **Valuation:** Not publicly disclosed
- **Infrastructure:** 4,000 m2 R&D center and GMP manufacturing facilities in Shanghai
- **Pipeline breadth:** Also developing UX-DA002 (allogeneic iPSC-derived cell therapy for PD), with NMPA IND application accepted — having both autologous and allogeneic programs de-risks the platform
- **Comparable deals:** Bayer acquired BlueRock ([[bemdaneprocel]]) for ~$1B ($240M upfront + $360M milestones) in 2019 at Phase 1. Aspen Neuroscience ([[anpd001]]) has raised >$340M through Series C with $115M closed November 2025. UniXell is earlier-stage but the dual-IND and first-in-China positioning could attract either a global pharma China partnership or cross-border licensing interest.
- Company press release explicitly invites "discussions with pharmaceutical companies and investors for strategic partnerships" — a signal they are actively seeking a partner or further financing

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "dopaminergic neuron replacement") AND file.name != "ux-da001"
SORT stage DESC
```

- [[bemdaneprocel]] (BlueRock/Bayer) is the most advanced cell therapy competitor, now in Phase 3 (exPDite-2, first patient September 2025). It uses allogeneic ESC-derived cells — manufacturing is more scalable but requires chronic immunosuppression. 36-month Phase 1 data showed 17.9-point MDS-UPDRS III improvement in high-dose cohort, comparable to UX-DA001's single-patient 21-point improvement
- [[anpd001|ANPD001]] (Aspen Neuroscience) is the closest direct competitor — also autologous iPSC-derived, also in Phase 1/2. ASPIRO 6-month data from three patients showed 45% MDS-UPDRS III OFF improvement and no immunosuppression required. Aspen uses skin biopsy-derived iPSCs vs. UniXell's blood-derived iPSCs; Aspen is US-based with $340M+ raised, while UniXell is China-based with a dual-IND strategy
- The autologous vs. allogeneic debate is the central competitive axis: autologous (UX-DA001, [[anpd001]]) avoids immunosuppression but faces COGS and scalability challenges; allogeneic ([[bemdaneprocel]]) is scalable but requires immunosuppression and carries rejection risk
- Other cell therapy programs include [[stem-pd|STEM-PD]] (academic, ESC-derived, Europe) and potentially CiRA-backed programs in Japan
- If [[bemdaneprocel]] Phase 3 succeeds, autologous approaches must justify their higher cost/complexity premium via superior long-term graft survival or the absence of immunosuppression. If allogeneic fails on immunogenicity, autologous programs like UX-DA001 and [[anpd001]] become the de facto path forward

## Analysis

UX-DA001 is a Phase 1 autologous iPSC cell therapy with striking single-patient 6-month data but essentially no statistical power — the n=1 results, while encouraging, cannot be separated from surgical placebo effects. The 21-point MDS-UPDRS III OFF improvement and PET evidence of graft integration are the right signals, but the cell therapy field has repeatedly seen early promise attenuate in larger cohorts. The meaningful data inflection will come when multi-patient results are available, likely in late 2026 or 2027.

**Analytical estimate — probability of technical success through Phase 1: 55-65%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Cell therapy Phase 1 success (safety/tolerability) is generally high (~70%) since primary endpoints are safety
- Adjustments upward: single-patient data clean with no AEs (+5%), PET imaging confirms graft survival (+5%), dual China/US IND regulatory validation (+5%)
- Adjustments downward: n=1 only (-5%), autologous manufacturing complexity and patient-to-patient variability (-10%), Chinese startup with no prior clinical track record (-5%)
- Net: ~55-65% for Phase 1 success; probability of eventual approval is substantially lower (~5-10%) given the field's early stage and the additional hurdles of Phase 2/3 in a sham-controlled surgical trial

**Signal analysis:**
- The dual China/US IND is the most notable strategic signal. Chinese biotech companies often pursue NMPA-only for cell therapies, especially given China's more favorable regulatory pathway for stem cell products. Obtaining an FDA IND signals ambition beyond China and suggests the company is building to a standard that could support global partnerships.
- The investor roster (Hillhouse, CDH, Fosun, Tencent) represents tier-1 Chinese healthcare capital — these are sophisticated investors who have backed successful Chinese biotech companies through IPO and beyond.
- The parallel development of UX-DA002 (allogeneic) alongside UX-DA001 (autologous) is a hedging strategy that mirrors the broader field debate. If autologous proves unscalable, UniXell has an allogeneic backup; if allogeneic fails on immunosuppression requirements, the autologous program gains value.
- The explicit invitation for partnership discussions in the MDS Congress press release suggests the company is at or approaching a financing inflection point — the Phase 1 data are being used to attract either a global pharma partner or a larger financing round.

## References

### Clinical Trials
- [UX-DA001 Phase 1](https://clinicaltrials.gov/ct2/show/NCT06778265) — NCT06778265

### Key Publications
- [UX-DA001 6-month case study | MDS Congress 2025 (poster/presentation)](https://www.prnewswire.com/news-releases/unixell-biotech-reported-a-case-study-of-ux-da001-an-ipsc-derived-autologous-cell-therapy-for-parkinson-diseases-at-mds-congress-2025-302586177.html)

### Press Releases & Filings
- [UniXell announces first patient dosed in Phase 1 study (May 2025)](https://www.prnewswire.com/news-releases/unixell-biotechnology-announces-the-first-patient-dosed-with-ux-da001-an-investigational-autologous-ipsc-based-cell-therapy-for-the-treatment-of-parkinsons-disease-in-its-phase-1-study-302464203.html)
- [UX-DA001 6-month follow-up data at MDS Congress 2025 (Oct 2025)](https://www.prnewswire.com/news-releases/unixell-biotech-reported-a-case-study-of-ux-da001-an-ipsc-derived-autologous-cell-therapy-for-parkinson-diseases-at-mds-congress-2025-302586177.html)
- [Early results show symptom gains in first patient | NeurologyLive](https://www.neurologylive.com/view/early-results-show-symptom-gains-first-patient-dosed-ux-da001-cell-therapy-pd)
- [First Parkinson's patient dosed in UniXell study | Parkinson's News Today](https://parkinsonsnewstoday.com/news/first-parkinsons-trial-participant-dosed-unixell-stem-cell-therapy-study/)

### Regulatory & Market
- [Shanghai FTZ biotech breakthrough in PD treatment | Pudong Gov](https://english.pudong.gov.cn/chinashftz/2025-01/03/c_1067771.htm)
