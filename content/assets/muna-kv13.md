---
drug_name: "MUNA Kv1.3 Blocker"
aliases: []
target: "Kv1.3 (voltage-gated potassium channel 1.3, microglial)"
mechanism: "Brain-penetrant small molecule blocker of the Kv1.3 potassium channel on disease-associated microglia, suppressing neuroinflammatory signaling and restoring neuroprotective microglial function"
modality: "small molecule"
developer: "MUNA Therapeutics"
company_type: "startup"
publicly_traded: false
partner: "GSK"
partner_type: "big pharma"
stage: "Preclinical"
status: "Active"
patient_population: "Parkinson's disease (planned); also targeting multiple sclerosis"
route_of_administration: "oral (expected)"
key_biomarkers: ["Kv1.3 expression (lymphocytes)", "neuroinflammatory cytokines (IL-1B, TNF-a, IL-6)", "microglial activation imaging"]
confidence_rating: "3/10"
next_catalyst: "Clinical candidate nomination / IND filing"
catalyst_date: "2025-2026 (estimated)"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# MUNA Kv1.3 Blocker

## Summary

MUNA Therapeutics (startup, private) is developing brain-penetrant small molecule Kv1.3 potassium channel blockers to suppress microglial neuroinflammation as a disease-modifying therapy for Parkinson's disease. The program is preclinical, funded in part by a $4.9M MJFF grant (October 2022), with clinical candidate finalization originally targeted for early 2025 and clinical entry in 2025 -- current status is unclear and likely delayed. MUNA's lead program is MNA-001 (oral TREM2 agonist for Alzheimer's), which entered Phase 1 in late 2025, demonstrating the company can advance assets to the clinic. The Kv1.3 target has strong genetic and pathological validation: upregulated in postmortem PD brains and in response to aggregated alpha-synuclein, with Fyn kinase-dependent regulation (JCI, 2020). If MUNA delivers a selective, brain-exposed Kv1.3 blocker into clinical trials and demonstrates target engagement biomarkers, it would be first-in-class for this mechanism in neurodegeneration. If competing neuroinflammation approaches like [[vtx3232|VTX3232 (NLRP3)]] or [[selnoflast]] succeed first, the rationale for Kv1.3 blockade may be subsumed by a validated alternative pathway.

## Notes

### Science
- Kv1.3 is a voltage-gated potassium channel highly expressed on disease-associated microglia (DAM) in the brain. In the resting state, microglia express low levels of Kv1.3; upon activation by aggregated alpha-synuclein or other inflammatory stimuli, Kv1.3 is transcriptionally upregulated and drives sustained neuroinflammatory signaling
- The Fyn/PKC-delta signaling cascade activates NF-kB and p38 MAPK pathways through Kv1.3, amplifying production of pro-inflammatory cytokines (IL-1B, TNF-alpha, IL-6). Fyn kinase directly binds Kv1.3 and posttranslationally modifies its channel activity -- Fyn itself is a genetic risk factor for PD
- PAP-1, a brain-penetrant tool compound Kv1.3 inhibitor, reduced neuroinflammation and protected dopaminergic neurons in three PD animal models (MitoPark, MPTP, alpha-synuclein PFF). This is preclinical proof-of-concept, not a drug candidate
- Key challenge: selectivity within the Kv1 family. Kv1.1 is critical for cardiac and neuronal function; non-selective blockers carry cardiac and seizure risk. MUNA claims single-digit nanomolar potency with high selectivity for Kv1.3 over other Kv1 family members
- Postmortem human PD brains show upregulated Kv1.3 immunoreactivity co-localized with IBA1-positive microglia in the substantia nigra and prefrontal cortex -- the pathological sites where dopaminergic neurons are lost
- B lymphocytes from PD patients also show elevated Kv1.3, raising the possibility of a peripheral biomarker for target engagement and patient selection
- Historical Kv1.3 drug development has focused on autoimmune indications (psoriasis, IBM) using peptide-based inhibitors (dalazatide/ShK derivatives) -- MUNA's approach is differentiated by using oral small molecules with brain penetration, which is required for CNS neuroinflammation

### Clinical

No clinical trials initiated for the Kv1.3 PD program. Key preclinical milestones:
- MJFF-funded studies (October 2022 - ongoing): medicinal chemistry optimization, structural biology, in vitro studies in human microglial cells, in vivo studies in humanized mouse models
- Clinical candidate selection was planned for early 2025 per May 2024 company statements; clinical entry targeted for 2025
- Current status (as of February 2026): no public announcement of clinical candidate nomination or IND filing for the Kv1.3 program. MUNA's MNA-001 (TREM2 agonist, Alzheimer's) entered Phase 1 in November 2025, suggesting organizational bandwidth may have prioritized the Alzheimer's program
- No NCT numbers registered for any MUNA Kv1.3-related study

### Financial
- **Series A:** $73M (July 2021) -- co-led by Novo Holdings, Sofinnova Partners, LSP Dementia Fund, Droia Ventures; with participation from Polaris Partners, Polaris Innovation Fund, Sanofi Ventures, V-Bio Ventures, VIB
- **Total raised:** ~$102M across 4 rounds (including grants)
- **MJFF grant:** $4.9M (October 2022) specifically for Kv1.3 PD program -- two-year funding for preclinical development
- **GSK strategic alliance (December 2024):** EUR 33.5M ($35M) upfront, up to EUR 140M ($147M) per target in milestones, plus tiered royalties. Focuses on Alzheimer's target discovery via MUNA's MiND-MAP spatial transcriptomics platform -- not directly related to Kv1.3 PD program, but validates MUNA's platform and provides non-dilutive capital
- **Alzheimer's Association grant:** $1M (2025) for MNA-001 Phase 1 support
- No disclosed peak sales estimates for the Kv1.3 program; too early-stage for revenue modeling
- Company reportedly planning Series B to fund clinical programs through Phase 1/2

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(thesis_cluster, "neuroinflammation") AND file.name != "muna-kv13"
SORT stage DESC
```

- **Distinct mechanism within the neuroinflammation cluster:** Kv1.3 blockade targets microglial activation at the ion channel level, upstream of inflammasome assembly. [[vtx3232|VTX3232]] targets NLRP3 inflammasome; [[selnoflast]] and [[dapansutrile]] target the same NLRP3 pathway; GLP-1 agonists ([[lixisenatide]], [[exenatide]], [[semaglutide]], [[liraglutide]]) have indirect anti-inflammatory effects. Each addresses a different node of the neuroinflammatory cascade
- Only known company pursuing small molecule Kv1.3 blockers for neurodegeneration. Kv1.3 Therapeutics LLC developed dalazatide (peptide Kv1.3 inhibitor) for autoimmune indications (psoriasis, IBM) but that is a subcutaneous peptide without CNS penetration -- not competitive in the neurodegeneration space
- The key competitive question is whether neuroinflammation is a viable standalone target in PD or merely a downstream consequence of protein aggregation. If [[vtx3232|VTX3232 Phase 2]] or [[selnoflast]] trials demonstrate that suppressing neuroinflammation alone can slow PD motor progression, it validates the entire cluster including Kv1.3 blockade. If they fail, Kv1.3 faces the same existential question
- MUNA's oral small molecule modality is advantageous for chronic dosing over decades compared to antibodies or peptides, but the program lags clinically behind [[vtx3232|VTX3232]] (Phase 2) and [[nly01|NLY01]] (Phase 2) by 3-5 years

## Analysis

The Kv1.3 program sits at the intersection of strong target biology and early-stage execution risk. The scientific rationale is compelling: Kv1.3 upregulation in PD microglia is validated in postmortem human tissue, the Fyn kinase connection provides a genetic link (Fyn is a PD risk gene), and PAP-1 proof-of-concept across three animal models is better preclinical evidence than many neuroinflammation targets can claim. The mechanistic logic -- blocking the ion channel that sustains microglial inflammatory activation -- is upstream of most competing approaches and could theoretically offer broader anti-inflammatory coverage than targeting a single cytokine or inflammasome.

**Analytical estimate -- Probability of reaching Phase 2 with clinical data: 25-30%.** This is our assessment, not from a published source. The reasoning: base rate for preclinical neuro programs reaching Phase 2 is ~30%. Adjustments upward: strong target validation in human tissue (+5%), experienced team that has already advanced MNA-001 to Phase 1 (+5%), MJFF grant provides validation and non-dilutive funding (+3%). Adjustments downward: Kv1.3 selectivity within the Kv1 family is a known medicinal chemistry challenge (-5%), no public clinical candidate nomination despite original 2025 target (-5%), company bandwidth may prioritize Alzheimer's programs over PD (-3%). Net: ~25-30%.

The GSK alliance and MNA-001 Phase 1 progression demonstrate MUNA can execute, but they also reveal a strategic tension: the company's primary commercial focus appears to be Alzheimer's (GSK deal, TREM2 agonist in clinic, MiND-MAP platform), with PD as a secondary indication. The Kv1.3 PD program's pace will depend on whether MUNA raises a Series B large enough to run multiple clinical programs simultaneously or must prioritize. The MJFF grant mitigates this somewhat by earmarking funds specifically for PD.

The broader neuroinflammation thesis in PD remains unvalidated clinically. The field is watching [[vtx3232|VTX3232's Phase 2]] (Lilly/Ventyx, NLRP3 inhibitor) as the near-term readout that will either validate or undermine the hypothesis that suppressing neuroinflammation alone modifies PD progression. If VTX3232 succeeds, it de-risks the neuroinflammation cluster and creates a rationale for second-generation approaches like Kv1.3 blockade that may offer differentiated or complementary mechanisms. If it fails, all neuroinflammation-targeted PD programs face increased skepticism from investors and regulators, making MUNA's path to a PD clinical trial substantially harder.

## References

### Key Publications
- [Kv1.3 modulates neuroinflammation and neurodegeneration in Parkinson's disease | Journal of Clinical Investigation (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7410064/) -- Sarkar et al., JCI 130(8):4195-4212
- [Kv1.3 inhibition attenuates neuroinflammation through disruption of microglial calcium signaling | Channels (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7781540/)
- [Kv1.3 Channel as a Key Therapeutic Target for Neuroinflammatory Diseases: State of the Art and Beyond | Frontiers in Neuroscience (2020)](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.01393/full)
- [Discovery of Kv1.3 ion channel inhibitors: Medicinal chemistry approaches and challenges | Medicinal Research Reviews (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8252768/)

### Press Releases & Filings
- [MUNA Therapeutics Awarded $4.9M Grant from The Michael J. Fox Foundation for Parkinson's Research (Oct 2022)](https://www.prnewswire.com/news-releases/muna-therapeutics-awarded-4-9m-grant-from-the-michael-j-fox-foundation-for-parkinsons-research-301645014.html)
- [MUNA Therapeutics Launches with $73M Series A (Jul 2021)](https://www.prnewswire.com/news-releases/muna-therapeutics-launches-with-us-73m-series-a-to-advance-novel-small-molecule-therapeutics-for-neurodegenerative-diseases-301328228.html)
- [MUNA Therapeutics Announces Strategic Alliance with GSK (Dec 2024)](https://www.prnewswire.com/news-releases/muna-therapeutics-announces-strategic-alliance-with-gsk-to-accelerate-development-of-novel-treatments-for-alzheimers-disease-302322958.html)
- [MUNA Therapeutics Awarded $1M Alzheimer's Association Grant for MNA-001 (2025)](https://www.prnewswire.com/news-releases/muna-therapeutics-awarded-1-million-alzheimers-association-grant-to-advance-clinical-development-of-novel-oral-trem2-agonist-mna-001-for-alzheimers-302656720.html)
- [GSK taps a startup for shot at Alzheimer's drug | BioPharma Dive (Dec 2024)](https://www.biopharmadive.com/news/gsk-alzheimers-drug-deal-muna-spatial-transcriptomics/734675/)

### Regulatory & Market
- [MUNA Therapeutics -- Our Science](https://munatherapeutics.com/our-science/)
- [MUNA Therapeutics -- Company Website](https://munatherapeutics.com/)
- [Kv1.3 In Microglia: Neuroinflammatory Determinant and Promising Pharmaceutical Target | J Neurology](https://www.jneurology.com/articles/kv13-in-microglia-neuroinflammatory-determinant-and-promising-pharmaceutical-target.html)
