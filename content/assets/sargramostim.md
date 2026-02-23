---
drug_name: "Sargramostim"
aliases: ["Leukine", "rhuGM-CSF", "GM-CSF"]
target: "neuroinflammation / immune modulation (Treg-mediated neuroprotection)"
mechanism: "Recombinant human GM-CSF that induces tolerogenic dendritic cells and expands regulatory T cells (Tregs), shifting the peripheral and CNS immune milieu from pro-inflammatory to neuroprotective"
modality: "recombinant protein (cytokine)"
developer: "University of Nebraska Medical Center (Howard Gendelman)"
company_type: "academic"
publicly_traded: false
partner: "Partner Therapeutics"
partner_type: "biotech"
stage: "Phase 1b"
status: "Active"
patient_population: "Parkinson's disease (mild-to-moderate, on stable therapy)"
route_of_administration: "SC (daily injection, 5 days on / 2 days off)"
key_biomarkers: ["CD4+CD25+FoxP3+ Treg count/function", "MDS-UPDRS Part III", "MEG cortical motor activity"]
confidence_rating: "3/10"
next_catalyst: "IND submission for Phase 2 multi-site RCT"
catalyst_date: "TBD (announced intent, no registered trial as of Feb 2026)"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline]
date: 2026-02-16
company_link: "[[companies/university-nebraska-medical-center]]"
partner_link: "[[companies/partner-therapeutics]]"
---

# Sargramostim (Leukine)

## Summary

Sargramostim (Leukine) is a recombinant human granulocyte-macrophage colony-stimulating factor (rhuGM-CSF), FDA-approved since 1991 for hematopoietic reconstitution, now being repurposed for PD as a Treg-mediated neuroprotective immunomodulator. Two small academic trials at UNMC (Dr. Howard Gendelman) have shown safety, Treg expansion, and suggestive motor stabilization (MDS-UPDRS Part III improvement of ~4 points vs. expected 2.4-point decline) in a combined total of fewer than 30 PD patients. Partner Therapeutics (biotech, private), which acquired Leukine from Sanofi in 2018, has announced intent to file an IND and initiate a Phase 2 randomized, placebo-controlled, multi-site trial -- but no NCT registration has appeared as of February 2026. If a well-powered Phase 2 confirms motor benefit and Treg-mediated biomarker changes, sargramostim would become the first immune-modulation therapy to show disease modification in PD, validating a peripheral-to-central neuroprotection axis distinct from [[exenatide|GLP-1 agonists]], [[dapansutrile|NLRP3 inhibitors]], and [[snk01|NK cell therapies]]. If the Phase 2 fails or never initiates, the Treg-neuroprotection hypothesis in PD remains preclinically interesting but clinically unproven, and attention shifts to next-generation long-acting GM-CSF constructs (PDM608, MJFF-funded) or other immune modulation approaches.

## Notes

### Science
- **Mechanism:** Subcutaneous GM-CSF stimulates bone marrow myeloid progenitors to produce anti-inflammatory monocytes, granulocytes, and tolerogenic dendritic cells. These tolerogenic DCs induce expansion of CD4+CD25+FoxP3+ regulatory T cells (Tregs) with elevated CTLA-4, ITGB7, CD45RO, and CD31 -- markers of stable immunosuppressive phenotype with enhanced migratory function
- **CNS pathway:** Peripherally induced Tregs infiltrate neuroinflammatory sites in the brain, polarizing resident microglia toward an anti-inflammatory phenotype with enhanced phagocytosis and autophagy. This leads to increased alpha-synuclein clearance, reduced Lewy body formation, and restored neural homeostasis
- **Preclinical validation:** In MPTP mouse models, GM-CSF treatment produced dose-dependent neuroprotection -- 21-36% increases in surviving dopaminergic neurons in the substantia nigra, with corresponding Treg expansion >2-fold and reduced microgliosis
- **GM-CSF mRNA approach:** Lipid nanoparticle-delivered GM-CSF mRNA also showed dose-dependent Treg induction and dopaminergic neuron protection in MPTP mice and alpha-synuclein-overexpressing rats, suggesting the mechanism is robust across delivery modalities
- **Autophagy link:** Transcriptomic and proteomic profiling of circulating monocytes post-sargramostim showed upregulation of autophagy-related genes -- relevant because dysfunctional autophagy is implicated in alpha-synuclein accumulation in PD
- **Key distinction from other neuroinflammation approaches:** [[dapansutrile|NLRP3 inhibitors]] and [[bhv-8000|TYK2/JAK1 inhibitors]] suppress specific inflammatory signaling nodes; sargramostim aims to restore global immune homeostasis by expanding the Treg compartment. This is a fundamentally different strategy -- immune modulation vs. immune suppression
- **Repurposed drug advantage:** Sargramostim has decades of safety data across oncology, radiation injury, and sepsis indications. The PD dose (3 mcg/kg/day) is lower than standard hematologic dosing, which de-risks the safety profile
- **Open question:** Whether peripheral Treg expansion translates to meaningful CNS immunomodulation at pharmacologically relevant levels remains debated. The BBB limits T cell trafficking, though neuroinflammatory conditions increase permeability

### Clinical

**Phase 1 (Randomized, Double-Blind, Placebo-Controlled)** | NCT01882010 | N=20 PD + 17 controls | Mild-to-moderate PD
- **Primary endpoint:** Safety/adverse events -> Adverse events were mild: injection-site reactions, elevated WBC, bone pain (all known GM-CSF effects)
- **Key secondary:** MDS-UPDRS Part III showed modest 3-point improvement in sargramostim group at weeks 6-8 vs. placebo; improved MEG-recorded cortical motor activity; increased Treg numbers and function
- **Dose:** 6 mcg/kg/day SC for 56 days
- **Status:** Completed (published 2017, npj Parkinson's Disease)
- **Interpretation:** Proof-of-concept for safety and immunomodulatory activity. Motor signal was small and reversed after treatment discontinuation, consistent with pharmacological effect rather than sustained disease modification. Dose was associated with more adverse events than later studies at lower doses.

**Pilot Open-Label Extension** | NCT03790670 | N=5 (of 10 enrolled; 7 completed) | PD patients from Phase 1 cohort
- **Primary endpoint:** MDS-UPDRS Part III at 12 months -> 4 of 5 patients improved; average 4-point improvement vs. expected 2.4-point decline on standard therapy
- **Dose optimization:** 3 mcg/kg/day (reduced from 6 mcg/kg) significantly reduced adverse events while sustaining Treg expansion
- **Duration:** 24 months on drug, 3-month washout, then 6 additional months (33 months total observation)
- **Key finding:** Long-term treatment at reduced dose was well-tolerated with sustained Treg increases displaying immunosuppressive phenotype (elevated FoxP3, CTLA-4). Clinical stability maintained over 2+ years
- **Status:** Completed (12-month data published 2021, EBioMedicine/Lancet; 33-month data published 2023, Translational Neurodegeneration)
- **Interpretation:** Safety and tolerability affirmed at optimized dose with sustained immune biomarker changes. However, N=5 is too small to draw efficacy conclusions, the study was open-label (no placebo control), and 7/10 completion is a 30% dropout rate. The data is hypothesis-generating, not confirmatory.

**Phase 2 (Planned)** | NCT TBD | N=TBD | Multi-site, randomized, double-blind, placebo-controlled
- **Status:** Announced by Partner Therapeutics (2021 press release); IND submission planned but no ClinicalTrials.gov registration as of February 2026
- **Interpretation:** The ~5-year gap between announcement and lack of trial registration is a significant concern. Possible explanations include Partner Therapeutics prioritizing other indications (BARDA-funded sepsis Phase 2, January 2025), funding constraints for a PD-specific trial, or regulatory hurdles for the PD IND. The absence of the Phase 2 is the single biggest risk factor for this asset.

### Financial
- **Partner Therapeutics:** Private company (Lexington, MA); raised $60M Series A in 2018 (led by Perceptive Advisors, with Adams Street Partners and MidCap Financial) to acquire Leukine from Sanofi
- **Revenue base:** Leukine is commercially available for hematopoietic reconstitution and acute radiation syndrome (FDA-approved 2018 for H-ARS). Revenue figures are not publicly disclosed as PTx is private
- **Government funding:** $35M DOD contract (2020) for COVID-19 respiratory study; BARDA partnership (January 2025) funding Phase 2 sepsis study -- government funding supports the Leukine franchise broadly but has not been earmarked for PD
- **Academic funding:** PD trials funded by NIH grants R01-NS034139 and R01-NS070190 (to Gendelman lab), plus community support. Michael J. Fox Foundation funded PDM608 (long-acting GM-CSF) preclinical development
- **Cost structure for PD:** As a repurposed, already-manufactured drug, the PD development cost is primarily clinical trial execution, not manufacturing scale-up. A multi-site Phase 2 would likely cost $15-30M depending on enrollment
- **No PD-specific deal:** There is no licensing or partnership deal specifically for PD. Partner Therapeutics owns Leukine globally across all indications; the PD work is investigator-initiated with PTx providing drug supply and press release support
- **Japan approval:** EMA CHMP recommended approval of sargramostim (branded IMREPLYS) in June 2025; separately received approval in Japan for autoimmune pulmonary alveolar proteinosis -- broadening the commercial franchise but not PD-specific

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[vent-02]] | Terminated | Terminated | Ventus Therapeutics | small molecule |
| [[adp065-abc]] | Preclinical | Active | Alector | siRNA |
| [[lbp-pd01]] | Preclinical | Active | LISCure Biosciences | live biotherapeutic product |
| [[muna-kv13]] | Preclinical | Active | MUNA Therapeutics | small molecule |
| [[neumora-nlrp3]] | Preclinical | Active | Neumora Therapeutics | small molecule |
| [[rome-line1]] | Preclinical | Active | ROME Therapeutics | small molecule |
| [[lys-therapeutics]] | IND-enabling | Active | Lys Therapeutics | monoclonal antibody |
| [[nly02]] | IND-enabling | Active | Neuraly (D&D Pharmatech) / 1ST Bio | small molecule |
| [[hl192]] | Phase 1 | Active | NurrOn Pharmaceuticals | small molecule |
| [[ism8969]] | Phase 1 | Active | Insilico Medicine | small molecule |
| [[lbt-3627]] | Phase 1 | Active | Longevity Biotech | peptide |
| [[nm-101]] | Phase 1 | Active | Neuramedy | monoclonal antibody |
| [[nt-0150]] | Phase 1 | Active | NodThera | small molecule |
| [[her-096]] | Phase 1b | Active | Herantis Pharma | peptide |
| [[nt-0796]] | Phase 1b | Active | NodThera | small molecule |
| [[sargramostim]] | Phase 1b | Active | University of Nebraska Medical Center (Howard Gendelman) | recombinant protein (cytokine) |
| [[selnoflast]] | Phase 1b | Active | Roche | small molecule |
| [[snk01]] | Phase 1/2 | Active | NKGen Biotech | cell therapy (autologous NK) |
| [[dapansutrile]] | Phase 2 | Active | Olatec Therapeutics | small molecule |
| [[liraglutide]] | Phase 2 | Active | Academic (Cedars-Sinai / Cure Parkinson's) | small molecule |
| [[lixisenatide]] | Phase 2 | Active | Toulouse University Hospital (academic) | small molecule |
| [[nly01]] | Phase 2 | Active | Neuraly (D&D Pharmatech) | small molecule |
| [[pt320]] | Phase 2 | Failed | Peptron | small molecule |
| [[semaglutide]] | Phase 2 | Active | Novo Nordisk / Osaka University | small molecule |
| [[vtx3232]] | Phase 2 | Active | Ventyx Biosciences | small molecule |
| [[bhv-8000]] | Phase 2/3 | Active | Biohaven | small molecule |
| [[ejs-act-pd]] | Phase 3 | Active | UCL / MRC Clinical Trials Unit | platform |
| [[exenatide]] | Phase 3 | Failed | UCL (Tom Foltynie) | small molecule |

- Sargramostim is unique in the neuroinflammation cluster for targeting **adaptive immune modulation via Treg expansion** rather than suppressing specific innate immune pathways. [[dapansutrile]], [[nt-0796]], [[selnoflast]], [[vtx3232]], and [[ism8969]] all target NLRP3 inflammasome (small molecules); [[bhv-8000]] targets TYK2/JAK1; [[nm-101]] targets TLR2 -- all are innate immune suppression strategies
- The GLP-1 agonist cluster ([[exenatide]], [[lixisenatide]], [[semaglutide]], [[nly01]]) has anti-neuroinflammatory effects as a secondary mechanism but primarily works through neuroprotective/metabolic signaling. [[exenatide]] failed Phase 3 definitively. [[lixisenatide]] showed a positive Phase 2 signal (LIXIPARK)
- [[snk01|Troculeucel (SNK01)]] is the closest mechanistic comparator -- also an immune cell-mediated approach (NK cells vs. Tregs), also from the neuroinflammation cluster, also facing capital/execution risk
- [[hb-admsc|HB-adMSCs]] represent another cell/immune modulation approach via mesenchymal stem cell paracrine effects
- Key competitive disadvantage: sargramostim's daily SC injection (5 days/week) is burdensome for a chronic PD population. PDM608 (long-acting GM-CSF, once or twice monthly dosing) is being developed preclinically to address this, but is years behind
- If sargramostim Phase 2 succeeds, it would validate the Treg-neuroprotection axis and create a new mechanistic category in PD disease modification -- potentially attracting pharma interest for PDM608 or other next-gen Treg-expanding approaches
- If it fails, the NLRP3 inhibitors (further advanced, with multiple Phase 1/2 assets) become the dominant neuroinflammation hypothesis in PD

## Analysis

Sargramostim represents one of the more intellectually coherent approaches in the PD neuroinflammation space. The preclinical biology is well-characterized: GM-CSF induces Tregs, Tregs reduce neuroinflammation, reduced neuroinflammation spares dopaminergic neurons. The MPTP model data is robust and dose-responsive. The repurposed-drug angle eliminates manufacturing risk and provides decades of safety data at higher doses in sicker populations. And the clinical data -- while tiny -- shows consistent Treg expansion and directionally positive motor signals across two studies.

The problem is entirely one of clinical maturity and execution risk. A combined total of fewer than 30 PD patients have been exposed, the largest controlled study enrolled only 20 patients, and the only motor efficacy data comes from an open-label N=5 pilot. No placebo-controlled study has been powered for motor endpoints. The announced Phase 2 has not materialized in nearly five years, and Partner Therapeutics appears to be prioritizing government-funded indications (sepsis, radiation injury) over PD.

**Analytical estimate -- Phase 2 initiation probability by end 2027: 40%.** This is our assessment, not from a published source. The reasoning: Partner Therapeutics has a commercial product generating revenue, government contracts providing non-dilutive funding, and a stated interest in PD -- but PD is clearly not the priority. The BARDA sepsis study (January 2025) suggests PTx is focused on indications with government funding support. A PD Phase 2 would require either dedicated capital allocation (~$15-30M), an NIH/NINDS grant mechanism, or a pharma partner -- none of which is currently visible. Upward adjustment: the Alzheimer's Phase 2 data (Potter 2021, positive cognitive signal in N=40) provides cross-indication validation of the Treg mechanism and could attract investor interest. Downward adjustment: the 5-year gap since announcement without trial registration is a strong negative signal.

**Analytical estimate -- Probability of meaningful clinical efficacy if Phase 2 initiates: 20-25%.** This is our assessment, not from a published source. The reasoning: base rate for neuroinflammation disease modification in PD is very low (no successes to date); the open-label motor signal could be entirely placebo effect; peripheral Treg expansion may not translate to sufficient CNS immunomodulation. Upward adjustments: consistent preclinical data across multiple models (+5%), mechanism addresses a validated pathological process (+5%), repurposed drug with known PK/safety (+5%). Downward adjustments: tiny sample sizes in existing trials (-10%), open-label design (-5%), daily injection compliance burden (-5%).

**Signal analysis:** The most informative signal is what Partner Therapeutics has NOT done. A company sitting on positive Phase 1b data for PD -- a massive unmet-need market -- that does not advance to Phase 2 for five years is telling you either: (1) they lack conviction in the PD data, (2) they lack capital for a PD-specific trial, or (3) they view the risk/reward as inferior to their government-funded programs. All three explanations are concerning for PD-specific prospects. The MJFF-funded PDM608 program (long-acting GM-CSF) suggests the Gendelman lab is already looking past sargramostim to a next-generation molecule, which further deprioritizes the near-term clinical path for the parent compound. The strongest bull case would be a scenario where the AD Phase 2 data (Potter 2021) or the sepsis program generates enough revenue/capital for PTx to fund a PD Phase 2 as a portfolio expansion -- but this remains speculative.

## References

### Clinical Trials
- [Leukine (Sargramostim) for Parkinson's Disease Phase 1](https://clinicaltrials.gov/study/NCT01882010) -- NCT01882010
- [Sargramostim Open-Label Pilot Study](https://clinicaltrials.gov/study/NCT03790670) -- NCT03790670

### Key Publications
- [Evaluation of the safety and immunomodulatory effects of sargramostim in a randomized, double-blind phase 1 clinical Parkinson's disease trial | npj Parkinson's Disease (2017)](https://www.nature.com/articles/s41531-017-0013-5)
- [Safety, tolerability, and immune-biomarker profiling for year-long sargramostim treatment of Parkinson's disease | EBioMedicine (2021)](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(21)00173-0/fulltext)
- [An open-label multiyear study of sargramostim-treated Parkinson's disease patients examining drug safety, tolerability, and immune biomarkers from limited case numbers | Translational Neurodegeneration (2023)](https://translationalneurodegeneration.biomedcentral.com/articles/10.1186/s40035-023-00361-1)
- [Safety and efficacy of sargramostim (GM-CSF) in the treatment of Alzheimer's disease | Alzheimer's & Dementia: TRCI (2021)](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/trc2.12158)
- [Granulocyte-Macrophage Colony-Stimulating Factor mRNA and Neuroprotective Immunity in Parkinson's Disease | PMC (2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382980/)
- [Neuroprotective Activities of Long-Acting GM-CSF (mPDM608) in MPTP-Intoxicated Mice | Neurotherapeutics (2020)](https://link.springer.com/article/10.1007/s13311-020-00877-8)
- [Development of an extended half-life GM-CSF fusion protein for Parkinson's disease | Journal of Controlled Release (2022)](https://www.sciencedirect.com/science/article/abs/pii/S0168365922003534)
- [Parkinson's Disease Drug Therapies in the Clinical Trial Pipeline: 2024 Update | JPD (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307066/)

### Press Releases & Filings
- [Partner Therapeutics Announces Publication of Clinical Trial Results of Leukine in Patients with Parkinson's Disease (May 2021)](https://www.partnertx.com/partner-therapeutics-announces-publication-of-clinical-trial-results-of-leukine-sargramostim-in-patients-with-parkinsons-disease/)
- [Immune transformation shows promise for Parkinson's disease | UNMC Newsroom (May 2021)](https://www.unmc.edu/newsroom/2021/05/19/immune-transformation-shows-promise-for-parkinsons-disease/)
- [Partner Therapeutics Acquires Leukine from Sanofi (Feb 2018)](https://www.partnertx.com/partner-therapeutics-ptx-acquires-leukine-from-sanofi/)
- [BARDA and Partner Therapeutics continue partnership for sepsis (Jan 2025)](https://www.partnertx.com/barda-and-partner-therapeutics-continue-partnership-around-development-of-leukine-sargramostim-rhu-gm-csf-to-potentially-improve-patient-care-for-sepsis/)
- [Long-acting GM-CSF Fusion Protein (PDM608) for the Treatment of PD | MJFF Grant](https://www.michaeljfox.org/grant/long-acting-gm-csf-fusion-protein-pdm608-treatment-parkinsons-disease)

### Regulatory & Market
- [Sargramostim Therapeutics Profile | Alzforum](https://www.alzforum.org/therapeutics/sargramostim)
- [Leukine (Sargramostim) for Parkinson's Disease | NINDS](https://www.ninds.nih.gov/health-information/clinical-trials/leukine-sargramostim-parkinsons-disease)
- [Sargramostim Improves Motor Symptoms of PD in Small Phase 1 Trial | Practical Neurology](https://practicalneurology.com/news/sargramostim-improves-motor-symptoms-of-parkinson-disease-in-small-phase-1-trial/2469597/)
- [Immunomodulator Shows Promise for Parkinson Disease in Small Study | NeurologyLive](https://www.neurologylive.com/view/sargramostim-demonstrates-safety-parkinson-disease-treatment-small-study)
