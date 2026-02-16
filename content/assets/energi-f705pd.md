---
drug_name: "ENERGI-F705PD"
aliases: ["F705PD", "ENERGI-F705"]
target: "cellular ATP levels / alpha-synuclein aggregation (metabolic)"
mechanism: "Oral sustained-release small molecule that enhances cellular ATP production via purine salvage, glycolysis, and pentose phosphate pathways; elevated ATP acts as a biological hydrotrope to prevent alpha-synuclein aggregation while boosting NADPH-driven antioxidant defense and restoring tyrosine hydroxylase expression for dopamine synthesis"
modality: "small molecule"
developer: "Energenesis Biomedical"
company_type: "biotech"
publicly_traded: true
ticker: "6657.TW"
partner: ""
partner_type: ""
stage: "Phase 1"
status: "Active"
patient_population: "Healthy volunteers (Phase 1 completed); PD patients (Phase 2 planned)"
route_of_administration: "oral"
key_biomarkers: ["cellular ATP levels", "alpha-synuclein aggregation markers", "reactive oxygen species (ROS)", "tyrosine hydroxylase expression"]
confidence_rating: "2/10"
next_catalyst: "Phase 2 IND filing and trial initiation in PD patients"
catalyst_date: "2026"
thesis_cluster: "mitophagy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# ENERGI-F705PD

## Summary

ENERGI-F705PD is a first-in-class oral small molecule from Energenesis Biomedical (Taiwan, TWSE: 6657) that completed a Phase 1 SAD study in 24 healthy volunteers with clean safety and validated sustained-release PK (announced August 2025). The mechanism is novel in the PD field: rather than targeting alpha-synuclein directly via antibodies or gene silencing, it exploits the ATP hydrotrope effect -- restoring depleted intracellular ATP to physiological concentrations where it acts as a biological solubilizer preventing alpha-synuclein aggregation, while simultaneously boosting antioxidant defense and dopamine synthesis. If Phase 2 shows target engagement (ATP elevation, alpha-synuclein reduction) in PD patients, it would validate a fundamentally different approach to disease modification that addresses the metabolic root cause of protein aggregation rather than the aggregation itself, positioning alongside other mitochondrial/metabolic assets like [[nrg5051]], [[mtx325]], and [[nicotinamide-riboside]]. If PK in patients is insufficient, if ATP elevation does not translate to measurable alpha-synuclein effects, or if the hydrotrope mechanism proves too weak in vivo, the program likely stalls -- and Energenesis as a small Taiwanese biotech with limited PD-specific infrastructure faces a difficult path to global development without a partner.

## Notes

### Science
- Leverages the discovery (Patel et al., 2017; Rice et al., 2023) that ATP at physiological concentrations (5-10 mM) functions as a **biological hydrotrope** -- clustering over hydrophobic patches on alpha-synuclein monomers while the triphosphate chain interacts with bulk water, preventing the intermolecular contacts that nucleate aggregation
- Engages three metabolic pathways simultaneously: **purine salvage** (ATP regeneration), **glycolysis** (ATP production), and **pentose phosphate pathway** (NADPH for antioxidant defense via glutathione reductase)
- Also claims to restore **tyrosine hydroxylase expression**, the rate-limiting enzyme in dopamine synthesis -- if real, this would address both disease modification (aggregation) and symptomatic benefit (dopamine)
- The ATP-alpha-synuclein relationship is bimodal and nuanced: ATP disrupts long-range electrostatic intramolecular contacts in alpha-synuclein monomers (which could paradoxically enhance early aggregation kinetics) while inhibiting late-stage beta-sheet fibril formation and secondary nucleation -- the net therapeutic effect depends on achieving sustained physiological ATP levels
- PD-associated mutations (E46K, A53T) modulate ATP's hydrotropic effect on alpha-synuclein, and magnesium ions further modulate the interaction -- whether the drug addresses these variant-specific effects is unknown
- Key distinction from [[nicotinamide-riboside]]: NR boosts ATP indirectly through NAD+ precursor supplementation; ENERGI-F705PD claims to enhance ATP production directly through multiple metabolic pathways
- Key distinction from [[nrg5051]]: NRG5051 prevents mitochondrial pore opening to preserve mitochondrial integrity; ENERGI-F705PD targets metabolic output (ATP levels) rather than mitochondrial structure
- Key distinction from [[mtx325]]: MTX325 enhances clearance of damaged mitochondria via mitophagy; ENERGI-F705PD aims to boost energy output from existing mitochondria
- Open question: the active pharmaceutical ingredient and its molecular target are undisclosed -- the platform claims to "restore cellular energy" but the specific pharmacological target within these pathways is not public, making independent scientific assessment difficult
- Energenesis has an established track record with their ENERGI platform in wound healing (Phase 3 for diabetic foot ulcers) and hair loss (Phase 2) -- the cellular energy restoration concept is not PD-specific, and the PD indication appears to be a platform extension rather than a PD-first program

### Clinical

**ENERGI-F705PD Phase 1 SAD** | NCT TBD (likely Taiwan TFDA registry) | N=24 | Healthy volunteers
- **Primary endpoint:** Safety and tolerability → Favorable; no safety signals reported
- **Key secondary:** PK validation of sustained-release oral formulation → Confirmed
- **Status:** Completed (announced August 1, 2025; trial commenced February 2025)
- **Interpretation:** Clean Phase 1 in healthy volunteers is a low bar -- the critical question is whether the drug achieves sufficient ATP elevation in the CNS of PD patients, where mitochondrial dysfunction is already present. No PK parameters (Cmax, AUC, half-life, CNS penetration) have been publicly disclosed, which limits external assessment. The sustained-release formulation is important because maintaining ATP levels above the hydrotrope threshold likely requires consistent drug exposure.

### Financial
- **TWSE: 6657** -- publicly traded on the Taiwan Stock Exchange since 2023; small-cap biotech
- **No disclosed PD-specific funding rounds** -- the company's broader ENERGI platform has funded development across diabetic foot ulcers (Phase 3), alopecia (Phase 2), epidermolysis bullosa (FDA Orphan Drug designation), and other indications
- **No partnerships announced** for the PD program -- a significant gap given the complexity and cost of global PD clinical development
- **Revenue model:** The company generates some revenue from experimental service analysis and reagent sales, but is fundamentally pre-revenue on therapeutics
- **CEO:** Dr. Han-Min Chen
- **Comparison:** Energenesis is substantially smaller and less well-capitalized than Western mitophagy-thesis peers like NRG Therapeutics (GBP 50M Series B, backed by Dementia Discovery Fund) or Mission Therapeutics ($13.3M raise for Phase 1b). A PD Phase 2 in Taiwan is feasible at lower cost than US/EU trials, but regulatory path to global markets would require a partner

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "ATP") OR contains(target, "mitochondrial") OR contains(target, "NAD+") AND file.name != "energi-f705pd"
SORT stage DESC
```

- The mitophagy/mitochondrial cluster is increasingly competitive: [[nicotinamide-riboside]] is already in Phase 3 (NOPARK), [[mtx325]] has confirmed CNS penetration, [[nrg5051]] is backed by Dementia Discovery Fund money, and [[progenra-pink1|Progenra/AbbVie]] are pursuing direct PINK1 activation
- ENERGI-F705PD's differentiation is mechanistic: it targets the metabolic *output* (ATP levels) rather than mitochondrial *quality control* (mitophagy) or *structural integrity* (mPTP inhibition) -- this is upstream of protein aggregation in a way that other mitochondrial assets are not
- The ATP hydrotrope mechanism theoretically addresses alpha-synuclein aggregation from a completely different angle than antibody-based clearance ([[prasinezumab]]) or production inhibition ([[aro-snca]]) -- if validated, it opens a new therapeutic axis
- Geographic competition: as a Taiwanese biotech, Energenesis faces the challenge of establishing credibility in a PD field dominated by US/EU companies. However, Taiwan's regulatory environment (TFDA) can provide a faster path to early clinical data, and the company presented at BIO International 2025, signaling global ambitions
- If [[nicotinamide-riboside]] NOPARK Phase 3 shows that boosting cellular energy (via NAD+) slows PD progression, it would validate the metabolic/energy thesis and benefit ENERGI-F705PD by de-risking the target class. If NOPARK fails, it raises questions about whether metabolic restoration alone is sufficient

## Analysis

ENERGI-F705PD represents a genuinely novel mechanistic approach to PD -- the ATP hydrotrope hypothesis is scientifically well-grounded (published in Chemical Science, eLife) and provides a compelling rationale for why metabolic decline and protein aggregation are causally linked rather than merely correlated. The concept that restoring ATP to physiological concentrations could dissolve or prevent alpha-synuclein aggregates -- essentially treating PD as an energy crisis that manifests as a proteinopathy -- is intellectually elegant and differentiates this from every other approach in the PD pipeline.

**Analytical estimate -- Probability of meaningful clinical efficacy: 5-10%.** This is our assessment, not from a published source. The reasoning:
- Base rate: ~5% for novel mechanism small molecules entering Phase 2 in neurodegeneration
- Adjustments upward: strong basic science on ATP hydrotrope effect (+5%), oral bioavailability and clean Phase 1 safety (+3%), platform validated in other indications (wound healing) showing cellular energy restoration works peripherally (+2%)
- Adjustments downward: no disclosed CNS penetration data (-5%), no preclinical PD efficacy data publicly available (-5%), undisclosed molecular target limits scientific scrutiny (-3%), small company without PD-specialist infrastructure (-3%), bimodal ATP effect on alpha-synuclein (could paradoxically enhance early aggregation) (-2%)
- Net: ~5-10%

**Signal analysis:**
- The company's decision to extend its cellular energy platform into PD is opportunistic but rational -- the ATP hydrotrope literature provides genuine scientific justification, and PD is a high-unmet-need indication that attracts investor interest. However, the PD program appears to be one of many indications rather than the company's primary focus, which typically correlates with less resource allocation and slower development.
- The Phase 1 press release is notably thin on data -- no PK parameters, no dose levels, no adverse event details. This is common for small companies managing disclosure strategically, but it limits external assessment and suggests the company may not yet have the data quality infrastructure expected by US/EU regulators.
- BIO International 2025 presentation suggests partnering intent. For this program to reach Phase 2/3 in major markets, Energenesis almost certainly needs a partner with PD clinical development expertise and regulatory infrastructure. The program's value as a licensing asset depends heavily on Phase 2 proof-of-concept data.
- The decision tree: if Phase 2 shows measurable ATP elevation and alpha-synuclein biomarker changes in PD patients, the program becomes a compelling licensing target for a pharma company seeking mechanistic differentiation in PD. If Phase 2 fails to show target engagement, the ATP hydrotrope mechanism may be valid in vitro but insufficient in the complex in vivo CNS environment, and the program likely does not advance.

## References

### Key Publications
- [Toward a molecular mechanism for the interaction of ATP with alpha-synuclein | Chemical Science (2023)](https://pubs.rsc.org/en/content/articlehtml/2023/sc/d3sc03612j)
- [Elucidating ATP's role as solubilizer of biomolecular aggregate | eLife (2024)](https://elifesciences.org/articles/99150/peer-reviews)
- [Alpha-synuclein amyloids catalyze the degradation of ATP and other nucleotides | Scientific Reports (2025)](https://www.nature.com/articles/s41598-025-32888-w)
- [Brain network and energy imbalance in PD: linking ATP reduction and alpha-synuclein pathology | Frontiers in Molecular Neuroscience (2024)](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2024.1507033/full)

### Press Releases & Filings
- [Energenesis Biomedical Announces Positive Phase I Results for ENERGI-F705PD (August 2025)](https://www.prnewswire.com/news-releases/energenesis-biomedical-announces-positive-phase-i-results-for-energi-f705pd-a-potential-disease-modifying-treatment-for-parkinsons-disease-302519474.html)
- [Energenesis Biomedical to Unveil Promising PD Therapy at BIO International 2025 (June 2025)](https://www.prnewswire.com/news-releases/energenesis-biomedical-to-unveil-promising-parkinsons-disease-therapy-energi-f705pd-at-bio-international-2025-302478818.html)
- [Disease-modifying Parkinson's therapy found safe in volunteers | Parkinson's News Today (2025)](https://parkinsonsnewstoday.com/news/energi-f705pd-parkinsons-disease-modifying-therapy-found-safe-volunteers/)
- [Energenesis Completes Phase I Trial | BioPharma APAC (2025)](https://biopharmaapac.com/news/93/6693/energenesis-completes-phase-i-trial-of-energi-f705pd-a-novel-oral-therapy-for-parkinsons-disease.html)
- [Energenesis Biomedical Commencement of Phase 1 (February 2025) | MarketScreener](https://www.marketscreener.com/quote/stock/ENERGENESIS-BIOMEDICAL-CO-45567571/news/Energenesis-Biomedical-Co-Ltd-Announces-Commencement-of-the-Phase-1-Clinical-Trial-for-ENERGI-F705-49147955/)

### Regulatory & Market
- [Energenesis Biomedical (TWSE: 6657) Company Profile | Yahoo Finance](https://finance.yahoo.com/quote/6657.TW/profile/)
- [Energenesis Biomedical Stock | MarketScreener](https://www.marketscreener.com/quote/stock/ENERGENESIS-BIOMEDICAL-CO-45567571/)
