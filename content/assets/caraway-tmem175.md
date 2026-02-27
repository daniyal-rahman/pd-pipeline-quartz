---
drug_name: "Caraway TMEM175 Modulator"
aliases: ["TMEM175 activator", "Merck TMEM175", "Rheostat Therapeutics"]
target: "TMEM175 (lysosomal potassium/proton channel)"
mechanism: "Small molecule activator of TMEM175 lysosomal potassium/proton channel to restore lysosomal pH homeostasis, enhance glucocerebrosidase activity, and reduce alpha-synuclein aggregation"
modality: "small molecule"
developer: "Caraway Therapeutics (acquired by Merck)"
company_type: "big pharma"
publicly_traded: true
ticker: "MRK"
partner: "AbbVie (pre-acquisition collaboration)"
partner_type: "big pharma"
stage: "Preclinical"
status: "Active"
patient_population: "Parkinson's disease (TMEM175 variant carriers and broader PD)"
route_of_administration: "oral"
key_biomarkers: ["glucocerebrosidase activity", "lysosomal pH", "alpha-synuclein levels", "phosphorylated alpha-synuclein"]
confidence_rating: "4/10"
next_catalyst: "IND-enabling study disclosure or clinical candidate nomination"
catalyst_date: "Unknown"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-16
company_link: "[[companies/caraway-therapeutics]]"
partner_link: "[[companies/abbvie]]"
---

# Caraway TMEM175 Modulator

## Summary

Merck (big pharma, MRK) acquired Caraway Therapeutics for up to $610M in biobucks in November 2023 to gain access to preclinical small molecule TMEM175 activators for Parkinson's disease and ALS. TMEM175 is among the strongest GWAS-validated PD risk genes -- the M393T loss-of-function variant (rs34311866) is present in over 20% of PD patients and causes lysosomal pH dysregulation, reduced glucocerebrosidase activity, and increased alpha-synuclein aggregation. No clinical candidates have been publicly disclosed; the program remains preclinical as of early 2026, with no mention on Merck's public pipeline page. This is Merck's second lysosomal channel acquisition after Calporta ($576M, TRPML1, 2019), bringing their total lysosomal ion channel investment to ~$1.2B -- a remarkable commitment to a thesis that has zero clinical validation. If Merck advances a TMEM175 activator to clinical trials and demonstrates biomarker movement (lysosomal pH normalization, GCase activity restoration), it validates an entirely new druggable node in the lysosomal pathway orthogonal to direct GCase activators like [[pariceract]] and chaperones like [[ambroxol]]. If the program stalls or is quietly deprioritized -- as often happens with preclinical acquisitions absorbed into big pharma -- the $610M becomes another data point in Merck's expensive neuroscience bet.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Merck (acquirer) |
| Deal Date | November 2023 |
| Upfront | Undisclosed |
| Total (Biobucks) | ~$610M |
| Deal Type | Acquisition |

## Notes

### Science
- TMEM175 is a lysosomal transmembrane potassium/proton channel that regulates lysosomal pH homeostasis. Under physiological acidic conditions, TMEM175 acts as a proton-activated, proton-selective channel mediating H+ leak from the lysosomal lumen to the cytosol, counterbalancing V-ATPase acidification to maintain optimal pH (~4.7-5.5)
- The GWAS signal at chromosome 4p16.3 identified rs34311866 (p.M393T) as the causal variant -- 20 orders of magnitude more significant than any other SNP in the locus. Functional knockdown of all genes under the GWAS peak confirmed only TMEM175 consistently influenced phosphorylated alpha-synuclein accumulation
- TMEM175 deficiency causes lysosomal over-acidification, which impairs glucocerebrosidase (GCase) activity (optimal at pH 4.7-5.5), reduces autophagosome clearance, increases alpha-synuclein aggregation, and decreases mitochondrial respiration -- connecting lysosomal dysfunction to both synucleinopathy and mitochondrial pathology
- The M393T variant is loss-of-function and possibly dominant-negative: CRISPR-edited homozygous M393T cells showed impaired lysosomal pH regulation, reduced TMEM175 lysosomal localization, and increased phospho-alpha-synuclein. Present in >20% of PD patients, making it one of the most common PD risk variants
- Caraway's approach: small molecule activators that increase TMEM175 channel activity to restore lysosomal pH, thereby rescuing downstream GCase activity and alpha-synuclein clearance. This is mechanistically distinct from direct GCase activators ([[pariceract]]) or GCase chaperones ([[ambroxol]]) -- it targets the upstream pH environment rather than the enzyme itself
- Recent academic work (Neuron, 2025) solved cryo-EM structures of human TMEM175 with three small molecule agonists (DCY1020, DCY1040, TUG-891), showing binding at the inter-subunit interface. DCY1040 and TUG-891 facilitated lysosomal degradation of aberrant alpha-synuclein and alleviated PD-like behaviors in vivo -- providing academic proof-of-concept for the activator approach
- Key connection to GBA1 pathway: TMEM175 deficiency reduces GCase activity by disrupting optimal lysosomal pH, meaning TMEM175 activation could theoretically benefit both TMEM175 variant carriers AND GBA1 mutation carriers (5-15% of PD) by optimizing the pH environment for residual GCase function
- Open questions: (1) whether TMEM175 activation in non-carrier idiopathic PD provides meaningful benefit, (2) therapeutic window between restoring normal lysosomal pH and over-alkalinization, (3) whether Merck's compounds have differentiated pharmacology vs. academic tool compounds

### Clinical

No clinical trials initiated. The TMEM175 program remains in preclinical development within Merck's internal neuroscience pipeline.

**Pre-acquisition milestones:**
- Caraway had "advanced drug discovery programs" against TMEM175 and TRPML1 targets as of the November 2023 acquisition
- AbbVie collaboration (June 2021): Caraway received $17M upfront with up to $267M in total payments for TMEM175 modulators. After Caraway completed certain preclinical R&D, AbbVie had an option to license the program for IND-enabling studies and clinical development. Status of this collaboration post-Merck acquisition is unclear
- No IND filing, clinical candidate nomination, or NHP data has been publicly disclosed

**Academic proof-of-concept (not Merck compounds):**
- DCY1040 and TUG-891 (academic TMEM175 agonists) alleviated PD-like behaviors in animal models and regulated lysosomal acidity in dopaminergic neurons derived from iPSCs of PD patients carrying TMEM175 variants (Neuron, 2025)

### Financial
- **Merck acquisition:** Up to $610M total (undisclosed upfront + contingent milestones); upfront expensed in Q4 2023
- **Prior AbbVie collaboration:** $17M upfront to Caraway (June 2021), up to $267M total potential including option payments and milestones, plus royalties. Caraway had option to co-develop for increased royalties. Fate of this collaboration under Merck ownership is undisclosed
- **Caraway fundraising:** Series A of $23M (2018), co-led by MRL Ventures Fund (Merck's VC arm) and AbbVie Ventures, with Amgen Ventures, Alexandria Venture Investments, and Mayo Clinic participating. Founded 2017 as Rheostat Therapeutics by Dementia Discovery Fund (DDF) and SV Fund VI, co-founded by SV Venture Partner Tim Harris
- **Merck's lysosomal channel thesis:** $576M for Calporta (TRPML1, 2019) + $610M for Caraway (TMEM175/TRPML1, 2023) = ~$1.2B total invested in lysosomal ion channel biology. This is one of the largest commitments by any pharma company to the lysosomal hypothesis in neurodegeneration
- **No public pipeline listing:** TMEM175 does not appear on Merck's public product pipeline (as of November 2025 update), which lists only MK-2214 (anti-tau, Phase 2) and MK-1167 (alpha-7 nAChR, Phase 2) in neuroscience. Preclinical programs are typically not listed, but the absence means no imminent IND
- **Context:** Merck's Keytruda patent cliff (~2028-2030) is driving aggressive pipeline diversification. Neuroscience is one of several therapeutic areas receiving increased investment, with 10+ BD deals executed

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[mair-tmem175]] | Discovery | Active | Mair Therapeutics | small molecule |
| [[caraway-tmem175]] | Preclinical | Active | Caraway Therapeutics (acquired by Merck) | small molecule |
| [[endlyz]] | Preclinical | Active | Endlyz Therapeutics | small molecule |
| [[casma-trpml1]] | IND-enabling | Active | Casma Therapeutics | small molecule |

- [[casma-trpml1|CSM-101]] (Casma Therapeutics, startup) targets TRPML1, a different lysosomal ion channel but in the same lysosomal restoration thesis. CSM-101 is more advanced (IND-enabling, IND planned H1 2026) but Casma has only ~11 employees and faces resource constraints. Merck's parallel TRPML1 program from Calporta is a direct competitive threat to Casma
- [[pariceract]] (Sanofi, Phase 2b) is the most advanced lysosomal/GCase approach -- a direct allosteric GCase activator. If pariceract succeeds, it validates lysosomal restoration broadly and supports TMEM175 as a complementary or second-line target. If it fails, the entire lysosomal thesis takes a hit, though TMEM175's distinct mechanism (pH correction upstream of GCase) could still differentiate
- [[ambroxol]] (academic/repurposed, Phase 2) is a GCase chaperone with a different mechanism -- it stabilizes the enzyme for proper folding and trafficking. Complementary rather than competitive to TMEM175 activation
- The lysosomal pathway has the broadest genetic validation in PD: GBA1 (5-15% of PD), TMEM175 (>20% of PD via M393T), LRRK2 (which affects lysosomal function), and TRPML1 (loss-of-function causes mucolipidosis IV). TMEM175 activation is unique in targeting the pH environment rather than a specific enzyme
- If TMEM175 activation proves to enhance GCase activity via pH optimization, it could be combined with direct GCase activators for synergistic effect -- a potential differentiation strategy

## Analysis

The Caraway TMEM175 program represents a scientifically compelling but early-stage and opaque asset. The genetic validation is exceptionally strong: TMEM175 M393T is one of the most statistically significant GWAS hits in PD, the functional biology connecting lysosomal pH to GCase activity to alpha-synuclein clearance is well-characterized, and academic proof-of-concept with small molecule agonists has been published. The problem is that none of this has translated into disclosed clinical progress. Merck paid up to $610M for a preclinical program in November 2023, and over two years later, the program does not appear on their public pipeline. This could mean active internal development below the disclosure threshold, or it could mean the program has encountered chemistry or toxicology challenges common to ion channel targets.

**Analytical estimate -- Probability of reaching Phase 2 with positive biomarker data: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: preclinical acquisitions by big pharma reach Phase 2 roughly 20-30% of the time
- Adjustments upward: exceptionally strong genetic validation (+5%), well-characterized biology with clear biomarker path (+5%), Merck's $1.2B cumulative investment in lysosomal channels signals sustained internal conviction (+5%), oral small molecule modality is relatively low-risk from a manufacturing/delivery perspective (+3%)
- Adjustments downward: ion channel targets are notoriously difficult to drug with selectivity (-10%), no disclosed clinical candidate after 2+ years under Merck ownership (-10%), big pharma absorption often kills acquired preclinical programs (-5%), zero clinical validation of TMEM175 modulation in any disease (-5%), unclear status of AbbVie collaboration adds complexity (-3%)
- Net: ~10-15%

**Signal analysis:** Merck's behavior is the most important signal here. Their MRL Ventures Fund co-led Caraway's Series A in 2018, giving them early diligence access. They then acquired the company for $610M five years later -- this is not a blind bet but a thesis they have tracked for years. Combined with the $576M Calporta acquisition, Merck has placed a $1.2B bet that lysosomal ion channels are druggable and therapeutically relevant in neurodegeneration. This is among the largest pre-IND commitments in the PD space by any single company. However, the complete absence of public updates -- no conference presentations, no pipeline listings, no clinical candidate announcements -- is concerning. Big pharma neuroscience programs frequently get deprioritized in portfolio reviews, especially when they are early-stage and competing for resources against faster-moving oncology programs. The Keytruda patent cliff could either accelerate Merck's neuroscience timeline (need for diversified revenue) or compress it (resources redirected to more proximal opportunities). For the lysosomal pathway broadly, the key decision tree runs through [[pariceract]]: if Sanofi's GCase activator succeeds in Phase 2b, it validates the pathway and increases urgency for TMEM175 programs. If [[pariceract]] fails, Merck's TMEM175 thesis becomes harder to justify internally, though the upstream pH mechanism provides a differentiation argument.

## References

### Key Publications
- [TMEM175 deficiency impairs lysosomal and mitochondrial function and increases alpha-synuclein aggregation | PNAS (2017)](https://www.pnas.org/doi/10.1073/pnas.1616332114)
- [Functionalization of the TMEM175 p.M393T variant as a risk factor for Parkinson disease | Human Molecular Genetics (2019)](https://academic.oup.com/hmg/article/28/19/3244/5520430)
- [Structural insights into the activation of TMEM175 by small molecule | Neuron (2025)](https://www.cell.com/neuron/fulltext/S0896-6273(25)00556-2)
- [TMEM175, SCARB2 and CTSB associations with Parkinson's disease risk across populations | npj Parkinson's Disease (2025)](https://www.nature.com/articles/s41531-025-01180-z)
- [Transmembrane Protein 175, a Lysosomal Ion Channel Related to Parkinson's Disease | Biomolecules (2023)](https://www.mdpi.com/2218-273X/13/5/802)
- [Mechanism and therapeutic targets of TMEM175 in Parkinson's disease | Ageing Research Reviews (2024)](https://www.sciencedirect.com/science/article/abs/pii/S1568163724001910)
- [Parkinson's disease-risk protein TMEM175 is a proton-activated proton channel in lysosomes | Cell (2022)](https://pubmed.ncbi.nlm.nih.gov/35750034/)
- [Discovery of Selective Inhibitors for the Lysosomal PD Channel TMEM175 | JACS (2024)](https://pubs.acs.org/doi/10.1021/jacs.4c05623)

### Press Releases & Filings
- [Merck to Acquire Caraway Therapeutics, Inc. (November 2023)](https://www.merck.com/news/merck-to-acquire-caraway-therapeutics-inc/)
- [Dementia Discovery Fund Announces the Acquisition of Caraway Therapeutics by Merck | Business Wire (November 2023)](https://www.businesswire.com/news/home/20231121891813/en/Dementia-Discovery-Fund-Announces-the-Acquisition-of-Caraway-Therapeutics-by-Merck)
- [Merck seals $610M biobucks deal to acquire preclinical neurodegenerative biotech Caraway | Fierce Biotech (November 2023)](https://www.fiercebiotech.com/biotech/merck-seals-610m-biobucks-deal-acquire-preclinical-neurodegenerative-biotech-caraway)
- [Caraway Therapeutics Establishes Collaboration with AbbVie for TMEM175 Modulators | Business Wire (June 2021)](https://www.businesswire.com/news/home/20210609005050/en/Caraway-Therapeutics-Establishes-Collaboration-with-AbbVie-to-Develop-Novel-Small-Molecule-Therapeutics-for-Parkinson%E2%80%99s-Disease-and-Other-Related-Disorders)
- [AbbVie snags another preclinical Parkinson's program with $17M Caraway pact | Fierce Biotech (June 2021)](https://www.fiercebiotech.com/biotech/abbvie-snags-another-preclinical-parkinson-s-program-17m-caraway-pact)
- [Rheostat Therapeutics Announces Rebrand to Caraway Therapeutics (October 2019)](https://www.globenewswire.com/news-release/2019/10/10/1927926/0/en/Rheostat-Therapeutics-Announces-Rebrand-to-Caraway-Therapeutics-and-New-Kendall-Square-Office.html)
- [COI Pharmaceuticals Announces Acquisition of Calporta by Merck | Business Wire (November 2019)](https://www.businesswire.com/news/home/20191112005846/en/COI-Pharmaceuticals-Announces-Acquisition-of-Calporta-by-Merck)

### Regulatory & Market
- [Merck Neuroscience Research Overview](https://www.merck.com/research/neuroscience/)
- [Merck Pipeline: Clinical Trials Overview](https://www.merck.com/research/product-pipeline/)
- [TMEM175 Maintains Lysosome pH by Pushing Out Protons | Alzforum](https://www.alzforum.org/news/research-news/tmem175-maintains-lysosome-ph-pushing-out-protons)
