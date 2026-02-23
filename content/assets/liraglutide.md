---
drug_name: "Liraglutide"
aliases: ["Victoza", "NN2211"]
target: "GLP-1 receptor (neuroprotection)"
mechanism: "GLP-1 receptor agonist repurposed from diabetes; crosses BBB to activate anti-inflammatory, anti-apoptotic, and mitochondrial protective pathways in dopaminergic neurons"
modality: "small molecule"
developer: "Academic (Cedars-Sinai / Cure Parkinson's)"
company_type: "academic"
publicly_traded: false
partner: "Novo Nordisk (originator)"
partner_type: "big pharma"
stage: "Phase 2"
status: "Active"
patient_population: "PD patients on stable symptomatic therapy"
route_of_administration: "SC (daily injection)"
key_biomarkers: ["MDS-UPDRS", "NMSS", "PDQ-39", "DaT-SPECT"]
confidence_rating: "4/10"
next_catalyst: "Larger confirmatory trial or class-level signal from semaglutide (NCT03659682)"
catalyst_date: "2026-2027"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/cedars-sinai]]"
partner_link: "[[companies/novo-nordisk]]"
---

# Liraglutide

## Summary

Liraglutide is a GLP-1 receptor agonist (marketed as Victoza for type 2 diabetes by Novo Nordisk) being repurposed for PD through an academic-led Phase 2 trial funded by Cure Parkinson's and Van Andel Institute. The completed Cedars-Sinai trial (NCT02953665, N=63) showed significant improvement in non-motor symptoms (NMSS adjusted mean difference 13.1 points, p<0.05) and quality of life (PDQ-39, p<0.001) but no motor benefit — a result complicated by a strong placebo effect. Liraglutide sits within a broader GLP-1 agonist class effort: [[lixisenatide]] showed motor slowing (p=0.007) in LixiPark, but [[exenatide]] failed Phase 3 (Lancet, Feb 2025), and NLY01 (pegylated exenatide) failed Phase 2. If the semaglutide trial (NCT03659682) delivers a positive readout, the class gets validated and liraglutide's non-motor signal gains significance; if semaglutide also fails, the GLP-1 thesis in PD is likely exhausted despite encouraging preclinical biology.

## Notes

### Science
- GLP-1 receptor agonists cross the blood-brain barrier and bind GLP-1R on neurons, activating cAMP and PI3K/Akt survival pathways that protect dopaminergic neurons
- Multi-mechanism neuroprotection: reduces neuroinflammation (suppresses NF-kB, increases GDNF expression), mitigates oxidative stress, improves mitochondrial quality control via PGC-1alpha activation, and reduces alpha-synuclein levels in preclinical MPTP models
- Liraglutide is a long-acting GLP-1 analogue (97% homology to human GLP-1) with a 13-hour half-life — originally designed for once-daily subcutaneous injection in diabetes
- Key distinction vs. [[exenatide]]: liraglutide is a human GLP-1 analogue while exenatide is exendin-4-based (lizard peptide); theoretical advantage in receptor pharmacology and immunogenicity, though this has not been clinically demonstrated in PD
- The neuroprotection hypothesis is target-agnostic — GLP-1R agonism may slow neurodegeneration regardless of whether the primary driver is alpha-synuclein, LRRK2, GBA, or other pathology. This is both its appeal (broad applicability) and its weakness (lacks a precision mechanism)
- Open question: the exenatide Phase 3 failure and NLY01 Phase 2 failure challenge whether the preclinical neuroprotection signals translate to humans. The lixisenatide motor signal (NEJM 2024) keeps the class alive, but the magnitude was modest (3.08-point MDS-UPDRS Part III difference)

### Clinical

**Liraglutide Phase 2 (Cedars-Sinai)** | NCT02953665 | N=63 | PD patients on stable symptomatic therapy
- **Primary endpoint:** Safety and tolerability → Liraglutide was safe and well tolerated at 1.2-1.8 mg daily for 52 weeks
- **Key secondary:** NMSS improved by 6.6 points in liraglutide group vs. worsening by 6.5 points in placebo (adjusted mean difference 13.1 points, p<0.05). MDS-UPDRS Part II (activities of daily living) significantly improved. PDQ-39 quality of life significantly improved (p<0.001). Parkinson's Anxiety Scale Avoidance Behavior improved (p<0.05)
- **Motor outcomes:** No significant difference in MDS-UPDRS Part III (motor) between liraglutide and placebo, attributed in part to a strong placebo effect
- **Status:** Completed (2022)
- **Interpretation:** The non-motor benefit signal is encouraging but the trial was small (N=63), single-center, and the motor null result is a significant limitation. The strong placebo effect confounds interpretation. The 2:1 randomization design was appropriate but underpowered for motor endpoints

### Financial
- Liraglutide is a generic-eligible molecule — Victoza patents have largely expired, with generic versions approved (Teva, 2023; Hikma, Dec 2024)
- The PD repurposing effort is entirely academically funded (Cure Parkinson's Trust, Van Andel Institute) — no pharma sponsor for the PD indication
- Novo Nordisk has no disclosed interest in pursuing a PD indication for liraglutide; their GLP-1 portfolio is focused on semaglutide (Ozempic/Wegovy) which has superseded Victoza commercially
- No commercial peak sales estimates exist for liraglutide in PD specifically — any approval would likely be off-label or generic-based, with minimal commercial value to any single company
- The investment thesis here is class-level: if GLP-1 agonists validate in PD, the commercial opportunity accrues to branded next-generation agents (semaglutide, dual GLP-1/GIP agonists like tirzepatide) rather than to liraglutide itself

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[liraglutide]] | Phase 2 | Active | Academic (Cedars-Sinai / Cure Parkinson's) | small molecule |
| [[lixisenatide]] | Phase 2 | Active | Toulouse University Hospital (academic) | small molecule |
| [[nly01]] | Phase 2 | Active | Neuraly (D&D Pharmatech) | small molecule |
| [[pt320]] | Phase 2 | Failed | Peptron | small molecule |
| [[semaglutide]] | Phase 2 | Active | Novo Nordisk / Osaka University | small molecule |
| [[exenatide]] | Phase 3 | Failed | UCL (Tom Foltynie) | small molecule |

- The GLP-1 agonist class in PD includes multiple agents at various stages: [[exenatide]] (Phase 3 failed, Feb 2025), [[lixisenatide]] (Phase 2 positive, NEJM 2024), semaglutide (Phase 2 ongoing, NCT03659682), and NLY01 (Phase 2 failed)
- [[lixisenatide]] is the strongest class validator — the only GLP-1 agonist to show statistically significant motor slowing in PD (MDS-UPDRS Part III difference of 3.08 points, p=0.007), though the clinical meaningfulness of this magnitude is debated
- The exenatide Phase 3 failure (Lancet, Feb 2025, N=194, 96 weeks) is the biggest class setback — no benefit on motor symptoms or DaT-SPECT imaging vs. placebo. However, exenatide is a short-acting agent with different pharmacology, and the trial used once-weekly extended-release formulation
- Semaglutide (NCT03659682) is the most commercially relevant trial — Novo Nordisk's blockbuster with weekly dosing, higher potency, and potentially superior brain penetration. Results will likely determine the class's future
- If liraglutide's non-motor signal is real, it may point to GLP-1 agonists being better suited as symptomatic treatments for non-motor PD features rather than disease-modifying agents

## Analysis

Liraglutide occupies an unusual position in the PD pipeline: it is a well-characterized, safe, generic-eligible drug with encouraging preclinical neuroprotection data and a small but positive Phase 2 signal — but only for non-motor symptoms, not the motor progression that defines disease modification. The Cedars-Sinai trial (N=63) is too small to draw firm conclusions, and the motor null result, even accounting for placebo effect, is a concern.

**Analytical estimate — Probability of liraglutide specifically advancing to Phase 3 in PD: 15-20%.** This is our assessment, not from a published source. The reasoning:
- Base rate: GLP-1 agonists in PD have a 1/4 positive Phase 2 rate (lixisenatide positive; exenatide, NLY01, liraglutide-motor all negative) → starting point ~25%
- Adjustments upward: non-motor signal is biologically plausible (+5%), strong safety profile as approved drug (+5%), academic/nonprofit funding model doesn't require commercial viability (+5%)
- Adjustments downward: small single-center trial (-10%), no motor benefit (-10%), no pharma sponsor for PD indication (-10%), exenatide Phase 3 failure dampens class enthusiasm (-5%), generic economics remove commercial incentive (-5%)
- Net: ~15-20% for liraglutide specifically; the class-level probability is higher (~35-40%) because semaglutide may succeed where others have not

The real question is not whether liraglutide advances but whether the GLP-1 class validates. The semaglutide trial (NCT03659682) is the pivotal readout. Semaglutide has advantages over liraglutide — higher potency, weekly dosing (better compliance), and Novo Nordisk's commercial interest to pursue a CNS indication for their flagship franchise. If semaglutide shows motor benefit, the class validates and liraglutide's non-motor data becomes supporting evidence for GLP-1R engagement in the PD brain. If semaglutide fails alongside exenatide, the GLP-1 neuroprotection thesis in PD is effectively dead despite strong preclinical rationale — another case of rodent models failing to predict human outcomes.

Liraglutide's contribution to the field is primarily as a proof-of-concept data point. Its non-motor benefit, if real, suggests GLP-1R agonism may address PD-related anxiety, autonomic dysfunction, and quality of life — valuable but not disease-modifying. The generic status and lack of pharma sponsorship mean this asset is unlikely to be the vehicle through which GLP-1 agonists reach PD patients, even in a class-validation scenario.

## References

### Clinical Trials
- [Liraglutide Phase 2 in PD](https://clinicaltrials.gov/study/NCT02953665) — NCT02953665
- [Semaglutide in PD (GLP1R)](https://clinicaltrials.gov/study/NCT03659682) — NCT03659682

### Key Publications
- [A Phase II, Randomized, Double-Blinded, Placebo-Controlled Trial of Liraglutide in Parkinson's Disease | SSRN (2022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4212371)
- [Liraglutide Improves Non-Motor Function and Activities of Daily Living in PD | Neurology (2022)](https://www.neurology.org/doi/10.1212/WNL.98.18_supplement.3068)
- [Trial of Lixisenatide in Early Parkinson's Disease (LixiPark) | NEJM (2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2312323)
- [GLP-1, Parkinson's Disease, and Neuroprotection (Editorial) | NEJM (2024)](https://www.nejm.org/doi/full/10.1056/NEJMe2401743)
- [Exenatide Phase 3 in PD | Lancet (2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02808-3/fulltext)
- [GLP-1 Receptor Agonists: A New Treatment in Parkinson's Disease | IJMS (2024)](https://www.mdpi.com/1422-0067/25/7/3812)
- [GLP-1 class drugs show clear protective effects in PD and AD clinical trials | Neuropharmacology (2024)](https://www.sciencedirect.com/science/article/pii/S0028390824001217)
- [Liraglutide Regulates Mitochondrial Quality Control via PGC-1alpha in PD Model | Neurotoxicity Research (2021)](https://link.springer.com/article/10.1007/s12640-021-00460-9)
- [Safety, tolerability, and efficacy of NLY01 in early untreated PD | Lancet Neurology (2023)](https://pubmed.ncbi.nlm.nih.gov/38101901/)

### Press Releases & Filings
- [Liraglutide trial: results | Cure Parkinson's (2022)](https://cureparkinsons.org.uk/2022/04/liraglutide-trial-results/)
- [Top-line results from clinical trial of diabetes drug in Parkinson's | Van Andel Institute (2022)](https://www.vai.org/article/top-line-results-reported-from-clinical-trial-of-diabetes-drug-in-parkinsons/)
- [Exenatide Phase 3 results published | Parkinson's UK (2025)](https://www.parkinsons.org.uk/news/2025/results-phase-3-trial-exenatide-published)
- [GLP-1 scientific justification | Cure Parkinson's (2024)](https://cureparkinsons.org.uk/wp-content/uploads/2024/07/CureParkinsons_GLP-1-scientific-justification_18June2024.pdf)

### Regulatory & Market
- [Victoza patent information | DrugPatentWatch](https://www.drugpatentwatch.com/p/tradename/VICTOZA)
- [Repositioning GLP-1 Drugs for Neurologic Disease | NeurologyLive (2025)](https://www.neurologylive.com/view/repositioning-glp-1-drugs-neurologic-disease-evidence-advances-outlook)
