---
drug_name: "NouvNeu001"
aliases: ["NN001"]
target: "dopaminergic neuron replacement (cell therapy)"
mechanism: "Chemically induced allogeneic iPSC-derived dopaminergic progenitor cells transplanted bilaterally into putamen to replace neurons lost in PD"
modality: "cell therapy (iPSC allogeneic)"
developer: "iRegene Therapeutics"
company_type: "startup"
publicly_traded: false
stage: "Phase 1/2"
status: "Active"
patient_population: "Mid-to-late stage PD"
route_of_administration: "intracranial (bilateral stereotactic injection into putamen)"
key_biomarkers: ["MDS-UPDRS Part III", "18F-DOPA PET (graft survival)", "DaT-SPECT"]
confidence_rating: "5/10"
next_catalyst: "China Phase 2 readout; US Phase 1 data"
catalyst_date: "Q4 2026 - 2027"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/iregene-therapeutics]]"
---

# NouvNeu001

## Summary

NouvNeu001 is the first allogeneic iPSC-derived cell therapy to hold both FDA Fast Track (August 2025) and RMAT (January 2026) designations, developed by iRegene Therapeutics (startup, private, Chengdu/Wuhan-based). China Phase 1 data showed striking MDS-UPDRS Part III improvements -- 30.6 points OFF (53% improvement) and 12.9 points ON (55% improvement) in the low-dose cohort at 12 months -- with PET-confirmed graft survival and no immunosuppression required after 6 months. A multicenter Phase 2 is underway in China (NCT06167681, launched April 2025) with readout expected by Q4 2026, and a US Phase 1 began enrollment in Q3 2025. The chemical induction platform differentiates from [[bemdaneprocel]]'s ESC-derived approach and [[anpd001|ANPD001]]'s autologous iPSC approach by using small-molecule reprogramming rather than transcription factors, which iRegene claims improves manufacturing scalability and cost. If the Phase 2 replicates Phase 1 motor improvements in a controlled setting, the dual FDA designations create a fast path to accelerated approval. If efficacy attenuates or immunogenicity emerges at longer follow-up, the advantage shifts back to [[bemdaneprocel]] (ESC-derived, Phase 3, Bayer-backed) and [[anpd001|ANPD001]] (autologous, no rejection risk).

## Notes

### Science
- NouvNeu001 consists of allogeneic iPSC-derived dopaminergic progenitor cells generated using iRegene's proprietary "chemical induction" platform -- small-molecule compounds guide cell fate reprogramming instead of viral transcription factor delivery, reducing insertional mutagenesis risk
- Transplanted cells are injected bilaterally into the posterior putamen via stereotactic surgery using a single injection trajectory per hemisphere; cells are designed to engraft, mature into functional dopaminergic neurons, integrate with host circuitry, and restore endogenous dopamine production
- Key differentiator: immunosuppression withdrawal at 6 months post-transplant with maintained safety and efficacy -- a notable finding for an allogeneic product, where immune rejection is a central concern. If reproducible, this eliminates a major disadvantage vs. autologous approaches like [[anpd001|ANPD001]]
- The "AI + chemical induction" platform reportedly enables higher manufacturing efficiency and lower cost vs. traditional iPSC differentiation protocols, addressing the COGS problem that limits cell therapy scalability
- Open scientific questions: (1) durability of graft survival beyond 15 months, (2) mechanism of apparent immune tolerance without sustained immunosuppression, (3) whether chemical induction yields functionally equivalent neurons to transcription factor-derived cells, (4) risk of graft-induced dyskinesia at higher doses or longer follow-up

### Clinical

**China Phase 1/2 (Phase 1 portion)** | NCT06167681 | N=not disclosed | Mid-to-late stage PD
- **Primary endpoint:** Safety, tolerability, and efficacy (MDS-UPDRS Part III)
- **Low-dose cohort (12 months):** OFF improvement of 30.6 points (52.82% from baseline); ON improvement of 12.9 points (54.67% from baseline)
- **High-dose cohort (9 months):** OFF improvement of 23.3 points; ON improvement of 9.67 points
- **Safety:** Excellent safety/tolerability through 15 months; no cell product-related adverse effects; immunosuppression discontinued after 6 months without rejection
- **Imaging:** PET confirmed long-term engraftment, survival, and maturation of transplanted cells
- **Status:** Phase 1 complete; Phase 2 multicenter portion launched April 2025 (Beijing Hospital, Zhongnan Hospital)
- **Interpretation:** Motor improvements are large in absolute magnitude and directionally encouraging, but lack of controlled comparator, small undisclosed patient numbers, and open-label design limit interpretability. The immunosuppression-free window after 6 months is the most intriguing signal -- if confirmed in Phase 2, it is a paradigm shift for allogeneic cell therapy.

**China Phase 2 (multicenter)** | NCT06167681 | N=TBD | Mid-to-late stage PD
- **Primary endpoint:** TBD (likely safety + MDS-UPDRS Part III)
- **Status:** First patient dosed April 2025; expected completion by Q4 2026
- **Interpretation:** Will provide larger dataset and potentially controlled design to validate Phase 1 signals

**US Phase 1/2** | IND approved June 2024 | NCT TBD | Mid-to-late stage PD
- **Primary endpoint:** Safety, tolerability, efficacy
- **Status:** FDA IND cleared June 2024; FDA Fast Track (August 2025); FDA RMAT (January 2026); patient enrollment began Q3 2025
- **Interpretation:** Dual FDA designations (FTD + RMAT) provide early and frequent agency interaction, potential accelerated approval, and priority review -- the strongest regulatory tailwind of any iPSC-derived PD therapy

**NouvNeu003 (early-onset PD variant)** | Phase 1 initiated December 2023
- Separate formulation targeting early-onset PD; limited data disclosed

### Financial
- **Total raised:** >RMB 300M (~$40M USD) through Series B+ (September 2025), described as the largest single financing in China's iPSC sector
- **Series B+ investors:** Northern Light Venture Capital, Chuangjing Capital, OneHealth Haihe Capital (co-leads)
- **Use of proceeds:** Global clinical development of NouvNeu001, manufacturing scale-up, team expansion, and development of NouvSight001 (retinal degeneration)
- **Valuation:** Not disclosed publicly
- **Context:** $40M total raised is modest relative to [[anpd001|Aspen Neuroscience's]] >$340M (including $115M Series C) and [[bemdaneprocel|BlueRock's]] ~$1B Bayer acquisition. China-origin cost structure partially offsets the gap -- labor, manufacturing, and trial costs are substantially lower in China
- **No big pharma partner** -- contrast with [[bemdaneprocel]] (Bayer) and [[anpd001|ANPD001]] (Kite/Gilead Series C participation). A partnership deal post-Phase 2 data is a likely catalyst

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[sana-program]] | Preclinical | Deprioritized | Sana Biotechnology | cell therapy (iPSC allogeneic) |
| [[alc01]] | Phase 1 | Active | iCamuno Biotherapeutics | cell therapy (iPSC allogeneic) |
| [[autologous-mdaps]] | Phase 1 | Active | McLean Hospital / Neuroregeneration Research Institute (NRI) | cell therapy (iPSC autologous) |
| [[cellino-ipsc]] | Phase 1 | Active | Cellino Biotech | platform |
| [[rndp-001]] | Phase 1 | Active | Kenai Therapeutics | cell therapy (iPSC allogeneic) |
| [[ux-da001]] | Phase 1 | Active | UniXell Biotechnology | cell therapy (iPSC autologous) |
| [[anpd001]] | Phase 1/2 | Active | Aspen Neuroscience | cell therapy (iPSC autologous) |
| [[kyoto-ipsc]] | Phase 1/2 | Active | CiRA (Kyoto University) / Sumitomo Pharma | cell therapy (iPSC allogeneic) |
| [[nouvneu001]] | Phase 1/2 | Active | iRegene Therapeutics | cell therapy (iPSC allogeneic) |
| [[sizhe-biopharma]] | Phase 1/2 | Active | XellSmart / Shize Bio (士泽生物) | cell therapy (iPSC allogeneic) |
| [[stem-pd]] | Phase 1/2 | Active | Lund University / University of Cambridge | cell therapy (ESC) |
| [[ted-a9]] | Phase 1/2 | Active | S.BIOMEDICS | cell therapy (ESC) |
| [[cbt-npc]] | Phase 2 | Active | CHA Biotech | cell therapy (ESC) |
| [[bemdaneprocel]] | Phase 3 | Active | BlueRock Therapeutics | cell therapy (ESC) |
| [[raguneprocel]] | NDA Filed | Active | Sumitomo Pharma / RACTHERA | cell therapy (iPSC allogeneic) |

- [[bemdaneprocel]] (BlueRock/Bayer) is the most advanced competitor: ESC-derived (not iPSC), Phase 3 sham-controlled trial (exPDite-2), Bayer acquisition provides unlimited capital. Uses hESC source cells rather than iPSC, avoiding reprogramming-related concerns but facing embryonic sourcing limitations and requiring 12 months of immunosuppression
- [[anpd001|ANPD001]] (Aspen Neuroscience) is the autologous iPSC competitor: patient-specific cells eliminate rejection risk entirely but face severe COGS and scalability constraints. $115M Series C with Kite/Gilead participation signals commercial manufacturing interest
- NouvNeu001 occupies a unique niche: allogeneic iPSC with apparent immune tolerance (no immunosuppression after 6 months). If this finding holds, it combines the scalability of allogeneic with the immune safety of autologous -- the best of both worlds
- China-origin development is a double-edged sword: lower costs enable faster iteration, but FDA regulatory path requires bridging studies, and Western investor/partner skepticism toward China-origin therapies creates a discount
- Manufacturing differentiation: chemical induction reportedly avoids viral vectors and transcription factors, potentially simplifying CMC (chemistry, manufacturing, controls) review and enabling lower COGS at scale

## Analysis

NouvNeu001 is a compelling dark horse in the PD cell therapy race. The Phase 1 motor improvements (30+ point MDS-UPDRS Part III OFF improvement) are headline-grabbing and exceed the signals seen in [[bemdaneprocel]]'s Phase 1 (though cross-trial comparisons are unreliable given different patient populations, designs, and endpoints). The real differentiator is the immunosuppression withdrawal at 6 months -- if this is reproducible and durable, it resolves the central objection to allogeneic cell therapy and positions NouvNeu001 as potentially best-in-class.

**Analytical estimate -- probability of meaningful Phase 2 success: 25-30%.** This is our assessment, not from a published source. The reasoning:
- Base rate: cell therapy for neurodegeneration has never succeeded in a controlled trial; historical base rate for Phase 2 success in neurology ~30% -> starting point ~25%
- Adjustments upward: striking Phase 1 efficacy signal (+5%), PET-confirmed graft survival (+5%), immunosuppression-free tolerability (+5%), dual FDA designations reflecting agency conviction (+3%)
- Adjustments downward: open-label uncontrolled Phase 1 with undisclosed N (-10%), China-origin data quality concerns (-3%), no big pharma validation via partnership (-3%), very early company with limited track record (-2%)
- Net: ~25-30%

**Signal analysis:**
- Dual FDA designations (FTD + RMAT) within 5 months of each other is aggressive agency engagement and suggests the FDA sees preliminary clinical evidence of serious potential. RMAT in particular requires evidence suggesting the therapy "may address an unmet medical need for a serious disease" -- this is the FDA's own assessment of the data.
- The $40M total raise is thin for a global Phase 1/2 program in two geographies. iRegene will need either a significant Series C or a partnership deal to fund through US clinical development. The Phase 2 China readout (Q4 2026) is the likely inflection point for a licensing deal.
- iRegene's broader pipeline (NouvNeu003 for early-onset PD, NouvNeu004 for MSA, NouvSight001 for retinal degeneration) suggests the chemical induction platform has versatility, but also dilutes capital across multiple programs.
- The decision tree: if China Phase 2 confirms efficacy in a larger, controlled setting, expect a major licensing deal (likely with a big pharma seeking cell therapy positioning) and accelerated US development leveraging RMAT/FTD. If Phase 2 disappoints or immunogenicity emerges, the $40M capital base offers limited runway for pivoting, and the advantage consolidates around [[bemdaneprocel]] and [[anpd001|ANPD001]].

## References

### Clinical Trials
- [NouvNeu001 Phase 1/2 China](https://clinicaltrials.gov/ct2/show/NCT06167681) -- NCT06167681

### Key Publications
- Limited peer-reviewed publications to date. Phase 1 data disclosed via press releases (October 2025). Requires primary research for supporting preclinical publications on chemical induction platform.

### Press Releases & Filings
- [iRegene Therapeutics announced promising NouvNeu001 Phase I clinical data (Oct 2025)](https://www.prnewswire.com/news-releases/iregene-therapeutics-announced-promising-nouvneu001-phase-i-clinical-data-302581682.html)
- [FDA Grants RMAT Designation to iRegene's NouvNeu001 (Jan 2026)](https://www.prnewswire.com/news-releases/fda-grants-regenerative-medicine-advanced-therapy-rmat-designation-to-iregenes-nouvneu001-making-it-the-worlds-first-ipsc-therapy-with-both-ftd-and-rmat-recognitions-302663450.html)
- [iRegene Therapeutics Secures Series B+ Financing (Sep 2025)](https://www.prnewswire.com/news-releases/iregene-therapeutics-secures-series-b-financing-following-fda-fast-track-designation-for-its-flagship-product-nouvneu001-302550348.html)
- [iRegene Receives IND Approval from U.S. FDA (Jun 2024)](https://www.prnewswire.com/news-releases/iregene-receives-ind-approval-from-us-fda-to-start-clinical-trial-for-parkinsons-disease-302180135.html)
- [NouvNeu001 First Patient Dosed in Multicenter Trial (Jan 2024)](https://www.prnewswire.com/news-releases/nouvneu001-achieves-milestone-with-successful-dosing-of-first-patient-signaling-smooth-progress-in-iregene-therapeutics-multicenter-clinical-trial-for-innovative-novel-parkinsons-disease-therapy-302053243.html)

### Regulatory & Market
- [FDA Grants RMAT Designation -- Practical Neurology (Jan 2026)](https://practicalneurology.com/news/fda-grants-rmat-designation-to-allogeneic-ipsc-derived-cell-therapy-for-parkinson-disease/2485408/)
- [FDA OKs Parkinson's clinical trial to test NouvNeu001 | Parkinson's News Today](https://parkinsonsnewstoday.com/news/fda-oks-parkinsons-clinical-trial-nouvneu001-cell-therapy/)
- [iRegene receives FDA RMAT designation | Pharmaceutical Business Review](https://www.pharmaceutical-business-review.com/news/iregene-receives-fda-rmat-designation)
