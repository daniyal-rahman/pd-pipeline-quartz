---
drug_name: "NLY01"
aliases: ["NLY01-PD"]
target: "GLP-1 receptor (neuroinflammation / microglial activation)"
mechanism: "Pegylated exendin-4 GLP-1R agonist that crosses BBB, inhibits microglial activation and A1 neurotoxic astrocyte conversion to prevent neuronal death"
modality: "small molecule"
developer: "Neuraly (D&D Pharmatech)"
company_type: "biotech"
publicly_traded: true
ticker: "347850.KQ"
stage: "Phase 2"
status: "Active"
patient_population: "Early untreated PD; signal in patients <60 years"
route_of_administration: "SC (weekly injection)"
key_biomarkers: ["MDS-UPDRS Parts II+III"]
confidence_rating: "3/10"
next_catalyst: "Decision on PD-specific follow-up trial enriched for younger patients"
catalyst_date: "TBD"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# NLY01

## Summary

NLY01 is a pegylated, long-acting exendin-4-based GLP-1 receptor agonist developed by Neuraly (biotech, subsidiary of D&D Pharmatech, KOSDAQ: 347850) that missed its primary endpoint in a 255-patient Phase 2 trial in early untreated PD (p=0.77 and p=0.79 for the two dose arms). A post-hoc subgroup analysis found a statistically significant ~5-point MDS-UPDRS improvement in patients under 60 (N=95, p<0.01), which was dose-related and persisted 8 weeks after discontinuation. The GLP-1 class in PD remains inconclusive: lixisenatide showed a positive Phase 2 signal (LixiPark, NEJM 2024), while exenatide failed a 96-week Phase 3 in the UK (2025). If D&D Pharmatech advances a PD trial enriched for younger patients and replicates the subgroup signal, NLY01 would validate the neuroinflammation-via-GLP-1R thesis and the age-stratification approach. If no enriched follow-up materializes, the company's neurology focus shifts to MS and Alzheimer's, and NLY01 in PD is effectively shelved.

## Notes

### Science
- NLY01 is a pegylated form of exendin-4, engineered for extended half-life allowing once-weekly subcutaneous dosing, compared to twice-daily for native exenatide
- Mechanism centers on **microglial GLP-1R activation**: NLY01 binds upregulated GLP-1 receptors on activated microglia, blocking their release of pro-inflammatory cytokines (TNF-alpha, IL-1alpha, C1q) that convert resting astrocytes into neurotoxic **A1 reactive astrocytes**
- By preventing the microglia-to-A1-astrocyte cascade, NLY01 inhibits neuronal cell death downstream -- a neuroinflammatory mechanism distinct from the direct neuroprotection proposed for other GLP-1 agonists
- Key preclinical paper: Yun et al., Nature Medicine 2018 (Johns Hopkins / Ted Dawson lab) demonstrated NLY01 blocked A1 astrocyte conversion and was neuroprotective in alpha-synuclein PFF and MPTP mouse models
- PEGylation improves BBB penetration relative to native exenatide -- a critical differentiator since GLP-1R engagement in brain parenchyma (not just peripheral) is hypothesized to drive the anti-neuroinflammatory effect
- Open question: why the <60 age effect? Younger PD patients may have more neuroinflammation-driven (vs. multi-pathology) disease, or GLP-1R expression/density may differ by age. This is unresolved and the subgroup finding is post-hoc
- The broader GLP-1 class shows mixed PD results: lixisenatide positive in Phase 2 (LixiPark, NEJM 2024), exenatide positive in Phase 2 (Athauda et al., Lancet 2017) but failed Phase 3 (Exenatide-PD3, Lancet 2025), semaglutide under investigation. NLY01 is the only pegylated/long-acting BBB-penetrant variant tested

### Clinical

**NLY01 Phase 1 (First-in-Human)** | NCT03672604 | N=~40 | Healthy volunteers
- **Primary endpoint:** Safety, tolerability, pharmacokinetics of single and multiple ascending doses (0.25-10 mg SC)
- **Key secondary:** PK profiling to select Phase 2 doses
- **Status:** Completed (2018-2019)
- **Interpretation:** Established safety and selected 2.5 mg and 5.0 mg weekly doses for Phase 2

**NLY01-PD-1 (Phase 2)** | NCT04154072 | N=255 | Early untreated PD, ages 30-80
- **Primary endpoint:** Change from baseline to Week 36 in MDS-UPDRS Parts II+III sum score --> **NOT significant** (difference vs. placebo: -0.39, p=0.77 for 2.5 mg; 0.36, p=0.79 for 5.0 mg)
- **Key secondary:** Non-motor assessments (MDS-UPDRS Part I, PDSS-2, MoCA) -- no significant differences reported
- **Post-hoc subgroup (<60 years, N=95, 37% of population):** ~5-point MDS-UPDRS reduction at 36 weeks (p<0.01 vs. placebo); dose-related; effect persisted 8 weeks post-discontinuation
- **Safety:** Well tolerated; GI adverse events (nausea) most common, consistent with GLP-1 class
- **Status:** Completed March 2023; published Lancet Neurology (Dec 2023)
- **Interpretation:** Clear primary miss with virtually zero separation from placebo in the overall population. The <60 subgroup is intriguing but post-hoc, small (N=95 split across 3 arms), and requires prospective confirmation. The persistence of effect after washout is the strongest disease-modification signal, as a symptomatic effect would reverse.

### Financial
- **D&D Pharmatech (KOSDAQ: 347850):** IPO on KOSDAQ May 2024; market cap ~$2.4B (as of late 2025)
- **Series C:** $51M raised October 2021, led by Praxis Capital, with DS Asset Management, Kudos Ventures, Korea Investment & Securities
- **Earlier rounds:** Included Smilegate Investment, InterVest, Magna Investment, LB Investment (Korean VCs)
- **Peter Thiel-backed:** Received preliminary approval for Korean IPO in late 2023
- **Neuraly is a US subsidiary** of D&D Pharmatech (Korea), structured as a disease-specific subsidiary model -- D&D also operates subsidiaries for MASH (DD01), Alzheimer's (NLY01-AD), diabetes (NLY01-D), and periodontal disease (P4M01)
- **No disclosed licensing deal or partnership** for NLY01 in PD -- fully internal development
- **Capital allocation signal:** D&D Pharmatech appears to be prioritizing the MASH program (DD01, Phase 2 enrolled Feb 2025) and MS indication for NLY01 over a PD follow-up, suggesting internal conviction on PD has waned post-Phase 2 miss

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "GLP-1") AND file.name != "nly01"
SORT stage DESC
```

- NLY01 sits within the broader **GLP-1 agonist class** in PD, which includes non-pegylated exenatide (failed Phase 3, 2025), lixisenatide (positive Phase 2 / LixiPark, NEJM 2024), and semaglutide (epidemiological signal, trials planned)
- Key differentiator vs. exenatide: PEGylation gives NLY01 longer half-life (weekly vs. daily/twice-daily dosing) and potentially improved BBB penetration, though this did not translate to efficacy in the overall Phase 2 population
- Lixisenatide (LixiPark) showed a 3.08-point MDS-UPDRS Part III benefit (p=0.007) at 12 months in 156 patients on stable treatment -- a cleaner positive result than NLY01, though also only Phase 2 and with high GI side-effect burden (46% nausea)
- As a neuroinflammation-targeting asset, NLY01 also competes conceptually with NLRP3 inflammasome inhibitors (e.g., [[dapansutrile]], [[selnoflast]]) and other anti-inflammatory approaches, though the mechanism is distinct
- The <60 age enrichment thesis overlaps with broader PD trial design trends toward patient stratification -- if validated, it would have implications for trial design across the neuroinflammation cluster

## Analysis

NLY01's Phase 2 result is a clear negative on the primary endpoint, with essentially zero treatment effect in the overall population. The asset's residual value rests entirely on the post-hoc <60 subgroup finding. While the signal is intriguing -- dose-related, statistically significant (p<0.01), and persistent after washout -- it carries all the limitations of post-hoc subgroup analyses in failed trials: small N per arm (~30 per group in the <60 subset), multiple comparisons risk, and the inherent temptation to mine failed data for positive signals.

**Analytical estimate -- Probability of NLY01 advancing to a PD-specific enriched trial: 25-30%.** This is our assessment, not from a published source. The reasoning: D&D Pharmatech's post-IPO capital and multi-indication strategy give them resources, but the company appears to be prioritizing MASH (DD01), MS, and Alzheimer's indications for NLY01 over a PD-specific follow-up. The exenatide Phase 3 failure (2025) further dampens enthusiasm for GLP-1 agonists in PD specifically. Against this: the lixisenatide LixiPark positive result keeps the class alive, and D&D Pharmatech's Korean investor base may favor continued PD development given the unmet need narrative.

**Analytical estimate -- If an enriched PD trial (<60 population) proceeds, probability of success: 20-25%.** This is our assessment, not from a published source. The reasoning: base rate for replicating post-hoc subgroup findings is low (~15-20%); adjustment upward for dose-response relationship (+5%), persistence after washout (+5%), biological plausibility of age-related neuroinflammation differential (+5%); adjustment downward for the overall population showing zero effect (-10%), exenatide Phase 3 class failure (-5%).

The GLP-1 agonist class in PD is at an inflection point. Lixisenatide's positive Phase 2 and exenatide's negative Phase 3 create genuine uncertainty about whether the mechanism works. NLY01 adds a third data point that is neither clean positive nor clean negative, but rather suggests the question may be "in whom?" rather than "does it work?" If the <60 finding is real, it implies PD is biologically heterogeneous in ways that matter for GLP-1R-mediated neuroprotection -- younger-onset PD may be more neuroinflammation-driven and thus more responsive. This age-stratification hypothesis deserves prospective testing, but it is unclear whether D&D Pharmatech/Neuraly will be the ones to do it.

## References

### Clinical Trials
- [NLY01 Phase 1](https://clinicaltrials.gov/study/NCT03672604) -- NCT03672604
- [NLY01-PD-1 Phase 2](https://clinicaltrials.gov/ct2/show/NCT04154072) -- NCT04154072

### Key Publications
- [Safety, tolerability, and efficacy of NLY01 in early untreated Parkinson's disease | Lancet Neurology (Dec 2023)](https://pubmed.ncbi.nlm.nih.gov/38101901/)
- [Block of A1 astrocyte conversion by microglia is neuroprotective in models of Parkinson's disease | Nature Medicine (2018)](https://www.nature.com/articles/s41591-018-0051-5)
- [Blocking microglial activation of reactive astrocytes is neuroprotective in models of Alzheimer's disease | Acta Neuropathologica Communications (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8074239/)
- [Trial of Lixisenatide in Early Parkinson's Disease (LixiPark) | NEJM (2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2312323)
- [Exenatide Phase 3 in Parkinson's Disease | Lancet (2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02808-3/fulltext)
- [GLP-1 Receptor Agonists: A New Treatment in Parkinson's Disease | IJMS (2024)](https://www.mdpi.com/1422-0067/25/7/3812)

### Press Releases & Filings
- [Neuraly Announces Topline Results from Phase 2 Trial of NLY01 in Parkinson's Disease (March 2023)](https://www.businesswire.com/news/home/20230327005069/en/Neuraly-Announces-Topline-Results-from-Phase-2-Trial-of-NLY01-in-Parkinsons-Disease)
- [Neuraly Announces Completion of Enrollment in Phase 2 Clinical Trial (April 2022)](https://www.businesswire.com/news/home/20220418005572/en/Neuraly-Announces-Completion-of-Enrollment-in-Phase-2-Clinical-Trial-of-NLY01-in-Patients-with-Parkinsons-Disease)
- [Neuraly Announces First Patient Dosed in Phase 2 (March 2020)](https://www.businesswire.com/news/home/20200303005084/en/CORRECTING-and-REPLACING-Neuraly-Announces-First-Patient-Dosed-in-Phase-2-Clinical-Trial-of-NLY01-for-Patients-with-Parkinsons-Disease)
- [D&D Pharmatech Raises $51M in Series C (Oct 2021)](https://www.fiercebiotech.com/biotech/d-d-pharma-snags-51m-ahead-1q22-korean-ipo-for-alzheimer-s-parkinson-s)
- [D&D Pharmatech receives FDA nod for Phase 2 MS trial](https://www.koreabiomed.com/news/articleView.html?idxno=25023)

### Regulatory & Market
- [NLY01 fails to slow motor symptom progression in Phase 2 trial | Parkinson's News Today](https://parkinsonsnewstoday.com/news/nly01-fails-slow-motor-symptom-progression-phase-2-trial/)
- [Phase 2 Trial of NLY01 in Parkinson's Disease | ACNR](https://acnr.co.uk/nly01/)
- [Exenatide Phase 3 results commentary | Cure Parkinson's (2025)](https://cureparkinsons.org.uk/2025/03/exenatide3/)
- [Neuraly points to younger patients for hope as Parkinson's bet fails Phase 2 | Fierce Biotech](https://www.fiercebiotech.com/biotech/neuraly-points-younger-patients-hope-parkinsons-bet-fails-phase-2)
