---
drug_name: "NurOwn (MSC-NTF cells)"
aliases: ["MSC-NTF", "autologous MSC-NTF cells"]
target: "neurotrophic factor delivery (GDNF, BDNF)"
mechanism: "Autologous bone marrow-derived mesenchymal stem cells differentiated to secrete neurotrophic factors (GDNF, BDNF) transplanted near affected tissue"
modality: "cell therapy (autologous MSC)"
developer: "BrainStorm Cell Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "BCLI"
partner: ""
partner_type: ""
stage: "Preclinical"
status: "Inactive"
patient_population: "N/A (preclinical only for PD; clinical development only in ALS and MS)"
route_of_administration: "intrathecal (ALS); intracranial injection proposed for PD"
key_biomarkers: []
confidence_rating: "1/10"
next_catalyst: "None foreseeable for PD"
catalyst_date: "N/A"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude, zombie-company, shell-risk]
date: 2026-02-15
---

# NurOwn (MSC-NTF cells) -- BrainStorm Cell Therapeutics

## Summary

BrainStorm Cell Therapeutics (OTCQB: BCLI) is a functionally zombie biotech with $5K cash, $231K restricted cash, a $7.7M stockholders' deficit, and $9.0M in current liabilities as of September 30, 2025. The company was delisted from Nasdaq in July 2025 for failing the minimum shareholder equity requirement and now trades on OTCQB. Its NurOwn platform (autologous MSC-NTF cells) has only ever been clinically tested in ALS and MS -- the Parkinson's disease program has never advanced beyond animal models and has no IND, no clinical trial, and no disclosed development timeline. The company's entire remaining operational focus is on a planned Phase 3b ALS trial (ENDURANCE) that it cannot fund with current resources. For PD, this is a dead program at a near-dead company. No decision tree applies -- there is no foreseeable PD catalyst.

## Notes

### Science
- NurOwn is BrainStorm's proprietary process for differentiating a patient's own bone marrow-derived mesenchymal stem cells (MSCs) into neurotrophic factor-secreting cells (MSC-NTF cells)
- The differentiated cells secrete elevated levels of GDNF (glial cell line-derived neurotrophic factor), BDNF (brain-derived neurotrophic factor), and other NTFs
- Concept: MSC-NTF cells act as a living drug delivery system, providing localized, sustained neurotrophic factor release at the site of neuronal damage
- For PD specifically: preclinical proof-of-concept was demonstrated in a 6-OHDA rat model of Parkinson's disease (a standard dopaminergic lesion model), showing protective effects of NTF-secreting cells on dopaminergic neurons
- The neurotrophic factor approach to PD has a long, disappointing clinical history -- direct GDNF infusion trials (Amgen, MedGenesis) failed to show efficacy in Phase 2 despite strong preclinical data, largely due to delivery challenges and incomplete coverage of the degenerating nigrostriatal system
- BrainStorm's PD concept does not solve the fundamental delivery problem: intracranial injection of autologous cells is invasive, requires neurosurgery, and the survival/engraftment of transplanted MSCs in the brain is poorly characterized
- Unlike iPSC-derived dopaminergic neuron replacement approaches (e.g., [[abl301|bemdaneprocel]] from BlueRock), NurOwn does not replace lost neurons -- it attempts to rescue surviving neurons via trophic support, which may be insufficient in moderate-to-advanced PD where substantial neuronal loss has already occurred
- The technology is licensed exclusively from Ramot (Tel Aviv University technology transfer office)

### Clinical
No clinical trials have been initiated for NurOwn in Parkinson's disease. The PD program remains at the preclinical/animal model stage with no disclosed IND-enabling studies.

For context, BrainStorm's clinical experience with NurOwn is entirely in other indications:

**Phase 3 ALS Trial** | NCT03280056 | N=189 | ALS patients
- **Primary endpoint:** Responder analysis on ALSFRS-R slope change → Did not meet primary endpoint
- **Status:** Completed
- **Interpretation:** Failed Phase 3 led to FDA refusal; company subsequently received FDA clearance for a Phase 3b trial (ENDURANCE, NCT06973629) under Special Protocol Assessment, but has no funding to initiate it

**Phase 2 Progressive MS Trial** | NCT03799718 | Open-label multicenter
- **Status:** Completed
- **Interpretation:** No disclosed path forward in MS

### Financial
- **Market cap:** ~$6-7M (as of early 2026)
- **Cash and cash equivalents:** $5K as of September 30, 2025
- **Restricted cash:** $231K
- **Current liabilities:** $9.0M
- **Stockholders' deficit:** ($7.7M)
- **Q3 2025 net loss:** $2.1M (down from $2.7M Q3 2024 -- cost-cutting, not revenue growth)
- **YTD 2025 net loss:** $7.9M
- **R&D spend (Q3 2025):** $899K (minimal, reflecting skeleton operations)
- **G&A spend (Q3 2025):** $1.1M (exceeds R&D -- overhead-heavy)
- **Shares outstanding:** 11.03M (up from 6.14M at year-end 2024 -- significant dilution)
- **Nasdaq delisted:** July 18, 2025, for non-compliance with Listing Rule 5550(b)(1) (minimum shareholder equity)
- **Now trades on:** OTCQB under BCLI
- **Promissory note (Oct 31, 2025):** $182,400 principal ($155K net proceeds after OID and fees) from Vanquish Funding Group, at 12% interest (22% on default), maturing August 30, 2026. Convertible at 35% discount on default -- predatory micro-cap financing
- **Going concern:** Management has disclosed substantial doubt about the company's ability to continue as a going concern
- **Funding gap:** The planned Phase 3b ALS trial (ENDURANCE, ~200 patients) would cost tens of millions; company has essentially zero cash. CEO has mentioned seeking a $15M non-dilutive grant and strategic partnerships, but no concrete financing has materialized
- There is zero allocated budget for PD research

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(thesis_cluster, "cell-therapy") AND file.name != "brainstorm-nurown"
SORT stage DESC
```

- [[abl301|Bemdaneprocel (ABL-301)]] from BlueRock/Bayer is the dominant cell therapy program in PD -- iPSC-derived dopaminergic neurons in Phase 2 with $1B+ Bayer backing. This is actual neuron replacement, not trophic factor delivery
- The neurotrophic factor delivery concept for PD has been pursued and abandoned by multiple larger companies (Amgen with GDNF infusion, Pfizer/Spark with AAV-GDNF gene therapy) -- all failed or were discontinued
- BrainStorm's autologous approach (patient's own cells) has inherent scalability limitations: each treatment requires individual bone marrow harvest, cell processing, and neurosurgical delivery
- Even if the science were validated, the company lacks the financial resources to advance any program, let alone a PD program that has never reached IND stage

## Analysis

BrainStorm Cell Therapeutics represents a textbook zombie biotech: a company that has exhausted its capital, failed its lead program (Phase 3 ALS), been delisted from a major exchange, and is now surviving on predatory micro-cap financing ($182K promissory note at 12-22% interest from Vanquish Funding Group). The PD program was never more than a line item on a pipeline slide -- preclinical animal data published years ago, no IND filed, no clinical development plan, and no funding to pursue one.

**Analytical estimate -- Probability of NurOwn reaching a PD clinical trial: <1%.** This is our assessment, not from a published source. The reasoning: the company has $5K in unrestricted cash, a $7.7M stockholders' deficit, going concern doubt, no PD-specific IND, and its entire remaining operational focus is an unfunded ALS Phase 3b trial. Even if BrainStorm were to secure the $15M+ needed to run the ALS trial, PD development would remain years and tens of millions of dollars away. The neurotrophic factor delivery approach has a poor clinical track record in PD across multiple companies and modalities. The autologous cell manufacturing model is unscalable for a commercial product.

**Signal analysis:** The corporate behavior tells the full story. A company with $5K cash, a $182K predatory note, and a $7.7M deficit is not advancing a preclinical PD program. The fact that BrainStorm still lists PD on its website pipeline page is aspirational marketing, not a reflection of active development. The Nasdaq delisting, 80%+ share dilution in 2025, and going concern disclosures all point to a company in terminal decline. The only scenario where this asset matters is a reverse merger or shell acquisition where someone acquires the NurOwn IP and the Ramot license -- but even then, any acquirer would likely pursue ALS (where clinical data exists) rather than PD (where none does).

## References

### Key Publications
- [Protective effects of NTF-secreting cells in a 6-OHDA rat model of PD | BrainStorm Publications](https://brainstorm-cell.com/publications_articles/)
- [Neurotrophic Factors in Parkinson's Disease: Clinical Trials, Open Challenges | Frontiers in Cellular Neuroscience (2021)](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2021.682597/full)
- [The Future of GDNF in Parkinson's Disease | PMC (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7750181/)

### Press Releases & Filings
- [BrainStorm Expands Patent Portfolio for NurOwn in PD and ALS (Oct 2017)](https://www.prnewswire.com/news-releases/brainstorm-expands-its-patent-portfolio-to-include-a-new-us-patent-for-its-nurown-technology-for-parkinsons-disease-and-als-300541102.html)
- [BrainStorm Announces Nasdaq Delisting and Transition to OTCQB (Jul 17, 2025)](https://ir.brainstorm-cell.com/2025-07-17-BrainStorm-Cell-Therapeutics-Announces-Nasdaq-Delisting-and-Transition-to-OTCQB)
- [BrainStorm Q3 2025 Financial Results and Corporate Update (Nov 14, 2025)](https://www.prnewswire.com/news-releases/brainstorm-cell-therapeutics-announces-third-quarter-2025-financial-results-and-provides-corporate-update-302615557.html)
- [BrainStorm Receives FDA Clearance for Phase 3b ALS Trial (May 19, 2025)](https://ir.brainstorm-cell.com/2025-05-19-BrainStorm-Receives-FDA-Clearance-to-Initiate-Phase-3b-Trial-of-NurOwn-R-for-ALS)
- [BrainStorm Q2 2025 Financial Results (Aug 2025)](https://www.prnewswire.com/news-releases/brainstorm-cell-therapeutics-announces-second-quarter-2025-financial-results-and-provides-corporate-update-302530090.html)
- [BrainStorm SEC 10-Q Filing, Q3 2025](https://www.sec.gov/Archives/edgar/data/1137883/000110465925112701/bcli-20250930x10q.htm)
- [Vanquish Funding Promissory Note -- Securities Purchase Agreement (Oct 31, 2025)](https://www.stocktitan.net/sec-filings/BCLI/8-k-brainstorm-cell-therapeutics-inc-reports-material-event-2ece35a95e84.html)

### Regulatory & Market
- [BCLI Stock Overview | Stock Analysis (OTCQB)](https://stockanalysis.com/quote/otc/BCLI/)
- [NurOwn AdisInsight Drug Profile](https://adisinsight.springer.com/drugs/800022859)
- [BrainStorm Cell Therapeutics Pipeline Page](https://brainstorm-cell.com/pipeline/)
