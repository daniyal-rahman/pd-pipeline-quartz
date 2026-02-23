---
drug_name: "Prasinezumab"
aliases: ["PRX002", "RO7046015"]
target: "alpha-synuclein (aggregated, C-terminal)"
mechanism: "Humanized IgG1 mAb selectively binding aggregated alpha-synuclein to block prion-like cell-to-cell spread"
modality: "Monoclonal antibody"
developer: "Prothena"
company_type: "biotech"
publicly_traded: true
ticker: "PRTA"
partner: "Roche"
partner_type: "big pharma"
stage: "Phase 3"
status: "Active"
patient_population: "Early PD on stable levodopa"
route_of_administration: "IV (monthly infusion)"
key_biomarkers: ["neuromelanin MRI", "DaT-SPECT", "iron accumulation imaging", "alpha-synuclein SAA"]
confidence_rating: "6/10"
next_catalyst: "PARAISO Phase 3 enrollment/design disclosure"
catalyst_date: "2027-2028 (readout)"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/prothena]]"
partner_link: "[[companies/roche]]"
---

# Prasinezumab

## Summary

PADOVA Phase 2b missed primary (p=0.0657) but a pre-specified levodopa subgroup showed 21% motor slowing (p=0.0431). The 4-year PASADENA OLE showed 51-65% slower decline vs. PPMI comparators, with early-start beating delayed-start — the strongest disease modification signal in the alpha-synuclein antibody field. Roche (big pharma) is advancing to Phase 3 (PARAISO) despite the miss — notable because they walked away from gantenerumab in Alzheimer's after a similar miss, showing they can kill programs. If PARAISO succeeds, this validates extracellular alpha-synuclein as a target and becomes the first PD disease-modifying therapy. If it fails, the antibody modality for alpha-synuclein is likely exhausted and the field shifts toward production inhibition via [[aro-snca|siRNA]] and [[ly3962681|intrathecal approaches]].

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Roche |
| Deal Date | 2013 |
| Upfront | $30M |
| Total (Biobucks) | ~$755M |
| Deal Type | Licensing/co-development |

## Notes

### Science
- Humanized IgG1 mAb with **800-fold selectivity** for aggregated vs. monomeric alpha-synuclein, targeting the C-terminus
- Mechanism: blocks prion-like cell-to-cell transmission of aggregated alpha-synuclein by clearing extracellular aggregates before they seed intracellular pathology in adjacent neurons
- Reduces a neurotoxic truncated form of alpha-synuclein and prevents inter-cellular propagation in preclinical models
- Key distinction vs. failed [[cinpanemab]]: prasinezumab targets **C-terminus**; [[cinpanemab]] targeted **N-terminus** (aa 1-10). Among five Phase 2 alpha-syn antibodies, only [[cinpanemab]] (N-terminal) failed — the other four target C-terminus
- Core scientific question: does targeting extracellular aggregates matter if pathology is predominantly intracellular? The prion-like spreading hypothesis says yes — blocking transmission could slow progression even if existing intracellular damage persists
- Standard mAb CNS penetration is ~0.1-0.2% of blood levels — whether this is sufficient for extracellular target engagement in the brain remains debated

### Clinical

**PRX002 (Phase 1b)** | NCT02157714 | N=80 | Healthy volunteers + PD patients
- **Primary endpoint:** Safety/tolerability → Clean safety profile
- **Key secondary:** Dose-dependent serum alpha-synuclein reduction; CSF penetration confirmed
- **Status:** Completed
- **Interpretation:** Established PK/PD relationship and safety profile; enabled Phase 2 progression

**PASADENA (Phase 2)** | NCT03100149 | N=316 | Early PD, de novo (not requiring symptomatic therapy)
- **Primary endpoint:** MDS-UPDRS total score change → Not statistically significant at 52 weeks
- **Key secondary:** Delayed-start design (placebo → prasinezumab at Year 1). At 2 years, delayed-start did NOT catch up to early-start on MDS-UPDRS, suggesting possible disease modification but not reaching statistical significance
- **4-year OLE (Nature Medicine, Oct 2024):** Early-start group showed **65% slower decline** vs. PPMI comparator; delayed-start showed **51% slower decline**. Early-start > delayed-start pattern supports disease modification over symptomatic effect
- **Status:** Completed; OLE ongoing (>750 patients remain on treatment)
- **Interpretation:** The OLE data is the strongest evidence for prasinezumab but relies on external comparator (PPMI), which introduces selection bias. The early-start > delayed-start separation is the key disease modification signal.

**PADOVA (Phase 2b)** | NCT04777331 | N=586 | Early PD on stable symptomatic treatment (75% on levodopa)
- **Primary endpoint:** Time to confirmed motor progression (MDS-UPDRS) → **HR=0.84 [0.69-1.01], p=0.0657** (MISSED significance)
- **Pre-specified levodopa subgroup:** HR=0.79 [0.63-0.99], p=0.0431 (21% slowing); covariate-adjusted HR=0.76, p=0.0175
- **Key secondary:** Numerically less neuromelanin MRI intensity/volume decline; **statistically significant** reduction in iron accumulation (exploratory biomarker)
- **Safety:** >900 patients dosed, >500 for 1.5-5 years, no new safety signals
- **Status:** Completed December 2024
- **Interpretation:** The primary miss is a statistical failure by conventional standards. The levodopa subgroup signal was pre-specified (not post-hoc) and biologically rational — levodopa-treated patients are faster progressors enriched for Lewy body pathology, reducing heterogeneity. Phase 3 will likely enrich for this population.

**PARAISO (Phase 3)** | NCT TBD | N=TBD | Likely levodopa-enriched early PD
- **Primary endpoint:** Expected time to motor progression, powered for HR~0.76-0.79
- **Status:** Announced June 2025; trial initiation by end-2025; readout ~2027-2028
- **Interpretation:** Roche advancing despite borderline Phase 2b — notable because they walked away from gantenerumab in Alzheimer's after a clean Phase 3 miss, demonstrating they can kill programs. Their choice to advance here signals data-driven conviction.

### Financial
- **$135M in milestones earned** to date out of ~$755M total potential; $620M remaining
- **Peak sales estimates:** Roche projects >$3B unadjusted; conservative third-party estimates $207M-$1.5B by 2033
- **Prothena stock (PRTA):** +11% on Phase 3 advancement announcement (June 2025)
- **Context:** 10% of FDA-approved drugs (2018-2021) were approved with null findings on at least 1 primary endpoint — common pathway was success on secondary/exploratory endpoints, which prasinezumab has
- **Deal comparison:** $30M upfront in 2013 is low conviction at signing (4% ratio), but $135M earned over 12 years shows sustained partnership. Roche's Phase 3 commitment is the real conviction signal — they're deploying $200-400M+ in Phase 3 costs

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[cinpanemab]] | Terminated | Failed | Biogen | monoclonal antibody |
| [[ion464]] | Discontinued | Discontinued | Ionis Pharmaceuticals | ASO |
| [[minzasolmin]] | Terminated | Terminated | UCB | small molecule |
| [[saamplify-asyn]] | Commercial | Active | Amprion | diagnostic assay |
| [[trimtech-trim21]] | Discovery | Active | TRIMTECH Therapeutics | small molecule |
| [[adp062-abc]] | Preclinical | Active | Alector | siRNA |
| [[aro-snca]] | Preclinical | Active | Arrowhead Pharmaceuticals | siRNA |
| [[booster-therapeutics]] | Preclinical | Active | Booster Therapeutics | small molecule |
| [[eubiologics-vaccine]] | Preclinical | Active | EuBiologics | active vaccine |
| [[lbp-pd01]] | Preclinical | Active | LISCure Biosciences | live biotherapeutic product |
| [[mor-a-syn]] | Preclinical | Active | AC Immune | small molecule |
| [[act-02]] | IND-enabling | Active | Accure Therapeutics | small molecule |
| [[dnl422]] | IND-enabling | Active | Denali Therapeutics | ASO |
| [[18f-fd4]] | Phase 1 | Active | SynuSight Biotech | PET tracer |
| [[abl301]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |
| [[energi-f705pd]] | Phase 1 | Active | Energenesis Biomedical | small molecule |
| [[ly3962681]] | Phase 1 | Active | Prevail Therapeutics (Eli Lilly subsidiary) | siRNA |
| [[mk-7337]] | Phase 1 | Discontinued | Merck | PET tracer |
| [[nm-101]] | Phase 1 | Active | Neuramedy | monoclonal antibody |
| [[sar446159]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |
| [[ucb7853]] | Phase 1 | Active | UCB | monoclonal antibody |
| [[vt-5006]] | Phase 1 | Active | Vertero Therapeutics | small molecule |
| [[emrusolmin]] | Phase 1b | Active | MODAG GmbH | small molecule |
| [[her-096]] | Phase 1b | Active | Herantis Pharma | peptide |
| [[ub-312]] | Phase 1b | Active | Vaxxinity | active vaccine |
| [[aci-7104]] | Phase 2 | Active | AC Immune | active vaccine |
| [[ath-434]] | Phase 2 | Active | Alterity Therapeutics | small molecule |
| [[exidavnemab]] | Phase 2 | Active | BioArctic | monoclonal antibody |
| [[lu-af67643]] | Phase 2 | Unverified | Lundbeck | monoclonal antibody |
| [[amlenetug]] | Phase 3 | Active | Lundbeck | monoclonal antibody |
| [[buntanetap]] | Phase 3 | Active | Annovis Bio | small molecule |
| [[prasinezumab]] | Phase 3 | Active | Prothena | Monoclonal antibody |

- Key distinction is **modality**: antibodies (clearance of extracellular aggregates) vs. [[aro-snca|siRNA]]/[[ly3962681|ASO]] (production inhibition at mRNA level) vs. [[cinpanemab|vaccines]] (endogenous antibody generation)
- [[aro-snca|ARO-SNCA]] is the main competitive threat — different modality (siRNA), targets production instead of clearance, subcutaneous delivery, $2.2B Novartis deal signals conviction
- [[ly3962681|LY3962681]] (Lilly) — same production-inhibition thesis as [[aro-snca]] but intrathecal delivery, which is a major disadvantage for chronic dosing. Biogen's discontinuation of [[ion464]] (also intrathecal alpha-syn) is a warning for this route
- If PARAISO succeeds: alpha-syn validated as target, active vaccines become the low-COGS scalable version, BBB-shuttled antibodies get a second life
- If PARAISO fails: antibody modality for alpha-syn likely exhausted; field shifts to gene silencing ([[aro-snca]], [[ly3962681]]) and non-alpha-syn targets ([[biib122|LRRK2]], [[pariceract|GBA1]])

## Analysis

The thesis rests on whether the p=0.0657 PADOVA primary miss was a real biological signal diluted by patient heterogeneity, or statistical noise. The pre-specified levodopa subgroup (p=0.0431) and 4-year OLE data (early-start > delayed-start) provide the case for "real signal." The field track record and missed primary provide the case for "noise."

**Analytical estimate — Phase 3 success probability: 30-35%.** This is our assessment, not from a published source. The reasoning:
- Base rate: 0/6 alpha-syn antibodies have met primary endpoints → starting point <10%
- Adjustments upward: pre-specified subgroup signal (+15%), 4-year OLE disease modification evidence (+10%), biomarker concordance on neuromelanin/iron (+10%), clean safety enabling approval with marginal efficacy (+5%), levodopa enrichment in Phase 3 design (+10%)
- Adjustments downward: missed primary endpoint (-15%), field-wide antibody failures in neurodegeneration (-10%), external comparator methodology concerns in OLE (-5%)
- Net: ~30-35%

**Signal analysis:**
- Roche advancing after PADOVA miss — this is a big pharma with a demonstrated willingness to kill programs (gantenerumab). Their Phase 3 commitment means their internal data review concluded the levodopa subgroup signal is reproducible. This is not sunk-cost behavior.
- Prothena is a clinical-stage biotech with prasinezumab as their lead PD asset. PRTA stock is directly tied to PARAISO outcome — binary risk.
- A positive PARAISO readout would validate extracellular alpha-synuclein targeting, create a $1-3B franchise, and revalue the entire alpha-syn ecosystem. A negative readout permanently closes the antibody modality and redirects capital toward [[aro-snca|gene silencing]] and [[pariceract|genetic PD targets]].
- The diagnostic/biomarker layer (SAA, PET tracers) benefits regardless of PARAISO outcome — needed for every alpha-syn trial and eventual commercial patient identification.

## References

### Clinical Trials
- [PASADENA Phase 2](https://clinicaltrials.gov/ct2/show/NCT03100149) — NCT03100149
- [PADOVA Phase 2b](https://clinicaltrials.gov/ct2/show/NCT04777331) — NCT04777331
- [PRX002 Phase 1b](https://clinicaltrials.gov/ct2/show/NCT02157714) — NCT02157714

### Key Publications
- [Sustained effect of prasinezumab on PD motor progression in PASADENA OLE | Nature Medicine (Oct 2024)](https://www.nature.com/articles/s41591-024-03270-6)
- [Trial of Prasinezumab in Early-Stage PD (PASADENA) | NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2202867)
- [Alpha-Synuclein Targeting Therapeutics for PD | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9124903/)
- [MEDI1341 Phase 1: CSF alpha-synuclein lowered >50% | Brain Communications](https://academic.oup.com/braincomms/article/7/5/fcaf304/8238147)
- [Targeting Alpha-Synuclein as Therapy for PD (prion-like spreading) | Frontiers Mol Neurosci](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2019.00299/full)
- [Update on immune-based alpha-synuclein trials in PD | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638298/)
- [Application of Neuromelanin MR Imaging in PD | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10086789/)
- [Trial of Cinpanemab in Early PD (SPARK) | NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2203395)

### Press Releases & Filings
- [Roche PADOVA Phase 2b topline results (Dec 2024)](https://www.roche.com/media/releases/med-cor-2024-12-19)
- [Roche advances prasinezumab to Phase 3 (June 2025)](https://www.roche.com/media/releases/med-cor-2025-06-16)
- [Prothena IR: Roche Phase 3 advancement](https://ir.prothena.com/investors/press-releases/news-details/2025/Prothenas-Partner-Roche-to-Advance-Prasinezumab-into-Phase-III-Development-for-Early-Stage-Parkinsons-Disease/default.aspx)
- [PADOVA MDS Abstract](https://www.mdsabstracts.org/abstract/padova-topline-results-from-a-phase-iib-study-of-prasinezumab-in-early-stage-parkinsons-disease-participants-on-stable-symptomatic-treatment/)
- [Prasinezumab profile | Alzforum](https://www.alzforum.org/therapeutics/prasinezumab)

### Regulatory & Market
- [US FDA Approval of Drugs Not Meeting Primary Endpoints | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9926353/)
- [Qualification of Enrichment Biomarkers for Clinical Trials | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700608/)
- [Roche Prasinezumab peak sales analysis | Clinical Trials Arena](https://www.clinicaltrialsarena.com/analyst-comment/roche-prasinezumab-parkinsons-disease/)
- [Roche Pharma Day 2025 (neuroscience strategy)](https://assets.roche.com/f/176343/x/059c686d27/20250922_pharma-day-2025_vf_online.pdf)
- [Roche commits to Phase 3 for prasinezumab | BioPharma Dive](https://www.biopharmadive.com/news/roche-prothena-parkinsons-drug-prasinezumab-phase3/750791/)
- [Gantenerumab Phase 3 failure analysis | BioPharma Dive](https://www.biopharmadive.com/news/roche-gantenerumab-trial-failure-alzheimers/636450/)
