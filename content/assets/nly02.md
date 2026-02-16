---
drug_name: "NLY02"
aliases: ["NLY-02"]
target: "RIPK2 (NOD2/RIPK2 neuroinflammatory signaling)"
mechanism: "Oral BBB-penetrating RIPK2 kinase inhibitor that blocks alpha-synuclein-triggered NOD2/RIPK2 microglial activation and neurotoxic A1 astrocyte conversion"
modality: "small molecule"
developer: "Neuraly (D&D Pharmatech) / 1ST Bio"
company_type: "biotech"
publicly_traded: true
ticker: "347850.KQ"
stage: "IND-enabling"
status: "Active"
patient_population: "PD (preclinical); also being evaluated in AD models"
route_of_administration: "oral"
key_biomarkers: []
confidence_rating: "2/10"
next_catalyst: "IND filing and Phase 1 initiation"
catalyst_date: "TBD"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/neuraly]]"
---

# NLY02

## Summary

NLY02 is an oral, BBB-penetrating RIPK2 kinase inhibitor co-developed by Neuraly (D&D Pharmatech subsidiary, KOSDAQ: 347850) and 1ST Bio (First Biotherapeutics), currently in IND-enabling studies for Parkinson's and Alzheimer's disease. It is Neuraly's second-generation neuroinflammation program behind [[nly01|NLY01]] (pegylated GLP-1R agonist, Phase 2 completed), targeting the same downstream pathology -- microglial activation and neurotoxic A1 astrocyte conversion -- through a different upstream mechanism: selective inhibition of RIPK2 in the alpha-synuclein/NOD2/RIPK2 signaling cascade. A US patent was granted in August 2025, with the USPTO recognizing NLY02 as a structurally novel compound with innovative methods of application. Preclinical data shows dopaminergic neuron protection and reduced neuroinflammation in PD models. If NLY02 reaches clinical development and demonstrates target engagement in humans, it would validate RIPK2 as a druggable neuroinflammation node in PD -- a mechanistically distinct approach from both the GLP-1R agonists ([[nly01|NLY01]], [[lixisenatide]], [[exenatide]]) and the NLRP3 inflammasome inhibitors ([[dapansutrile]], [[selnoflast]]). If preclinical translation fails or D&D Pharmatech deprioritizes the program in favor of NLY01's Alzheimer's and MS indications, NLY02 remains an early-stage asset with limited near-term impact.

## Notes

### Science
- NLY02 is a selective RIPK2 (receptor-interacting serine/threonine-protein kinase 2) inhibitor designed to cross the blood-brain barrier and achieve CNS concentrations sufficient to block microglial neuroinflammatory signaling
- Mechanism centers on the **alpha-synuclein/NOD2/RIPK2 axis**: pathological alpha-synuclein aggregates bind to the NOD2 receptor on microglia, triggering NOD2 self-oligomerization and complex formation with RIPK2; RIPK2 is then phosphorylated and ubiquitinated, activating NF-kB and MAPK downstream pathways that drive pro-inflammatory cytokine release and neurotoxic A1 reactive astrocyte conversion
- By blocking RIPK2 kinase activity, NLY02 aims to interrupt this cascade at the kinase node -- upstream of the cytokine release and A1 astrocyte conversion that [[nly01|NLY01]] (GLP-1R agonist) targets at the receptor level
- Key preclinical validation: NOD2/RIPK2 signaling is elevated in microglia of human PD brains and in the alpha-synuclein preformed fibril (PFF) mouse model; genetic depletion of NOD2 or RIPK2 reduces neuroinflammation and protects dopaminergic neurons in these models (Bhatt et al., bioRxiv 2024)
- Oral bioavailability is a significant advantage over injectable GLP-1R agonists -- if BBB penetration and target engagement are confirmed in humans, this would be a more practical chronic dosing regimen for PD patients
- Open questions: (1) selectivity of NLY02 for RIPK2 vs. other RIPKs (RIPK1, RIPK3) which have distinct roles in neuroinflammation and necroptosis, (2) whether sufficient CNS RIPK2 inhibition can be achieved at tolerable oral doses, (3) whether RIPK2 inhibition produces immunosuppressive side effects given RIPK2's role in innate immune signaling beyond the CNS
- The NOD2/RIPK2 pathway is mechanistically distinct from both the NLRP3 inflammasome pathway (targeted by [[dapansutrile]], [[selnoflast]]) and the GLP-1R-mediated anti-inflammatory pathway ([[nly01|NLY01]], [[lixisenatide]], [[exenatide]]) -- all converge on reducing neuroinflammation but through different upstream nodes

### Clinical

No clinical trials initiated. NLY02 is in IND-enabling preclinical studies.

Key preclinical evidence:
- NLY02 reduced neuroinflammation and protected dopamine-producing neurons in PD animal models (details undisclosed; referenced in US patent filings and company communications)
- The alpha-synuclein-NOD2-RIPK2 signaling axis has been characterized in human PD brain tissue and alpha-synuclein PFF mouse models (Bhatt et al., bioRxiv 2024), providing target validation independent of NLY02 compound data
- Co-development with 1ST Bio (First Biotherapeutics) since 2018, with 1ST Bio leading compound optimization and safety profiling, and D&D Pharmatech handling clinical strategy
- US patent granted August 2025 -- a prerequisite for IND-enabling investment, suggesting the program may be approaching IND filing

### Financial
- **D&D Pharmatech (KOSDAQ: 347850)** is the parent company, IPO on KOSDAQ May 2024; market cap ~$2.4B (late 2025)
- **1ST Bio (First Biotherapeutics)** is the co-development partner; led compound optimization and safety work since 2018
- **Total D&D Pharmatech funding:** ~$206M across Series A ($16.5M, 2018), Series B ($137M, 2019, led by Octave Life Sciences and Smilegate Investment), and Series C ($51M, 2021, led by Praxis Capital)
- **No disclosed external licensing or partnership** for NLY02 -- co-developed internally between D&D subsidiaries/partners
- **Capital allocation context:** D&D Pharmatech is prioritizing NLY01 in Alzheimer's (Phase 2b, IND cleared 2020) and MS, plus DD01 (dual GLP-1/glucagon agonist) in MASH. NLY02 appears to be a lower-priority pipeline asset, which creates risk that IND-enabling studies are under-resourced or deprioritized
- **No independent valuation** of NLY02 as a standalone asset; value is embedded within D&D Pharmatech's overall portfolio

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "neuroinflam") AND file.name != "nly02"
SORT stage DESC
```

- NLY02 sits within the **neuroinflammation thesis cluster** but targets a distinct pathway (NOD2/RIPK2) vs. other neuroinflammation assets:
  - [[nly01|NLY01]] (Neuraly's own lead, GLP-1R agonist): Phase 2 completed, missed primary in overall PD population, post-hoc signal in patients <60; targets the same downstream effector (A1 astrocyte conversion) but via GLP-1 receptor activation rather than RIPK2 kinase inhibition
  - [[lixisenatide]] (academic-led): Phase 2 positive in LixiPark (p=0.007); only GLP-1 agonist with a positive PD trial
  - [[exenatide]] (academic-led): Phase 3 failed definitively (Lancet 2025); low CSF penetration cited as likely cause
  - [[dapansutrile]], [[selnoflast]] (NLRP3 inflammasome inhibitors): target a parallel innate immune pathway; early stage
- NLY02's oral route of administration is a meaningful competitive advantage over injectable GLP-1R agonists if efficacy can be demonstrated -- chronic PD therapy benefits from pill-based convenience
- The RIPK2 target is scientifically novel for PD -- no other PD-specific RIPK2 inhibitor is in clinical development, though several RIPK2 inhibitors exist in oncology and inflammatory disease pipelines (e.g., GSK's RIPK2 program in inflammatory bowel disease)
- Key risk: NLY02 is very early stage (IND-enabling) competing for internal resources against NLY01's more advanced clinical programs. D&D Pharmatech's multi-subsidiary model means NLY02 may not receive dedicated capital or management attention

## Analysis

NLY02 is a scientifically interesting but very early-stage asset whose development trajectory depends heavily on D&D Pharmatech's internal prioritization decisions. The NOD2/RIPK2 pathway has genuine biological validation in PD -- the 2024 bioRxiv preprint showing that pathological alpha-synuclein directly engages NOD2 to activate RIPK2, and that genetic ablation of either protein is neuroprotective, provides the strongest mechanistic rationale. The US patent grant in August 2025 confirms structural novelty and suggests ongoing investment, but no public preclinical efficacy data (dose-response, pharmacokinetics, toxicology) has been disclosed beyond general statements about dopaminergic neuron protection.

**Analytical estimate -- Probability of NLY02 reaching Phase 1 within 3 years: 30-40%.** This is our assessment, not from a published source. The reasoning: base rate for IND-enabling assets advancing to Phase 1 is approximately 50-60% in oncology but lower in neuroscience (~35-45%) due to BBB penetration challenges and higher attrition; adjustment upward for US patent grant signaling continued investment (+5%), co-development with 1ST Bio providing dedicated medicinal chemistry resources (+5%), and biological target validation from independent academic work (+5%); adjustment downward for D&D Pharmatech's apparent prioritization of NLY01 (AD, MS) and DD01 (MASH) over NLY02 (-10%), no disclosed pharmacokinetic or safety data (-5%), and the general difficulty of achieving sufficient CNS kinase inhibition with oral small molecules (-5%).

**Analytical estimate -- If NLY02 reaches Phase 2 in PD, probability of clinically meaningful efficacy: 10-15%.** This is our assessment, not from a published source. The reasoning: base rate for neuroinflammation-targeting agents in PD Phase 2 is very low (NLY01 missed, exenatide Phase 2 positive but Phase 3 failed, lixisenatide positive but awaiting Phase 3); adjustment upward for novel mechanism distinct from GLP-1R (+5%), oral BBB-penetrating small molecule pharmacology (+5%), alpha-synuclein-specific pathway engagement (+5%); adjustment downward for the overall track record of anti-neuroinflammatory approaches in neurodegeneration (-10%), unknown PK/PD relationship in human CNS (-5%).

The strategic context within D&D Pharmatech is important. NLY01's Phase 2 miss in PD overall and the exenatide Phase 3 failure have likely dampened the parent company's enthusiasm for PD-specific neuroinflammation programs. NLY02 targeting RIPK2 rather than GLP-1R provides mechanistic differentiation, but the internal competition for capital and management attention from NLY01-AD, NLY01-MS, and DD01-MASH programs is a practical headwind. The 1ST Bio partnership provides some insulation -- compound optimization and safety work are handled by a dedicated partner -- but clinical-stage investment decisions rest with D&D Pharmatech. Watch for IND filing announcements as the key near-term signal of continued commitment.

## References

### Key Publications
- [Pathologic alpha-Synuclein-NOD2 Interaction and RIPK2 Activation Drives Microglia-Induced Neuroinflammation in Parkinson's Disease | bioRxiv (2024)](https://www.biorxiv.org/content/10.1101/2024.02.19.580982v3)
- [Block of A1 astrocyte conversion by microglia is neuroprotective in models of Parkinson's disease | Nature Medicine (2018)](https://www.nature.com/articles/s41591-018-0051-5)
- [RIPK2 profoundly contributes to post-stroke neuroinflammation and behavioral deficits with microglia as unique perpetrators | J Neuroinflammation (2023)](https://jneuroinflammation.biomedcentral.com/articles/10.1186/s12974-023-02907-6)
- [Pharmacological inhibition of RIPK2 elicits neuroprotective effects following experimental ischemic stroke | Exp Neurol (2024)](https://www.sciencedirect.com/science/article/abs/pii/S0014488624001389)
- [Safety, tolerability, and efficacy of NLY01 in early untreated Parkinson's disease | Lancet Neurology (Dec 2023)](https://pubmed.ncbi.nlm.nih.gov/38101901/)

### Press Releases & Filings
- [1ST Bio and D&D Pharmatech win US patent for disease-modifying Parkinson's drug | Korea Biomedical Review (Aug 2025)](https://www.koreabiomed.com/news/articleView.html?idxno=28511)
- [Neuraly Pipeline](https://www.neuralymed.com/pipeline)
- [Neuraly Science](https://www.neuralymed.com/science)
- [D&D Pharmatech Raises $51M in Series C (Oct 2021)](https://biobuzz.io/dd-pharmatech-raises-51m-in-series-c-financing-to-advance-potential-disease-modifying-treatments-for-neurodegenerative-fibrotic-and-metabolic-diseases/)
- [D&D Pharmatech $137.1M Series B (2019) | BioSpace](https://www.biospace.com/d-and-d-pharmatech-closes-137-1-million-series-b)

### Regulatory & Market
- [Neuraly points to younger patients for hope as Parkinson's bet fails Phase 2 | Fierce Biotech](https://www.fiercebiotech.com/biotech/neuraly-points-younger-patients-hope-parkinsons-bet-fails-phase-2)
- [RIPKs and Neuroinflammation | Mol Neurobiol (2024)](https://link.springer.com/article/10.1007/s12035-024-03981-4)
