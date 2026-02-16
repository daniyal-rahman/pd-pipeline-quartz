---
drug_name: "Autologous mDAPs (NRI/McLean)"
aliases: ["mDAPs", "NRI autologous iPSC-DA", "NCT06422208"]
target: "dopaminergic neuron replacement (autologous iPSC-derived DA progenitors)"
mechanism: "Patient blood-derived iPSCs differentiated into midbrain dopaminergic progenitors (mDAPs), transplanted bilaterally into putamen to replace lost DA neurons without immunosuppression"
modality: "cell therapy (iPSC autologous)"
developer: "McLean Hospital / Neuroregeneration Research Institute (NRI)"
company_type: "academic"
publicly_traded: false
partner: "Oryon Cell Therapies"
partner_type: "biotech"
stage: "Phase 1"
status: "Active"
patient_population: "PD ages 55-80, disease duration >=5 years, levodopa-responsive"
route_of_administration: "intracranial (bilateral stereotactic injection into putamen)"
key_biomarkers: ["18F-DOPA PET (graft survival)", "MDS-UPDRS Part III", "ON/OFF time diary"]
confidence_rating: "4/10"
next_catalyst: "Phase 1 12-month safety/feasibility readout"
catalyst_date: "H2 2025 - H1 2026"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Autologous mDAPs (NRI/McLean)

## Summary

The first-in-human autologous iPSC-derived dopamine neuron transplant for PD, pioneered at McLean Hospital's Neuroregeneration Research Institute (NRI) (academic) with surgical implantation at Brigham and Women's Hospital. A single-patient proof-of-concept (Schweitzer et al., NEJM 2020) demonstrated graft survival on 18F-DOPA PET and stabilization/improvement in MDS-UPDRS Part III at 24 months without immunosuppression. A formal Phase 1 trial (NCT06422208, N=6) received FDA IND clearance in August 2023, dosed its first patient September 2024, and has treated 3 of 6 patients as of March 2025. Oryon Cell Therapies (biotech, founded by Ole Isacson) holds the commercial license and has raised $11.7M with Takeda Ventures backing. If Phase 1 confirms safety and signals efficacy, a Phase 2a expansion follows; if manufacturing variability proves unmanageable (one of four preclinical patient lines failed efficacy in the Cell Stem Cell 2025 study), the autologous paradigm weakens further relative to allogeneic approaches like [[bemdaneprocel]] and [[kyoto-ipsc|Kyoto iPSC-DA]].

## Notes

### Science
- Patient blood cells are reprogrammed into iPSCs via episomal reprogramming, then differentiated into midbrain dopaminergic progenitors (mDAPs) using a refined 21-day dual-SMAD inhibition protocol under GMP conditions
- Cells are characterized as having phenotypic properties of substantia nigra pars compacta (A9-type) dopaminergic neurons — the specific subtype lost in PD
- Key autologous advantage: transplanted cells are immunologically self, eliminating the need for immunosuppressive drugs entirely. Neither immunosuppressants, glucocorticoids, nor anticonvulsants were used at any point in the original case or the Phase 1 trial
- Preclinical NHP data (Hallett, Cell Stem Cell 2015) showed autologous iPSC-derived DA neurons survived and functioned in MPTP-lesioned cynomolgus monkeys, providing proof-of-concept for the approach
- The 2025 Cell Stem Cell preclinical study (Kim, Isacson et al.) tested clinical-grade iPSC lines from four sporadic PD patients — mDAPs from all four met safety criteria in a 39-week GLP-compliant mouse study, but mDAPs from one patient failed to improve behavioral outcomes in rodent models
- Critical finding: in vitro quality assessments did not reliably predict in vivo efficacy; dopaminergic fiber density was identified as the key efficacy predictor — this has major implications for patient-to-patient variability and lot release criteria
- Original iPSC derivation used skin fibroblasts (NEJM 2020 case); the Phase 1 trial switched to blood-derived iPSCs, which is less invasive and more standardized
- Open question: inter-individual variability in iPSC line quality and mDAP differentiation efficiency may make consistent manufacturing across patients fundamentally challenging at scale

### Clinical

**Schweitzer Single-Patient Case (First-in-Human)** | No NCT | N=1 | 69-year-old man, 10-year PD history
- **Primary endpoint:** Safety/feasibility → No serious adverse events; no graft-induced dyskinesia
- **Key secondary:** MDS-UPDRS Part III off-dopamine improved from 43 (4 weeks post-implant) to 33 (24 months). On-dopamine improved from 38 to 29. Off-time decreased from 3 hrs/day to 1 hr/day at 24 months
- **Imaging:** 18F-DOPA PET suggested graft survival at 24 months (left side) and 18 months (right side)
- **Procedure:** Left putamen implantation followed by right putamen 6 months later; no immunosuppression at any point
- **Status:** Completed (published NEJM May 2020)
- **Interpretation:** Landmark proof-of-concept that autologous iPSC-derived DA neurons can survive in human brain and are associated with clinical stabilization. N=1 prevents any efficacy conclusions, but the absence of immunogenicity and graft-induced dyskinesia is notable. The patient was on complex polypharmacy (carbidopa/levodopa ER, rotigotine, rasagiline), making attribution of clinical improvement difficult.

**NRI Phase 1 Trial** | NCT06422208 | N=6 | PD ages 55-80, disease >=5 years, levodopa-responsive
- **Primary endpoint:** Safety — adverse event monitoring at 12 and 18 months post-surgery
- **Key secondary:** MDS-UPDRS Parts II and III, dyskinesia assessment, cognitive function, ON/OFF time diary
- **Design:** Open-label, single-arm, conducted at Brigham and Women's Hospital
- **Procedure:** Blood-derived autologous iPSC-mDAPs transplanted into putamen in single surgical session; no immunosuppression
- **PI:** John Rolston, MD, PhD (Neurosurgery); Michael Hayes, MD (Neurology)
- **Funding:** NINDS CREATE Bio grant (U01NS109463), awarded 2020
- **FDA IND:** Cleared August 23, 2023
- **Status:** Active — first patient dosed September 9, 2024; 3 of 6 patients treated as of March 2025; seeking 3 additional participants
- **Interpretation:** A safety/feasibility study only. The N=6 design provides no statistical power for efficacy but will inform whether the manufacturing process can reliably produce transplant-quality mDAPs across multiple patients — the key question raised by the Cell Stem Cell 2025 preclinical data showing 1-of-4 patient lines failed.

### Financial
- **Funding model:** Academic grant-funded, not venture-backed at the research level. The NINDS CREATE Bio grant (U01NS109463) funds the Phase 1 trial
- **Oryon Cell Therapies** holds the commercial license to the NRI technology. Total raised: $11.7M. Key investor: Takeda Ventures
- **Scale comparison:** Oryon's $11.7M contrasts sharply with competitor [[anpd001|Aspen Neuroscience's]] $115M Series C (2025, with Kite/Gilead) and [[bemdaneprocel|BlueRock's]] $1B acquisition by Bayer — the NRI/Oryon program is dramatically under-capitalized relative to the competitive field
- **Fundamental COGS challenge:** Autologous cell therapy requires manufacturing a unique GMP product for every patient — estimated weeks to months per manufacturing run, with individual lot release testing and QC. No published cost estimates exist for autologous mDAP production, but analogous autologous CAR-T therapies (Kymriah, Yescarta) cost $373K-$475K per patient at COGS of ~$100K+. Autologous mDAPs requiring iPSC derivation + differentiation + characterization could exceed these costs
- **Market context:** If autologous approaches prove viable but expensive, the addressable population narrows to patients who cannot tolerate immunosuppression or who fail allogeneic therapies

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "dopaminergic neuron replacement") AND file.name != "autologous-mdaps"
SORT stage DESC
```

- [[bemdaneprocel]] (BlueRock/Bayer) is the clear front-runner: allogeneic ESC-derived, Phase 3 (exPDite-2, N~102), FDA RMAT + Fast Track, first patient dosed September 2025. Off-the-shelf manufacturing scales inherently better than autologous
- [[anpd001|ANPD001]] (Aspen Neuroscience) is the direct competitor — also autologous iPSC-derived, but significantly better capitalized ($115M Series C), further in clinical development (ASPIRO Phase 1/2a, 3 cohorts dosed, 6-month data showing 45% MDS-UPDRS Part III improvement), and developing automated manufacturing for commercial scale
- [[kyoto-ipsc|Kyoto iPSC-DA]] (CiRA/Sumitomo) takes the allogeneic iPSC route — N=7 Phase I/II published in Nature, underpinning [[raguneprocel]] NDA in Japan. If approved, this validates iPSC-derived DA neurons as a class but does not specifically validate the autologous approach
- [[stem-pd|STEM-PD]] (Novo Nordisk/Lund) is another ESC-based allogeneic approach in Phase 1 (first patient dosed 2023)
- The NRI/Oryon program's academic origin and limited funding position it as a scientific proof-of-concept rather than a commercial program — the question is whether Oryon or a partner can translate the science into a scalable therapeutic
- If [[bemdaneprocel]] Phase 3 succeeds, the commercial case for autologous approaches narrows to patients who cannot tolerate immunosuppression — a small but real population
- If allogeneic approaches encounter immune rejection problems long-term, the autologous paradigm gains significant strategic value

## Analysis

The NRI/McLean autologous mDAP program holds a singular place in the cell therapy field: it produced the first-ever published case of a PD patient receiving their own iPSC-derived dopaminergic neurons (Schweitzer et al., NEJM 2020). That case remains one of the most compelling proof-of-concept demonstrations in regenerative neurology — graft survival confirmed on PET, clinical stabilization without any immunosuppression, and no safety signals over 24 months. But single-patient anecdotes do not make therapies, and the program's transition from landmark science to clinical development has been slow relative to competitors.

**Analytical estimate — Phase 1 success probability (safety): 70-75%; probability of meaningful efficacy signal: 20-30%.** This is our assessment, not from a published source. The reasoning: Base rate for Phase 1 cell therapy safety in PD is high (~80-90%) given the N=1 precedent and clean NHP data. Adjustment downward for manufacturing variability (1-of-4 preclinical lines failed efficacy, -10-15%). For efficacy, the N=6 open-label design with no comparator limits interpretability even if improvements are observed — placebo/surgical placebo effects in PD are substantial (+15-20% UPDRS improvement common in sham arms).

**Signal analysis:** The program's core vulnerability is not scientific — the biology is sound and the NEJM case was remarkable. The vulnerability is commercial. Oryon Cell Therapies has raised only $11.7M, compared to Aspen Neuroscience's $280M+ total and BlueRock's Bayer backing. Manufacturing autologous cell therapies at scale remains an unsolved problem industry-wide. The Cell Stem Cell 2025 preclinical data showing inter-patient variability in efficacy (1-of-4 lines failed) directly challenges the reliability assumption that every patient's cells will produce a functional product. If the Phase 1 trial confirms this variability in the clinical setting, it undermines the autologous thesis broadly — affecting [[anpd001|ANPD001]] as well, not just this program.

The strategic value of the NRI program may ultimately be as a scientific platform rather than a standalone therapeutic franchise. If Oryon can attract a pharma partner (Takeda Ventures' involvement is a signal), the technology could be combined with gene correction approaches — for example, autologous iPSCs from LRRK2 or GBA1 mutation carriers could be gene-corrected before differentiation, creating a personalized disease-modifying cell therapy that allogeneic approaches cannot replicate. This intersection of autologous cell therapy with [[biib122|LRRK2]] and [[pariceract|GBA1]] genetic PD represents the most compelling long-term thesis for the platform.

## References

### Clinical Trials
- [NRI Phase 1 Trial](https://clinicaltrials.gov/study/NCT06422208) — NCT06422208

### Key Publications
- [Personalized iPSC-Derived Dopamine Progenitor Cells for Parkinson's Disease | NEJM (May 2020)](https://www.nejm.org/doi/full/10.1056/NEJMoa1915872)
- [Human autologous iPSC-derived dopaminergic progenitors restore motor function in PD models | JCI (Nov 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6994130/)
- [Pre-clinical safety and efficacy of human iPSC-derived products for autologous cell therapy in PD | Cell Stem Cell (Mar 2025)](https://www.cell.com/cell-stem-cell/abstract/S1934-5909(25)00006-2)
- [Successful function of autologous iPSC-derived dopamine neurons in NHP PD model | Cell Stem Cell (2015)](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(15)00056-9)
- [Optimizing maturity and dose of iPSC-derived dopamine progenitor cell therapy for PD | npj Regen Med (2022)](https://www.nature.com/articles/s41536-022-00221-y)

### Press Releases & Filings
- [Clinical Trial Tests Novel Stem-Cell Treatment for Parkinson's Disease | Mass General Brigham (Mar 2025)](https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/clinical-trial-novel-stem-cell-treatment-for-parkinsons)
- [Phase 1 trial of stem cell therapy seeking three more Parkinson's patients | Parkinson's News Today](https://parkinsonsnewstoday.com/news/phase-1-trial-stem-cell-therapy-seeking-three-parkinsons-patients/)
- [Clinical trial tests novel stem-cell treatment for Parkinson's disease | ScienceDaily (Mar 2025)](https://www.sciencedaily.com/releases/2025/03/250309203153.htm)
