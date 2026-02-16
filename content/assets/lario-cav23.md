---
drug_name: "Lario CaV2.3 Inhibitor"
aliases: ["Lario Cav2.3 blocker", "CACNA1E inhibitor"]
target: "CaV2.3 (R-type voltage-gated calcium channel, CACNA1E)"
mechanism: "Selective small molecule inhibitor of CaV2.3 R-type calcium channels to reduce pathological calcium influx in substantia nigra dopaminergic neurons and prevent neurodegeneration"
modality: "small molecule"
developer: "Lario Therapeutics"
company_type: "startup"
publicly_traded: false
partner: "Oxford Parkinson's Disease Centre (OPDC)"
partner_type: "academic"
stage: "Preclinical"
status: "Active"
patient_population: "Early PD (disease modification)"
route_of_administration: "oral"
key_biomarkers: ["DaT-SPECT", "CaV2.3 mRNA levels"]
confidence_rating: "3/10"
next_catalyst: "IND filing"
catalyst_date: "2026-2027"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-16
company_link: "[[companies/lario-therapeutics]]"
partner_link: "[[companies/oxford-parkinsons-disease-centre]]"
---

# Lario CaV2.3 Inhibitor

## Summary

Lario Therapeutics (startup, Edinburgh) is developing first-in-class, orally active, CNS-penetrant selective CaV2.3 (R-type) calcium channel inhibitors for Parkinson's disease modification. The program is funded by a $6M MJFF grant (July 2024) and builds on genetic knockout data showing complete neuroprotection of substantia nigra dopaminergic neurons in a PD mouse model (Benkert et al., Nature Communications, 2019). This is the first attempt to selectively target CaV2.3 in PD after the failure of the non-selective CaV1.3 approach with isradipine (STEADY-PD III, Phase 3, 2020). Compounds are being evaluated in patient-derived iPSC neuronal models at the Oxford Parkinson's Disease Centre. If IND-enabling studies confirm neuroprotection with an acceptable safety profile, this would be the first selective calcium channel blocker to enter PD clinical trials. If preclinical models fail to translate or safety signals emerge from blocking a widely expressed channel, the calcium channel neuroprotection thesis may be set back further after the isradipine failure.

## Notes

### Science
- CaV2.3 encodes the alpha-1E subunit of R-type voltage-gated calcium channels (gene: CACNA1E). In adult substantia nigra dopaminergic (DA) neurons, CaV2.3 is the **most abundantly expressed** voltage-gated calcium channel subtype, and expression increases with aging
- DA neurons of the substantia nigra are uniquely vulnerable because they are autonomous pacemakers — they fire continuously without synaptic input, driving sustained calcium influx through voltage-gated channels. This creates chronic calcium overload and oxidative stress that selectively kills these neurons in PD
- Genetic validation: CaV2.3 knockout mice showed **complete protection** from dopaminergic neuron degeneration in a 6-OHDA neurotoxin PD model (Benkert et al., 2019). Knockout also reduced somatic calcium signals and calcium-dependent after-hyperpolarizations
- CaV2.3 deficiency upregulated NCS-1 (neuronal calcium sensor-1), a calcium-binding protein independently implicated in neuroprotection — suggesting a reinforcing protective mechanism
- CaV2.3 protein levels are higher in substantia nigra DA neurons than in ventral tegmental area DA neurons, which do not degenerate in PD — providing anatomical selectivity rationale
- Elevated CaV2.3 mRNA has been found in blood samples of PD patients, suggesting potential as a peripheral biomarker for patient selection or disease monitoring
- Key distinction from isradipine (STEADY-PD III failure): isradipine was a non-selective L-type (CaV1.3) calcium channel blocker repurposed from hypertension. It lacked selectivity for the disease-relevant channel subtype and was dose-limited by cardiovascular effects. Lario's compounds are designed as **first-in-class selective CaV2.3 inhibitors**, which could achieve therapeutic CNS exposure without cardiovascular dose limitations
- Until Lario's program, no selective CaV2.3 inhibitors existed — this was identified as a critical unmet pharmacological need in the calcium channel neuroprotection literature
- Open questions: (1) Will CaV2.3 selectivity over CaV1.x, CaV2.1, CaV2.2 be sufficient to avoid off-target effects? (2) Does the neurotoxin mouse model (6-OHDA) predict human PD pathology adequately? (3) Can oral dosing achieve sufficient CNS exposure for target engagement?

### Clinical
No clinical trials initiated. Preclinical stage.

- **MJFF-funded preclinical program (2024-ongoing):** Testing Lario CaV2.3 inhibitor compounds in patient-derived iPSC neuronal models at the Oxford Parkinson's Disease Centre (OPDC), led by Professor Richard Wade-Martins. Also evaluating in two preclinical in vivo PD models
- **IND timeline:** Per MJFF grant description, Lario aims to file an IND application in approximately 12-18 months from grant award (July 2024), suggesting a potential IND filing in late 2025 to early 2026. As of February 2026, no IND filing has been publicly announced
- **Patent activity:** Lario disclosed new CaV2.3 antagonist chemical matter in patent filings (August 2025), suggesting active medicinal chemistry optimization

### Financial
- **Total raised:** ~$9.8M as of latest available data
- **MJFF grant:** $6M (July 2024) — largest single funding event; grant from the Parkinson's Disease Therapeutics Pipeline Program
- **Seed investors:** Epidarex Capital and Axxam (at founding, 2021)
- **Company origin:** Spun out from Epidarex Exeed (Epidarex Capital's therapeutic discovery engine) in November 2021
- **Dual-indication strategy:** CaV2.3 inhibitors are also being developed for genetic epilepsies (CDKL5 Deficiency Disorder, CACNA1E-related disorders), which may provide a faster path to clinical proof-of-concept and de-risk the PD program. Epilepsy indications could generate early revenue or partnership interest independent of PD
- **Context:** $6M MJFF grant for a preclinical program is a substantial non-dilutive validation. MJFF is the largest private funder of PD research and conducts rigorous scientific review — their backing signals credibility of the CaV2.3 target hypothesis
- **No known VC institutional round:** The company appears to have bootstrapped on seed capital plus grant funding. A Series A would be the expected next financing milestone to fund IND-enabling toxicology and first-in-human studies

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "calcium") AND file.name != "lario-cav23"
SORT stage DESC
```

- The calcium channel neuroprotection thesis was heavily damaged by isradipine's STEADY-PD III Phase 3 failure (2020), but that was a **non-selective L-type (CaV1.3) blocker** repurposed from cardiology. Lario's selective CaV2.3 approach addresses the key criticism: wrong channel subtype, insufficient CNS selectivity
- No other companies are known to be developing selective CaV2.3 inhibitors for PD — Lario has first-mover advantage on this target
- Broader neuroprotection competitors include [[pariceract|GBA1 activators]], [[k0706|c-Abl inhibitors]], and [[nicotinamide-riboside|mitochondrial approaches]] — all targeting different aspects of dopaminergic neuron vulnerability
- The GLP-1 receptor agonist class ([[exenatide]], [[lixisenatide]], [[semaglutide]]) is the most advanced neuroprotection competitor, with multiple Phase 2/3 programs showing motor benefit signals through a different mechanism (neuroinflammation/metabolic)
- If CaV2.3 inhibition shows neuroprotection in clinical trials, it would validate a fundamentally new mechanism and could be combined with other approaches (e.g., alpha-synuclein clearance + calcium channel blockade)
- If it fails, the calcium channel neuroprotection thesis is likely permanently closed, as this represents the most rational and selective pharmacological test of the hypothesis

## Analysis

The CaV2.3 program represents a second-generation attempt at calcium channel-mediated neuroprotection in PD, informed by the specific failures of isradipine. The scientific rationale is compelling: CaV2.3 is the dominant calcium channel in substantia nigra DA neurons, its expression correlates with vulnerability (high in SN, low in VTA), it increases with aging, and complete knockout is fully neuroprotective in mouse models. The isradipine failure can be rationalized as a selectivity problem — a non-selective L-type blocker dose-limited by hypotension never achieved adequate target engagement on the disease-relevant channel.

**Analytical estimate — probability of reaching Phase 1: 40-50%.** This is our assessment, not from a published source. The reasoning:
- Base rate for preclinical-to-Phase-1 transition in neuroscience: ~30%
- Adjustments upward: strong genetic validation via knockout (+10%), MJFF grant validation (+5%), oral and CNS-penetrant compound series (+5%), dual-indication de-risk via epilepsy (+5%)
- Adjustments downward: first-in-class target with no clinical precedent (-5%), small startup with limited capital (-5%), CaV2.3 expressed outside CNS raises safety questions (-5%)
- Net: ~40-50% chance of reaching Phase 1

**Analytical estimate — probability of clinical success in PD (conditional on reaching Phase 2): 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate for Phase 2 success in neurodegeneration: ~15%
- Adjustments upward: strong preclinical knockout data (+5%), addresses specific failure mode of isradipine (+5%)
- Adjustments downward: neurotoxin mouse models have poor PD translation history (-10%), calcium homeostasis is complex and blocking one channel may trigger compensatory responses (-5%)
- Net: ~10-15%

**Signal analysis:**
- MJFF's $6M commitment is notable. MJFF funds hundreds of grants but this is among the larger awards, suggesting high confidence in the CaV2.3 target validation from their scientific advisory board
- The Oxford Parkinson's Disease Centre collaboration (Richard Wade-Martins) adds academic credibility. OPDC is a leading PD research center with patient-derived iPSC models that are considered closer to human disease than standard animal models
- Lario's dual-indication strategy (epilepsy + PD) is smart capital efficiency. Epilepsy trials are shorter and cheaper than PD disease modification trials, providing faster pharmacological proof-of-concept for CaV2.3 blockade in humans
- Patent filings in August 2025 with new chemical matter suggest active medicinal chemistry — the program is not stalled
- The absence of a Series A is a risk signal. The company will need $20-40M+ to fund IND-enabling studies and a Phase 1 trial. Whether they can raise this depends partly on epilepsy program progress and preclinical data package strength
- Key watch items: (1) announcement of a lead candidate nomination, (2) IND filing for either epilepsy or PD indication, (3) Series A financing

## References

### Key Publications
- [Cav2.3 channels contribute to dopaminergic neuron loss in a model of Parkinson's disease | Nature Communications (2019)](https://www.nature.com/articles/s41467-019-12834-x)
- [Voltage-Gated Ca2+ Channels in Dopaminergic Substantia Nigra Neurons: Therapeutic Targets for Neuroprotection in Parkinson's Disease? | Frontiers in Synaptic Neuroscience (2021)](https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2021.636103/full)
- [Cav2.3 R-type calcium channels: from its discovery to pathogenic de novo CACNA1E variants: a historical perspective | PMC (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7351833/)
- [Cav2.3 channels stimulate in vivo burst activity of vulnerable dopamine neurons and are elevated in Parkinson's disease | ResearchGate (2024)](https://www.researchgate.net/publication/394600522_Cav23_channels_stimulate_in_vivo_burst_activity_of_vulnerable_dopamine_neurons_and_are_elevated_in_Parkinson's_disease)
- [Structures of the R-type human Cav2.3 channel reveal conformational crosstalk of the intracellular segments | Nature Communications (2022)](https://www.nature.com/articles/s41467-022-35026-6)
- [Beta2-subunit alternative splicing stabilizes Cav2.3 Ca2+ channel activity during continuous midbrain dopamine neuron-like activity | eLife (2021)](https://elifesciences.org/articles/67464)

### Press Releases & Filings
- [Lario Therapeutics Awarded $6M Grant From The Michael J. Fox Foundation for Parkinson's Research | Business Wire (July 2024)](https://www.businesswire.com/news/home/20240722221034/en/Lario-Therapeutics-Awarded-6M-Grant-From-The-Michael-J.-Fox-Foundation-for-Parkinson%E2%80%99s-Research)
- [Lario Therapeutics awarded $6M for Parkinson's drug research | DDW (July 2024)](https://www.ddw-online.com/lario-therapeutics-awarded-6m-for-parkinsons-drug-research-30836-202407/)
- [Lario Therapeutics receives "Company Making a Difference Award" from CDKL5 Forum | Business Wire (November 2023)](https://www.businesswire.com/news/home/20231107572931/en/Lario-Therapeutics-receives-Company-Making-a-Difference-Award-from-CDLK5-Forum-recognising-its-unique-approach-to-precision-medicine-for-genetic-epilepsies)
- [New Cav2.3 antagonists described in Lario Therapeutics patents | BioWorld (2025)](https://www.bioworld.com/articles/698061-new-cav23-antagonists-described-in-lario-therapeutics-patents?v=preview)
- [Lario Therapeutics divulges new Cav2.3 blockers | BioWorld (2025)](https://www.bioworld.com/articles/723417-lario-therapeutics-divulges-new-cav23-blockers?v=preview)

### Regulatory & Market
- [Development of Selective Ion Channel Inhibitors as a Disease-modifying Therapy for Parkinson's Disease | MJFF Grant Page](https://www.michaeljfox.org/grant/development-selective-ion-channel-inhibitors-disease-modifying-therapy-parkinsons-disease)
- [Isradipine Versus Placebo in Early Parkinson Disease (STEADY-PD III): A Randomized Trial | Annals of Internal Medicine (2020)](https://pubmed.ncbi.nlm.nih.gov/32227247/)
- [STEADY-PD III trial results analysis | The Science of Parkinson's](https://scienceofparkinsons.com/2020/04/03/steadypd/)
