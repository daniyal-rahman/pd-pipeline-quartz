---
drug_name: "Dapansutrile"
aliases: ["OLT1177"]
target: "NLRP3 inflammasome"
mechanism: "Oral selective NLRP3 inflammasome inhibitor that blocks ATPase-dependent assembly, preventing IL-1beta and IL-18 release to reduce neuroinflammation"
modality: "small molecule"
developer: "Olatec Therapeutics"
company_type: "biotech"
publicly_traded: false
stage: "Phase 2"
status: "Active"
patient_population: "Early PD (H&Y <=2, disease duration <=5 years) with peripheral inflammation (hsCRP >1)"
route_of_administration: "oral (1000mg BID)"
key_biomarkers: ["hsCRP", "IL-6", "IL-1beta", "microglial activation"]
confidence_rating: "4/10"
next_catalyst: "DAPA-PD Phase 2 safety/tolerability readout"
catalyst_date: "2027"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/olatec-therapeutics]]"
---

# Dapansutrile

## Summary

Dapansutrile (OLT1177) is an oral selective NLRP3 inflammasome inhibitor developed by Olatec Therapeutics (private biotech) now entering the DAPA-PD Phase 2 trial at the University of Cambridge, funded by Cure Parkinson's and Van Andel Institute. Preclinical data presented in 2025 showed disease-modifying activity in two translational PD mouse models -- reduced alpha-synuclein inclusions, attenuated gliosis, prevented nigral neurodegeneration, and reversed PD-associated microglial transcriptional signatures. The drug has a clean safety profile across ~350 patients dosed in gout, heart failure, COVID-19, and diabetes trials, and crosses the blood-brain barrier. However, a 2024 large-scale genetic study found no association between NLRP3 variants and PD risk, creating a disconnect between strong preclinical data and absent genetic validation. If DAPA-PD shows safety and biomarker engagement, it would de-risk a larger efficacy trial and validate neuroinflammation as a tractable PD mechanism. If it fails to show target engagement or tolerability, the NLRP3-specific neuroinflammation thesis for PD weakens relative to broader anti-inflammatory approaches and competing NLRP3 programs like Roche's [[selnoflast]].

## Notes

### Science
- Dapansutrile is a beta-sulfonyl nitrile that inhibits NLRP3 ATPase activity, blocking assembly of the NLRP3 inflammasome and preventing downstream caspase-1 activation, IL-1beta release, and IL-18 release
- Selective for NLRP3 -- does not affect NLRC4 or AIM2 inflammasomes, and does not alter mRNA levels of NLRP3, ASC, caspase-1, IL-1beta, or IL-18 genes, meaning it modulates pathological inflammation while preserving normal immune surveillance
- Secondary targets include phosphorylated kinases (Src, Fyn, HcK, STAT3), which may contribute to anti-inflammatory activity beyond pure NLRP3 inhibition
- Crosses the blood-brain barrier at pharmacologically relevant concentrations -- critical differentiator for neurological applications vs. peripherally restricted NLRP3 inhibitors
- In two PD mouse models (alpha-synuclein propagation model and transgenic alpha-synuclein model), six months of oral dapansutrile at human-equivalent doses: improved motor performance, reduced alpha-synuclein inclusions, attenuated microglial and astroglial activation, and mitigated nigral neurodegeneration
- Microglial transcriptomic analysis showed dapansutrile reversed key transcriptional signatures of PD-associated reactive microglia -- suggesting it reprograms disease-state microglia rather than just suppressing them
- **Genetic validation gap:** A 2024 study in npj Parkinson's Disease found no genetic association between NLRP3 common/rare variants and PD risk via Mendelian randomization, concluding that altering NLRP3, IL-1beta, or IL-18 expression does not affect PD risk or progression. An earlier 2018 study identified one SNP (rs7525979) associated with reduced PD risk, but this has not been replicated at scale
- The neuroinflammation hypothesis in PD posits that microglial NLRP3 activation is downstream of alpha-synuclein aggregation and upstream of dopaminergic neuronal death -- targeting this node could break a self-amplifying cycle even without genetic causation

### Clinical

**Phase 1 (Healthy Volunteers)** | NCT02134964 | N=54 | Healthy volunteers
- **Primary endpoint:** Safety/tolerability/PK -> Well tolerated at all doses up to 2000mg; adequate plasma concentrations for NLRP3 inhibition confirmed
- **Status:** Completed
- **Interpretation:** Established human safety and PK profile enabling clinical development

**Gout Flares (Phase 2a)** | NCT03534297 | N=34 | Acute monoarticular gout flare
- **Primary endpoint:** Target joint pain reduction -> Marked pain reduction across all dose groups (100mg-2000mg/day)
- **Key secondary:** Significant decline in plasma IL-6 (NLRP3-dependent) but not TNF-alpha (NLRP3-independent), confirming mechanism selectivity
- **Status:** Completed
- **Interpretation:** Proof-of-concept for NLRP3 target engagement in a human inflammatory disease; dose-response and biomarker data informed PD trial design

**Heart Failure (Phase 1b)** | NCT03534297 | N=30 | NYHA II-III systolic heart failure
- **Primary endpoint:** Safety/tolerability over 14 days -> Well tolerated
- **Key secondary:** At 2000mg dose, improvement in LVEF (31.5% to 36.5%, p=0.039) and exercise time (570s to 616s, p=0.039)
- **Status:** Completed
- **Interpretation:** First clinical evidence of NLRP3 inhibition improving cardiac function; demonstrated safety in a chronic disease population

**COVID-19 (Phase 2)** | NCT04540120 | N=unknown | COVID-19 patients
- **Primary endpoint:** Safety/efficacy against cytokine release syndrome
- **Status:** Completed; full results not publicly available
- **Interpretation:** Additional safety data in an acute inflammatory setting

**DAPA-PD (Phase 2)** | NCT07157735 | N=36 | Early PD (H&Y <=2, <=5 years), hsCRP >1, on stable dopaminergic therapy
- **Primary endpoint:** Safety and tolerability of dapansutrile 1000mg BID over 6 months
- **Key secondary:** Biomarkers of neuroinflammation, motor function (MDS-UPDRS), non-motor symptoms
- **Design:** Randomized double-blind placebo-controlled (2:1 dapansutrile:placebo) for 6 months, followed by optional 6-month open-label extension
- **Site:** John van Geest Centre for Brain Repair, University of Cambridge, UK
- **PI:** Dr. Caroline Williams-Gray
- **Status:** Active; recruitment expected to begin early 2026; estimated completion March 2027
- **Interpretation:** Small proof-of-concept study enriched for inflammatory PD phenotype (hsCRP >1). Primary is safety, but the 12-month treatment duration with MDS-UPDRS secondary opens the possibility of detecting a disease-modifying signal. The hsCRP enrichment is a pragmatic strategy to select patients most likely to benefit from anti-inflammatory therapy.

### Financial
- Olatec Therapeutics is privately held; total funding raised ~$102M across 10 rounds
- **$40M Series A** closed February 2023, led by Sanders Morris Harris, with participation from Advection Growth Capital and Milano Investment Partners
- DAPA-PD trial is funded by Cure Parkinson's and Van Andel Institute (non-dilutive grant funding) -- Olatec contributes drug supply but does not bear full trial costs
- Michael J. Fox Foundation has also funded preclinical PD studies with dapansutrile
- No disclosed partnership with big pharma for the PD indication -- Olatec retains full rights
- Comparison: Novartis acquired IFM Tre (NLRP3 inhibitor portfolio) for $310M upfront + $1.265B milestones in 2019; Roche acquired Inflazome (inzomelid/selnoflast) in 2020 -- both deals validate the NLRP3 class commercially but neither was PD-focused at the time of acquisition
- No publicly available peak sales estimates for dapansutrile in PD given early stage

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "NLRP3") AND file.name != "dapansutrile"
SORT stage DESC
```

- The NLRP3 inhibitor class in PD is nascent -- dapansutrile is the most clinically advanced NLRP3 inhibitor specifically in a PD trial (Phase 2), though Roche's selnoflast (RO7486967) completed a Phase 1 study in early PD patients in 2025 with 28-day dosing
- Roche acquired Inflazome in 2020 for its NLRP3 program, initially planning to test inzomelid in PD, but withdrew that trial and pivoted to selnoflast -- a second-generation CNS-penetrant NLRP3 inhibitor. Selnoflast backed by big pharma resources represents the most direct competitive threat
- Novartis holds DFV890 (IFM-2427) from the IFM Tre acquisition but has not disclosed PD-specific development plans; their program is focused on systemic inflammatory diseases
- NodThera raised ~$40M for NLRP3 inhibitors but has not announced PD-specific programs
- Broader neuroinflammation competitors in PD include non-NLRP3 approaches: azathioprine (ISRCTN85338453, immunosuppressant tested in PD with early positive signals from Cambridge group), [[risvodetinib]] (c-Kit/LRRK2 pathway), and general anti-inflammatory strategies
- The DAPA-PD trial is notably enriched for patients with peripheral inflammation (hsCRP >1), a design choice that could identify a responder subpopulation -- if successful, this biomarker-enriched approach could differentiate dapansutrile from broader NLRP3 programs not using this selection strategy

## Analysis

The neuroinflammation thesis for PD rests on the observation that microglial NLRP3 activation amplifies alpha-synuclein-driven neurodegeneration, creating a feed-forward loop. Dapansutrile's preclinical package is compelling: disease-modifying effects in two complementary mouse models, CNS penetration, and reprogramming of disease-state microglial transcriptomes. The drug's extensive human safety database (~350 patients across four indications) substantially de-risks the clinical path. However, the 2024 genetic analysis finding no NLRP3 variants associated with PD risk is a meaningful counterpoint -- it suggests NLRP3 may be a downstream effector rather than a causal driver, which could limit therapeutic impact.

**Analytical estimate -- Phase 2 success probability (safety primary): 75-80%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Phase 2 safety studies for well-tolerated oral drugs in neurology succeed at ~80%
- Adjustments upward: extensive prior safety data across 4 indications (+5%), oral small molecule with known PK (+5%)
- Adjustments downward: new population (PD patients on dopaminergic therapy) may reveal interactions (-5%), 12-month treatment duration is longer than prior studies (-5%)
- Net: ~75-80% for the safety primary

**Analytical estimate -- Probability of meaningful disease modification signal: 15-20%.** This is our assessment, not from a published source. The reasoning:
- Base rate: anti-inflammatory approaches in neurodegeneration have a poor track record (<10% success)
- Adjustments upward: strong preclinical package with alpha-synuclein reduction (+5%), hsCRP enrichment strategy may identify responders (+5%), CNS penetration confirmed (+5%), NLRP3-specific mechanism vs. broad anti-inflammatory (+3%)
- Adjustments downward: no genetic validation for NLRP3 in PD (-5%), N=36 is severely underpowered for efficacy (-5%), single-site study limits generalizability (-3%)
- Net: ~15-20%

**Signal analysis:** The funding structure is revealing. Cure Parkinson's and Van Andel Institute are bearing trial costs, with MJFF funding preclinical work -- this is a nonprofit-driven program, not a pharma-conviction-driven one. Olatec contributes drug but not full trial economics. This lowers the bar for Olatec (limited downside) but also signals that no pharma partner has licensed the PD indication despite the class being validated by the Novartis/IFM Tre ($1.6B) and Roche/Inflazome deals. The fact that Roche -- which owns an NLRP3 program -- chose to develop its own molecule (selnoflast) rather than in-license dapansutrile is notable. The Cambridge group's decision to enrich for hsCRP >1 is scientifically sound and could identify a precision-medicine angle that larger, undifferentiated NLRP3 programs miss. If DAPA-PD shows safety and inflammatory biomarker engagement, the next step would be a larger multi-center efficacy trial -- likely requiring pharma partnership or substantially larger grant funding. If biomarker engagement fails despite the enriched population, the NLRP3-specific thesis for PD would weaken materially relative to broader immunomodulatory approaches.

## References

### Clinical Trials
- [DAPA-PD Phase 2](https://clinicaltrials.gov/study/NCT07157735) -- NCT07157735
- [Dapansutrile in Gout Phase 2a](https://clinicaltrials.gov/ct2/show/NCT03534297) -- NCT03534297
- [Dapansutrile in COVID-19 Phase 2](https://clinicaltrials.gov/ct2/show/NCT04540120) -- NCT04540120

### Key Publications
- [Dapansutrile, an oral selective NLRP3 inflammasome inhibitor, for treatment of gout flares: Phase 2a trial | Lancet Rheumatology (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7523621/)
- [Phase 1B Safety/PD Study of Dapansutrile in Systolic Heart Failure | J Cardiovasc Pharmacol (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7774821/)
- [OLT1177 (Dapansutrile) Ameliorates Experimental Autoimmune Encephalomyelitis Pathogenesis | Frontiers Immunol (2019)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2019.02578/full)
- [Clinically advanced NLRP3 inhibitor modulates microglial transcriptome and alleviates alpha-synuclein-induced progression of parkinsonism | J Neuroinflammation (2026)](https://link.springer.com/article/10.1186/s12974-026-03716-3)
- [Pharmacologic NLRP3 Inhibition Modulates Parkinson's Disease Pathogenesis | bioRxiv (2025)](https://www.biorxiv.org/content/10.1101/2025.10.22.683837v1.full.pdf)
- [Lack of genetic evidence for NLRP3 inflammasome involvement in PD pathogenesis | npj Parkinson's Disease (2024)](https://www.nature.com/articles/s41531-024-00744-9)
- [NLRP3 expression in mesencephalic neurons and a rare polymorphism associated with decreased PD risk | npj Parkinson's Disease (2018)](https://www.nature.com/articles/s41531-018-0061-5)
- [Targeting the inflammasome in Parkinson's disease | Frontiers Aging Neurosci (2022)](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.957705/full)
- [Dapansutrile in multidisciplinary therapeutic applications: mechanisms and clinical perspectives | Frontiers Pharmacol (2025)](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1731165/full)

### Press Releases & Filings
- [Olatec Therapeutics Presented Preclinical Evidence of Disease-Modifying Activity with Dapansutrile in its Parkinson's Studies (2025)](https://www.prnewswire.com/news-releases/olatec-therapeutics-presented-preclinical-evidence-of-disease-modifying-activity-with-dapansutrile-in-its-parkinsons-studies-302665774.html)
- [Olatec Therapeutics to Conduct Phase 2 Clinical Trial in Early PD (Feb 2024)](https://www.businesswire.com/news/home/20240220762945/en/Olatec-Therapeutics-to-Conduct-a-Phase-2-Clinical-Trial-in-Patients-with-Early-Parkinsons-Disease-with-its-NLRP3-Inhibitor-Dapansutrile)
- [Cure Parkinson's and Van Andel Institute Fund Phase 2 Clinical Trial of Dapansutrile (2024)](https://www.vai.org/article/cure-parkinsons-and-van-andel-institute-fund-phase-2-clinical-trial-of-dapansutrile-for-parkinsons/)
- [Olatec $40M Series A Financing Closure (Feb 2023)](https://www.businesswire.com/news/home/20230223005975/en/Olatec-Therapeutics-Announces-the-Final-Closing-Led-by-Sanders-Morris-Harris-on-Its-$40-Million-Series-A-Financing-Round)
- [Dapansutrile profile | Alzforum](https://www.alzforum.org/therapeutics/dapansutrile)
- [MJFF Grant: Assessing Dapansutrile in NLRP3 Pathway for PD](https://www.michaeljfox.org/grant/assessing-ability-dapansutrile-selective-oral-inhibitor-nlrp3-neuroinflammatory-pathway)

### Regulatory & Market
- [Novartis acquires IFM Tre -- NLRP3 portfolio ($310M upfront + $1.265B milestones) | Novartis (2019)](https://www.novartis.com/news/media-releases/novartis-adds-clinical-and-preclinical-anti-inflammatory-programs-portfolio-acquisition-ifm-tre)
- [NLRP3 inhibitors stoke anti-inflammatory ambitions | Nature Reviews Drug Discovery (2019)](https://www.nature.com/articles/d41573-019-00086-9)
- [PD Drug Therapies in the Clinical Trial Pipeline: 2024 Update | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307066/)
- [2026: Research Progress and Outlook | Cure Parkinson's](https://cureparkinsons.org.uk/2026/01/2026-research-progress/)
