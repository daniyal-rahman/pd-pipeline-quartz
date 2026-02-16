---
drug_name: "Montara BrainOnly LRRK2"
aliases: ["BrainOnly LRRK2 inhibitor"]
target: "LRRK2 kinase"
mechanism: "Brain-selective LRRK2 kinase inhibitor using binary pharmacology: a brain-penetrant LRRK2 inhibitor paired with a non-brain-penetrant peripheral blocker (FKBP12-dependent) to eliminate lung/kidney on-target toxicity"
modality: "small molecule"
developer: "Montara Therapeutics"
company_type: "startup"
publicly_traded: false
partner: ""
partner_type: ""
stage: "Preclinical"
status: "Active"
patient_population: "TBD (expected: LRRK2 mutation carriers and/or idiopathic PD)"
route_of_administration: "oral (expected)"
key_biomarkers: ["p-Rab10", "p-LRRK2 (pS935)", "urinary BMP"]
confidence_rating: "3/10"
next_catalyst: "Development candidate nomination for LRRK2 program"
catalyst_date: "2026-2027 (estimated)"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-16
---

# Montara BrainOnly LRRK2

## Summary

Montara Therapeutics (startup, private) is developing a brain-selective LRRK2 kinase inhibitor using its proprietary BrainOnly platform -- a binary pharmacology approach pairing a brain-penetrant LRRK2 inhibitor with a peripheral FKBP12-dependent blocker (MT1110) that neutralizes the inhibitor outside the CNS. Funded by a $3.3M MJFF grant through the LITE consortium, the program is preclinical with no development candidate yet disclosed for the LRRK2 indication (the company's lead TSC/epilepsy program has reached development candidate stage with IND planned H2 2026, validating the platform). If [[biib122|BIIB122]] LUMA Phase 2b reads out positively in March 2026, the LRRK2 target is validated and Montara's brain-selective approach becomes a compelling next-generation candidate that could solve the peripheral toxicity question definitively. If LUMA fails, the entire LRRK2 inhibitor class faces an existential question, and Montara's platform differentiation (brain selectivity) becomes less relevant since target biology, not safety, would be the binding constraint.

## Notes

### Science
- The BrainOnly platform originates from Kevan Shokat's lab at UCSF, published in Nature (2022) as "brain-restricted mTOR inhibition with binary pharmacology" -- uses a brain-penetrant kinase inhibitor + a non-brain-penetrant FKBP12 ligand ("RapaBlock") that deactivates the inhibitor in peripheral tissues
- Applied to LRRK2: the concept pairs a brain-penetrant LRRK2 kinase inhibitor with Montara's universal peripheral blocker (MT1110), which saturates FKBP12 binding sites peripherally, preventing FKBP12-dependent drugs from engaging targets outside the brain
- This directly addresses the key safety concern for LRRK2 inhibitors: preclinical studies across multiple compounds showed non-adverse but concerning vacuolation of type II pneumocytes in lung and pigmentation in renal tubular epithelial cells -- effects that are dose-dependent and reversible but have constrained dosing in clinical programs like [[biib122|BIIB122]]
- LRRK2 gain-of-function mutations (G2019S most common) cause ~1-2% of sporadic PD and ~5% of familial PD. Pathologically, mutant LRRK2 hyperphosphorylates Rab GTPases (especially Rab10), impairing lysosomal and vesicular trafficking
- Key scientific question: does brain-selective LRRK2 inhibition provide a meaningful safety advantage? Clinical data from [[biib122|BIIB122]] Phase 1b showed the lung/kidney findings were manageable at therapeutic doses -- if peripheral toxicity proves clinically insignificant, Montara's differentiation weakens
- Second question: LRRK2 is expressed in immune cells (monocytes, neutrophils); peripheral LRRK2 inhibition may contribute to efficacy through neuroinflammatory pathways. By blocking peripheral activity, Montara may sacrifice a potentially beneficial component of the mechanism
- Scientific co-founders are a significant strength: Kevan Shokat (UCSF, binary pharmacology inventor), Thomas Sudhof (Stanford, Nobel laureate in vesicle trafficking), Martin Kampmann (UCSF, CRISPRi screening in neurodegeneration)
- CEO Nicholas Hertz co-founded Mitokinin (PINK1 activator), acquired by AbbVie for $110M+ in 2023 -- direct PD drug development track record on a genetically validated target

### Clinical
- No clinical trials initiated
- No development candidate disclosed for the LRRK2 program specifically
- The company's lead program (MTX-E1, BrainOnly mTOR for TSC-related epilepsy) has reached development candidate stage with IND planned H2 2026 -- this is the closest proxy for platform validation timeline
- The LRRK2 program was described in the March 2025 seed expansion press release as an "age-related neurodegenerative disease program progressing to development candidate stage"
- MJFF LITE consortium membership provides access to LRRK2-relevant clinical biomarker development and shared preclinical resources

### Financial
- **Total raised:** $28M in Series Seed funding ($8M seed July 2024 + $20M oversubscribed seed expansion March 2025)
- **MJFF grant:** $3.3M non-dilutive for the LRRK2 program (announced May 2025)
- **Key investors:** SV Health Investors' Dementia Discovery Fund (lead), Two Bear Capital (co-lead), KdT Ventures, Dolby Family Ventures, BEVC
- **Board:** Troy E. Wilson, Ph.D., J.D. (Chairman; CEO of Kura Oncology; serial biotech founder of Avidity, Araxes, Intellikine, Ambrx) -- notable signal of investor quality
- **Founder track record:** Nicholas Hertz's prior company Mitokinin was acquired by AbbVie (~$110M+ upfront; PINK1 activator for PD) -- this is rare repeat-founder credibility in the PD space
- **Valuation:** Not disclosed; at $28M raised with $3.3M non-dilutive on top, likely valued in the $50-100M range (estimated)
- **Context:** The $3.3M MJFF grant through LITE is a meaningful validation signal -- MJFF is the most sophisticated non-profit funder in PD and their LRRK2 portfolio is extensive
- **Comparison:** [[biib122|BIIB122]] (Denali/Biogen) is a $2.15B deal; [[arv-102|ARV-102]] (Arvinas) has Novartis backing. Montara is orders of magnitude earlier and smaller but the platform thesis is orthogonal rather than competitive

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "LRRK2") AND file.name != "montara-lrrk2"
SORT stage DESC
```

- [[biib122|BIIB122]] (Denali/Biogen) is the class-leading LRRK2 kinase inhibitor in Phase 2b -- if LUMA succeeds, it validates the target and creates demand for next-generation LRRK2 inhibitors with improved safety profiles, which is exactly Montara's pitch
- [[arv-102|ARV-102]] (Arvinas) takes a fundamentally different approach: LRRK2 protein degradation via PROTAC rather than kinase inhibition. Degradation eliminates both kinase and scaffolding functions of LRRK2 but may also eliminate any protective LRRK2 functions
- [[biib094|BIIB094]] (Ionis/Biogen) uses ASO-mediated LRRK2 mRNA knockdown -- another total protein reduction strategy
- [[snp614|SNP614]] (Serina Therapeutics) is an LRRK2 mRNA-targeting approach
- [[neu-723|NEU-723]] (Neuron23) takes a precision medicine approach with biomarker-selected patients
- Montara's differentiation is unique in the LRRK2 landscape: not a better inhibitor, but a delivery innovation that restricts inhibition to the CNS. If peripheral LRRK2 toxicity proves to be dose-limiting in late-stage trials, this becomes a critical advantage
- The binary pharmacology platform is modality-agnostic in principle -- Montara could potentially apply BrainOnly to other LRRK2 modalities or to entirely different PD targets

## Analysis

Montara's thesis rests on a specific bet: that peripheral LRRK2 inhibition is a meaningful clinical liability. The preclinical evidence supports this concern (type II pneumocyte vacuolation, renal tubular changes across multiple LRRK2 inhibitors in primates), but the clinical evidence from [[biib122|BIIB122]] Phase 1b suggests these effects are manageable at therapeutic doses. The critical data point will be long-term safety in Phase 2b/3 -- chronic LRRK2 inhibition over years may reveal cumulative peripheral effects not visible in shorter trials. If that happens, Montara's brain-selective approach is perfectly positioned.

**Analytical estimate -- Probability of reaching Phase 1: 25-35%.** This is our assessment, not from a published source. The reasoning:
- Base rate for preclinical programs reaching Phase 1: ~30-40% for well-funded startups
- Adjustments upward: platform validated in lead TSC program approaching IND (+5%), experienced PD founder with exit track record (+5%), MJFF LITE consortium support and resources (+5%), strong scientific founders (+3%)
- Adjustments downward: no disclosed development candidate for LRRK2 specifically (-10%), binary pharmacology adds complexity (two-drug combination, PK matching required) (-5%), if BIIB122 LUMA fails in March 2026, the LRRK2 target loses conviction and funding becomes harder (-10% risk-weighted)
- Net: ~25-35%

**Signal analysis:**
- MJFF granting $3.3M for this program is a meaningful quality signal. MJFF's LRRK2 portfolio is the deepest in the field and they have direct visibility into the competitive landscape. Their willingness to fund a brain-selective approach implies they see peripheral toxicity as a real long-term concern, even if short-term clinical data looks clean.
- Troy Wilson joining as Chairman is notable -- he has founded five companies with multiple successful exits. His involvement at the board level (not just advisory) signals belief in platform value beyond a single indication.
- The $20M oversubscribed seed expansion in March 2025 indicates strong investor demand despite being pre-development-candidate on the LRRK2 program. The Dementia Discovery Fund leading suggests sophisticated neuroscience-specific investors, not generalist VCs.
- The key decision tree depends heavily on the [[biib122|BIIB122]] LUMA Phase 2b readout expected March 2026: if positive, Montara becomes a compelling next-generation play with differentiated safety; if negative, the LRRK2 inhibitor field contracts and Montara's platform value shifts entirely to non-PD indications (TSC, brain cancer) where it may have more immediate impact.

## References

### Key Publications
- [Brain-restricted mTOR inhibition with binary pharmacology | Nature (2022)](https://www.nature.com/articles/s41586-022-05213-y) — foundational platform science
- [LRRK2-targeting therapies march through the Valley of Death | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11076002/)
- [LRRK2 Inhibition by BIIB122 in Healthy Participants and Patients with Parkinson's Disease | Movement Disorders (2023)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.29297)

### Press Releases & Filings
- [Montara Therapeutics to Develop Novel Treatments Using the BrainOnly Platform with Grant from The Michael J. Fox Foundation (May 2025)](https://montaratx.com/montara-therapeutics-to-develop-novel-treatments-using-the-brainonly-tm-platform-with-grant-from-the-michael-j-fox-foundation/)
- [Montara Therapeutics Closes $20M Oversubscribed Seed Expansion (March 2025)](https://montaratx.com/montara-therapeutics-closes-20m-oversubscribed-seed-expansion/)
- [Montara Therapeutics Closes $8 Million Seed Round (July 2024)](https://montaratx.com/montara-therapeutics-closes-8-million-seed-round/)
- [Montara Therapeutics Announces Development Candidate for First BrainOnly Program in TSC-Related Epilepsy (Dec 2025)](https://montaratx.com/montara-therapeutics-announces-development-candidate-for-first-brainonly/)
- [Montara gets grant to develop LRRK2 inhibitor drug for Parkinson's | Parkinson's News Today](https://parkinsonsnewstoday.com/news/montara-gets-grant-develop-lrrk2-inhibitor-drug-parkinsons/)
- [AbbVie announces acquisition of Mitokinin | PMLiVE](https://pmlive.com/pharma_news/abbvie_acquires_mitokinin_in_deal_worth_over_650m_1501593/)

### Regulatory & Market
- [LRRK2 inhibitor lung effects are mild | Alzforum](https://www.alzforum.org/news/research-news/sigh-relief-lung-effects-lrrk2-inhibitors-are-mild)
- [Targeting LRRK2 in Parkinson's Disease | PMC (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589013/)
