---
drug_name: "Mair TMEM175 Agonist"
aliases: ["Mair Therapeutics TMEM175 program"]
target: "TMEM175 (lysosomal potassium/proton channel)"
mechanism: "Small molecule agonist of the lysosomal ion channel TMEM175, restoring proton leak function to normalize lysosomal pH and enhance degradation of alpha-synuclein aggregates"
modality: "small molecule"
developer: "Mair Therapeutics"
company_type: "startup"
publicly_traded: false
partner: ""
partner_type: ""
stage: "Discovery"
status: "Active"
patient_population: "Parkinson's disease (genetically defined TMEM175 carriers initially, then broader PD)"
route_of_administration: "oral (expected)"
key_biomarkers: ["lysosomal pH", "alpha-synuclein levels", "GCase activity"]
confidence_rating: "2/10"
next_catalyst: "Preclinical candidate nomination from Radboud collaboration"
catalyst_date: "2027 (estimated)"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-16
---

# Mair TMEM175 Agonist

## Summary

Mair Therapeutics (startup, private, Netherlands) is developing small molecule TMEM175 agonists to restore lysosomal function and enhance alpha-synuclein clearance in Parkinson's disease. The company launched in February 2025 with pre-seed funding from Torrey Pines Investment and Oost NL, and announced a scientific collaboration with Radboud University in January 2026 to evaluate its compound portfolio in human neuron models. TMEM175 is one of the strongest GWAS-validated PD risk genes, and loss-of-function variants correlate with earlier onset and increased dementia risk -- providing robust genetic validation. However, the company is very early (discovery-stage, no named compounds, pre-seed funded) and faces a formidable competitor: Merck & Co. acquired Caraway Therapeutics for up to $610M in 2023, inheriting a TMEM175 agonist program with an AbbVie collaboration ($267M biobucks). If Mair generates differentiated TMEM175 agonists with superior properties in the Radboud neuron assays, the genetic validation and Merck's deal precedent create a clear partnering path. If compounds fail to show lysosomal pH normalization or alpha-synuclein reduction in human neuron models, the program lacks the financing to iterate extensively and Merck/AbbVie retain the field.

## Notes

### Science
- TMEM175 is a lysosomal proton-activated proton channel that mediates lysosomal H+ leak, maintaining optimal pH (~4.5-5.0) for hydrolase activity and protein aggregate degradation
- Loss-of-function variants (most notably p.M393T, rs34311866) impair lysosomal pH regulation, reduce GCase activity, impair autophagosome clearance, and increase alpha-synuclein aggregation -- confirmed by CRISPR knock-in and knockout studies (Jinn et al., PNAS 2017)
- GWAS signal at chromosome 4p16.3 is among the strongest PD risk loci; the TMEM175 missense SNP is 20 orders of magnitude more significant than other SNPs in the region, and functional knockdown confirmed TMEM175 as the causal gene under the peak
- Protective TMEM175 variants reduce PD susceptibility, establishing bidirectional genetic evidence -- the ideal profile for a drug target (loss-of-function = disease, gain-of-function = protection)
- Structural biology breakthrough in 2025: cryo-EM structures of human TMEM175 with three agonists (DCY1020, DCY1040, TUG-891) revealed the binding site at the subunit interface and the mechanism of channel opening, enabling rational drug design
- Mechanism is orthogonal to direct GCase activation ([[pariceract]]) -- TMEM175 agonism restores the lysosomal environment broadly, not just one enzyme. It is also orthogonal to TRPML1 agonism ([[casma-trpml1|CSM-101]]), which restores lysosomal cation efflux rather than proton leak
- Open question: whether pharmacological TMEM175 agonism can achieve sufficient CNS exposure and target engagement to replicate the protection seen in genetic gain-of-function carriers

### Clinical
No clinical trials initiated. The program is in discovery/early preclinical:
- Mair's compound portfolio is being evaluated in Dr. Marijn Kuijpers' laboratory at Radboud University's Donders Centre for Neuroscience
- Assays use human neuron models derived from PD and healthy donor cells, measuring lysosomal pH regulation and degradation capacity
- No IND-enabling studies announced; preclinical candidate nomination is likely 12-18 months away at earliest
- Academic tool compounds (DCY1020/1040, TUG-891) have demonstrated alpha-synuclein reduction and restoration of PD-associated TMEM175 variant function in neurons (published 2025), but these are not drug candidates

### Financial
- **Pre-seed funding** raised February 2025 from Torrey Pines Investment (San Diego) and Oost NL (Dutch regional development agency); amount undisclosed publicly
- Incubated through Expert Systems accelerator, which provides drug development infrastructure
- Extremely lean operation -- no disclosed headcount, two named leadership: CEO Dr. Vasily Kazey (neuroscience PhD, MBA) and VP MedChem Dr. Alexei Pushechnikov (20+ years medicinal chemistry)
- **Competitive deal benchmark:** Merck & Co. paid up to $610M for Caraway Therapeutics (2023), whose TMEM175 program was preclinical with an AbbVie collaboration worth up to $267M. This values a preclinical TMEM175 program with pharma optionality at $200-300M+, providing a ceiling valuation reference for Mair if it can reach equivalent stage
- The Radboud collaboration is likely funded through Oost NL regional innovation support and academic partnership structures rather than large venture capital

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "lysosomal") AND file.name != "mair-tmem175"
SORT stage DESC
```

- **Merck & Co. / Caraway Therapeutics** is the primary competitor with a TMEM175 agonist program acquired for up to $610M in November 2023. Caraway's program was preclinical at acquisition and was developed under an AbbVie collaboration ($17M upfront, up to $267M biobucks). Current status of the Merck TMEM175 program is undisclosed but presumably advancing through IND-enabling studies with big pharma resources
- [[casma-trpml1|CSM-101]] (Casma Therapeutics) targets a different lysosomal ion channel -- TRPML1 -- with an IND-enabling program and H1 2026 IND filing target. TRPML1 and TMEM175 are both lysosomal ion channels but serve different functions (cation efflux vs. proton leak), so they are scientifically complementary rather than directly competitive
- [[pariceract]] (BIAL) addresses the same lysosomal dysfunction thesis through direct GCase activation rather than ion channel modulation; ACTIVATE Phase 2b data mid-2026 will test whether lysosomal restoration approaches work in PD patients. A positive ACTIVATE readout would validate the broader lysosomal thesis and benefit TMEM175 programs
- [[ambroxol]] (GCase chaperone) and [[pr001|PR001]] (GBA1 gene therapy) are alternative paths to lysosomal restoration in GBA-PD. TMEM175 agonism could theoretically complement any of these by improving the lysosomal environment at the organelle level
- Mair's differentiation must come from compound quality (potency, selectivity, CNS penetration, oral bioavailability) since the target is shared with a much better-resourced Merck program

## Analysis

Mair Therapeutics sits at the intersection of strong target biology and challenging competitive dynamics. TMEM175 is among the best-validated PD targets from a genetics perspective -- the bidirectional evidence (loss-of-function = risk, gain-of-function = protection) is the gold standard for drug target validation, matched in PD only by GBA1 and LRRK2. The 2025 cryo-EM structural work resolving TMEM175-agonist complexes has transformed this from a genetically validated but structurally opaque target into one amenable to rational medicinal chemistry, creating a window for new entrants with computational chemistry capabilities.

**Analytical estimate -- probability of reaching Phase 1: 10-15%.** This is our assessment, not from a published source. The reasoning: base rate for discovery-stage programs reaching IND is roughly 10-15%. Adjustments upward: exceptional genetic validation (+5%), recent structural enablement of rational design (+5%), experienced medicinal chemistry leadership (+3%). Adjustments downward: pre-seed funding with no disclosed venture backing (-10%), competing against Merck & Co. with 2-3 year head start (-5%), no disclosed animal data or lead series (-5%). Net: 10-15%, weighted toward the lower end.

**Signal analysis:** The Merck-Caraway $610M acquisition (2023) and AbbVie's $267M option deal (2021) are the strongest signals that major pharma considers TMEM175 a high-value PD target. This validates Mair's thesis but simultaneously creates the primary obstacle -- can a pre-seed Dutch startup outcompete or differentiate against Merck & Co.'s resources? The plausible path is not to outrun Merck but to generate differentiated chemical matter (different binding site, superior selectivity, better oral CNS penetration) that becomes attractive as a second-generation program or alternative scaffold for a pharma partner seeking TMEM175 optionality. The Radboud collaboration provides access to disease-relevant human neuron assays early, which could accelerate compound triage relative to a purely biochemical screening approach.

The decision tree is straightforward: if Radboud assays demonstrate robust lysosomal pH normalization and alpha-synuclein reduction in human PD neurons, and compounds show drug-like properties (oral bioavailability, CNS penetration), Mair becomes an attractive seed/Series A investment and potential partnering candidate given the Merck deal precedent. If compounds fail in the neuron assays or cannot achieve CNS exposure, there is no path forward without significant medicinal chemistry iteration that the current funding cannot support. The [[pariceract]] ACTIVATE readout (mid-2026) is an external catalyst -- positive data would validate lysosomal restoration in PD and increase interest across the entire lysosomal target class including TMEM175.

## References

### Key Publications
- [TMEM175 deficiency impairs lysosomal and mitochondrial function and increases alpha-synuclein aggregation | PNAS (2017)](https://www.pnas.org/doi/10.1073/pnas.1616332114)
- [Functionalization of the TMEM175 p.M393T variant as a risk factor for Parkinson disease | Human Molecular Genetics (2019)](https://academic.oup.com/hmg/article/28/19/3244/5520430)
- [Parkinson's disease-risk protein TMEM175 is a proton-activated proton channel in lysosomes | Cell (2022)](https://pubmed.ncbi.nlm.nih.gov/35750034/)
- [Structural insights into the activation of TMEM175 by small molecule | Neuron (2025)](https://www.sciencedirect.com/science/article/pii/S0896627325005562)
- [TMEM175, SCARB2 and CTSB associations with Parkinson's disease risk across populations | npj Parkinson's Disease (2025)](https://www.nature.com/articles/s41531-025-01180-z)
- [What We Know About TMEM175 in Parkinson's Disease | CNS Neuroscience & Therapeutics (2025)](https://onlinelibrary.wiley.com/doi/10.1111/cns.70195)
- [Mechanism and therapeutic targets of TMEM175 in Parkinson's disease | Ageing Research Reviews (2024)](https://www.sciencedirect.com/science/article/abs/pii/S1568163724001910)

### Press Releases & Filings
- [Mair Therapeutics Secures Pre-Seed Funding and Launches (Feb 2025)](https://www.prnewswire.com/news-releases/mair-therapeutics-secures-pre-seed-funding-and-launches-to-pioneer-therapies-for-parkinsons-disease-302375687.html)
- [Mair Therapeutics Announces Scientific Collaboration with Radboud University (Jan 2026)](https://www.prnewswire.com/news-releases/mair-therapeutics-announces-scientific-collaboration-with-radboud-university-to-advance-tmem175-agonists-for-parkinsons-disease-302669941.html)
- [Merck to Acquire Caraway Therapeutics (Nov 2023)](https://www.merck.com/news/merck-to-acquire-caraway-therapeutics-inc/)
- [Caraway and AbbVie TMEM175 Collaboration](https://parkinsonsnewstoday.com/news/caraway-abbvie-partner-tmem175-modulators-parkinsons/)
- [Merck seals $610M biobucks deal to acquire Caraway | Fierce Biotech](https://www.fiercebiotech.com/biotech/merck-seals-610m-biobucks-deal-acquire-preclinical-neurodegenerative-biotech-caraway)
