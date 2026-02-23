---
drug_name: "VENT-02"
aliases: []
target: "NLRP3 inflammasome"
mechanism: "Oral, brain-penetrant small molecule that inhibits NLRP3 inflammasome oligomerization, blocking IL-1B/IL-18 secretion and pyroptotic neuroinflammation"
modality: "small molecule"
developer: "Ventus Therapeutics"
company_type: "biotech"
publicly_traded: false
partner: ""
partner_type: ""
stage: "Terminated"
status: "Terminated"
patient_population: "Mild to moderate PD"
route_of_administration: "oral"
key_biomarkers: ["IL-1B", "IL-18", "hsCRP", "CSF drug levels", "digital motor assessments"]
confidence_rating: "2/10"
next_catalyst: "Phase 2a data disclosure (if released)"
catalyst_date: "TBD"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/ventus-therapeutics]]"
---

# VENT-02

## Summary

Ventus Therapeutics (biotech, private) developed VENT-02 as an oral, brain-penetrant NLRP3 inflammasome inhibitor -- arguably the best-characterized CNS-penetrant compound in the NLRP3 class, with clean Phase 1 safety, 100% peripheral IL-1B inhibition, and confirmed CSF drug levels over 24 hours. The Phase 2a in mild-to-moderate PD (NCT06822517, ~30 patients, 28-day treatment) was terminated in October 2025 after enrolling 29 of 30 planned patients, with no public disclosure of results or rationale. If Ventus eventually releases the Phase 2a data showing target engagement and biomarker movement in PD patients, it would inform the broader neuroinflammation thesis and competitors like NodThera (NT-0796) and Ventyx/Roche (VTX3232). If the data are never disclosed or show poor CNS target engagement, the termination becomes a negative signal for NLRP3 inhibition in PD specifically, though the target remains active via competing programs.

## Notes

### Science
- NLRP3 is a cytosolic pattern-recognition receptor that, when activated by damage-associated molecular patterns (including alpha-synuclein aggregates), oligomerizes into a large inflammasome complex that activates caspase-1, cleaving pro-IL-1B and pro-IL-18 into active cytokines and triggering pyroptosis (inflammatory cell death)
- In PD, alpha-synuclein fibrils activate microglial NLRP3, creating a feed-forward neuroinflammatory cycle: aggregated alpha-syn triggers NLRP3 activation, which produces IL-1B/IL-18 and causes microglial pyroptosis, releasing more inflammatory mediators and further promoting alpha-syn aggregation
- Genetic validation: NLRP3 pathway polymorphisms are associated with PD risk in GWAS; postmortem PD brain tissue shows elevated NLRP3/caspase-1/IL-1B levels in substantia nigra; NLRP3 knockout mice are protected from dopaminergic neurodegeneration in toxin models
- VENT-02 is differentiated from most NLRP3 inhibitors by confirmed **brain penetrance** -- CSF drug levels were sustained for 24 hours in Phase 1, critical for targeting microglial NLRP3 in the CNS. Many competitors (e.g., IFM Tre/Novartis compounds, VENT-01/Novo Nordisk) are peripherally restricted by design
- Ventus used computational structural biology to design VENT-02, leveraging high-resolution cryo-EM structures of NLRP3 in active/inactive conformations to achieve high potency and selectivity
- Key open question: whether 28 days of NLRP3 inhibition is sufficient to produce measurable biomarker changes in PD patients, given the chronic and slowly progressive nature of neuroinflammation. NodThera's NT-0796 showed biomarker changes at 28 days, suggesting it may be feasible

### Clinical

**VENT-02 Phase 1 (SAD/MAD)** | NCT TBD | N=87 | Healthy volunteers
- **Primary endpoint:** Safety/tolerability --> Well tolerated across all doses up to 1600mg single dose and 400mg BID for 6.5 days; no dose-limiting toxicities or serious adverse events
- **Key secondary:** 100% IL-1B inhibition in ex vivo whole blood assay; robust hsCRP reduction; significant CSF drug levels sustained for 24 hours; favorable PK supporting once-daily dosing
- **Status:** Completed (results announced March 2024)
- **Interpretation:** Best-in-class CNS penetration data for an NLRP3 inhibitor. The 100% peripheral target engagement and confirmed CSF levels provided strong rationale for PD trial, though CSF drug levels do not directly prove CNS target engagement on microglia

**VENT-02 Phase 2a in PD** | NCT06822517 | N=~30 (29 enrolled) | Mild to moderate PD
- **Primary endpoint:** Safety and tolerability over 28-day treatment
- **Key secondary:** Changes in plasma and CSF biomarkers of target engagement, inflammation, and disease activity; motor function and QoL via digital health technologies
- **Status:** Terminated (October 2025). First patient dosed March 2025. Trial terminated after enrolling 29 of ~30 patients. No results disclosed.
- **Interpretation:** Near-complete enrollment before termination suggests the decision was driven by emerging data review (possibly interim safety, PK/PD, or biomarker signals) rather than enrollment difficulty. The lack of public disclosure is unusual -- companies typically release data even from terminated trials. This could indicate the data are being analyzed for future publication, or that the results were uninformative/negative.

### Financial
- **Total raised:** ~$300M across three rounds (Series A: $60M in 2020, Versant Ventures/GV; Series B: $100M in 2021, RA Capital-led; Series C: $140M in 2022, SoftBank Vision Fund 2/RA Capital co-led)
- **Novo Nordisk deal (VENT-01, separate compound):** $70M upfront + up to $633M in milestones for exclusive worldwide rights to peripherally-restricted NLRP3 inhibitors targeting NASH, CKD, cardiometabolic diseases. Ventus retained all rights to brain-penetrant NLRP3 (VENT-02) and certain other compounds
- **Key investors:** SoftBank Vision Fund 2, RA Capital Management, Andreessen Horowitz, Qatar Investment Authority, BVF Partners, Casdin Capital, Cormorant, GV, Versant Ventures
- **Valuation:** Not publicly disclosed; $300M raised and Novo deal economics suggest last-round valuation in the $500M-$800M range (typical for Series C biotech with Phase 1 data and big pharma partnership)
- **Pipeline diversification:** VENT-02 PD termination is a setback but not existential -- Ventus retains VENT-02 development optionality for osteoarthritis (Phase 2 planned) and epilepsy, plus VENT-03 (cGAS inhibitor, Phase 2 in lupus, first patient dosed December 2025), and the Novo Nordisk-partnered VENT-01 program generates milestones

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[vent-02]] | Terminated | Terminated | Ventus Therapeutics | small molecule |
| [[adp065-abc]] | Preclinical | Active | Alector | siRNA |
| [[neumora-nlrp3]] | Preclinical | Active | Neumora Therapeutics | small molecule |
| [[ism8969]] | Phase 1 | Active | Insilico Medicine | small molecule |
| [[nt-0150]] | Phase 1 | Active | NodThera | small molecule |
| [[nt-0796]] | Phase 1b | Active | NodThera | small molecule |
| [[selnoflast]] | Phase 1b | Active | Roche | small molecule |
| [[dapansutrile]] | Phase 2 | Active | Olatec Therapeutics | small molecule |
| [[vtx3232]] | Phase 2 | Active | Ventyx Biosciences | small molecule |

- **NodThera (NT-0796):** Most direct competitor. Phase 1b/2a in PD showed reversal of neuroinflammatory biomarkers (IL-1B, IL-18) to levels of healthy elderly controls over 28 days; well tolerated. Now in advanced Phase 2 planning. Published in Movement Disorders (2025). NT-0796's positive data make the VENT-02 termination more puzzling -- either VENT-02 had a compound-specific issue or the termination was for strategic/financial reasons
- **Ventyx/Roche (VTX3232):** Brain-penetrant NLRP3 inhibitor in Phase 1b/2a for PD. Early data showed safety, tolerability, and reductions in IL-1B/IL-18 with improvements in motor and nonmotor symptoms. Roche (via Ventyx acquisition) provides deep resources for PD development
- **Insilico Medicine (ISM8969):** AI-designed oral NLRP3 inhibitor received FDA IND clearance for PD in January 2026. Preclinical/early clinical stage
- **IFM Tre/Novartis:** Acquired for $310M upfront; NLRP3 inhibitors are peripherally restricted (not brain-penetrant), focused on gout, CV, NASH -- not directly competing in PD
- **Inflazome/Roche:** Inzomelid is a CNS-penetrant NLRP3 inhibitor being investigated for Alzheimer's and PD, but development status unclear post-Roche acquisition
- The NLRP3-in-PD space is increasingly crowded with at least 3-4 brain-penetrant compounds, which may have influenced Ventus's strategic decision to terminate

## Analysis

The VENT-02 termination in PD is a notable but ambiguous event. The compound itself has arguably the strongest Phase 1 profile in the brain-penetrant NLRP3 class -- 100% peripheral target engagement, confirmed and sustained CSF exposure, clean safety, and once-daily oral dosing potential. That this compound was terminated in PD after near-complete enrollment (29/30 patients) raises questions that cannot be resolved without data disclosure.

**Analytical estimate -- probability of VENT-02 returning to PD development: 10-15%.** This is our assessment, not from a published source. The reasoning: base rate for terminated Phase 2 programs being restarted is ~5%; adjustment upward for near-complete enrollment suggesting possible data availability (+5%), retained compound rights (+3%), osteoarthritis Phase 2 keeping the compound alive (+2%); adjustment downward for competitive pressure from NT-0796 and VTX3232 (-5%), company pivot toward cGAS/VENT-03 (-3%), no public statement of intent to resume (-2%). Net: ~10-15%.

The termination's impact on the neuroinflammation thesis in PD depends entirely on the reason. If Ventus stopped for strategic/financial reasons (prioritizing VENT-03 in lupus, preserving cash for higher-conviction programs), it says nothing about NLRP3 biology. If the 28-day biomarker data showed no CNS target engagement despite confirmed CSF levels, it would be a significant negative for the mechanism. NodThera's positive NT-0796 data argue against a class-wide target engagement problem, suggesting the termination may be compound-specific or strategic. The fact that Ventus still plans to advance VENT-02 in osteoarthritis supports the "strategic reprioritization" interpretation over a safety or efficacy concern.

For the broader neuroinflammation cluster, the critical assets to watch are now NodThera's NT-0796 (most advanced positive data in PD) and Ventyx/Roche's VTX3232 (big pharma backing). NLRP3 inhibition in PD remains a viable thesis -- the target biology is strong, and competing programs are generating encouraging biomarker data. The VENT-02 termination is a single data point in a rapidly expanding competitive landscape.

## References

### Clinical Trials
- [VENT-02 Phase 2a in PD](https://clinicaltrials.gov/study/NCT06822517) -- NCT06822517

### Key Publications
- [Anti-Neuroinflammatory and Anti-Inflammatory Effects of the NLRP3 Inhibitor NT-0796 in Subjects with PD | Movement Disorders (2025)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.30307)
- [Safety, Tolerability, PK and PD of VENT-02, a Novel CNS-Penetrant NLRP3 Inhibitor for PD | MDS Abstracts](https://www.mdsabstracts.org/abstract/safety-tolerability-pharmacokinetics-and-pharmacodynamics-of-vent-02-a-novel-cns-penetrant-nlrp3-inhibitor-for-the-treatment-of-parkinsons-disease/)
- [Role of NLRP3 Inflammasome in PD and Therapeutic Considerations | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9661339/)
- [NLRP3 Inflammasome-Mediated Neuroinflammation and Related Mitochondrial Impairment in PD | Neuroscience Bulletin](https://link.springer.com/article/10.1007/s12264-023-01023-y)

### Press Releases & Filings
- [Ventus Announces First Patient Dosed in Phase 2a Trial of VENT-02 in PD (March 2025)](https://www.businesswire.com/news/home/20250307125796/en/Ventus-Therapeutics-Announces-First-Patient-Dosed-in-Phase-2a-Clinical-Trial-Evaluating-VENT-02-an-Oral-Brain-Penetrant-NLRP3-Inhibitor-in-Parkinsons-Disease)
- [Ventus Announces Phase 1 Results for VENT-02 (March 2024)](https://www.ventustx.com/ventus-therapeutics-announces-results-from-phase-1-clinical-trial-of-vent-02-a-novel-orally-administered-brain-penetrant-nlrp3-inhibitor/)
- [Ventus Initiates Phase 1 Dosing of VENT-02 (August 2023)](https://www.ventustx.com/ventus-therapeutics-initiates-dosing-in-a-phase-1-clinical-trial-of-vent-02-a-novel-orally-administered-brain-penetrant-nlrp3-inhibitor/)
- [Ventus Enters License Agreement with Novo Nordisk for NLRP3 Program (September 2022)](https://www.ventustx.com/ventus-therapeutics-enters-exclusive-development-and-license-agreement-with-novo-nordisk-for-nlrp3-inhibitor-program/)
- [Ventus Closes $140M Series C (2022)](https://www.ventustx.com/ventus-therapeutics-closes-140-million-series-c-financing/)
- [Ventus Stops Phase 2 of NLRP3 Inhibitor in Parkinson's | Endpoints News (October 2025)](https://endpoints.news/ventus-stops-phase-2-of-nlrp3-inhibitor-that-was-being-tested-in-parkinsons/)

### Regulatory & Market
- [NodThera NT-0796 Reverses Neuroinflammation in PD Phase 1b/2a | NodThera](https://www.nodthera.com/news/nodtheras-nlrp3-inhibitor-nt-0796-reverses-neuroinflammation-in-parkinsons-disease-phase-ib-iia-trial/)
- [AI-Designed NLRP3 Inhibitor (ISM8969) Receives FDA IND Clearance for PD (January 2026)](https://www.news-medical.net/news/20260123/AI-designed-NLRP3-inhibitor-receives-FDA-clearance-for-Parkinson-disease-trials.aspx)
- [NLRP3 Inhibitors for PD -- Alzheimer's Drug Discovery Foundation Review (2024)](https://www.alzdiscovery.org/uploads/cognitive_vitality_media/NLRP3_Inhibitors_UPDATE_(drug_in_development).pdf)
