---
drug_name: "STEM-PD"
aliases: ["STEM-PD product", "RC17-derived DA progenitors"]
target: "dopaminergic neuron replacement (hESC-derived DA progenitors)"
mechanism: "Dopaminergic neural progenitor cells derived from the RC17 hESC line, transplanted bilaterally into the putamen to replace DA neurons lost in PD"
modality: "cell therapy (ESC)"
developer: "Lund University / University of Cambridge"
company_type: "academic"
publicly_traded: false
partner: "Novo Nordisk"
partner_type: "big pharma"
stage: "Phase 1/2"
status: "Active"
patient_population: "Moderately advanced PD (Hoehn and Yahr 2-3 in OFF), age 50-75"
route_of_administration: "intracranial (bilateral intraputamenal stereotactic injection)"
key_biomarkers: ["dopamine PET (graft survival)", "cranial MRI (safety)", "MDS-UPDRS Part III"]
confidence_rating: "4/10"
next_catalyst: "12-month safety data from high-dose cohort; 36-month efficacy readout from low-dose cohort"
catalyst_date: "2026-2027"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# STEM-PD

## Summary

STEM-PD is the first European stem cell-derived dopamine neuron replacement trial for PD, led by Prof. Malin Parmar (Lund University) and Prof. Roger Barker (University of Cambridge). The Phase 1/2 dose-escalation trial (NCT05635409, N=8) completed transplantation of all patients across two dose cohorts by 2024, with early PET imaging at 6-12 months showing signs of dopamine cell survival and no concerning safety signals. Novo Nordisk (big pharma) provided funding and was intended to carry further development and commercialization, but exited cell therapy broadly in late 2024 -- creating uncertainty around the commercial pathway despite ongoing academic trial execution. If 36-month efficacy data demonstrate meaningful motor improvement and durable engraftment, STEM-PD validates the ESC-derived dopaminergic progenitor paradigm alongside [[bemdaneprocel]] and competes for follow-on development partners. If safety issues emerge or graft survival proves insufficient, the program remains a proof-of-concept contribution to the field, with [[bemdaneprocel]] (Phase 3) and [[raguneprocel]] (NDA filed in Japan) holding stronger commercial positions.

## Notes

### Science
- STEM-PD uses dopaminergic neural progenitor cells derived from the **RC17 human embryonic stem cell line**, programmed to become A9-type midbrain dopamine neurons -- the specific subtype lost in PD
- The cell product is manufactured under GMP at the Royal Free Hospital in London, addressing the key limitation of historical fetal tissue transplantation: unreliable and non-scalable cell sourcing
- Mechanism: transplanted progenitors are injected bilaterally into the putamen, where they mature into functional dopaminergic neurons, integrate into host circuitry, and restore local dopamine production
- Preclinical validation: 39-week rat GLP safety study showed no toxicity, tumorigenicity, or biodistribution concerns; non-GLP efficacy study demonstrated **full functional recovery** in a rat PD model
- Key distinction from [[bemdaneprocel]]: STEM-PD uses the RC17 cell line with a European GMP manufacturing process; BlueRock uses a different hESC line with proprietary differentiation. Both target the same biological principle (A9-type DA neuron replacement) but represent independent manufacturing and quality control systems
- Key distinction from [[ted-a9|TED-A9]]: S.BIOMEDICS uses a small-molecule-only differentiation protocol; STEM-PD follows a morphogen-based patterning approach developed by Parmar lab
- Immunosuppression: all participants receive a renal transplant-grade regimen -- basiliximab induction, tacrolimus (or cyclosporine if intolerant), azathioprine, and steroids for 12 months post-grafting. This is more aggressive than the Kyoto iPSC trial (tacrolimus monotherapy), reflecting the allogeneic nature of the hESC-derived product
- Open question: whether 12 months of immunosuppression is sufficient for long-term graft survival, or whether chronic immunosuppression will be required

### Clinical

**STEM-PD (Phase 1/2)** | NCT05635409 | N=8 | Moderately advanced PD (H&Y 2-3 OFF), age 50-75
- **Primary endpoint:** Safety and tolerability at 12 months (then extended to 24 months per protocol paper), assessed by number/nature of adverse events and absence of space-occupying lesions on cranial MRI
- **Secondary endpoints:** Graft survival via dopamine PET imaging at 12 and 36 months; clinical efficacy measures (MDS-UPDRS, medication changes) at 36 months
- **Dose escalation:** Low dose: 3.5M cells/putamen (7M total), N=4; High dose: 7M cells/putamen (14M total), N=4
- **Sites:** Skane University Hospital (Lund, Sweden), Cambridge University Hospital (UK)
- **Timeline:** First patient transplanted February 2023 (Sweden); low-dose cohort (N=4) completed; high-dose cohort initiated after safety review, first high-dose patient transplanted, remaining patients grafted during 2024
- **Interim results:** No concerning safety signals; all patients "doing well"; PET imaging at 6-12 months shows **signs of dopamine cell survival** -- but too early to evaluate clinical efficacy
- **Regulatory:** Swedish Medical Products Agency approval October 2022; UK MHRA approval October 2023; authorized under EU Clinical Trial Regulation 536/2014
- **Status:** Active -- dosing complete, follow-up ongoing
- **Interpretation:** The clean safety signal across both cohorts is encouraging and consistent with [[bemdaneprocel]] Phase 1 and [[ted-a9|TED-A9]] Phase 1/2a findings. PET evidence of graft survival is the minimum necessary signal. The 36-month efficacy readout is what matters for the field -- but with N=8 and no control arm, clinical interpretation will necessarily be limited and hypothesis-generating.

### Financial
- **Funding model:** Entirely non-commercial to date. Funded by EU and national (Swedish, UK) research agencies, the New York Stem Cell Foundation (NYSCF -- Robertson Investigator Award to Parmar), and Novo Nordisk
- **Novo Nordisk involvement:** Signed licensing and research collaboration agreements in 2017; provided funding, regulatory expertise, and infrastructure for large-scale development and commercialization. However, Novo Nordisk **exited all cell therapy programs in October 2024** as part of a strategic refocusing on diabetes and obesity. The fate of the STEM-PD commercial license is unclear
- **No disclosed financial terms:** Unlike industry-sponsored trials, the Novo Nordisk deal terms (upfront, milestones, royalties) were never publicly disclosed
- **Commercial pathway uncertainty:** With Novo Nordisk's exit, STEM-PD needs a new commercial partner to advance beyond academic proof-of-concept. The Lund/Cambridge consortium lacks the infrastructure for Phase 2/3 registrational trials and GMP scale-up
- **Comparator economics:** [[bemdaneprocel]] has ~$1B in Bayer backing; [[raguneprocel]] has Sumitomo Pharma's NDA resources; [[ted-a9|TED-A9]] has S.BIOMEDICS (KOSDAQ-listed). STEM-PD is the only first-in-human PD cell therapy without a secured commercial partner

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "dopaminergic neuron replacement") AND file.name != "stem-pd"
SORT stage DESC
```

- All four first-in-human PD cell therapy trials ([[bemdaneprocel]], [[raguneprocel]], [[ted-a9|TED-A9]], STEM-PD) have now reported early safety and graft survival data -- the field has crossed the proof-of-concept threshold collectively
- [[bemdaneprocel]] is the primary competitive benchmark: same ESC source type, same intraputamenal delivery, but further ahead clinically (Phase 3 enrolling, RMAT designation) and fully resourced by Bayer
- [[raguneprocel]] (Sumitomo/Kyoto) uses allogeneic iPSCs rather than ESCs, which may offer immunological advantages through HLA-matched donors -- NDA filed in Japan with decision expected H2 2026
- [[ted-a9|TED-A9]] (S.BIOMEDICS) published the most detailed efficacy data to date (12-month MDS-UPDRS improvements in 12 patients), creating the best quantitative benchmark for what STEM-PD's efficacy data will be compared against
- STEM-PD's differentiation is scientific rather than commercial: it originates from one of the most established dopamine neuron biology labs globally (Parmar/Bjorklund at Lund, Barker at Cambridge), and the RC17 manufacturing process represents an independent European cell source with its own GMP track record
- If [[bemdaneprocel]]'s exPDite-2 succeeds, the cell therapy paradigm is validated and STEM-PD's value as an alternative cell source increases for licensing. If exPDite-2 fails, STEM-PD's 36-month data becomes more important for determining whether the failure was product-specific or paradigm-level

## Analysis

STEM-PD occupies a unique position in the PD cell therapy landscape: scientifically credible, academically rigorous, but commercially orphaned. The Parmar and Barker labs represent decades of foundational work on dopamine neuron transplantation -- from fetal tissue grafting studies through pluripotent stem cell differentiation protocols. The RC17-derived product passed preclinical benchmarks cleanly and the first-in-human data so far (safety + PET survival signal) is consistent with the broader field's findings.

**Analytical estimate -- probability of meaningful clinical effect at 36 months: 35-45%.** This is our assessment, not from a published source. The reasoning:
- Base rate: historical fetal tissue grafts showed functional dopaminergic engraftment in ~60% of well-selected patients, but high variability in clinical outcomes (+10% starting point above pure chance)
- Adjustments upward: standardized GMP cell product eliminates tissue variability (+10%); preclinical full recovery in rat model (+5%); early PET survival signal at 6-12 months (+5%); experienced surgical team with decades of stereotactic neurosurgery expertise (+5%)
- Adjustments downward: N=8 with no control arm means placebo/regression-to-mean effects cannot be excluded (-10%); 12-month immunosuppression may be insufficient for long-term graft survival (-5%); cell dose may be subtherapeutic at the low end (-5%)
- Net: ~35-45% probability of seeing a clinically meaningful motor signal at 36 months in at least the high-dose cohort

The critical strategic question is the commercial pathway. Novo Nordisk's exit in October 2024 removed the only partner positioned to take STEM-PD through registrational trials. The academic team can generate proof-of-concept data, but Phase 2/3 would require manufacturing scale-up, multi-center surgical standardization, and hundreds of millions in investment. Potential acquirers of the license include Bayer (already invested in [[bemdaneprocel]] -- unlikely to add a competing ESC product), other big pharma with regenerative medicine interest, or mid-cap biotechs seeking cell therapy platforms.

The timing is consequential: [[bemdaneprocel]]'s exPDite-2 readout (2027-2028) will arrive before STEM-PD generates 36-month efficacy data. A positive exPDite-2 result would validate the paradigm and make STEM-PD attractive as a second-source or next-generation product. A negative result would suppress commercial interest in all ESC-derived DA neuron programs, regardless of STEM-PD's own data. The program's fate is therefore partially tied to [[bemdaneprocel]]'s outcome -- a dependency that is unusual for an independently developed academic asset.

## References

### Clinical Trials
- [STEM-PD Phase 1/2](https://clinicaltrials.gov/study/NCT05635409) -- NCT05635409

### Key Publications
- [STEM-PD trial protocol: multi-centre, single-arm, first-in-human, dose-escalation trial | BMJ Open (2025)](https://lup.lub.lu.se/search/publication/7924f787-568e-43e9-97dd-d1ddcf2d968d)
- [Preclinical quality, safety, and efficacy of a human embryonic stem cell-derived product for the treatment of Parkinson's disease, STEM-PD | Cell Stem Cell (2023)](https://pubmed.ncbi.nlm.nih.gov/37802036/)
- [Preclinical and dose-ranging assessment of hESC-derived dopaminergic progenitors for a clinical trial on Parkinson's disease | Cell Stem Cell (2023)](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(23)00401-0)
- [Strategies for bringing stem cell-derived dopamine neurons to the clinic: A European approach (STEM-PD) | Prog Brain Res (2017)](https://pubmed.ncbi.nlm.nih.gov/28552228/)
- [Human Trials of Stem Cell-Derived Dopamine Neurons for Parkinson's Disease: Dawn of a New Era | Cell Stem Cell (2017)](https://pubmed.ncbi.nlm.nih.gov/29100010/)
- [The history and status of dopamine cell therapies for Parkinson's disease | BioEssays (2024)](https://onlinelibrary.wiley.com/doi/full/10.1002/bies.202400118)
- [Stem cell-derived dopamine cell therapies for Parkinson's disease: what have the first trials shown? | Brain (2025)](https://academic.oup.com/brain/article/148/10/3428/8246373)
- [Clinical trial highlights: Dopamine cell-replacement therapies | J Parkinsons Dis (2026)](https://journals.sagepub.com/doi/10.1177/1877718X251397277)

### Press Releases & Filings
- [Update on STEM-PD clinical trial -- stem cell-based transplant for Parkinson's disease | Lund University (2024)](https://www.lunduniversity.lu.se/article/update-stem-pd-clinical-trial-stem-cell-based-transplant-parkinsons-disease)
- [Clinical trial for new stem cell-based treatment for Parkinson's disease given go ahead | University of Cambridge (2022)](https://www.cam.ac.uk/research/news/clinical-trial-for-new-stem-cell-based-treatment-for-parkinsons-disease-given-go-ahead)
- [Swedish Medical Products Agency grants approval for clinical study | Lund University (2022)](https://www.lunduniversity.lu.se/article/swedish-medical-products-agency-grants-approval-clinical-study-new-stem-cell-based-parkinsons)
- [NYSCF Innovator Malin Parmar's Cell Therapy Reaches First Patient | NYSCF (2023)](https://nyscf.org/resources/nyscf-innovator-malin-parmars-cell-therapy-for-parkinsons-reaches-first-patient-in-clinical-trial/)
- [Collaboration between Lund University researchers and Novo Nordisk | Lund University](https://www.lunduniversity.lu.se/article/collaboration-between-lund-university-researchers-and-novo-nordisk-paves-way-large-scale-cell)
- [Novo Nordisk offloads diabetes assets amid cell therapy retreat | Fierce Biotech (2024)](https://www.fiercebiotech.com/biotech/novo-nordisk-offloads-diabetes-assets-aspect-amid-cell-therapy-retreat)
- [STEM-PD cell-replacement trial releases latest update | Cure Parkinson's (2024)](https://cureparkinsons.org.uk/2024/06/stem-pd-a-cell-replacement-trial-for-parkinsons-releases-latest-update/)

### Regulatory & Market
- [Clinical trials test the safety of stem-cell therapy for Parkinson's disease | Nature (2025)](https://www.nature.com/articles/d41586-025-00688-x)
- [Two New Trials Explore Stem-Cell Therapy for Parkinson's | Parkinson's Foundation](https://www.parkinson.org/blog/science-news/cell-replacement)
