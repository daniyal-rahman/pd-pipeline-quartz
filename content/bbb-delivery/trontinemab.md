---
drug_name: "Trontinemab"
aliases: ["RO7126209", "RG6102", "brain shuttle gantenerumab"]
target: "amyloid-beta (BBB-shuttled via TfR1)"
mechanism: "BrainShuttle bispecific antibody combining anti-amyloid-beta (gantenerumab) with monovalent TfR1 binding for enhanced brain penetration via receptor-mediated transcytosis"
modality: "bispecific antibody"
developer: "Roche"
company_type: "big pharma"
publicly_traded: true
ticker: "ROG.SW"
partner: ""
partner_type: ""
stage: "Phase 3"
status: "Active"
patient_population: "Early Alzheimer's disease"
route_of_administration: "IV"
key_biomarkers: ["amyloid PET", "ARIA-E MRI", "pTau217", "pTau181", "CSF MTBR-tau243", "neurogranin"]
confidence_rating: "7/10"
next_catalyst: "Phase 3 readout"
catalyst_date: "~2028"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery, claude]
date: 2026-02-16
company_link: "[[companies/roche]]"
---

# Trontinemab

## Summary

Trontinemab is the first BBB shuttle antibody to demonstrate human proof-of-concept: 92% amyloid PET negativity at 28 weeks (3.6 mg/kg Q4W) with <5% ARIA-E — a transformative safety advantage over [[lecanemab]] (13% ARIA-E) and [[donanemab]] (24% ARIA-E). Roche (big pharma, ROG.SW) initiated the TRONTIER 1 and 2 Phase 3 trials in September 2025, enrolling ~1,600 patients across 18 countries, with CDR-SB primary endpoint readout expected ~2028. The critical PD implication: Roche published preclinical data (npj Parkinson's Disease, 2025) on a BrainShuttle-enabled anti-alpha-synuclein antibody showing enhanced brain exposure and aggregate clearance, and the modular 2+1 format is explicitly designed for payload swapping — meaning [[prasinezumab]] or a successor anti-alpha-synuclein could be BrainShuttle-enabled if trontinemab validates the platform in Phase 3. If TRONTIER succeeds, it validates TfR1-mediated transcytosis as the leading CNS delivery platform and positions Roche to apply BrainShuttle across AD, PD, and broader neurodegeneration; if it fails, the entire BBB shuttle thesis suffers a major setback and competing platforms ([[bbb-delivery/grabody-b|Grabody-B/IGF1R]], [[bbb-delivery/ban2803|BioArctic BrainTransporter]]) inherit the clinical leadership burden.

## Notes

### Science

- **Molecular architecture:** 2+1 bispecific format — bivalent anti-amyloid-beta Fab arms (derived from gantenerumab) plus a single anti-TfR1 cross-Fab fused to the HC C-terminus. The monovalent TfR1 arm is the key design choice: bivalent TfR1 binding traps antibodies in lysosomes for degradation, whereas monovalent low-affinity binding enables "bind-and-release" transcytosis across brain endothelium
- **Fc engineering:** The cross-Fab is sterically positioned so that when the BrainShuttle module binds TfR1 on endothelial cells, the anti-amyloid arms clash with FcgammaR on effector cells, preventing ADCC/CDC against TfR1-expressing cells. This is the structural solution to the reticulocyte toxicity problem — complemented by LALA/PGLALA Fc mutations that further silence effector function
- **Brain penetration (NHP data):** 4-18x higher brain AUC compared to unmodified gantenerumab, depending on brain region. Striatum showed the greatest enhancement (33x higher Kp, 17.5x AUC gain). Cerebellum showed the least (7x Kp, 3.77x AUC gain). Brain Kp values reached ~0.5% across tissues, vs ~0.03% for standard IgG
- **Dose efficiency:** Human PK modeling predicted 210 mg trontinemab Q4W would match 600 mg gantenerumab Q4W for amyloid reduction — a ~3x dose reduction achieved through improved brain delivery rather than higher systemic exposure. In clinical practice, 3.6 mg/kg (approximately 250-290 mg for average adult) is the selected Phase 3 dose
- **Target-mediated drug disposition (TMDD):** The transcytosis process that shuttles trontinemab across the BBB simultaneously clears it from plasma. This creates an inverse relationship: more brain delivery = less systemic exposure = lower peripheral side effects. This is a fundamental pharmacologic advantage over conventional antibodies, which rely on high systemic concentrations to achieve modest CNS penetration
- **TfR1 biology concerns:** TfR1 is expressed on immature red blood cells (reticulocytes) and is essential for iron uptake during erythropoiesis. Monovalent binding + Fc silencing mitigates but does not eliminate the risk of reticulocyte depletion. Age-related TfR1 expression at the BBB is a second concern: vascular TfR protein is significantly elevated in neonatal vs adult mice, with a modest decline from young to aged adults, though TfR-mediated transport remains functionally stable in adult and aged animals and in Alzheimer's mouse models
- **Anti-TfR1 Fab does not compete with natural transferrin:** The binding epitope is non-overlapping with transferrin's TfR1 binding site, so iron metabolism is not disrupted

### Clinical

**Phase 1 (Healthy Volunteers)** | NCT04023994 | N=not disclosed | Healthy adults
- **Primary endpoint:** Safety, tolerability, PK → Completed, clean safety profile
- **Key finding:** Established PK parameters and confirmed TfR1-mediated transcytosis in humans
- **Status:** Completed

**BrainShuttle AD (Phase 1b/2a)** | NCT04639050 | N=114 (dose-expansion) | Prodromal or mild-to-moderate AD, amyloid-positive
- **Design:** Four sequential dose cohorts (0.2, 0.6, 1.8, 3.6 mg/kg) given IV Q4W for 28 weeks; randomized, double-blind, placebo-controlled
- **Primary endpoint (amyloid PET):**
  - 1.8 mg/kg: -78 centiloid mean reduction at 28 weeks; 67% amyloid-negative (<24 CL)
  - 3.6 mg/kg: -99 centiloid mean reduction at 28 weeks; **92% amyloid-negative** (<24 CL); **71% deeply cleared** (<11 CL)
- **Exploratory clinical efficacy (not powered):** CDR-SB favored treatment by 0.2 points; MMSE favored treatment by 1.5 points vs placebo at 28 weeks
- **Tau biomarkers (AAIC 2025 data):** Significant reductions in CSF pTau181, pTau217, total tau, and neurogranin. CSF MTBR-tau243 (a tangle marker) rose 22% in placebo, remained flat at 1.8 mg/kg, and declined 8% at 3.6 mg/kg — suggesting downstream tau pathology reduction
- **Safety (blinded, N=149 across 1.8 + 3.6 mg/kg cohorts):**
  - **ARIA-E:** 4/149 cases (<5%), all radiographically mild. In Part 1 (N=60): 1 ARIA-E, 1 ARIA-H
  - **Anemia:** 18% at 1.8 mg/kg, 10% at 3.6 mg/kg — mostly mild, transient, resolved upon treatment cessation. Paradoxically lower at higher dose (possibly due to faster receptor saturation at higher dose reducing reticulocyte engagement duration)
  - **Infusion-related reactions:** Most common AE; mild-to-moderate; significantly reduced with steroid premedication
- **Status:** Ongoing (extended follow-up); Part 2 dose expansion data presented at AD/PD 2025 (April) and AAIC 2025 (July)
- **Interpretation:** The amyloid clearance data are best-in-class. 92% amyloid negativity at 28 weeks at a dose of 3.6 mg/kg (roughly one-third the systemic exposure of lecanemab at 10 mg/kg Q2W) is unprecedented. The ARIA-E rate of <5% (blinded, includes placebo) compares favorably to 13% for lecanemab and 24% for donanemab. The anemia signal is manageable but requires monitoring. The tau biomarker reductions are an important secondary signal suggesting that aggressive amyloid clearance reduces downstream tauopathy.

**TRONTIER 1 (Phase 3)** | NCT07169578 | N=800 | Early symptomatic AD (MCI to mild dementia, MMSE >=22)
- **Design:** Multicenter, randomized, double-blind, placebo-controlled. 3.6 mg/kg IV Q4W for 6 months, then Q3M for total 18 months
- **Primary endpoint:** CDR-SB change from baseline at 18 months
- **Secondary endpoints:** ADAS-Cog13, ADCS-ADL, global CDR, cognition/function composites, behavioral symptoms, QoL
- **Status:** Recruiting as of October 2025; 18 countries
- **Primary completion:** July 2028

**TRONTIER 2 (Phase 3)** | NCT07170150 | N=800 | Identical design to TRONTIER 1
- **Status:** Recruiting as of October 2025
- **Primary completion:** July 2028

**PrevenTRON (Phase 3, planned)** | NCT TBD | N=TBD | Preclinical AD (amyloid-positive, cognitively normal)
- **Design:** Prevention trial in at-risk individuals, supported by TRAVELLER pre-screening study using Elecsys pTau217 blood test for community outreach
- **Status:** Planned; details pending

### Financial

- **Roche context:** Trontinemab is internally developed — Roche built the BrainShuttle platform in-house, not via acquisition. This is significant because it means Roche retains full IP ownership and manufacturing control, with no upfront payments, milestone obligations, or royalties owed to a licensor
- **Gantenerumab history:** Roche previously advanced gantenerumab (the parent antibody, without BrainShuttle) to Phase 3 in AD (GRADUATE 1 and 2 trials), where it failed to slow cognitive decline despite showing amyloid clearance. Roche wrote off the program and pivoted to trontinemab. The failure of unconjugated gantenerumab at high doses (subcutaneous, limited brain penetration) is actually the strongest validation of the BrainShuttle concept: the same antibody, reformulated for brain delivery, produces dramatically superior amyloid clearance at lower doses
- **BrainShuttle deal ecosystem:**
  - **Manifold Bio (November 2025):** $55M upfront, up to $2B total. Roche licensed Manifold's AI-driven mDesign platform to discover next-generation BBB shuttles beyond TfR1. Manifold leads early discovery; Roche takes over preclinical/clinical. Manifold retains rights to shuttles outside Roche's licensed targets
  - **Sangamo Therapeutics (August 2024):** $50M upfront, up to $1.9B total. Genentech (Roche) exclusively licensed Sangamo's STAC-BBB neurotropic AAV capsid (IV-administered, BBB-crossing) plus zinc finger repressors targeting MAPT (tau). ZFR lead achieved >95% MAPT knockdown with no off-targets; STAC-BBB demonstrated widespread CNS expression after single IV dose in NHP
- **Peak sales context:** The AD antibody market is projected at $15-20B by 2030. If trontinemab's safety advantage (lower ARIA-E, lower dose, less frequent dosing) translates to a Phase 3 win, it could displace [[lecanemab]] and [[donanemab]] as best-in-class. Consensus peak sales estimates for a best-in-class AD antibody with superior ARIA profile are $5-10B
- **Dosing regimen economics:** Q4W for 6 months transitioning to Q3M thereafter — significantly fewer infusions than lecanemab (Q2W indefinitely). The dosing regimen alone is a major competitive advantage for payers and patients

### Competitive

**vs. Conventional AD antibodies:**

| Parameter | Trontinemab | Lecanemab | Donanemab |
|-----------|-------------|-----------|-----------|
| Dose | 3.6 mg/kg Q4W -> Q3M | 10 mg/kg Q2W | 700/1400 mg Q4W |
| Amyloid negativity (28 wk) | 92% | ~68% (18 mo) | ~84% (18 mo) |
| ARIA-E | <5% (blinded) | 12.6% | 24% |
| Anemia | 10-18% (mild, transient) | Not reported | Not reported |
| Dosing frequency | Monthly then quarterly | Biweekly | Monthly then stop |
| Phase 3 CDR-SB | Pending (~2028) | -0.45 pts (27% slowing) | -0.67 pts (36% slowing) |
| Regulatory status | Phase 3 | Approved (Jan 2023) | Approved (Jul 2024) |

- Trontinemab achieves equivalent or superior amyloid clearance at roughly one-third the systemic exposure of lecanemab, with dramatically lower ARIA-E. The clinical question is whether this translates to equivalent or superior cognitive benefit — amyloid clearance correlates with but does not perfectly predict CDR-SB improvement
- If TRONTIER replicates the 27-36% CDR-SB slowing seen with lecanemab/donanemab at <5% ARIA-E, trontinemab becomes the clear best-in-class AD antibody. The lower ARIA rate would expand the treatable population (currently ~15-25% of eligible patients are excluded from lecanemab/donanemab due to ARIA risk factors including APOE4 homozygosity)

**vs. Other BBB shuttle platforms:**

- [[bbb-delivery/grabody-b|ABL Bio Grabody-B (IGF1R)]]: Three pharma deals ($5.4B total) but no human efficacy data. First clinical asset (ABL301) deprioritized by Sanofi before Phase 2. IGF1R theoretically avoids reticulocyte toxicity but this advantage is unproven in humans. Trontinemab's Phase 2 data showing manageable anemia weakens IGF1R's primary differentiation argument
- [[bbb-delivery/ban2803|BioArctic BrainTransporter (TfR)]]: Three deals (BMS, Eisai, Novartis) totaling $2B+. Uses the same TfR1 receptor as BrainShuttle but with a different engineering approach. Less public clinical data than trontinemab
- **Denali Transport Vehicle (TfR1/CD98hc):** BLA submitted for tividenofusp alfa (Hunter syndrome) with PDUFA April 2026. Closest to regulatory approval among BBB shuttles but targets a lysosomal storage disorder, not neurodegeneration

**PD-relevant competitive positioning:**

- Roche published preclinical data (Greter et al., npj Parkinson's Disease 2025) on a BrainShuttle-enabled anti-alpha-synuclein antibody demonstrating preferential binding to aggregates, prevention of seeding in vitro and in vivo, and enhanced brain exposure vs non-shuttled counterpart. This is a distinct program from SAR446159 (which uses IGF1R-based shuttle)
- The modular 2+1 BrainShuttle format is explicitly designed for payload swapping. If trontinemab validates in AD, Roche could rapidly advance a BrainShuttle-[[prasinezumab]] construct. Roche's existing alpha-synuclein program (prasinezumab, co-developed with [[companies/prothena|Prothena]]) provides the natural payload candidate
- ABL Bio's Grabody-B-prasinezumab combination ([[abl301|ABL301]]) was deprioritized by Sanofi — Roche's in-house BrainShuttle could be the alternative BBB-shuttled anti-alpha-synuclein approach if the delivery hypothesis is correct

## Analysis

**Analytical estimate — Probability of TRONTIER Phase 3 success: ~55-60%. This is our assessment, not from a published source. The reasoning:** Base rate for Phase 3 AD antibodies that clear amyloid is improving (lecanemab succeeded, donanemab succeeded), suggesting ~50% as a floor. Upward adjustments: (1) trontinemab achieves deeper, faster amyloid clearance than either predecessor, and amyloid clearance depth correlates with CDR-SB benefit across the class; (2) the dramatically lower ARIA-E rate should reduce dropouts and confounding from ARIA-related cognitive effects; (3) the tau biomarker reductions suggest an effect beyond amyloid clearance. Downward adjustments: (1) Roche's history with gantenerumab Phase 3 failure is a reminder that amyloid clearance alone does not guarantee clinical benefit; (2) the 18-month endpoint may be too short to capture the full benefit of a lower-ARIA regimen (the safety advantage may matter more for chronic multi-year dosing); (3) Phase 2 exploratory clinical signals were modest (0.2 CDR-SB points, 1.5 MMSE points at 28 weeks in an underpowered study). Net: slightly above base rate.

**Analytical estimate — Probability that BrainShuttle is applied to a PD target within 5 years: ~40%. This is our assessment, not from a published source. The reasoning:** Roche has already published preclinical data on BrainShuttle-anti-alpha-synuclein (npj Parkinson's Disease 2025) and has the prasinezumab program in Phase 3. If TRONTIER validates BrainShuttle in AD, the regulatory and scientific rationale for a BrainShuttle-prasinezumab construct would be strong. However, prasinezumab itself has marginal efficacy signals (PADOVA primary miss at p=0.0657), and Roche may reasonably conclude that the target biology is insufficient regardless of delivery. The key decision node: does Roche believe prasinezumab's marginal results are due to insufficient brain penetration (in which case BrainShuttle fixes the problem) or insufficient target biology (in which case BrainShuttle does not help)?

**Reticulocyte/anemia risk assessment:** The 10-18% anemia rate in Phase 1b/2a is the primary safety liability. It is manageable (mild, transient, reversible) but distinguishes trontinemab from conventional AD antibodies that do not carry this risk. For an Alzheimer's population (median age 70+, many with comorbid iron deficiency or chronic disease anemia), even mild additional anemia may be clinically significant. Phase 3 will need to demonstrate that anemia does not lead to treatment discontinuation or serious adverse outcomes. If it does, this becomes a labeling liability even if TRONTIER meets its primary endpoint.

**TfR1 age-related decline:** Recent data (PMC12357843, 2025) suggest that TfR-mediated BBB transport is elevated in early development but remains stable across adult aging and in Alzheimer's mouse models. This partially alleviates the concern that trontinemab would lose efficacy in elderly patients, though human aging data on TfR1 BBB expression remain limited.

**Decision tree for PD implications:**
- TRONTIER positive + PARAISO (prasinezumab) positive → Roche almost certainly develops BrainShuttle-prasinezumab; the combination of validated delivery and validated target biology is compelling. This would be the most important development in PD disease modification
- TRONTIER positive + PARAISO negative → BrainShuttle platform validated but prasinezumab target biology questioned. Roche pivots BrainShuttle to alternative PD payloads (anti-LRRK2 antibody, GCase enzyme, neuroinflammation target). Timeline extends 3-5 years
- TRONTIER negative → BBB shuttle thesis takes a major hit. IGF1R-based alternatives ([[bbb-delivery/grabody-b|Grabody-B]]) inherit burden of proof but also lose the broader momentum for shuttle technology. PD application deprioritized
- TRONTIER negative + PARAISO positive → Roche advances prasinezumab without BrainShuttle. The insufficient-brain-penetration hypothesis for alpha-synuclein antibodies is weakened (prasinezumab works at 0.1-0.2% CNS penetration). BBB shuttles for PD become unnecessary for this target

## References

### Clinical Trials
- [BrainShuttle AD Phase 1b/2a](https://clinicaltrials.gov/study/NCT04639050) — NCT04639050
- [Phase 1 Healthy Volunteers](https://clinicaltrials.gov/study/NCT04023994) — NCT04023994
- [TRONTIER 1 (Phase 3)](https://clinicaltrials.gov/study/NCT07169578) — NCT07169578
- [TRONTIER 2 (Phase 3)](https://clinicaltrials.gov/study/NCT07170150) — NCT07170150

### Key Publications
- [Delivery of the BrainShuttle amyloid-beta antibody fusion trontinemab to NHP brain and projected efficacious dose regimens in humans | mAbs (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10572082/)
- [Latest results from the dose-expansion part (Part 2) of the BrainShuttle AD study | PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12740976/)
- [Interim biomarker results for trontinemab, a novel BrainShuttle antibody | PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12740797/)
- [A brain-shuttled antibody targeting alpha synuclein aggregates for the treatment of synucleinopathies | npj Parkinson's Disease (2025)](https://www.nature.com/articles/s41531-025-01117-6)
- [Age, dose, and binding to TfR on blood cells influence brain delivery of a TfR-transported antibody | Fluids and Barriers of the CNS (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10173660/)
- [TfR-mediated transport at the BBB is elevated during early development and maintained across aging | PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12357843/)
- [Transferrin receptor-binding BBB shuttle enhances brain delivery and plaque-clearing efficacy | Fluids and Barriers of the CNS (2025)](https://link.springer.com/article/10.1186/s12987-025-00737-7)
- [Balancing brain exposure, pharmacokinetics and safety of transferrin receptor antibodies | mAbs (2025)](https://www.tandfonline.com/doi/full/10.1080/19420862.2025.2592422)
- [Brain-penetrant antibodies for Alzheimer's disease: The next generation? | PMC Editorial (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12413714/)

### Press Releases & Filings
- [Roche presents novel therapeutic and diagnostic advancements at AD/PD 2025 (April 2025)](https://www.roche.com/media/releases/med-cor-2025-04-03)
- [Roche presents new insights at AAIC 2025 (July 2025)](https://www.roche.com/media/releases/med-cor-2025-07-28)
- [Manifold Bio announces strategic collaboration with Roche (November 2025)](https://www.manifold.bio/news/manifold-bio-announces-strategic-collaboration-with-roche-to-develop-multiple-next-generation-brain-shuttles-for-neurological-diseases)
- [Sangamo announces epigenetic regulation and capsid delivery license with Genentech (August 2024)](https://investor.sangamo.com/news-releases/news-release-details/sangamo-therapeutics-announces-global-epigenetic-regulation-and)
- [Roche to advance prasinezumab into Phase 3 for early-stage PD (June 2025)](https://www.roche.com/media/releases/med-cor-2025-06-16)

### Regulatory & Market
- [Trontinemab therapeutics page | AlzForum](https://www.alzforum.org/therapeutics/trontinemab)
- [Trontinemab data strengthen hope for brain shuttles | AlzForum](https://www.alzforum.org/news/conference-coverage/trontinemab-data-strengthen-hope-brain-shuttles)
- [Fast plaque clearance with little ARIA? Trontinemab at AD/PD 2024 | AlzForum](https://www.alzforum.org/news/conference-coverage/fast-plaque-clearance-little-aria-so-teases-trontinemab-adpd-2024)
- [Genentech pipeline — Trontinemab](https://www.gene.com/medical-professionals/pipeline/trontinemab)
- [Roche spells out Phase 3 plans for trontinemab | Global Alzheimer's Platform (August 2025)](https://globalalzplatform.org/2025/08/22/alz-forum-roche-spells-out-phase-three-plans-for-trontinemab/)
- [AD/PD 2025: Roche's BrainShuttle technology promises next generation of amyloid beta mAbs | Clinical Trials Arena](https://www.clinicaltrialsarena.com/analyst-comment/roche-brainshuttle-technology-next-generation-amyloid-beta-mabs/)

---

*Generated: 2026-02-16 | Status: #claude #bbb-delivery*
