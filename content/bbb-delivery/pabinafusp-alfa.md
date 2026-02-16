---
drug_name: "Pabinafusp alfa"
aliases: ["JR-141", "IZCARGO"]
target: "iduronate-2-sulfatase enzyme delivery (BBB-shuttled via TfR1)"
mechanism: "J-Brain Cargo platform fusing anti-TfR1 antibody to iduronate-2-sulfatase for receptor-mediated transcytosis across the BBB"
modality: "bispecific antibody"
developer: "JCR Pharmaceuticals"
company_type: "biotech"
publicly_traded: true
ticker: "4552.T"
partner: "Takeda"
partner_type: "big pharma"
stage: "Approved"
status: "Active"
patient_population: "Hunter syndrome (MPS II)"
route_of_administration: "IV"
key_biomarkers: ["CSF heparan sulfate", "CSF dermatan sulfate", "neurocognitive development"]
confidence_rating: "9/10"
next_catalyst: "Global Phase 3 readout / US filing"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery, claude]
date: 2026-02-16
company_link: "[[companies/jcr-pharmaceuticals]]"
partner_link: "[[companies/takeda]]"
---

# Pabinafusp Alfa

## Summary

Pabinafusp alfa (IZCARGO) is the **first blood-brain barrier-crossing drug approved anywhere in the world** -- a recombinant fusion protein of an anti-human transferrin receptor (TfR1) antibody and iduronate-2-sulfatase (IDS), developed by JCR Pharmaceuticals (biotech, 4552.T) using the J-Brain Cargo platform. Approved by Japan's MHLW in March 2021 under SAKIGAKE designation for MPS II (Hunter syndrome), it demonstrated a 64% reduction in CSF heparan sulfate at 52 weeks (p < 0.001) in a Phase 2/3 trial of 28 patients, with neurocognitive maintenance or improvement in 21/25 evaluable patients (Okuyama et al., Molecular Therapy 2021). Five-year post-marketing data presented at ICIEM 2025 confirmed sustained CSF HS reduction with no new safety signals, making this the most mature clinical dataset for any BBB shuttle drug. A global Phase 3 trial (NCT04573023) completed enrollment in July 2025 across the US, Europe, and Latin America, and Takeda holds ex-US commercialization rights with a US option. The platform's clinical validation is directly relevant to PD: it proves that anti-TfR1 receptor-mediated transcytosis can deliver therapeutic proteins to the CNS via IV dosing -- the same mechanism underlying Denali's Transport Vehicle platform ([[dnl111]], [[dnl422]]) and a direct competitor to ABL Bio's Grabody-B IGF1R shuttle ([[abl301|ABL301]]).

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Takeda |
| Deal Date | September 2021 |
| Upfront | Undisclosed |
| Total (Biobucks) | Undisclosed (upfront + milestones + tiered royalties) |
| Deal Type | Licensing/co-development |
| Territory | Takeda: ex-US (excluding Japan/certain APAC). US option upon Phase 3 completion. JCR retains Japan and select APAC |

**Alexion/AstraZeneca deals (platform-level, not pabinafusp-specific):**

| Deal | Date | Terms | Scope |
|------|------|-------|-------|
| J-Brain Cargo for neurodegenerative disease | April 2023 | Undisclosed upfront + milestones | Single undisclosed neurodegenerative target |
| J-Brain Cargo for oligonucleotide therapeutics | December 2023 | Undisclosed | ASO/siRNA + BBB shuttle discovery |
| JUST-AAV capsid license | July 2025 | Undisclosed upfront + up to $825M milestones | Up to 5 genomic medicine programs |

## Notes

### Science
- Pabinafusp alfa is a recombinant fusion protein consisting of a humanized anti-human transferrin receptor 1 (TfR1) IgG antibody with intact human iduronate-2-sulfatase (IDS) enzyme genetically fused to each Fab arm, creating a bivalent molecule with both BBB-crossing and enzymatic activity ([Sonoda et al., Molecular Therapy 2018](https://pubmed.ncbi.nlm.nih.gov/29606503/))
- The J-Brain Cargo platform exploits TfR1-mediated transcytosis: the antibody binds TfR1 on BBB endothelial cells, triggers receptor-mediated endocytosis, crosses the endothelial cell via transcytosis, and releases the fusion protein into the brain parenchyma. Once in the CNS, the fused IDS enzyme is internalized by neurons and glia via the mannose-6-phosphate receptor for lysosomal delivery ([Nature Drug Discovery 2021](https://www.nature.com/articles/d41573-021-00066-y))
- Preclinical validation: in hTfR knockin mice and nonhuman primates, IV-administered JR-141 was detected in the brain, while unconjugated IDS was not. In IDS-knockout hTfR-KI mice (MPS II model), IV JR-141 reduced GAG accumulation in both peripheral tissues and brain ([Sonoda et al., Molecular Therapy 2018](https://pubmed.ncbi.nlm.nih.gov/29606503/))
- Key molecular distinction from Denali's Transport Vehicle: pabinafusp alfa uses a full anti-TfR1 antibody as the shuttle, while Denali's tividenofusp alfa uses an engineered Fc domain (not a full antibody) that binds TfR1. Both exploit the same receptor but differ in binding affinity, avidity, and recycling kinetics -- parameters that affect brain exposure, peripheral clearance, and safety
- Key distinction from [[abl301|ABL301]] (Grabody-B): pabinafusp uses TfR1 as the transcytosis receptor, while Grabody-B uses IGF1R. The pabinafusp approval proves TfR1-mediated transcytosis works in humans; IGF1R-based approaches have not yet demonstrated comparable clinical evidence
- The platform is modular: JCR has applied J-Brain Cargo to multiple lysosomal enzymes (MPS I, MPS IIIA, MPS IIIB, GM2 gangliosidosis), and to non-enzyme payloads via the Alexion collaborations (ASOs, small molecules)
- Open scientific question for PD relevance: TfR1-mediated transcytosis has been validated for enzyme replacement in lysosomal storage disorders where the therapeutic is taken up by cells via mannose-6-phosphate receptor. Whether this mechanism achieves sufficient exposure for targets requiring sustained extracellular or synaptic drug levels (e.g., alpha-synuclein antibodies, LRRK2 inhibitors) remains unproven

### Clinical

**Phase 1/2 (Japan, first-in-human)** | N=14 | MPS II patients
- **Primary endpoint:** Safety/tolerability and CSF GAG reduction
- **Key finding:** Marked reduction of GAG accumulation in the cerebrospinal fluid of patients with MPS-II, demonstrating for the first time in humans that an IV-administered protein could cross the BBB via TfR1-mediated transcytosis and achieve pharmacodynamic effect in the CNS
- **Status:** Completed
- **Publication:** [Okuyama et al., Molecular Therapy 2019; 27(2):456-464](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391590/)

**Phase 2/3 (Japan)** | NCT04573023 | N=28 | MPS II patients | 52 weeks
- **Primary endpoint:** Change in CSF heparan sulfate (HS) concentration --> HS decreased from 5,856 +/- 2,614 ng/mL to 2,124 +/- 882.6 ng/mL at week 52 (64% reduction, p < 0.001)
- **Key secondary:** Neurocognitive development assessment: maintenance or improvement of age-equivalent function in 21/25 evaluable patients. Serum HS and DS concentrations, liver and spleen volumes comparable to conventional idursulfase ERT
- **Safety:** Drug-related AEs in 15/28 patients, all mild or moderate. 14/15 were infusion-associated reactions (IARs), transient. 14/28 patients developed anti-pabinafusp alfa antibodies, but no correlation between antibodies and IARs or reduced efficacy. IAR frequency declined over time
- **Status:** Completed. Formed the basis for MHLW approval
- **Publication:** [Okuyama et al., Molecular Therapy 2021; 29(2):671-679](https://pubmed.ncbi.nlm.nih.gov/33038326/)

**Phase 2 (Brazil)** | N=not specified | MPS II patients | 26 weeks
- **Design:** Open-label, randomized, parallel-group comparing 1.0, 2.0, and 4.0 mg/kg/week doses
- **Key finding:** 2.0 mg/kg group demonstrated best combination of safety and efficacy, with marked reductions in substrate concentrations in CSF, serum, and urine
- **Status:** Completed
- **Publication:** [Giugliani et al., Molecular Therapy 2021](https://pubmed.ncbi.nlm.nih.gov/33781915/)

**Global Phase 3** | NCT04573023 | US, Europe, Latin America
- **Design:** Multinational, intended to support US FDA and EU EMA filings
- **Status:** Target enrollment achieved July 2025. Trial ongoing
- **Regulatory designations:** FDA Fast Track, FDA orphan drug, EMA PRIME designation, FDA IND accepted
- **Interpretation:** Successful readout would support Takeda's US commercialization option exercise and EU filing

**Post-Marketing Surveillance (Japan)** | Ongoing through 2030
- **5-year data (ICIEM 2025, September 2025):** Sustained long-term reduction in CSF HS levels up to 5 years. Patients treated before significant neuronopathy showed sustained neurocognitive and somatic benefits; patients with advanced disease showed stabilization. No new safety signals in interim post-marketing analysis. Treatment well tolerated over extended period
- **Source:** [JCR Pharmaceuticals, BusinessWire September 2025](https://www.businesswire.com/news/home/20250908973558/en/JCR-Pharmaceuticals-Presents-Long-Term-Clinical-Data-on-Pabinafusp-Alfa-for-the-Treatment-of-Mucopolysaccharidosis-Type-II-MPS-II-at-ICIEM-2025)

### Financial
- **IZCARGO Japan sales:** JPY 5,700 million (~$38M USD) for FY ending March 2025, growing >10% year-over-year. Q1 FY2025 sales JPY 1,562M, up 13.9% YoY ([JCR FY2025 Q2 Financial Report](https://jcrpharm.com/wp-content/uploads/2025/10/FY2025-Q2-Financial-report-Jul.-1-Sep.-30-2025.pdf))
- JCR projects return to profitability in FY2026: net sales JPY 37,800M, net income JPY 3,000M, driven by IZCARGO growth and contract revenues from Alexion/Takeda partnerships
- **Takeda deal:** Undisclosed upfront + development/commercial milestones + tiered royalties for ex-US rights. Takeda holds US option exercisable upon Phase 3 completion -- Takeda's decision to exercise or pass will be a major signal for the commercial opportunity
- **Alexion/AZ JUST-AAV deal (July 2025):** Undisclosed upfront, up to $225M R&D milestones + $600M commercial milestones ($825M total) for up to 5 programs. This validates JCR's broader platform beyond J-Brain Cargo ([FierceBiotech](https://www.fiercebiotech.com/biotech/astrazenecas-alexion-strengthens-gene-therapy-offering-825m-aav-capsid-pact))
- **Alexion J-Brain Cargo milestones:** First research milestone achieved March 2024 for the neurodegenerative disease collaboration, triggering a payment to JCR ([BusinessWire March 2024](https://www.businesswire.com/news/home/20240319953062/en/JCR-Pharmaceuticals-Announces-Achievement-of-Milestone-Using-J-Brain-Cargo-Technology-for-Neurodegenerative-Disease-in-Research-Collaboration-with-Alexion))
- JCR Pharmaceuticals market cap: ~JPY 100B ($670M USD). Founded 1975, headquartered in Ashiya, Hyogo Prefecture, Japan. Global subsidiaries in US, Europe, and Brazil
- **WORLDSymposium New Treatment Award** received in February 2022 for IZCARGO, recognizing its significance as the first BBB-crossing ERT

### Competitive

The competitive landscape is best understood at two levels: (1) Hunter syndrome specifically and (2) BBB shuttle platforms broadly.

**Hunter syndrome (MPS II) competitors:**
- **Tividenofusp alfa (DNL310, Denali):** Direct competitor using Denali's Transport Vehicle (engineered Fc domain binding TfR1) fused to IDS. BLA submitted; PDUFA date April 5, 2026 (extended from January 5, 2026). Phase 1/2 data published in NEJM (2025). If approved, would be the first BBB-crossing ERT on the US market. Denali's COMPASS Phase 2/3 study (NCT05371613, N=54) uses CSF HS change at 24 weeks as primary endpoint with Vineland Adaptive Behavior Scale as key secondary. FDA granted Breakthrough Therapy Designation
- **Conventional idursulfase (Elaprase, Takeda):** Standard of care ERT; does not cross the BBB, thus ineffective for neuronopathic manifestations. Pabinafusp alfa was designed to replace/supplement this therapy
- Pabinafusp alfa has a 5-year head start on approval over tividenofusp alfa, but only in Japan. The US/EU market is still contested

**BBB platform competitive landscape (PD-relevant):**
- Pabinafusp alfa's approval proves that TfR1-mediated transcytosis works in humans at a pharmacodynamically meaningful level. This directly validates the mechanism used by [[dnl111|DNL111]] (ETV:GCase, Denali), [[dnl422|DNL422]] (OTV:SNCA, Denali), and Roche's Brain Shuttle (trontinemab for Alzheimer's)
- [[abl301|ABL301]] (Grabody-B, IGF1R shuttle) competes at the platform level: ABL Bio's pitch is that IGF1R is safer than TfR1 for chronic dosing (avoids reticulocyte depletion risk). Pabinafusp's 5-year safety record with no new signals weakens this argument, though the MPS II population is small and young -- chronic dosing in older PD patients may differ
- BioArctic BrainTransporter (TfR-based) has deals with BMS, Eisai, and Novartis ($2B+) but no approved products
- The JUST-AAV platform extends JCR's delivery innovation from protein-based BBB shuttles to gene therapy vectors, using miniaturized antibodies on AAV capsid surfaces for tissue-targeted delivery -- a potential competitor to Capsida's engineered AAV approach

## Analysis

Pabinafusp alfa's significance extends far beyond Hunter syndrome. As the first-ever approved drug designed to cross the blood-brain barrier via receptor-mediated transcytosis, it establishes a foundational proof-of-concept that the entire BBB shuttle field depends on. Before IZCARGO, the concept of engineering proteins to exploit endogenous transport receptors for brain delivery was preclinical hypothesis; after IZCARGO, it is regulatory-grade clinical reality. The 5-year post-marketing data showing sustained CSF biomarker reduction and no new safety signals transforms a single clinical trial into a durability dataset -- exactly what regulators and pharma partners need to see before committing to the next wave of BBB-shuttled therapeutics for neurodegeneration.

**Implications for PD drug delivery:** The J-Brain Cargo platform validates TfR1 as a viable transcytosis receptor for chronic IV enzyme delivery. This is directly relevant to Denali's ETV:GCase program ([[dnl111|DNL111]]), which uses the same receptor system to deliver GCase across the BBB for GBA1-PD. However, the translation is not automatic: lysosomal enzyme replacement targets a well-defined intracellular compartment (the lysosome) with a known uptake receptor (mannose-6-phosphate), while PD targets like alpha-synuclein aggregates are extracellular/cytoplasmic and require different pharmacokinetic properties. The question is not whether TfR1 shuttles can get drugs into the brain -- pabinafusp proves they can -- but whether the concentration, distribution, and duration of brain exposure achievable via this mechanism is sufficient for neurodegeneration targets that lack the convenient lysosomal endpoint.

**Analytical estimate -- Platform validation score: 8/10.** This is our assessment, not from a published source. The reasoning: pabinafusp alfa provides the strongest clinical validation of any BBB shuttle platform (regulatory approval + 5-year durability data), earning it the highest score in the field. Adjustments downward: the patient population is pediatric and small (MPS II affects ~500 patients in Japan), limiting generalizability to older, larger populations; the lysosomal endpoint is pharmacologically "easier" than neurodegeneration targets; and the safety profile in children with rare disease may not predict safety in elderly PD patients receiving chronic dosing. The platform's true PD validation will come from Denali's Transport Vehicle programs, not from pabinafusp itself.

**Signal analysis:** The Alexion/AstraZeneca relationship is the strongest platform validation signal. Three separate deals (2023, 2023, 2025) with a major rare disease pharma company, escalating from a single neurodegenerative disease program to a 5-program JUST-AAV capsid license worth $825M in biobucks, indicates increasing confidence in JCR's delivery engineering. The March 2024 research milestone for the neurodegenerative disease program -- achieved within 12 months of the collaboration start -- suggests the J-Brain Cargo technology translated rapidly to a new target. The specific target was not disclosed, but if it is Alzheimer's or PD-related, it would represent a direct entry of JCR's platform into the neurodegenerative space.

**Decision tree:** If the global Phase 3 succeeds and tividenofusp alfa wins US approval (PDUFA April 2026), the BBB shuttle field is validated by two independent programs using TfR1 -- the strongest possible proof-of-concept for the mechanism. This would accelerate investment into TfR1-based PD programs. If pabinafusp's global Phase 3 fails (unlikely given consistent data), or if tividenofusp alfa receives a CRL, the field faces a setback specific to the MPS II indication but the platform concept survives on the strength of Japan's approval and Roche's trontinemab Alzheimer's data.

## References

### Clinical Trials
- [JR-141 Global Phase III Clinical Trial](https://clinicaltrials.gov/study/NCT04573023) -- NCT04573023

### Key Publications
- [A BBB-penetrating anti-human TfR antibody fusion protein for neuronopathic MPS II | Sonoda et al., Molecular Therapy (2018)](https://pubmed.ncbi.nlm.nih.gov/29606503/) -- Preclinical proof-of-concept
- [Iduronate-2-sulfatase with anti-human TfR antibody for neuropathic MPS II: Phase 1/2 trial | Okuyama et al., Molecular Therapy (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391590/) -- First-in-human
- [A Phase 2/3 trial of pabinafusp alfa targeting neurodegeneration in MPS-II | Okuyama et al., Molecular Therapy (2021)](https://pubmed.ncbi.nlm.nih.gov/33038326/) -- Pivotal trial
- [Pabinafusp alfa for MPS-II: Phase 2 trial in Brazil | Giugliani et al., Molecular Therapy (2021)](https://pubmed.ncbi.nlm.nih.gov/33781915/) -- Dose-ranging
- [ERT with pabinafusp alfa for neuronopathic MPS II: integrated preclinical/clinical analysis | IJMS (2021)](https://www.mdpi.com/1422-0067/22/20/10938)
- [TfR-targeting property of pabinafusp alfa: uptake by human brain-derived cells | Frontiers in Drug Delivery (2023)](https://www.frontiersin.org/journals/drug-delivery/articles/10.3389/fddev.2023.1082672/full)
- [Nonclinical safety evaluation of pabinafusp alfa | PMC (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8081988/)
- [CSF heparan sulfate as biomarker for MPS II disease severity and treatment monitoring | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11590453/)

### Press Releases & Filings
- [JCR Pharmaceuticals Announces Approval of IZCARGO (March 2021)](https://www.businesswire.com/news/home/20210323005577/en/JCR-Pharmaceuticals-Announces-Approval-of-IZCARGO-Pabinafusp-Alfa-for-Treatment-of-MPS-II-Hunter-Syndrome-in-Japan)
- [Takeda-JCR Commercialization Agreement (September 2021)](https://www.takeda.com/newsroom/newsreleases/2021/takeda-to-commercialize-next-generation-hunter-syndrome-therapy-through-collaboration-with-jcr-pharmaceuticals/)
- [JCR WORLDSymposium New Treatment Award (February 2022)](https://www.businesswire.com/news/home/20220203005511/en/JCR-Pharmaceuticals-Receives-the-WORLDSymposium%E2%84%A2-New-Treatment-Award-for-IZCARGO%C2%AE-Pabinafusp-Alfa)
- [Alexion J-Brain Cargo Neurodegenerative Disease Milestone (March 2024)](https://www.businesswire.com/news/home/20240319953062/en/JCR-Pharmaceuticals-Announces-Achievement-of-Milestone-Using-J-Brain-Cargo-Technology-for-Neurodegenerative-Disease-in-Research-Collaboration-with-Alexion)
- [JCR 5-Year Long-Term Data at ICIEM 2025 (September 2025)](https://www.businesswire.com/news/home/20250908973558/en/JCR-Pharmaceuticals-Presents-Long-Term-Clinical-Data-on-Pabinafusp-Alfa-for-the-Treatment-of-Mucopolysaccharidosis-Type-II-MPS-II-at-ICIEM-2025)
- [Global Phase III Enrollment Complete (July 2025)](https://www.businesswire.com/news/home/20250702082624/en/JCR-Pharmaceuticals-Announces-the-Achievement-of-Enrollment-in-the-JR-141-Global-Phase-III-Clinical-Trial)
- [Alexion JUST-AAV Capsid License Agreement (July 2025)](https://www.businesswire.com/news/home/20250708539488/en/JCR-Pharmaceuticals-Enters-License-Agreement-with-Alexion-for-Proprietary-JUST-AAV-Capsids-to-be-Used-in-the-Development-of-Genomic-Medicines)

### Regulatory & Market
- [BBB-traversing biologic secures regulatory approval in Japan | Nature Drug Discovery (2021)](https://www.nature.com/articles/d41573-021-00066-y)
- [A new avenue for CNS biotherapeutics | Nature (2024)](https://www.nature.com/articles/d43747-024-00003-z)
- [AstraZeneca's Alexion pens $825M AAV capsid pact with JCR | FierceBiotech (2025)](https://www.fiercebiotech.com/biotech/astrazenecas-alexion-strengthens-gene-therapy-offering-825m-aav-capsid-pact)
- [Denali tividenofusp alfa FDA BLA acceptance and priority review | Denali (2025)](https://investors.denalitherapeutics.com/news-releases/news-release-details/denali-therapeutics-announces-fda-acceptance-and-priority-review)
- [Denali FDA review extension for tividenofusp alfa (November 2025)](https://www.biospace.com/press-releases/denali-therapeutics-announces-fda-review-extension-of-bla-for-tividenofusp-alfa-for-the-treatment-of-mps-ii-hunter-syndrome)
- [JCR FY2025 Q2 Financial Report](https://jcrpharm.com/wp-content/uploads/2025/10/FY2025-Q2-Financial-report-Jul.-1-Sep.-30-2025.pdf)
