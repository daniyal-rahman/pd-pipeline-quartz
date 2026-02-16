---
drug_name: "Radotinib"
aliases: ["Radotinib HCl", "Supect", "RT51EP1902"]
target: "c-Abl tyrosine kinase"
mechanism: "Second-generation c-Abl tyrosine kinase inhibitor that suppresses alpha-synuclein phosphorylation and aggregation via c-Abl inhibition, with 3.3x superior BBB penetration vs. nilotinib"
modality: "kinase inhibitor"
developer: "Il-Yang Pharmaceutical"
company_type: "biotech"
publicly_traded: true
ticker: "007570.KS (KOSPI)"
partner: ""
partner_type: ""
stage: "Phase 2"
status: "Active"
patient_population: "Clinically probable PD within 3 years of symptom onset, positive DAT-SPECT"
route_of_administration: "oral (once daily)"
key_biomarkers: ["MDS-UPDRS", "DaT-SPECT", "PK/CSF levels"]
confidence_rating: "3/10"
next_catalyst: "Phase 2 data readout (safety, tolerability, PK, exploratory efficacy)"
catalyst_date: "2026-2027 (estimated)"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/il-yang-pharmaceutical]]"
---

# Radotinib

## Summary

Radotinib is a second-generation c-Abl tyrosine kinase inhibitor developed by Il-Yang Pharmaceutical (Korean biotech, KOSPI: 007570) and approved in South Korea for chronic myeloid leukemia (CML) since 2012, now being repurposed for Parkinson's disease. The Phase 2 trial (NCT04691661, N=40) is a small, dose-escalation safety/tolerability/PK study across four dose levels (50-200 mg) running at seven Korean sites. As of mid-2024, the trial was still listed as recruiting — significantly delayed from its original 2022 completion target — and no clinical results have been disclosed. Preclinical work from Johns Hopkins (Lee et al., Human Molecular Genetics 2018) showed 3.3x superior brain penetration vs. nilotinib and neuroprotection in alpha-synuclein PFF mouse models, but the c-Abl field has since suffered devastating setbacks: [[k0706|vodobatinib]] (PROSEEK, N=513) was terminated for futility with concerning NfL elevations, and nilotinib (NILO-PD) showed no benefit. If radotinib's Phase 2 demonstrates clean safety and adequate CNS exposure, it could provide supportive data for the c-Abl hypothesis alongside [[risvodetinib]]. If it fails or shows harm signals similar to [[k0706|vodobatinib]], it further narrows the path for the entire c-Abl class to [[risvodetinib]] alone.

## Notes

### Science
- c-Abl (Abelson tyrosine kinase) is activated by misfolded alpha-synuclein and in turn phosphorylates alpha-synuclein at Y39, impairing parkin function and autophagy, creating a toxic feedforward loop of aggregation and dopaminergic neuron death — inhibiting c-Abl aims to break this amplification cycle
- Radotinib is a second-generation Bcr-Abl kinase inhibitor structurally related to imatinib and nilotinib, originally developed and approved in South Korea for Philadelphia chromosome-positive CML (brand name: Supect, approved January 2012)
- Key preclinical finding (Lee et al., Human Molecular Genetics 2018, Johns Hopkins/Il-Yang collaboration): radotinib achieves **3.3x higher brain concentrations** than nilotinib after single oral administration — the superior BBB penetration addresses the primary failure mode of nilotinib in NILO-PD
- In vitro: radotinib reduced alpha-synuclein PFF-induced Lewy body and Lewy neurite-like aggregates in a dose-dependent manner and rescued impaired mitochondrial respiration in neurons exposed to pathological aggregates
- In vivo (alpha-synuclein PFF mouse model): oral radotinib at 3, 10, and 30 mg/kg inhibited c-Abl activation, prevented dopaminergic neuron loss, suppressed neuroinflammation (microglial/astrocyte activation in substantia nigra), and restored behavioral deficits — notably, the lowest dose (3 mg/kg) was effective, suggesting a wide therapeutic window
- Key distinction from [[risvodetinib]]: radotinib is a repurposed oncology drug (like nilotinib and [[k0706|vodobatinib]]), not purpose-built for neurological indications — this matters because oncology-derived c-Abl inhibitors carry off-target kinase activity, cardiotoxicity risk, and myelosuppression potential that purpose-built neuro compounds avoid
- Open scientific questions: (1) whether the 50 mg PD dose achieves sufficient brain c-Abl inhibition without oncology-level toxicity; (2) whether radotinib produces the concerning NfL elevations seen with [[k0706|vodobatinib]] in PROSEEK; (3) whether the preclinical BBB advantage translates to clinical CNS exposure at PD-relevant doses

### Clinical

**Phase 2 (RT51EP1902)** | NCT04691661 | N=40 | Clinically probable PD, symptom onset within 3 years, positive DAT-SPECT, age 40-80
- **Primary endpoint:** Safety and tolerability
- **Secondary endpoints:** Pharmacokinetics; exploratory efficacy measures
- **Design:** Randomized, double-blind, placebo-controlled, dose-escalation across 4 dose cohorts (50 mg, 100 mg, 150 mg, 200 mg); 8 active : 2 placebo per cohort; 6 months treatment per dose level
- **Sites:** 7 sites in South Korea
- **Status:** Recruiting (last updated July 2024); significantly delayed from original estimated completion of 2022. Trial initiated September 2021
- **Interpretation:** This is a small safety/PK study, not powered for efficacy. The dose-escalation design (50-200 mg) will establish whether CML-level dosing is needed for PD or whether lower doses with adequate brain penetration suffice. No results have been disclosed as of February 2026. The extended delay raises questions about enrollment pace — 40 patients across 7 Korean sites should not require 4+ years unless regulatory, manufacturing, or strategic issues intervened

### Financial
- Il-Yang Pharmaceutical (KOSPI: 007570) is a mid-size Korean pharma company with market cap ~$169M USD (as of mid-2025); also traded as IYPHF on US OTC markets
- Il-Yang's core business spans pharmaceuticals, food products, cosmetics, and antacid raw materials — PD is not a primary therapeutic focus
- Radotinib generates revenue from Korean CML indication (marketed as Supect); PD development appears to be a low-investment academic-originated initiative leveraging existing drug supply
- No disclosed pharma partnership or licensing deal for the PD indication — Il-Yang appears to be funding the small Phase 2 internally
- The 40-patient Korean-only trial is extremely low-cost by global standards (estimated $3-8M), consistent with a toe-in-the-water approach rather than a committed disease modification program
- No disclosed venture or external financing specifically for the PD program

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "c-Abl") AND file.name != "radotinib"
SORT stage DESC
```

- Radotinib enters a c-Abl competitive field defined by failure: nilotinib (NILO-PD, N=76) showed no benefit and insufficient CNS exposure; [[k0706|vodobatinib]] (PROSEEK, N=513) was terminated for futility with dose-dependent NfL elevations suggesting neuronal harm
- [[risvodetinib]] (ABLi Therapeutics, Phase 2b) is the clear c-Abl class leader — purpose-built for brain penetration, clean safety profile, the only c-Abl inhibitor to show alpha-synuclein aggregate clearance in human skin biopsy, and advancing to registrational CAMPD Phase 2b/3 (~450 patients)
- Radotinib's competitive position is weak: it is a repurposed oncology drug (same origin story as the two failed c-Abl inhibitors), running a small safety trial (N=40) in a single country, with no disclosed results and multi-year delays
- The one potential advantage: radotinib is an approved, marketed drug in Korea with known manufacturing, supply chain, and human safety database from CML — if the PD trial shows clean safety and CNS exposure, regulatory pathways in Korea could be accelerated
- If [[risvodetinib]] CAMPD succeeds, radotinib becomes redundant unless it demonstrates a differentiated profile. If CAMPD fails, the c-Abl hypothesis is likely dead and radotinib's PD program becomes unjustifiable

## Analysis

Radotinib's PD program occupies an awkward position in the c-Abl landscape. The preclinical data from Johns Hopkins was genuinely compelling in 2018 — 3.3x better brain penetration than nilotinib, dose-dependent neuroprotection, and a strong mechanistic rationale. But the field has moved dramatically since then, and not in a favorable direction. Two c-Abl inhibitors have failed clinically (nilotinib and [[k0706|vodobatinib]]), and [[risvodetinib]] has leapfrogged radotinib with human biomarker data showing synuclein clearance and a clear registrational path.

**Analytical estimate — Probability of meaningful clinical contribution: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: c-Abl inhibitors in PD are 0/2 on efficacy endpoints, and radotinib shares the "repurposed oncology drug" profile of both failures → starting point ~8%
- Adjustments upward: 3.3x better brain penetration than nilotinib is a genuine pharmacological differentiator (+5%); preclinical neuroprotection data is robust and from a top lab (Johns Hopkins) (+3%); approved drug with known human safety profile reduces Phase 1-level risk (+2%)
- Adjustments downward: N=40 trial too small to generate efficacy signal (-3%); multi-year enrollment delays suggest low organizational commitment (-3%); oncology-derived compound carries off-target toxicity risk highlighted by vodobatinib NfL findings (-3%); no pharma partner signals limited external validation (-2%)
- Net: ~10-15%

**Signal analysis:**
- Il-Yang's behavior signals low conviction: a 40-patient trial at 7 domestic sites is the minimum viable clinical experiment. The multi-year delay without public explanation suggests this is not a strategic priority. Compare this to ABLi Therapeutics, which was purpose-built to advance [[risvodetinib]] with dedicated leadership, FDA engagement, and registrational trial planning
- The Korean-only geography limits the trial's regulatory and commercial impact. Even with positive results, a 40-patient safety study in Korean patients would not support U.S. or EU registration — it would only justify a larger multinational trial, adding years to the development timeline
- The most valuable outcome from this trial is not a path to registration for radotinib itself, but corroborative data for the c-Abl hypothesis. If radotinib shows clean safety (no NfL elevations) and confirmed CSF exposure at PD doses, it strengthens the case that [[k0706|vodobatinib]]'s failure was compound-specific rather than target-specific — which directly benefits [[risvodetinib]]
- The preclinical collaboration with Johns Hopkins (Valina Dawson lab) is notable — this is the same group that has driven much of the foundational c-Abl/PD research. However, academic preclinical enthusiasm has not translated to clinical success in this target class

**Decision tree:**
- If Phase 2 shows clean safety + CSF exposure → supports c-Abl hypothesis alongside [[risvodetinib]], but radotinib likely needs a larger multinational trial to advance meaningfully
- If Phase 2 shows NfL elevations or safety concerns → another repurposed oncology c-Abl inhibitor fails, further isolating [[risvodetinib]] as the only viable approach and raising the question of whether purpose-built design is essential for this target
- If Phase 2 data is never disclosed (trial abandoned quietly) → signals that Il-Yang has deprioritized PD, consistent with the enrollment delays

## References

### Clinical Trials
- [Phase 2 Safety/Tolerability/PK/Efficacy Study](https://clinicaltrials.gov/study/NCT04691661) — NCT04691661

### Key Publications
- [The c-Abl inhibitor, Radotinib HCl, is neuroprotective in a preclinical Parkinson's disease mouse model | Human Molecular Genetics (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6005030/)
- [Parkinson's Disease Modification Through Abl Kinase Inhibition: An Opportunity | Movement Disorders (2022)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.28858)
- [c-Abl and Parkinson's Disease: Mechanisms and Therapeutic Potential | PMC (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5676866/)
- [Radotinib Decreases Prion Propagation and Prolongs Survival Times in Models of Prion Disease | IJMS (2023)](https://www.mdpi.com/1422-0067/24/15/12241)

### Press Releases & Filings
- [Radotinib Profile | Veeva Clinical Trials](https://ctv.veeva.com/study/safety-tolerability-pharmacokinetics-and-efficacy-study-of-radotinib-in-parkinsons-disease)
- [Is Radotinib ABL to beat Nilotinib? | Science of Parkinson's (2018)](https://scienceofparkinsons.com/2018/06/17/radotinib/)

### Regulatory & Market
- [Ilyang Pharmaceutical Co., Ltd (KOSPI: 007570) | Yahoo Finance](https://finance.yahoo.com/quote/007570.KS/)
- [Radotinib Drug Profile | Patsnap Synapse](https://synapse.patsnap.com/drug/14b174c61c60454ca3605ac7d431145c)
- [Radotinib | ScienceDirect Topics](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/radotinib)
