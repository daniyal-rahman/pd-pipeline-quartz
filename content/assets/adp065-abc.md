---
drug_name: "ADP065-ABC"
aliases: ["ADP065"]
target: "NLRP3 inflammasome"
mechanism: "siRNA targeting NLRP3 mRNA, conjugated to Alector Brain Carrier (ABC) for transferrin receptor-mediated transcytosis; peripheral dosing achieves CNS-wide NLRP3 gene silencing to reduce microglial-driven neuroinflammation"
modality: "siRNA"
developer: "Alector"
company_type: "biotech"
publicly_traded: true
ticker: "ALEC"
stage: "Preclinical"
status: "Active"
patient_population: "Alzheimer's disease, Parkinson's disease"
route_of_administration: "SC (expected; peripheral dosing via ABC platform)"
key_biomarkers: ["CSF IL-1beta", "CSF IL-18", "NLRP3 mRNA levels", "TSPO PET"]
confidence_rating: "2/10"
next_catalyst: "Preclinical data disclosure or IND timeline announcement"
catalyst_date: "TBD"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# ADP065-ABC

## Summary

ADP065-ABC is Alector's (biotech, ALEC) NLRP3 siRNA conjugated to the Alector Brain Carrier (ABC) platform, targeting neuroinflammation in AD and PD. Currently at the research stage -- the earliest of the NLRP3-targeting PD programs, well behind [[nt-0796|NT-0796]] (NodThera, Phase 1b completed with positive CSF biomarker data), [[selnoflast]] (Roche, Phase 1b completed), and [[vtx3232|VTX3232]] (Ventyx/Roche). The siRNA modality offers a mechanistically distinct approach to NLRP3 inhibition: rather than blocking inflammasome assembly with small molecules, ADP065-ABC silences NLRP3 mRNA production entirely, which could provide more complete target suppression in CNS-resident microglia. However, this advantage is theoretical until the ABC platform demonstrates siRNA delivery to microglia specifically. If [[nt-0796|NT-0150]] (NodThera's next-gen oral NLRP3 inhibitor) Phase 2 shows clinical motor benefit in PD, oral small molecule NLRP3 inhibition becomes the dominant approach and ADP065-ABC must demonstrate superiority to justify injectable siRNA complexity. If small molecule NLRP3 inhibitors fail to translate biomarker changes to clinical outcomes, the entire neuroinflammation thesis for PD weakens regardless of modality.

## Notes

### Science
- Mechanism: anti-NLRP3 siRNA that inhibits NLRP3 mRNA translation, preventing synthesis of the NLRP3 protein and thereby blocking inflammasome assembly, caspase-1 activation, and IL-1beta/IL-18 release
- Conjugated to Alector Brain Carrier (ABC) for TfR-mediated BBB transcytosis, enabling peripheral dosing with CNS target engagement
- NLRP3 inflammasome activation is a key driver of microglial-mediated neuroinflammation in PD; activated microglia release pro-inflammatory cytokines that accelerate dopaminergic neuron loss
- Alpha-synuclein aggregates directly activate the NLRP3 inflammasome, creating a feed-forward loop: alpha-synuclein aggregation triggers NLRP3 activation, which increases neuroinflammation, which promotes further alpha-synuclein aggregation
- Preclinical validation: NLRP3 inhibition prevents alpha-synuclein pathology and dopaminergic neurodegeneration in MPTP mouse models (Science Translational Medicine, 2017); Nlrp3-siRNA delivered via lentivirus reduced inflammasome activation and protected dopamine neurons in mouse models
- Key distinction vs. [[selnoflast]]: selnoflast is peripherally restricted (does not cross BBB), relying on the hypothesis that peripheral NLRP3 inhibition reduces neuroinflammation indirectly. ADP065-ABC targets NLRP3 directly in CNS cells
- Key distinction vs. [[nt-0796|NT-0796]]/NT-0150: NodThera's compounds are brain-penetrant oral small molecules -- same CNS targeting but different modality (reversible inhibition vs. mRNA silencing). Oral dosing is more convenient than injectable siRNA
- Key distinction vs. [[vtx3232|VTX3232]]: Ventyx's compound is also a brain-penetrant oral NLRP3 inhibitor (acquired by Roche)
- siRNA offers theoretical advantages: (1) more complete target suppression vs. competitive inhibitors, (2) potentially longer dosing intervals if knockdown is durable, (3) avoids off-target binding issues of small molecules
- Open scientific questions: (1) does ABC deliver siRNA to microglia specifically, or primarily to neurons? NLRP3 is predominantly expressed in microglia -- neuronal delivery would miss the relevant cell type; (2) is complete NLRP3 silencing safe, or is some inflammasome activity needed for CNS immune surveillance? (3) does NLRP3 inhibition matter if alpha-synuclein aggregation (the upstream trigger) is not also addressed?
- Limited source material -- requires primary research on ABC-siRNA microglial targeting, NLRP3 knockdown kinetics, and safety of sustained NLRP3 silencing in CNS

### Clinical
No clinical trials initiated. No IND timeline disclosed for ADP065-ABC.

- Listed as "Research" stage on Alector pipeline (earlier than Preclinical)
- The ABC platform's lead siRNA program is ADP064-ABC (anti-tau siRNA for AD/FTD), in IND-enabling studies -- first ABC-siRNA to enter humans
- Competitive NLRP3 programs are significantly more advanced: [[nt-0796|NT-0796]] completed Phase 1b/2a in PD (positive CSF biomarker data), [[selnoflast]] completed Phase 1b in PD, [[vtx3232|VTX3232]] in Phase 1

### Financial
- Alector (NASDAQ: ALEC) had $291.1M cash as of September 30, 2025, with runway estimated through 2027
- No disclosed partnerships or licensing deals specific to ADP065-ABC
- Post-restructuring (October 2025, 49% workforce reduction), ADP065-ABC appears to be a lower priority than AL050 (IND 2027) and AL137 (IND 2026)
- NLRP3 space deal comparators: Roche acquired Inflazome for ~EUR 380M (2020, [[selnoflast]]) and subsequently acquired Ventyx ([[vtx3232|VTX3232]]) -- both oral small molecules. No precedent deal for CNS-targeted NLRP3 siRNA exists
- ADP065-ABC likely needs external funding or partnership to advance given Alector's constrained resources and lower prioritization

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "NLRP3") AND file.name != "adp065-abc"
SORT stage DESC
```

- [[nt-0796|NT-0796]] (NodThera, Phase 1b completed) demonstrated CSF neuroinflammation reversal in PD patients -- the first clinical proof that NLRP3 inhibition can engage CNS targets in PD. NodThera is advancing NT-0150 (next-gen) to Phase 2
- [[selnoflast]] (Roche, Phase 1b completed) is peripherally restricted -- open question whether peripheral-only NLRP3 inhibition is sufficient. Results undisclosed as of early 2026
- [[vtx3232|VTX3232]] (Ventyx/Roche, Phase 1) is brain-penetrant oral NLRP3 inhibitor -- Roche's second shot at NLRP3 after the peripheral-only [[selnoflast]] question emerged
- [[dapansutrile]] (Olatec/ZyVersa, Phase 1b) is another oral NLRP3 inhibitor in PD
- ADP065-ABC is the only siRNA approach to NLRP3 in the PD space -- unique modality but earliest stage
- Shares ABC platform risk with [[al050-abc|AL050-ABC]] and [[adp062-abc|ADP062-ABC]]: platform validation or failure affects all three programs

## Analysis

ADP065-ABC occupies an unusual position: a novel modality (siRNA) against a target (NLRP3) that already has multiple oral small molecule competitors further advanced in clinical development. The theoretical case for siRNA over small molecules -- more complete target suppression, potentially longer dosing intervals, avoidance of off-target binding -- is intellectually sound but unproven. The practical case is weak: oral dosing is strongly preferred for chronic neurodegenerative disease, and the NLRP3 small molecule programs already have clinical biomarker data showing CNS engagement.

The most critical scientific question is cell-type specificity. NLRP3 is predominantly a microglial target, and the ABC platform's TfR-mediated transcytosis was originally designed for neuronal delivery. Whether ABC-conjugated siRNA can effectively silence NLRP3 in microglia -- which express TfR at different levels than neurons -- is a fundamental pharmacological question that must be answered before this program has clinical relevance.

**Analytical estimate -- probability of reaching IND within 5 years: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: research-stage programs at restructured biotechs have ~10-15% chance of reaching IND
- Adjustments upward: NLRP3 is a validated neuroinflammation target with clinical biomarker proof-of-concept from [[nt-0796]] (+5%), siRNA is a differentiated modality in a small-molecule-dominated space (+3%)
- Adjustments downward: research stage with no disclosed preclinical data (-5%), Alector cash constraints and lower prioritization vs. AL050/AL137 (-10%), three oral competitors ahead in clinical development (-5%), unresolved cell-type targeting question (-5%)
- Net: ~10-15%

The decision tree: if [[nt-0796|NT-0150]] Phase 2 shows clinical motor benefit in PD (2026-2027 timeframe), NLRP3 is validated as a PD target and ADP065-ABC's siRNA modality becomes interesting for best-in-class positioning or combination approaches. If NT-0150 shows biomarker engagement without clinical benefit (the current fear for all neuroinflammation programs), the entire NLRP3-for-PD thesis collapses and ADP065-ABC is shelved. In the upside scenario, ADP065-ABC is most likely to advance as a partnered program, positioning the ABC-siRNA platform as a differentiated NLRP3 approach for a partner who wants a non-oral modality or deeper target suppression.

## References

### Key Publications
- [Inflammasome inhibition prevents alpha-synuclein pathology and dopaminergic neurodegeneration in mice | Science Translational Medicine (2017)](https://www.science.org/doi/10.1126/scitranslmed.aah4066)
- [Role of NLRP3 Inflammasome in Parkinson's Disease and Therapeutic Considerations | PMC (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9661339/)
- [NLRP3 Inflammasome-Mediated Neuroinflammation and Related Mitochondrial Impairment in PD | Neuroscience Bulletin (2023)](https://link.springer.com/article/10.1007/s12264-023-01023-y)
- [Inhibition of hepatic Nlrp3 protects dopaminergic neurons via attenuating systemic inflammation in MPTP/p mouse model | Journal of Neuroinflammation (2018)](https://link.springer.com/article/10.1186/s12974-018-1236-z)
- Limited source material -- requires primary research on ADP065-ABC specifically

### Press Releases & Filings
- [Alector Q3 2025 Financial Results and Business Update (Nov 2025)](https://investors.alector.com/news-releases/news-release-details/alector-reports-third-quarter-2025-financial-results-and)
- [Alector Pipeline](https://alector.com/pipeline/)
- [Alector Latozinemab Phase 3 Results and Restructuring (Oct 2025)](https://investors.alector.com/news-releases/news-release-details/alector-announces-topline-results-latozinemab-phase-3-trial)

### Regulatory & Market
- [Anti-Neuroinflammatory Effects of NLRP3 Inhibitor NT-0796 in PD | Movement Disorders (2025)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.30307)
- [NodThera NT-0796 Reverses Neuroinflammation in PD Phase 1b/2a](https://www.nodthera.com/news/nodtheras-nlrp3-inhibitor-nt-0796-reverses-neuroinflammation-in-parkinsons-disease-phase-ib-iia-trial/)
- [Alector January 2026 Corporate Presentation | MarketScreener](https://www.marketscreener.com/news/alector-january-2026-corporate-presentation-ce7e59dfd18af12d)
