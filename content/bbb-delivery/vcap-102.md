---
drug_name: "VCAP-102"
aliases: ["Voyager TRACER capsid"]
target: "BBB penetration via ALPL-mediated AAV transcytosis"
mechanism: "Engineered AAV capsid targeting alkaline phosphatase (ALPL) on brain endothelium for IV-to-CNS gene therapy delivery, achieving 98% substantia nigra DA neuron transduction in NHP"
modality: "AAV gene therapy"
developer: "Voyager Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "VYGR"
partner: "Neurocrine Biosciences"
partner_type: "biotech"
stage: "IND-enabling"
status: "Active"
patient_population: "GBA1-PD (lead program); CNS diseases broadly"
route_of_administration: "IV"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery]
date: 2026-02-16
company_link: "[[companies/voyager-therapeutics]]"
partner_link: "[[companies/neurocrine-biosciences]]"
---

# VCAP-102

## Summary

VCAP-102 is the foundational BBB-penetrant AAV capsid from Voyager Therapeutics (biotech, VYGR) that underpins the company's entire CNS gene therapy strategy. Discovered via the TRACER platform and confirmed to cross the blood-brain barrier through ALPL (tissue-nonspecific alkaline phosphatase)-mediated receptor transcytosis, VCAP-102 achieves 20-400x higher brain transduction than AAV9 across rodents and NHPs with simultaneous 14-fold liver detargeting. Second-generation capsids evolved from VCAP-102 reach 98% transduction of dopaminergic neurons in the substantia nigra at a clinically relevant IV dose of 3e13 vg/kg in NHP -- the single most PD-relevant preclinical transduction metric reported for any IV-delivered AAV capsid. The capsid's mechanism is species-conserved: ALPL orthologs share >92% amino acid identity across humans, mice, and macaques, and VCAP-102 binds and transcytoses human ALPL in vitro, directly addressing the PHP.eB translation catastrophe where mouse-specific LY6A dependence rendered an otherwise exceptional capsid useless in primates. Voyager has licensed VCAP-102-derived capsids to Neurocrine ($175M upfront, up to ~$4.4B total for GBA1-PD and 3 additional CNS programs -- see [[gba1-voyager]]) and Novartis ($1.2B+ for HD and SMA), validating the platform through two major pharma partnerships. The lead PD application -- Neurocrine's GBA1 gene therapy -- expects IND filing in 2025-2026 with Phase 1 initiation in 2026. If the capsid translates from NHP to human with similar BBB penetrance, VCAP-102 becomes the enabling platform for the entire IV CNS gene therapy field; if human BBB penetration falls short of NHP data, or immunogenicity/safety signals emerge, it joins the list of promising preclinical capsids that failed to translate.

## Notes

### Science

- **TRACER platform discovery**: VCAP-102 was identified through Voyager's TRACER (Tropism Redirection of AAV by Cell-type-specific Expression of RNA) platform. A "hotspot library" testing random 6-amino acid peptide insertions at 153 capsid surface positions on AAV9 was screened through two rounds of in vivo selection in cynomolgus macaque brain tissue. From approximately 1,500 recovered variants, VCAP-102 emerged as a top performer, sharing a conserved serine-proline-histidine (SPH) motif at positions 456-458 followed by a positively charged amino acid ([Huang et al., bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.03.12.584703v1.full))
- **ALPL receptor mechanism**: Voyager identified ALPL (tissue-nonspecific alkaline phosphatase, also called TNAP) as the primary receptor mediating VCAP-102's BBB crossing. ALPL is a GPI-anchored cell surface protein expressed on brain microvascular endothelial cells. In transwell assays, ectopic expression of human ALPL induced a >100-fold increase in VCAP-102 transcytosis with no measurable effect on AAV9 migration. Surface plasmon resonance confirmed direct binding with KD ~20 nM at pH 7.4 and rapid dissociation at pH 5.5 -- consistent with pH-dependent receptor-mediated transcytosis (bind at endothelial surface, release in acidified endosome) ([Huang et al., Molecular Therapy 2025](https://pubmed.ncbi.nlm.nih.gov/40340250/))
- **Species conservation -- why this matters**: ALPL isoforms from human, murine, and macaque origin share >92% amino acid identity, and VCAP-102 interacts with human, macaque, mouse, and porcine ALPL isoforms ([Huang et al., bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.03.12.584703v1.full)). This directly addresses the field's biggest historical failure: AAV-PHP.eB, which showed extraordinary brain transduction in C57BL/6 mice but relied on LY6A (SCA-1), a receptor absent in ~50% of mouse strains and entirely absent in primates ([Hordeaux et al., Mol Ther 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6520463/)). ALPL, by contrast, is a highly conserved, ubiquitously expressed enzyme -- 469 of 524 residues are unchanged or conservatively substituted across 220 million years of mammalian evolution ([Molecular Therapy 2025](https://pubmed.ncbi.nlm.nih.gov/40340250/))
- **Liver detargeting**: VCAP-102 shows 14-fold lower liver gene expression than AAV9 in mice and markedly reduced liver accumulation in primates. This is critical for IV AAV safety, as hepatotoxicity is the most common adverse event with systemic AAV delivery, driven by the liver acting as a sink for circulating vectors ([Huang et al., bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.03.12.584703v1.full))
- **DRG sparing**: VCAP-102 showed slightly reduced tropism for dorsal root ganglia compared to AAV9 in primates -- a meaningful advantage given that DRG toxicity (manifesting as sensory neuropathy, nerve fiber loss, NfL elevation) is a major safety concern for systemic AAV gene therapy and was specifically the issue that paused Voyager's own SOD1 ALS program ([Huang et al., bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.03.12.584703v1.full); [Voyager SOD1 update, Feb 2025](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-provides-update-sod1-als-gene-therapy-program/))
- **Second-generation capsids**: Through continued directed evolution of VCAP-101 and VCAP-102, Voyager evolved a second generation with further enhanced BBB penetrance, greater liver detargeting, and 50-75% of cells transduced across diverse brain regions at clinically relevant doses ([Voyager ASGCT 2024 press release](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-presents-data-second-generation-tracertm/))
- **Distinction from other engineered capsids**: Unlike Capsida's approach (which uses transferrin receptor for BBB crossing; see [[cap-003]]) and Sangamo's STAC-BBB/CNSRCV300 (receptor unidentified, ~65x over AAV9), VCAP-102's ALPL mechanism provides a known, highly conserved receptor target with demonstrated cross-species functionality. Known receptors allow rational optimization of binding affinity, pH-dependent release, and tissue selectivity

### Clinical

No clinical trials initiated for VCAP-102 as a standalone capsid product. The capsid is the enabling technology for multiple therapeutic programs now advancing toward clinical trials.

**Programs using VCAP-102-derived capsids advancing toward IND:**

- **GBA1-PD gene therapy** (Neurocrine collaboration): Development candidate selected April 2024. GLP toxicology ongoing. IND filing expected 2025-2026, Phase 1 initiation targeted 2026. Neurocrine funds through completion of Phase 1. See [[gba1-voyager]] for full program details ([Voyager Q3 2025 financials](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-reports-third-quarter-2025-financial-and-operating))
- **Friedreich's ataxia gene therapy (NBIB-223)** (Neurocrine collaboration): IND timeline update expected by end of 2025; clinical trials anticipated 2026. Uses TRACER capsid for IV delivery of frataxin gene ([FARA drug development page](https://www.curefa.org/drug-development/neurocrine-biosciences-voyager-therapeutics-aav-gene-therapy/))
- **Tau silencing gene therapy (VY1706)** (Voyager wholly owned): Development candidate selected November 2024 for Alzheimer's disease. IND filing anticipated 2026. Uses second-generation TRACER capsid delivering siRNA payload for tau knockdown. The same capsid was well-tolerated in 3-month NHP studies and achieved desired activity levels ([Voyager tau press release, Nov 2024](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-selects-tau-silencing-gene-therapy-development-candidate/))
- **SOD1 ALS gene therapy (VY9323)** (Voyager wholly owned): **Paused** February 2025. The capsid component was not the problem -- the siRNA payload showed off-target neurotoxicity (tremors, nerve fiber loss, NfL elevation at higher doses), narrowing the therapeutic window. Voyager is assessing alternate payloads while retaining the same capsid ([Voyager SOD1 update, Feb 2025](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-provides-update-sod1-als-gene-therapy-program/))
- **Novartis programs**: Huntington's disease (Voyager responsible for preclinical, Novartis for clinical development and commercialization) and SMA (Novartis responsible for all development). Separate from Neurocrine collaboration ([Novartis-Voyager deal, Jan 2024](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-enters-capsid-license-agreement-and))

**Key NHP transduction data (ASGCT 2024):**
Single IV dose of 3e13 vg/kg in NHP using second-generation VCAP-102-derived capsids:
- **Substantia nigra dopaminergic neurons**: up to 98% transduction
- **Spinal motor neurons**: up to 94% transduction
- **Purkinje neurons (cerebellum)**: upwards of 95% transduction
- **Thalamic neurons**: up to 66% transduction
- **Motor cortex neurons**: up to 43% transduction
- **Astrocytes across brain regions**: 87-99% transduction
- SOD1 mRNA knockdown in spinal cord motor neurons: up to 80%

([Voyager ASGCT 2024 press release](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-presents-data-second-generation-tracertm/); [Voyager ALPL Molecular Therapy publication, May 2025](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-demonstrates-alpl-receptor-mediated-blood-brain-barrier))

**Historical context -- VY-AADC (eladocagene):**
Voyager's first PD gene therapy (AAV2-AADC for dopamine restoration) used intracranial delivery, not IV capsid technology. The program was partnered with Neurocrine in 2019 ($165M upfront, $1.7B potential), but was clinically held by the FDA after MRI abnormalities in RESTORE-1 participants, and Neurocrine terminated the partnership in February 2021. The current IV capsid strategy represents Voyager's pivot from intracranial delivery to systemic IV delivery enabled by BBB-penetrant capsids. See [[eladocagene]] for the VY-AADC history ([Neurocrine terminates VY-AADC, 2021](https://www.biospace.com/neurocrine-terminates-2019-parkinson-s-disease-collaboration-with-voyager-therapeutics))

### Financial

- **Neurocrine collaboration (Jan 2023)**: $175M upfront ($136M cash + $39M equity at $8.88/share, 50% premium to 30-day VWAP). Total potential: ~$4.4B across GBA1 + 3 additional programs. GBA1 program alone: up to $985M development milestones + low-double-digit-to-20% US royalties + high-single-digit-to-mid-teen ex-US royalties if Voyager declines co-development option. If Voyager elects co-development: 50/50 US cost/profit sharing. Per additional program: up to $175M development milestones + royalties. Neurocrine returned 2 of 4 discovery-stage programs (undisclosed targets) in May 2025 but retained GBA1 and FA ([Voyager-Neurocrine collaboration PR, Jan 2023](https://ir.voyagertherapeutics.com/news-releases/news-release-details/neurocrine-biosciences-and-voyager-therapeutics-enter-strategic/); [Fiercebiotech, May 2025](https://www.fiercebiotech.com/biotech/neurocrine-hands-back-2-cns-gene-therapy-programs-voyager))
- **Novartis collaboration (Jan 2024)**: Target-exclusive capsid license for HD and SMA. Up to $1.2B in preclinical, development, regulatory, and sales milestones + tiered royalties. Expanded from earlier March 2022 option agreement where Novartis paid $25M upfront + exercised option for two targets at up to $600M. In September 2024, Novartis entered a further capsid license, bringing total partnered TRACER-enabled programs to 14 ([Novartis-Voyager deal, Jan 2024](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-enters-capsid-license-agreement-and); [Novartis expansion, Sep 2024](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-enters-license-next-generation-capsid-bringing-partnered))
- **Additional licensing**: Voyager has licensed TRACER capsids to multiple undisclosed pharma partners (14 partnered programs total as of September 2024), generating licensing fees and milestones
- **Milestones expected**: Up to $35M in 2025-2026 from IND filings for GBA1 and FA programs
- **Voyager market cap**: ~$205M (early 2026); stock ~$3.68, down from 52-week high of $7.44. Cash runway extended to mid-2027 ([Voyager Q3 2025](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-reports-third-quarter-2025-financial-and-operating))
- **Platform valuation signal**: Combined upfront payments from Neurocrine ($175M) and Novartis (~$25M+) plus licensing fees from 14 partnered programs significantly exceed Voyager's current market cap, suggesting the market assigns low probability to clinical-stage value creation from the platform

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[abl301]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |
| [[sar446159]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |

- **Capsida Biotherapeutics / [[cap-003]]**: The most direct competitor. Uses an engineered AAV capsid targeting human transferrin receptor (hTfR1) for BBB crossing. IND cleared June 2025, Phase 1/2 dosing initiated Q3 2025 for PD-GBA (NCT07011771). NHP data showed 200-fold greater brain GBA1 expression than AAV9, 19-fold less liver, 17-fold less DRG. Capsida has the clinical lead for IV BBB-crossing AAV in PD. AbbVie partnership ($90M upfront + $40M opt-in) ([Capsida IND clearance, 2025](https://capsida.com/))
- **Sangamo STAC-BBB (CNSRCV300)**: Directed evolution-derived AAV9 variant with ~65x higher brain transduction than AAV9. Cross-species (C57BL/6, NHP, human models). Key disadvantage: BBB receptor has not been identified, limiting rational optimization and raising translation uncertainty
- **PHP.eB (Caltech/academic)**: The cautionary tale. ~100x brain transduction in C57BL/6 mice, but entirely dependent on LY6A (absent in primates and ~50% of mouse strains). Rendered non-translatable. VCAP-102's ALPL mechanism directly addresses this failure mode ([Hordeaux et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6520463/))
- **BI-hTFR1 (Broad Institute)**: Engineered AAV binding human transferrin receptor; 40-50x CNS expression over AAV9 in humanized TfRC knock-in mice. Academic-stage; published in Science 2024. Related to Capsida's approach ([An AAV capsid reprogrammed to bind human transferrin receptor | Science 2024](https://www.science.org/doi/10.1126/science.adm8386))
- **Intracisternal AAV gene therapies** ([[pr001]], [[aav-gad]], [[eladocagene]]): These bypass the BBB problem entirely by delivering directly to the CNS, but require invasive procedures (stereotactic injection, cisterna magna access). If VCAP-102 or Capsida's capsid translates to humans, IV delivery renders intracisternal approaches less attractive for diseases requiring widespread CNS coverage
- **Key competitive distinction**: VCAP-102's identified ALPL mechanism enables rational next-generation engineering (affinity tuning, pH-dependent release optimization), while competitors with unidentified receptors (Sangamo) or different receptor targets (Capsida/hTfR1) face different risk profiles. Transferrin receptor is more widely studied but also mediates iron transport -- potential safety interactions with iron homeostasis are theoretically possible

## Analysis

The VCAP-102 capsid platform represents one of the highest-conviction bets in CNS gene therapy delivery, backed by two major pharma validations (Neurocrine $4.4B total potential, Novartis $1.2B+) and the strongest published mechanistic rationale of any BBB-crossing AAV capsid. Three features make VCAP-102 distinctive among engineered capsids: (1) the receptor has been identified (ALPL) and confirmed to mediate transcytosis, not just binding; (2) species conservation is demonstrated across rodents, NHP, pig, and human cells; and (3) the pH-dependent binding/release kinetics (KD ~20 nM at pH 7.4, rapid dissociation at pH 5.5) are consistent with efficient transcytosis.

The 98% substantia nigra dopaminergic neuron transduction figure is the most PD-relevant data point from any IV AAV platform. For context, PD neurodegeneration begins with dopaminergic neuron loss in the substantia nigra -- any gene therapy targeting PD pathology (GBA1 restoration, alpha-synuclein knockdown, neurotrophic factor delivery) depends on efficient transduction of precisely these neurons. Achieving near-complete transduction at a dose of 3e13 vg/kg (considered clinically feasible) in NHP is a strong preclinical signal. However, these are second-generation capsids evolved from VCAP-102, and the specific capsid variants used in therapeutic programs may differ in their transduction profiles.

**Analytical estimate -- probability that VCAP-102-derived capsids achieve meaningful human BBB penetration (>10x AAV9 in brain): 40-50%.** This is our assessment, not from a published source. The reasoning:
- Base rate: novel AAV capsid NHP-to-human translation for BBB crossing ~30% (historically poor, but the field is early)
- Adjustments upward: identified receptor with >92% cross-species conservation (+10%), confirmed human ALPL binding and transcytosis in vitro (+5%), pH-dependent binding kinetics consistent with known transcytosis biology (+3%), multi-species in vivo validation (mice, marmosets, AGMs, cynomolgus) (+5%)
- Adjustments downward: no human in vivo data (-5%), ALPL expression levels on human brain endothelium may differ from NHP (-3%), potential neutralizing antibodies to engineered capsid surface motifs (-3%)
- Net: ~42%

The SOD1 ALS program pause (February 2025) is instructive: the capsid was not the problem -- the siRNA payload caused off-target neurotoxicity. The same capsid in the tau silencing program (VY1706) was well-tolerated at 3 months in NHP. This suggests the VCAP-102 capsid family has an acceptable safety profile, with program-specific payload toxicity as the variable risk. For [[gba1-voyager]], the payload is a well-characterized endogenous enzyme (GCase), which has a more predictable toxicity profile than synthetic siRNA constructs.

The competitive race against [[cap-003|Capsida/CAP-003]] is the critical dynamic. Capsida has the clinical lead (Phase 1/2 dosing initiated Q3 2025), uses a different receptor (transferrin receptor vs. ALPL), and has AbbVie backing. If CAP-003 Phase 1 shows safe, durable GCase restoration in brain, it validates IV BBB-crossing AAV gene therapy for PD and creates pressure on Voyager to demonstrate comparable or superior results. If CAP-003 encounters safety issues (DRG toxicity, hepatotoxicity, immunogenicity), it may reflect either capsid-specific or class-wide risks -- and the answer to that question determines whether VCAP-102's different receptor mechanism provides an advantage or faces the same obstacles.

The decision tree for PD: if Voyager/Neurocrine's GBA1 IND is filed on schedule (2025-2026) and Phase 1 dosing begins in 2026, initial safety data would emerge by late 2026/early 2027. Positive safety plus evidence of CNS GCase activity increase would be a major derisking event for the VCAP-102 platform broadly -- not just for PD but for the 14+ partnered programs. Negative safety data, particularly any signal of complement activation, hepatotoxicity, or DRG toxicity, would pressure the entire TRACER-derived capsid portfolio and shift PD gene therapy capital toward Capsida or back to intracisternal approaches like [[pr001]].

## References

### Key Publications
- [Highly conserved brain vascular receptor ALPL mediates transport of engineered AAV vectors across the blood-brain barrier | Molecular Therapy (2025)](https://pubmed.ncbi.nlm.nih.gov/40340250/)
- [Highly conserved brain vascular receptor ALPL mediates transport of engineered viral vectors across the blood-brain barrier | bioRxiv (2024)](https://www.biorxiv.org/content/10.1101/2024.03.12.584703v1.full)
- [The GPI-Linked Protein LY6A Drives AAV-PHP.B Transport across the Blood-Brain Barrier | Mol Ther (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6520463/)
- [An AAV capsid reprogrammed to bind human transferrin receptor mediates brain-wide gene delivery | Science (2024)](https://www.science.org/doi/10.1126/science.adm8386)
- [Lethal immunotoxicity in high-dose systemic AAV therapy | Mol Ther (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10638066/)
- [Tissue-Nonspecific Alkaline Phosphatase in Central Nervous System Health and Disease | Int J Mol Sci (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8156423/)

### Press Releases & Filings
- [Voyager Demonstrates ALPL Receptor-Mediated BBB Transport of Novel AAV Capsids (May 2025)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-demonstrates-alpl-receptor-mediated-blood-brain-barrier)
- [Voyager Presents Data for Second-Generation TRACER Capsids at ASGCT 27th Annual Meeting (May 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-presents-data-second-generation-tracertm/)
- [Voyager Presents Robust Multi-Species Results at ASGCT 26th Annual Meeting (May 2023)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-presents-robust-multi-species-results/)
- [Neurocrine and Voyager Enter Strategic Collaboration (January 2023)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/neurocrine-biosciences-and-voyager-therapeutics-enter-strategic/)
- [Voyager Enters Capsid License Agreement with Novartis (January 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-enters-capsid-license-agreement-and)
- [Voyager Enters License for Next-Generation Capsid, 14 Partnered Programs (September 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-enters-license-next-generation-capsid-bringing-partnered)
- [Voyager Announces Selection of Development Candidate for GBA1 Program (April 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-announces-selection-development-candidate-0/)
- [Voyager Selects Tau Silencing Gene Therapy Development Candidate (November 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-selects-tau-silencing-gene-therapy-development-candidate/)
- [Voyager Provides Update on SOD1 ALS Gene Therapy Program (February 2025)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-provides-update-sod1-als-gene-therapy-program/)
- [Neurocrine Hands Back 2 CNS Gene Therapy Programs to Voyager (May 2025)](https://www.fiercebiotech.com/biotech/neurocrine-hands-back-2-cns-gene-therapy-programs-voyager)
- [Voyager Reports Third Quarter 2025 Financial and Operating Results](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-reports-third-quarter-2025-financial-and-operating)
- [Neurocrine Terminates VY-AADC Parkinson's Collaboration (2021)](https://www.biospace.com/neurocrine-terminates-2019-parkinson-s-disease-collaboration-with-voyager-therapeutics)
- [NBIB-223 Friedreich's Ataxia Program | FARA](https://www.curefa.org/drug-development/neurocrine-biosciences-voyager-therapeutics-aav-gene-therapy/)
