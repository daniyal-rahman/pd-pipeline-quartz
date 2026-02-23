---
drug_name: "ASN51"
aliases: []
target: "O-GlcNAcase (OGA)"
mechanism: "Small molecule OGA inhibitor that preserves O-GlcNAcylation of tau and alpha-synuclein, reducing their propensity to form toxic aggregates"
modality: "small molecule"
developer: "Asceneuron"
company_type: "biotech"
publicly_traded: false
partner: ""
stage: "Phase 1"
status: "Deprioritized"
patient_population: "Neurodegenerative diseases (AD primary; PD preclinical)"
route_of_administration: "oral"
key_biomarkers: ["OGA brain occupancy (PET)", "O-GlcNAcylation (PBMC assay)", "plasma pTau217"]
confidence_rating: "2/10"
next_catalyst: "Clarity on program restart or pivot after class-wide OGA failures"
catalyst_date: "Unknown"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/asceneuron]]"
---

# ASN51

## Summary

ASN51 is an oral OGA inhibitor from Asceneuron (biotech, private, Switzerland) that completed five Phase 1 studies demonstrating full CNS uptake and >90% brain OGA occupancy. The Phase 2 trial in Alzheimer's was terminated in November 2024 after just one month of enrollment, following class-wide OGA inhibitor failures at Lilly (ceperognastat) and Biogen (BIIB113). For Parkinson's, ASN51 remains preclinical — an MJFF-funded study in A53T alpha-synuclein mouse models was underway, but the program's future is uncertain given the AD termination and OGA class headwinds. If the OGA mechanism is rehabilitated by new biomarker data or a revised trial design, ASN51's clean Phase 1 profile and demonstrated target engagement could enable rapid re-entry into clinical development. If the class remains cold, Asceneuron's remaining pipeline rests on [[asn90|ASN90]] (licensed to Ferrer for PSP) and early preclinical programs.

## Notes

### Science
- OGA (O-GlcNAcase) removes O-linked N-acetylglucosamine (O-GlcNAc) sugar modifications from intracellular proteins; inhibiting OGA increases O-GlcNAcylation of tau and alpha-synuclein, stabilizing them in soluble form and reducing toxic aggregation
- Alpha-synuclein has nine identified O-GlcNAcylation sites in human and rodent brains; in vitro O-GlcNAcylation prevents aggregation and toxicity (PNAS 2019)
- OGA inhibition also reduces cellular internalization of alpha-synuclein preformed fibrils, potentially blocking prion-like spread (FEBS Journal 2021)
- Dual tau + alpha-synuclein activity is the key differentiator — tau and synuclein pathologies frequently co-exist in PD (especially PD dementia), making OGA inhibitors potentially multimodal
- Related compound [[asn90|ASN90]] showed reduced tau and alpha-synuclein levels, improved motor function, and reduced astrogliosis in synuclein-dependent rodent PD models (ACS Chemical Neuroscience 2022)
- Core open question: Lilly's ceperognastat showed significant hippocampal volume preservation and tau PET slowing but accelerated cognitive decline at higher doses with cardiac/neoplasm safety signals — does OGA inhibition have a therapeutic window problem, or was this Lilly-compound-specific?

### Clinical

**ASN51-101 (Phase 1 SAD/MAD)** | NCT04759365 | N=64 planned | Healthy volunteers
- **Primary endpoint:** Safety/tolerability → Clean profile; no serious or severe adverse events
- **Key secondary:** Single 20-50 mg doses and multiple 20 mg doses safe; plasma half-life 40-50 hours (dose-proportional); CSF concentrations correlated with plasma, confirming CNS penetration
- **Status:** Terminated August 2022 (site delays, COVID impact) after completing single-dose and one multiple-dose cohort
- **Interpretation:** Established favorable PK and safety; long half-life supports once-daily dosing

**ASN51-102 (Phase 1 PET)** | NCT05725005 | N=12 | Healthy men
- **Primary endpoint:** Brain OGA occupancy after repeated doses → Exceeded 90% within hours of first dose
- **Key secondary:** O-GlcNAcylation pharmacodynamic response in PBMCs confirmed dose-response; steady state reached within one week at 10-20 mg daily
- **Status:** Completed June 2023
- **Interpretation:** Demonstrated full CNS target engagement — the strongest pharmacological proof-of-concept in the OGA class

**ASN51-103 (Phase 1 DDI)** | NCT06232109 | N=50 | Healthy volunteers
- **Primary endpoint:** Drug-drug interaction with fluvoxamine, itraconazole, and paroxetine
- **Status:** Completed July 2024
- **Interpretation:** Characterized metabolic pathway interactions to de-risk Phase 2 dosing in elderly polypharmacy populations

**Phase 2 (AD)** | NCT06677203 | N=123 planned | Early AD (MCI/mild dementia, elevated pTau217)
- **Primary endpoint:** Safety and suicidality (coprimary); secondary: biomarker changes over 6 months
- **Status:** Terminated November 2024, one month after enrollment began; described as "strategic" without details
- **Interpretation:** Termination followed Lilly ceperognastat Phase 2 failure (August 2024) and Biogen BIIB113 discontinuation — class-wide retreat rather than ASN51-specific safety signal

**PD Preclinical (MJFF-funded)** | No NCT | A53T alpha-synuclein mouse model
- **Primary endpoint:** Efficacy in genetic model of early-onset familial PD
- **Status:** MJFF grant awarded ~2022; results expected by end of 2022
- **Interpretation:** No public disclosure of results; if positive, was intended to support clinical trial in familial PD patients

### Financial
- **Total raised:** ~$137M across 5 funding rounds
- **Series C (July 2024):** $100M oversubscribed round led by Novo Holdings; new investors EQT Life Sciences (LSP Dementia Fund), OrbiMed, SR One; existing investors M Ventures, Sofinnova Partners, GSK Equities, J&J Innovation (JJDC)
- **Series A:** Led by Sofinnova Partners
- **Other funding:** $2.2M ADDF grant for Phase 1; two MJFF grants (amounts undisclosed) for PD preclinical work
- **Key investors:** Novo Holdings, OrbiMed, Sofinnova Partners, GSK, J&J — strong syndicate but $100M raised primarily to fund the now-terminated AD Phase 2
- **Burn rate concern:** With Phase 2 terminated within one month of the $100M raise, Asceneuron likely retains significant cash but faces strategic uncertainty on how to deploy it
- **ASN90 licensing:** Licensed to Ferrer (February 2023) for PSP — provides some revenue/milestone potential independent of ASN51

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[asn51]] | Phase 1 | Deprioritized | Asceneuron | small molecule |

- OGA inhibition is a distinct mechanism from direct alpha-synuclein targeting ([[prasinezumab]], [[aro-snca|ARO-SNCA]]) — it modifies synuclein post-translationally rather than clearing or reducing it
- **Lilly ceperognastat** — the most advanced OGA inhibitor (Phase 2 in AD) — showed mixed results: significant hippocampal volume preservation and tau PET slowing, but accelerated cognitive decline at 3 mg dose and safety signals (cardiac, neoplasm, nervous system). This creates ambiguity: the biomarker data supports the mechanism, but clinical outcomes undermine it
- **Biogen BIIB113** — discontinued February 2025 after Phase 1; achieved >90% brain target occupancy at low doses (similar to ASN51) but Biogen chose not to advance
- The OGA class is in crisis: three programs terminated/failed within 6 months (Lilly Aug 2024, Asceneuron Nov 2024, Biogen Feb 2025). Any rehabilitation of the mechanism would require reinterpretation of ceperognastat data or a new trial design
- For PD specifically, OGA inhibition competes with approaches targeting alpha-synuclein directly ([[prasinezumab]], [[aro-snca|ARO-SNCA]]) and genetic PD targets ([[biib122|LRRK2 inhibitors]], [[pariceract|GBA1 activators]]). The multimodal tau + synuclein angle is unique but unproven clinically

## Analysis

ASN51 has the best Phase 1 pharmacology data in the OGA class — full CNS uptake, >90% target occupancy, clean safety, and a half-life enabling once-daily oral dosing. The problem is not the molecule; it is the mechanism. The rapid class-wide retreat following ceperognastat's Phase 2 failure suggests the field has concluded that OGA inhibition, despite strong preclinical rationale and biomarker engagement, does not translate to clinical benefit in neurodegeneration. Asceneuron's "strategic" termination language, combined with timing one month after Lilly's failure, confirms this was a mechanism-driven decision rather than an ASN51-specific issue.

**Analytical estimate — Probability of ASN51 advancing to PD clinical trials: 10-15%.** This is our assessment, not from a published source. The reasoning: Base rate for OGA class continuation is near zero given three consecutive terminations (~5%). Adjustments upward: ASN51 has differentiated PK/target engagement data (+5%), MJFF-funded PD preclinical work may have generated positive data (+5%), and Asceneuron retains significant cash from the $100M raise to pivot (+5%). Adjustments downward: no public PD preclinical results (-5%), company's remaining pipeline focus is on ASN90/PSP via Ferrer (-5%), and investor syndicate funded the AD indication specifically (-5%). Net: ~10-15%.

The scenario where ASN51 matters again requires one of three triggers: (1) reanalysis of ceperognastat data demonstrates the mechanism works at lower doses, rehabilitating the class; (2) Asceneuron publishes positive PD preclinical data from the MJFF study that differentiates the PD use case from the AD failure; or (3) a partner acquires or licenses ASN51 specifically for PD/synucleinopathy, where co-pathology of tau and synuclein provides a distinct rationale from pure AD. Absent these triggers, ASN51 for PD remains an interesting preclinical-stage hypothesis stranded by class-level clinical failure.

The broader signal for PD pipeline watchers: OGA inhibition was the most promising indirect approach to alpha-synuclein (modify rather than clear/reduce). Its apparent failure narrows the field toward direct approaches — antibodies ([[prasinezumab]]), gene silencing ([[aro-snca|ARO-SNCA]]), and genetic targets ([[biib122|LRRK2]], [[pariceract|GBA1]]).

## References

### Clinical Trials
- [ASN51-101 Phase 1 SAD/MAD](https://clinicaltrials.gov/study/NCT04759365) — NCT04759365
- [ASN51-102 Phase 1 PET Study](https://clinicaltrials.gov/study/NCT05725005) — NCT05725005
- [ASN51-103 Drug-Drug Interaction Study](https://clinicaltrials.gov/study/NCT06232109) — NCT06232109
- [ASN51 Phase 2 AD (Terminated)](https://clinicaltrials.gov/study/NCT06677203) — NCT06677203

### Key Publications
- [O-GlcNAcase Inhibitor ASN90 is a Multimodal Drug Candidate for Tau and alpha-Synuclein Proteinopathies | ACS Chemical Neuroscience (2022)](https://pubs.acs.org/doi/10.1021/acschemneuro.2c00057)
- [alpha-Synuclein O-GlcNAcylation alters aggregation and toxicity | PNAS (2019)](https://www.pnas.org/doi/10.1073/pnas.1808845116)
- [O-GlcNAc modification blocks aggregation and toxicity of alpha-synuclein | PMC (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4618406/)
- [Pharmacological inhibition of O-GlcNAcase reduces cellular internalization of alpha-synuclein preformed fibrils | FEBS Journal (2021)](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.15349)

### Press Releases & Filings
- [Asceneuron Secures $100M Series C Financing (July 2024)](https://asceneuron.com/asceneuron-secures-100-million-series-c-financing/)
- [Novo Holdings Leads $100M Raise for Asceneuron (July 2024)](https://www.biospace.com/business/novo-holdings-leads-100m-raise-for-asceneurons-alzheimers-push)
- [MJFF Grant Advances Preclinical Study of ASN51 in Familial PD](https://parkinsonsnewstoday.com/news/mjff-grant-advances-preclinical-study-asn51-familial-parkinsons/)
- [Asceneuron Halts Alzheimer's Trial Adding to Tau-Targeting Setbacks | Clinical Trials Arena](https://www.clinicaltrialsarena.com/news/asceneuron-halts-alzheimers-trial-adding-to-tau-targeting-setbacks/)
- [ASN51 Profile | Alzforum](https://www.alzforum.org/therapeutics/asn51)
- [Tau Modification Drugs Take a Hit with Negative Trial | Alzforum](https://www.alzforum.org/news/conference-coverage/tau-modification-drugs-take-hit-negative-trial)

### Regulatory & Market
- [ASN-51 Likelihood of Approval for PD | Pharmaceutical Technology](https://www.pharmaceutical-technology.com/data-insights/asn-51-asceneuron-parkinson-s-disease-likelihood-of-approval/)
- [Asceneuron Raises $100M for Alzheimer's Treatment | Labiotech](https://www.labiotech.eu/more-news/asceneuron-raises-100m-asn51/)
