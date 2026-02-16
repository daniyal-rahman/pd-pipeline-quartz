---
drug_name: "ROME LINE-1 RT Inhibitor"
aliases: ["LINE-1 reverse transcriptase inhibitor"]
target: "LINE-1 reverse transcriptase (retrotransposon-driven neuroinflammation)"
mechanism: "Small molecule inhibitor of LINE-1 reverse transcriptase, blocking retrotransposon-driven cytoplasmic DNA accumulation and cGAS-STING-mediated neuroinflammation while reducing genomic instability in aging neurons"
modality: "small molecule"
developer: "ROME Therapeutics"
company_type: "startup"
publicly_traded: false
partner: ""
stage: "Preclinical"
status: "Active"
patient_population: "Neurodegenerative diseases (PD not yet specified as lead indication)"
route_of_administration: "oral"
key_biomarkers: ["LINE-1 Orf1p expression", "alpha-synuclein levels", "neurofilament light chain"]
confidence_rating: "3/10"
next_catalyst: "IND filing (autoimmune indication expected first; neuro program behind)"
catalyst_date: "2026-2027 (autoimmune); neuro IND TBD"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-16
company_link: "[[companies/rome-therapeutics]]"
---

# ROME LINE-1 RT Inhibitor

## Summary

ROME Therapeutics (startup, private) is developing first-in-class small molecule inhibitors of LINE-1 reverse transcriptase (RT), a viral-like enzyme encoded by retrotransposable elements that becomes aberrantly active in aging and disease. Preclinical data presented at the 3rd Annual Dark Genome Symposium (November 2024) showed dopaminergic neuron protection and dose-dependent alpha-synuclein reduction in 6-OHDA models, with oral bioavailability and brain penetrance in rodents. However, the lead clinical program targets autoimmune disease (lupus/type I interferonopathies), not PD -- neurodegeneration is a secondary pipeline expansion still in early preclinical stages. If ROME's autoimmune Phase 1 validates the LINE-1 RT inhibition mechanism in humans and the company advances a neuro-specific IND, this becomes a novel neuroinflammation approach orthogonal to NLRP3 inflammasome inhibitors like [[dapansutrile]] and [[selnoflast]]. If the autoimmune program fails or the company deprioritizes neuro, the PD-relevant science remains academic.

## Notes

### Science
- LINE-1 (Long Interspersed Nuclear Element-1) is the only autonomously active retrotransposon in the human genome, comprising ~17% of genomic DNA. In healthy young cells, LINE-1 is epigenetically silenced via DNA methylation and histone modification. With aging, these silencing mechanisms fail, and LINE-1 becomes de-repressed
- Active LINE-1 encodes two proteins: ORF1p (RNA-binding chaperone) and ORF2p (which contains both endonuclease and **reverse transcriptase** domains). ORF2p's RT activity reverse-transcribes LINE-1 RNA into cDNA in the cytoplasm, generating foreign-appearing DNA that triggers the **cGAS-STING innate immune pathway**, producing type I interferon and chronic neuroinflammation
- Separately, LINE-1 retrotransposition (reinsertion into new genomic loci) causes **insertional mutagenesis, DNA double-strand breaks, and genomic instability** in post-mitotic neurons -- a dual-hit mechanism combining inflammation and DNA damage
- **Genetic validation in PD:** PPMI cohort analysis (N=372 PD, 178 controls) showed that increased burden of highly active retrotransposition-competent LINE-1 elements (>=9) was associated with PD risk (OR 1.25, 95% CI 1.03-1.51, p=0.02) and correlated with 72 clinical progression markers (Pfaff et al., *Int J Mol Sci* 2020)
- **cGAS-STING in PD specifically:** Nature 2023 paper (Gulen et al.) demonstrated cGAS-STING drives aging-related inflammation and neurodegeneration; separate 2025 work showed cGAS-STING-dependent inflammation contributes to dopaminergic neurodegeneration in synucleinopathy models
- ROME's compounds are **non-nucleoside RT inhibitors** (distinct from nucleoside analogs like lamivudine/censavudine), designed for selectivity against LINE-1 RT over human DNA polymerases -- critical for chronic dosing safety in neurodegeneration
- Key differentiator vs. other neuroinflammation approaches: targets the **upstream trigger** (retrotransposon-derived cytoplasmic DNA) rather than downstream effectors (NLRP3, TLR2, TYK2). If LINE-1 activation is a root cause of age-related neuroinflammation, RT inhibition could be more disease-modifying than inflammasome blockade
- Open question: is LINE-1 de-repression a **cause** or **consequence** of neurodegeneration? Epigenetic erosion with aging suggests it may be an independent driver, but it could also be secondary to alpha-synuclein-induced chromatin changes

### Clinical
No clinical trials initiated for PD or any neurodegenerative indication.

**Preclinical data (Dark Genome Symposium, November 2024):**
- **In vitro (6-OHDA model):** ROME's LINE-1 RT inhibitors prevented cell death in dopaminergic (TH+) mouse primary neurons exposed to 6-hydroxydopamine; showed dose-dependent decrease in alpha-synuclein expression; suppressed LINE-1 ORF1p protein upregulation following injury
- **In vivo (6-OHDA model):** Orally dosed LINE-1 RT inhibitors were neuroprotective after 14 days of treatment, with protection correlating with both LINE-1 RT potency and pharmacokinetic properties; no adverse events reported
- **ADME profile:** Favorable oral bioavailability, tolerability, and brain penetrance demonstrated in rodent studies
- **Pipeline status:** Company has stated it is conducting further in vivo studies in Parkinson's and ALS mouse models; no IND-enabling studies disclosed for neurodegenerative indications
- **Lead clinical program is autoimmune, not neuro:** ROME's first IND is planned for type I interferonopathies (lupus), with the $72M Series B extension specifically earmarked for advancing the lead autoimmune candidate into Phase 1

### Financial
- **Total raised:** ~$199M across Series A ($50M, April 2020) and Series B ($77M, September 2021) + Series B extension ($72M, September 2023)
- **Key investors:** GV (Google Ventures), ARCH Ventures, Andreessen Horowitz, Sanofi Ventures, Section 32 (led Series B), Casdin Capital, Alexandria Venture Investments, Mass General Brigham Ventures
- **Strategic investors:** Johnson & Johnson Innovation (JJDC) and Bristol Myers Squibb participated in the Series B extension -- pharma validation of the repeatome platform thesis
- **Valuation:** Not publicly disclosed; $199M total raised with a syndicate of this quality suggests a post-money north of $500M, though the majority of that value is attributed to the autoimmune lead program, not neurodegenerative indications
- **CEO:** Rosana Kapeller, MD, PhD -- previously founding CSO of Nimbus Therapeutics (sold allosteric TYK2 inhibitor to Takeda for up to $6B), first EIR at GV. Strong drug development pedigree
- **Cash runway:** Series B extension (September 2023) funds expected to carry through Phase 1 in autoimmune; neuro program funded from same pool but at lower priority
- **Comparator:** Transposon Therapeutics (private, Canaan Partners-backed) is the closest competitor with censavudine (TPN-101) in Phase 2 for PSP and ALS/FTD; ROME is earlier-stage but with a more modern chemistry approach (non-nucleoside vs. nucleoside analog)

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(thesis_cluster, "neuroinflammation") AND file.name != "rome-line1"
SORT stage DESC
```

- The neuroinflammation cluster in PD is crowded but largely focused on **downstream effectors**: NLRP3 inflammasome inhibitors ([[dapansutrile]], [[selnoflast]], [[vtx3232]], [[nt-0796]], [[ism8969]]), TLR2 antagonist ([[nm-101]]), TYK2/JAK1 inhibitor ([[bhv-8000]]), and GLP-1R agonists ([[exenatide]], [[semaglutide]], [[lixisenatide]]). ROME targets an **upstream trigger** -- retrotransposon-driven innate immune activation -- which is mechanistically orthogonal
- **Transposon Therapeutics (censavudine/TPN-101)** is the most direct competitor: also a LINE-1 RT inhibitor, but a nucleoside analog (stavudine derivative) in Phase 2 for PSP with FDA Fast Track designation. TPN-101 showed NfL reduction and dose-related IL-6 decrease at 48 weeks in PSP. However, TPN-101 is not being developed for PD specifically, and nucleoside analogs carry known long-term toxicity risks (mitochondrial toxicity from stavudine lineage) that may limit chronic use in neurodegeneration
- **Lamivudine** (generic HIV NRTI) has academic validation: neuroprotection in tau transgenic mice, cognitive rescue in Down syndrome models, and epidemiological association with reduced Alzheimer's risk in long-term HIV patients. However, lamivudine lacks LINE-1 selectivity and carries its own safety profile concerns for chronic neurodegeneration dosing
- If ROME succeeds in autoimmune and advances to neuro: first-in-class opportunity in a novel mechanistic space for PD with strong genetic validation (PPMI L1 burden data). If ROME stays focused on autoimmune: the PD-relevant LINE-1 RT inhibition thesis remains validated only by academic data and the Transposon Therapeutics program in non-PD tauopathies

## Analysis

ROME Therapeutics represents a genuinely novel mechanism for PD neuroinflammation -- retrotransposon biology is a frontier that has only recently moved from basic science curiosity to druggable target. The genetic validation from the PPMI cohort (LINE-1 burden associated with PD risk and progression), the cGAS-STING pathway link to dopaminergic neurodegeneration, and the preclinical data showing both neuroprotection and alpha-synuclein reduction provide a coherent biological rationale. The dual mechanism -- blocking both neuroinflammation (cGAS-STING) and genomic instability (retrotransposition) -- is more compelling than targeting either pathway alone.

**Analytical estimate -- Probability of ROME advancing a PD-specific IND: 25-30%.** This is our assessment, not from a published source. The reasoning: the company's stated priority and funding are directed at autoimmune disease (lupus) as the lead indication. PD is a secondary pipeline expansion that would require the autoimmune program to succeed (validating the mechanism in humans), generate sufficient capital for a second clinical program, and compete for internal resources against cancer indications that ROME is also exploring. Base rate for a startup pivoting from its lead indication therapeutic area to neurodegenerative disease: low (~15%). Adjustments upward: strong preclinical PD data (+5%), high-quality investor syndicate with J&J/BMS strategic backing (+5%), CEO track record at Nimbus (+5%). Adjustments downward: neurodegenerative disease is not the company's core mission (-5%). Net: ~25-30%.

**Signal analysis:** The J&J and BMS strategic investments are notable -- both have neuroscience portfolios and could provide a licensing/partnership path for the neuro program even if ROME itself stays autoimmune-focused. Rosana Kapeller's track record at Nimbus (built and sold a TYK2 inhibitor program to Takeda for $6B) demonstrates her ability to create high-value assets, but Nimbus was laser-focused on its lead program rather than expanding broadly. The Dark Genome Symposium preclinical data disclosure (November 2024) signals that ROME is actively building the neurodegenerative disease data package, even if it is not the lead program -- this is a deliberate expansion, not an afterthought.

The key watch item is whether ROME's autoimmune Phase 1 (expected 2025-2026) demonstrates proof of mechanism: reduction in type I interferon signature, acceptable safety with chronic dosing, and evidence of LINE-1 pathway modulation. If positive, the neuro expansion becomes viable. If negative, the entire LINE-1 RT inhibition thesis is challenged, and Transposon Therapeutics' censavudine data in PSP becomes the field's primary clinical anchor. For PD specifically, the field would need to wait for either ROME or another group to run a PD-specific clinical study, which is likely 3-5 years away from any human PD data.

## References

### Key Publications
- [Increased Burden of Highly Active RC-L1s Associated with PD Risk and Progression in PPMI Cohort | Int J Mol Sci (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7554759/)
- [Reference LINE-1 Insertion Polymorphisms Correlate with PD Progression and Differential Transcript Expression in PPMI | PMC (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10449770/)
- [cGAS-STING Drives Ageing-Related Inflammation and Neurodegeneration | Nature (2023)](https://www.nature.com/articles/s41586-023-06373-1)
- [Crosstalk Between DNA Damage and cGAS-STING Immune Pathway Drives Neuroinflammation and Dopaminergic Neurodegeneration in PD | Brain Behav Immun (2025)](https://www.sciencedirect.com/science/article/abs/pii/S0889159125002995)
- [Retrotransposons as a Source of DNA Damage in Neurodegeneration | Front Aging Neurosci (2021)](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.786897/full)
- [The Role of Retrotransposons and Endogenous Retroviruses in Age-Dependent Neurodegenerative Disorders | Annu Rev Neurosci (2024)](https://www.annualreviews.org/content/journals/10.1146/annurev-neuro-082823-020615)
- [Lamivudine (3TC) Prevents Neuropathological Alterations in Mutant Tau Transgenic Mice | PMC (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10342792/)

### Press Releases & Filings
- [ROME Therapeutics Debuts First Preclinical Data of LINE-1 RT Inhibitors in Neurodegenerative Diseases at Dark Genome Symposium (Nov 2024)](https://www.globenewswire.com/news-release/2024/11/21/2985070/0/en/ROME-Therapeutics-Debuts-First-Preclinical-Data-of-its-LINE-1-Reverse-Transcriptase-RT-Inhibitors-in-Neurodegenerative-Diseases-at-3rd-Annual-Dark-Genome-Symposium.html)
- [ROME Therapeutics Closes $72M Series B Extension for Autoimmune Disease (Sep 2023)](https://rometx.com/press-releases/rome-therapeutics-closes-oversubscribed-72-million-series-b-extension-to-support-advancement-of-lead-program-into-clinical-development-for-autoimmune-disease/)
- [ROME Therapeutics Secures $77M Series B Financing (Sep 2021)](https://rometx.com/press-releases/rome-therapeutics-secures-77-million-in-series-b-financing-to-advance-repeatome-derived-pipeline-for-cancer-and-autoimmune-diseases-and-expand-repeatomics-platform/)
- [ROME Therapeutics Launches with $50M Series A (Apr 2020)](https://rometx.com/press-releases/rome-therapeutics-launches-to-develop-novel-therapies-for-cancer-and-autoimmune-diseases-by-harnessing-the-power-of-the-repeatome/)
- [ROME Therapeutics Presents First Data Validating LINE-1 RT as Novel Target in Autoimmune Diseases (2024)](https://rometx.com/press-releases/rome-therapeutics-presents-first-data-to-validate-line-1-rt-as-a-novel-target-in-autoimmune-diseases-and-the-therapeutic-potential-of-its-first-in-class-line-1-rt-inhibitors/)
- [Transposon Therapeutics Phase 2 Results for TPN-101 in PSP and C9orf72 ALS/FTD (Jan 2024)](https://www.prnewswire.com/news-releases/transposon-announces-final-results-from-a-phase-2-study-of-its-line-1-reverse-transcriptase-inhibitor-tpn-101-for-the-treatment-of-progressive-supranuclear-palsy-and-interim-results-from-a-phase-2-study-of-tpn-101-for-the-treatmen-302060254.html)
- [Nature Communications: Pan-Cancer Analysis of LINE-1 Expression and Retrotransposon Activity (Mar 2025)](https://www.globenewswire.com/news-release/2025/03/03/3035481/0/en/ROME-Therapeutics-Announces-Publication-in-Nature-Communications-of-First-Large-Scale-Pan-Cancer-Analysis-of-LINE-1-Expression-Levels-and-Retrotransposon-Activity.html)
