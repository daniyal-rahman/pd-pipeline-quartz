---
drug_name: "GBA1 Gene Therapy (VYGR)"
aliases: ["VYGR-GBA1", "Voyager GBA1"]
target: "GBA1 / GCase (glucocerebrosidase)"
mechanism: "IV-administered AAV gene therapy using TRACER-derived BBB-penetrant capsid to deliver functional GBA1 gene, restoring glucocerebrosidase activity across the CNS"
modality: "AAV gene therapy"
developer: "Voyager Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "VYGR"
partner: "Neurocrine Biosciences"
partner_type: "biotech"
stage: "IND-enabling"
status: "Active"
patient_population: "PD patients with GBA1 mutations; also Gaucher disease"
route_of_administration: "IV"
key_biomarkers: ["GCase activity", "neurofilament light chain (NfL)", "glucosylsphingosine (GluSph)"]
confidence_rating: "5/10"
next_catalyst: "IND filing and Phase 1 initiation"
catalyst_date: "2026"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# GBA1 Gene Therapy (VYGR)

## Summary

Voyager Therapeutics (biotech, VYGR) is advancing an IV-administered AAV gene therapy for GBA1-associated Parkinson's disease in collaboration with Neurocrine Biosciences (biotech, NBIX), with IND filing expected in 2025-2026 and first-in-human dosing targeted for 2026. The program's core differentiator is Voyager's TRACER-derived novel capsid, which enables IV delivery with blood-brain barrier penetration and CNS-wide transduction -- a potential leap over [[pr001|PR001/LY3884961]]'s intracisternal route, which requires invasive cisterna magna injection and carries immunogenicity risk. Voyager retains a 50% US co-development/co-commercialization option exercisable after Phase 1. If preclinical-to-clinical translation confirms the IV capsid achieves therapeutic GCase levels in the substantia nigra and putamen, this becomes the strongest gene therapy candidate in GBA-PD. If IND-enabling studies reveal toxicity signals (DRG toxicity, liver sequestration, immunogenicity) or the capsid underperforms in human BBB penetration vs. NHP models, the program stalls and capital stays with oral approaches like [[pariceract]] and the more clinically advanced [[pr001|PR001]].

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Neurocrine Biosciences |
| Deal Date | January 2023 |
| Upfront | $175M ($136M cash + $39M equity at $8.88/share, 50% premium to 30-day VWAP) |
| Total (Biobucks) | Up to ~$1.7B (up to $1.5B development milestones + commercial milestones + tiered royalties) |
| Deal Type | Licensing/co-development |

## Notes

### Science
- GBA1 mutations are the most common genetic risk factor for PD, present in 5-10% of patients, conferring 5-30x increased risk depending on variant severity (N370S mild, L444P severe)
- Loss-of-function mutations reduce glucocerebrosidase (GCase) activity, causing lysosomal dysfunction, lipid accumulation (glucosylceramide/glucosylsphingosine), impaired autophagy of alpha-synuclein aggregates, and ultimately neuronal death
- The gene therapy approach delivers a functional GBA1 gene to restore GCase enzymatic activity -- mechanistically distinct from oral GCase activators ([[pariceract]]), substrate reduction ([[venglustat]], failed), and chaperone approaches ([[ambroxol]])
- **TRACER capsid platform** is the key differentiator: Voyager's proprietary RNA-based screening platform (Tropism Redirection of AAV by Cell-type-specific Expression of RNA) identified AAV capsids with 50-60x superior CNS transduction vs. conventional AAV9 in mice and NHPs following IV administration
- Novel capsids demonstrate preferential transduction of glial cells with significant detargeting from liver and dorsal root ganglia (DRG) -- addressing the two main AAV toxicity concerns
- IV delivery enables whole-brain GCase restoration without the invasive intracisternal injection required by [[pr001|PR001]], which is critical for a progressive disease requiring widespread enzyme distribution
- In a GBA1 loss-of-function mouse model, single IV doses using the BBB-penetrant capsid restored therapeutically relevant GCase levels, reduced NfL (neurodegeneration marker), and improved motor function
- In NHP studies, TRACER capsids showed substantially improved biodistribution and gene expression in the putamen and substantia nigra (the two brain regions most affected in PD) compared to conventional AAV9
- Open scientific questions: (1) will NHP-to-human capsid translation hold for BBB penetration? (2) will a single IV dose achieve durable GCase restoration over years? (3) immunogenicity of novel capsid in humans unknown; (4) pre-existing anti-AAV antibodies may exclude a significant patient fraction

### Clinical
No clinical trials initiated. Program is in IND-enabling studies (GLP toxicology).

- **Development candidate selected** April 2024, triggering a milestone payment to Voyager
- **GLP toxicology studies** ongoing as of Q3 2025
- **IND filing** expected from Neurocrine in 2025-2026; timeline dependent on GLP tox outcomes, FDA acceptance, and Neurocrine's internal strategic assessment
- **Phase 1 trial initiation** targeted for 2026; Neurocrine funds development through completion of first Phase 1
- After Phase 1, Voyager may elect to co-develop and co-commercialize under a 50/50 cost/profit-sharing arrangement in the US
- Dual indication strategy: GBA1-PD and Gaucher disease (separate IND expected)

### Financial
- **Upfront received:** $175M in January 2023 ($136M cash, $39M equity)
- **Milestones earned to date:** Development candidate selection milestone (April 2024); third candidate selection milestone (September 2024); up to $35M in milestones expected in 2025-2026 from IND filings
- **Remaining milestones:** Up to $1.5B in development milestones + uncapped commercial milestones + tiered royalties on net sales
- **Voyager market cap:** ~$205M (as of early 2026); stock at ~$3.68, down significantly from 52-week high of $7.44
- **Analyst coverage:** H.C. Wainwright Buy (PT $25), Wells Fargo, Canaccord Genuity, and Wedbush all maintain Buy ratings -- significant gap between current price and analyst targets reflects market skepticism about timeline and execution
- **Voyager cash runway:** Extended to 2027 based on Q1 2025 reporting, bolstered by Neurocrine program funding and capsid licensing deals (Pfizer, Novartis, others)
- **Deal comparison:** The $175M upfront (10.3% of total biobucks) is a moderately high conviction signal for a preclinical program; comparable to Novartis/Alnylam's early-stage alpha-syn deal structure. The 50% US co-commercialization option is unusual and favorable to Voyager
- **Neurocrine returned 2 of 4 programs** (two undisclosed discovery-stage targets) in May 2025 but retained the GBA1 and Friedreich's ataxia programs, signaling selective conviction rather than broad retreat

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "GBA1") AND file.name != "gba1-voyager"
SORT stage DESC
```

- **Route of administration is the key differentiator**: IV (Voyager) vs. intracisternal ([[pr001|PR001/LY3884961]]) vs. oral ([[pariceract]]). IV delivery avoids the procedural risk and patient burden of cisterna magna injection while achieving broader CNS distribution than intracisternal approaches
- [[pr001|PR001]] (Lilly/Prevail) is the most clinically advanced GBA1 gene therapy (Phase 1/2, PROPEL trial), but uses conventional AAV9 via intracisternal injection -- an invasive route that required aggressive immunosuppression after a serious adverse event in the first patient
- [[pariceract]] (BIAL) is the main non-gene-therapy competitor -- oral GCase activator in Phase 2b (ACTIVATE, N=273, topline data mid-2026). If ACTIVATE succeeds, it validates a cheaper, less risky oral approach and pressures gene therapy valuations; if it fails, gene therapy becomes the primary path for GBA-PD
- **Spur Therapeutics (SPR301)** is a direct gene therapy competitor using AAV with an engineered GCase variant (GCase85) claimed to have order-of-magnitude higher enzymatic activity vs. wildtype -- currently preclinical
- [[cap-003|Capsida CAP-003]] is another IV AAV gene therapy approach using Capsida's proprietary capsid (LUNG and BRAIN platforms), also in preclinical/IND-enabling stage
- If [[pariceract]] ACTIVATE trial fails in mid-2026, gene therapy approaches including this program gain significant strategic importance as the remaining viable path for GBA-PD disease modification
- The competitive timeline matters: Voyager's Phase 1 would start ~2026, while PR001's PROPEL 5-year data reads out in 2029 and exPDite-2 Phase 3 launches 2025 -- Lilly has a multi-year clinical head start

## Analysis

The Voyager/Neurocrine GBA1 program is a bet on next-generation capsid technology solving the delivery problem that has historically limited CNS gene therapy. The TRACER platform's 50-60x improvement over AAV9 in preclinical models is impressive, but the NHP-to-human translation gap for BBB-penetrant capsids remains the single biggest technical risk. Multiple companies (including Capsida, Passage Bio, and others) have shown promising NHP data for novel capsids that have not yet been validated in humans.

**Analytical estimate -- probability of reaching Phase 2 with positive data: 15-20%.** This is our assessment, not from a published source. The reasoning:
- Base rate: gene therapy IND-to-Phase-2 success in CNS ~30-35%
- Adjustments upward: strong genetic validation for GBA1 target (+5%), novel capsid with superior preclinical biodistribution (+5%), IV route avoids intracisternal risk (+5%), well-funded partnership with Neurocrine (+3%)
- Adjustments downward: NHP-to-human capsid translation risk (-15%), no human data for this specific capsid (-10%), pre-existing AAV antibody exclusion may limit eligible patients (-5%), Neurocrine already returned 2 of 4 collaboration programs (-3%)
- Net: ~15-20%

**Signal analysis:**
- Neurocrine's decision to retain the GBA1 program while returning two other collaboration programs is a meaningful positive signal. It suggests their preclinical data review for GBA1 specifically passed their internal bar, rather than broad enthusiasm for the TRACER platform waning.
- Voyager's market cap (~$205M) against up to $1.7B in biobucks and multiple capsid licensing deals (Pfizer, Novartis) implies the market assigns low probability to clinical success but values the platform optionality. The $175M upfront alone nearly matches the current market cap, suggesting the market views remaining milestones as unlikely.
- The 50% US co-commercialization option after Phase 1 is a critical strategic lever. If Phase 1 data is strong, Voyager can elect into a 50/50 structure on what could be a multi-billion-dollar franchise in GBA-PD. If Phase 1 disappoints, they can decline and collect milestones/royalties from Neurocrine -- an asymmetric structure.
- The decision tree: if Phase 1 demonstrates safe IV delivery with GCase restoration in human CNS, this becomes the most attractive gene therapy candidate in PD and Voyager likely exercises the co-commercialization option. If it fails on delivery (inadequate BBB penetration) or safety (DRG toxicity, hepatotoxicity, immunogenicity), the program stalls and [[pr001|PR001]]'s intracisternal route becomes the gene therapy standard despite its procedural burden. Either way, the oral [[pariceract]] ACTIVATE readout in mid-2026 will reshape the competitive landscape before Voyager's Phase 1 generates meaningful data.

## References

### Key Publications
- [Gene Therapy for Parkinson's Disease Associated with GBA1 Mutations | PMC (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8543272/)
- [Clinical, mechanistic, biomarker, and therapeutic advances in GBA1-associated Parkinson's disease | Transl Neurodegen (2024)](https://translationalneurodegeneration.biomedcentral.com/articles/10.1186/s40035-024-00437-6)
- [Glucocerebrosidase and its relevance to Parkinson disease | Mol Neurodegen (2019)](https://link.springer.com/article/10.1186/s13024-019-0336-2)
- [Investigational Gene Therapies for Parkinson's Disease | CNS Drugs (2025)](https://link.springer.com/article/10.1007/s40263-025-01203-6)

### Press Releases & Filings
- [Neurocrine Biosciences and Voyager Therapeutics Enter Strategic Collaboration (January 2023)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/neurocrine-biosciences-and-voyager-therapeutics-enter-strategic/)
- [Voyager Announces Selection of Development Candidate for GBA1 Program (April 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-announces-selection-development-candidate-0/)
- [Voyager Advances Collaboration with Neurocrine; Third Gene Therapy Development Candidate Selected (September 2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-advances-collaboration-neurocrine-third-gene-therapy/)
- [Voyager Reports Third Quarter 2025 Financial and Operating Results](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-reports-third-quarter-2025-financial-and-operating)
- [Neurocrine Hands Back 2 CNS Gene Therapy Programs to Voyager (May 2025)](https://www.fiercebiotech.com/biotech/neurocrine-hands-back-2-cns-gene-therapy-programs-voyager)
- [Voyager TRACER Capsids Demonstrate Enhanced CNS Transduction (May 2022)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-tracertm-capsids-demonstrate-enhanced-cns/)
- [Voyager Presents Data for Second-Generation TRACER Capsids at ASGCT 27th Annual Meeting (2024)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-presents-data-second-generation-tracertm/)

### Regulatory & Market
- [Spur Therapeutics Presents Positive Preclinical Data on GBA1 PD Gene Therapy (2025)](https://www.biospace.com/press-releases/spur-therapeutics-presents-positive-new-preclinical-data-on-its-gene-therapy-candidate-for-gba1-parkinsons-disease-at-2025-gba1-meeting)
- [Previewing Parkinson Disease Pipeline: Emerging Trials to Watch in 2026 | NeurologyLive](https://www.neurologylive.com/view/previewing-parkinson-disease-pipeline-emerging-trials-to-watch-in-2026)
- [The Evolving Landscape of Gene and Cell Therapies in Parkinson Disease | CGTlive](https://www.cgtlive.com/view/evolving-landscape-gene-cell-therapies-parkinson-disease)
