---
drug_name: "Ursodeoxycholic acid"
aliases: ["UDCA", "ursodiol", "Ursofalk", "Actigall"]
target: "mitochondrial dysfunction (respiratory chain / membrane potential)"
mechanism: "Bile acid that rescues mitochondrial function by increasing respiratory chain complex activity, restoring membrane potential, reducing oxidative stress, and activating pro-survival Akt signaling via glucocorticoid receptor"
modality: "small molecule"
developer: "University of Sheffield / UCL"
company_type: "academic"
publicly_traded: false
partner: "Cure Parkinson's / MRC / NIHR"
partner_type: "academic"
stage: "Phase 2"
status: "Active"
patient_population: "Early PD (within 3 years of diagnosis)"
route_of_administration: "oral"
key_biomarkers: ["31P-MRS (midbrain ATP/phosphate)", "wearable gait sensors", "MDS-UPDRS"]
confidence_rating: "4/10"
next_catalyst: "EJS ACT-PD Arm 3 initiation"
catalyst_date: "2026"
thesis_cluster: "mitophagy"
tags: [pd-pipeline, claude]
date: 2026-02-16
---

# Ursodeoxycholic acid (UDCA)

## Summary

UDCA is a naturally occurring bile acid approved since the 1980s for primary biliary cholangitis and gallstone dissolution, now being repurposed for PD disease modification via mitochondrial rescue. The Sheffield UP study (Phase 2, N=30) showed UDCA was safe at 30 mg/kg/day, demonstrated midbrain target engagement on 31P-MRS (increased Gibbs free energy and inorganic phosphate), and produced a statistically significant improvement in gait cadence (+1.5 vs. -4.5 steps/min, p=0.0253) -- but MDS-UPDRS Part III did not separate from placebo, and the trial was underpowered for clinical endpoints. UDCA is now planned as the third arm of the [[ejs-act-pd|EJS ACT-PD]] Phase 3 MAMS platform in 2026, which will provide a definitive test in 400 patients over 36 months. If the ACT-PD arm succeeds, UDCA becomes the first disease-modifying PD therapy -- and as an off-patent generic costing pennies per dose, it would be immediately globally accessible. If it fails, the mitochondrial rescue hypothesis via bile acids is closed at the clinical level, though mechanistically distinct mitochondrial approaches ([[nrg5051|mPTP inhibition]], [[mtx325|USP30 inhibition]], [[nicotinamide-riboside|NAD+ replenishment]]) would remain viable.

## Notes

### Science
- UDCA is an endogenous secondary bile acid produced by gut bacteria; in PD patients, endogenous UDCA and its taurine conjugate (TUDCA) are reduced, suggesting a disease-associated deficit in the bile acid pool
- Mechanism identified via a 2,000-compound screen in Parkin-mutant fibroblasts (Mortiboys, Bandmann et al., Brain 2013): UDCA and the related compound ursocholanic acid rescued mitochondrial function by increasing activity of all four respiratory chain complexes
- The rescue effect operates via glucocorticoid receptor activation leading to Akt phosphorylation, a pro-survival kinase cascade -- mechanistically distinct from direct respiratory chain targeting
- Validated across multiple PD genetic forms: rescues mitochondrial dysfunction in both Parkin-mutant and LRRK2 G2019S-mutant fibroblasts and neurons, suggesting applicability beyond a single genetic subtype
- In LRRK2 G2019S carriers (Mortiboys et al., Neurology 2015): ATP levels were 35-38% lower than controls; UDCA recovered intracellular ATP in non-manifesting carriers; in transgenic flies, UDCA doubled photoreceptor response and increased lamina/medulla responses 3-4 fold
- Additional preclinical mechanisms: anti-apoptotic effects, reduction of oxidative stress, protection of dopaminergic neurons in MPTP models, and potential regulation of mitochondrial turnover (mitophagy)
- TUDCA (taurine-conjugated UDCA) has similar neuroprotective properties and better CNS bioavailability in some models, but UDCA was selected for clinical development because it is already licensed with decades of human safety data
- Key distinction from other mitochondrial approaches: [[nrg5051]] targets the mitochondrial permeability transition pore (mPTP), [[mtx325]] inhibits USP30 to promote mitophagy, [[nicotinamide-riboside]] replenishes NAD+ -- UDCA acts upstream on respiratory chain complex activity and membrane potential, a different and potentially complementary mechanism
- Open scientific question: whether the dose needed for CNS mitochondrial rescue (30 mg/kg, well above the standard 15 mg/kg hepatology dose) achieves sufficient brain penetration, and whether peripheral bile acid effects (gut-brain axis, microbiome modulation) contribute to any clinical benefit

### Clinical

**Minnesota Phase 1 Pilot** | NCT02967250 | N=5 | PD patients
- **Primary endpoint:** Safety, tolerability, and PK of ascending-dose oral UDCA (15-50 mg/kg/day over 6 weeks)
- **Key finding:** Safe and well tolerated; modest increases in brain ATP levels on imaging
- **Status:** Completed (published 2020, J Clin Pharmacol)
- **Interpretation:** Open-label proof-of-concept confirming oral UDCA reaches the brain at doses sufficient to detect bioenergetic changes; established feasibility for the larger UP study

**UP Study (Phase 2)** | NCT03840005 / ISRCTN73371260 | N=30 (20 UDCA, 10 placebo) | Early PD (within 3 years of diagnosis)
- **Primary endpoint:** Safety and tolerability of UDCA 30 mg/kg/day over 48 weeks → Safe and well tolerated; only mild transient GI adverse events (nausea, diarrhea) more frequent in UDCA group
- **Key secondary (31P-MRS):** Midbrain target engagement demonstrated -- UDCA group showed increased Gibbs free energy and inorganic phosphate levels compared to placebo, indicating improved ATP hydrolysis. This is the first in vivo human evidence of UDCA's mitochondrial mechanism in PD brain tissue
- **Key secondary (gait analysis):** Wearable sensor-based cadence improved in UDCA group (median change +1.5 steps/min) vs. deterioration in placebo (-4.5 steps/min), **p=0.0253**
- **MDS-UPDRS Part III:** Failed to detect a difference between treatment groups
- **Design:** Two-centre (Sheffield Teaching Hospitals, UCLH), double-blind, 2:1 randomization, 48 weeks treatment + 8-week washout
- **Investigators:** Prof. Oliver Bandmann (Sheffield, PI), Prof. Thomas Foltynie (UCL)
- **Status:** Completed; results published Payne et al., Movement Disorders, August 2023
- **Interpretation:** The trial was designed and powered for safety/tolerability (Phase 2 objectives), not clinical efficacy. The 31P-MRS target engagement is the critical finding -- it confirms the preclinical mechanism translates to human brain. The gait signal is encouraging but based on N=30. MDS-UPDRS non-separation is expected at this sample size and duration. The overall package was sufficient for the iLCT committee to advance UDCA to the Phase 3 ACT-PD platform

**EJS ACT-PD Arm 3 (Phase 3)** | ISRCTN17799294 (platform) | N=400 (UDCA arm) | Adults 30+ with PD on dopaminergic therapy
- **Primary endpoint:** 30% reduction in rate of progression on MDS-UPDRS Parts 1 & 2 combined over 36 months
- **Key secondary:** Wearable sensor-derived motor/gait measures; molecular biomarkers (MJFF sub-study)
- **Status:** Planned for 2026 initiation as third arm of the MAMS platform (telmisartan and terazosin already recruiting since October 2025)
- **Interpretation:** This is the definitive test. The MAMS design provides a shared placebo arm, shared infrastructure, and interim futility analyses -- if UDCA is not working, the arm can be dropped early without wasting the full 36 months. The 400-patient, 36-month design is adequately powered for disease modification, unlike the 30-patient UP study

### Financial
- **No commercial sponsor** -- UDCA development for PD is entirely funded by academic and nonprofit sources
- **UP study funding:** Cure Parkinson's (formerly the Cure Parkinson's Trust) and the Virtual Biotech programme, part of the iLCT (international Linked Clinical Trials) initiative
- **EJS ACT-PD funding:** Part of the GBP 26M (~$33M) platform funded by MRC/NIHR, Cure Parkinson's, MJFF, Parkinson's UK, and philanthropy
- **Drug cost:** UDCA is a cheap, off-patent generic; drug supply costs are negligible
- **No peak sales estimates applicable** -- even if UDCA demonstrates disease modification, there is no patent exclusivity and no branded commercial pathway; the drug would be prescribed as a generic
- **Context:** The economics are similar to other repurposed generics in the ACT-PD platform (telmisartan, terazosin) and the broader Cure Parkinson's iLCT portfolio ([[exenatide]], [[ambroxol]], [[lixisenatide]]). The absence of commercial incentive is both a strength (no profit motive biasing trial design) and a weakness (no pharma company will fund post-approval marketing or lifecycle management)

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "mitochondri") AND file.name != "udca"
SORT stage DESC
```

- UDCA occupies the mitochondrial rescue / bioenergetics space within PD disease modification, competing with mechanistically distinct approaches to the same biological problem
- [[nrg5051]] (Neurogene/NRG Therapeutics) targets the mitochondrial permeability transition pore (mPTP) -- a different downstream mechanism, and is a proprietary small molecule unlike UDCA's generic status
- [[mtx325]] (Mitokinin) inhibits USP30 to promote selective mitophagy of damaged mitochondria -- upstream clearance rather than UDCA's functional rescue approach
- [[nicotinamide-riboside]] (NAD+ precursor) replenishes NAD+ to support mitochondrial electron transport -- complementary mechanism that could theoretically be combined with UDCA
- The EJS ACT-PD platform itself creates internal competition: the terazosin arm (PGK1/glycolysis) addresses bioenergetics via a different pathway (glycolytic ATP vs. mitochondrial ATP), and both could theoretically succeed or fail independently
- [[exenatide]] (GLP-1 agonist, failed Phase 3) had mitochondrial/bioenergetic effects among its proposed mechanisms -- its failure is a cautionary precedent for the mitochondrial hypothesis, though UDCA's mechanism is distinct
- Key competitive advantage: UDCA has direct human brain target engagement data (31P-MRS showing improved ATP hydrolysis in midbrain) -- most competing mitochondrial approaches lack this level of translational evidence
- Key competitive disadvantage: the UP study was N=30 with no clinical endpoint separation, placing UDCA behind [[nrg5051]] and other proprietary molecules that have dedicated pharma funding and development resources

## Analysis

UDCA's case rests on a clean mechanistic chain: preclinical screen identifies bile acid class as mitochondrial rescuers across multiple PD genetic forms (Parkin, LRRK2), a Phase 1 pilot confirms brain penetration, and a Phase 2 trial demonstrates midbrain target engagement in humans via 31P-MRS. This is a stronger translational package than most repurposed drugs entering PD trials, which typically rely on epidemiological association or preclinical models alone. The gait improvement signal (p=0.0253) adds a functional correlate, though it must be interpreted cautiously given N=30.

**Analytical estimate -- Probability of success in EJS ACT-PD Arm 3: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: repurposed drugs in PD disease-modification Phase 3 trials have a 0% success rate to date ([[exenatide]] failed, isradipine failed, creatine failed, CoQ10 failed, inosine failed) -- starting point <5%
- Adjustments upward: human brain target engagement confirmed via 31P-MRS (+5%), mechanism validated across multiple PD genetic forms in vitro (+3%), gait cadence signal in Phase 2 (+3%), decades of safety data eliminating tolerability risk (+2%), generic status eliminating commercial bias in trial design (+1%)
- Adjustments downward: Phase 2 MDS-UPDRS showed no separation (-3%), N=30 Phase 2 severely underpowered for clinical conclusions (-2%), field-wide failure of mitochondrial/bioenergetic approaches in neurodegeneration (-3%), uncertainty about whether 30 mg/kg achieves sufficient sustained CNS levels (-2%)
- Net: ~10-15%

**Signal analysis:** The key signal is the iLCT committee's decision to advance UDCA to the ACT-PD platform. This committee of 20-30 PD experts has evaluated 239 drug dossiers and 171 unique agents since 2012; UDCA was among the drugs prioritized from this pool. Prof. Bandmann (Sheffield, UP study PI) and Prof. Foltynie (UCL, ACT-PD co-chief investigator) both participated in the UP study, providing continuity of scientific judgment. The committee's willingness to invest a GBP 26M platform arm on a bile acid -- after seeing [[exenatide]] fail in Phase 3 -- indicates they view the 31P-MRS target engagement data as meaningfully different from prior repurposed-drug candidates.

The decision tree is straightforward. If the ACT-PD UDCA arm succeeds: a generic bile acid costing pennies per dose becomes the first disease-modifying PD therapy, immediately available worldwide. This would validate the mitochondrial rescue hypothesis, attract commercial interest in next-generation mitochondrial agents ([[nrg5051]], [[mtx325]]), and fundamentally alter the economics of PD treatment. If it fails: the bile acid / mitochondrial rescue hypothesis is closed at the clinical level for PD (definitive Phase 3 negative data), though mechanistically distinct mitochondrial approaches (mPTP, USP30, NAD+) would remain viable since they target different nodes of the same pathway.

## References

### Clinical Trials
- [UP Study (Phase 2)](https://clinicaltrials.gov/ct2/show/NCT03840005) -- NCT03840005
- [UP Study ISRCTN](http://www.isrctn.com/ISRCTN73371260) -- ISRCTN73371260
- [Minnesota Phase 1 Pilot](https://clinicaltrials.gov/ct2/show/NCT02967250) -- NCT02967250
- [EJS ACT-PD Platform](https://www.isrctn.com/ISRCTN17799294) -- ISRCTN17799294

### Key Publications
- [A Double-Blind, Randomized, Placebo-Controlled Trial of UDCA in Parkinson's Disease | Movement Disorders (Aug 2023)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.29450) -- Payne et al.
- [Ursocholanic acid rescues mitochondrial function in common forms of familial Parkinson's disease | Brain (Oct 2013)](https://academic.oup.com/brain/article-abstract/136/10/3038/328243) -- Mortiboys, Aasly, Bandmann
- [UDCA exerts beneficial effect on mitochondrial dysfunction in LRRK2 G2019S carriers and in vivo | Neurology (Sept 2015)](https://www.neurology.org/doi/abs/10.1212/wnl.0000000000001905) -- Mortiboys et al.
- [UP Study Protocol | BMJ Open (Aug 2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7409998/) -- protocol paper
- [UDCA protects dopaminergic neurons from oxidative stress via mitochondrial function, autophagy, and apoptosis in MPTP model | Neurosci Lett (2020)](https://www.sciencedirect.com/science/article/abs/pii/S0304394020307631)
- [Tauroursodeoxycholic acid: a potential therapeutic tool in neurodegenerative diseases | Transl Neurodegener (2022)](https://translationalneurodegeneration.biomedcentral.com/articles/10.1186/s40035-022-00307-z) -- Khalaf et al.
- [Treatment Selection and Prioritization for the EJS ACT-PD MAMS Trial Platform | Movement Disorders (2025)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.30190)
- [Outcome Measures for Disease-Modifying Trials in PD: EJS ACT-PD Consensus | J Parkinsons Dis (2023)](https://pubmed.ncbi.nlm.nih.gov/37545260/)

### Press Releases & Filings
- [The UP Study results | Cure Parkinson's (June 2023)](https://cureparkinsons.org.uk/2023/06/up-study/)
- [The UP Study: UDCA and Parkinson's | Cure Parkinson's](https://cureparkinsons.org.uk/research/research-projects/udca/)
- [Positive results from an early clinical trial for a drug boosting cell batteries | Parkinson's UK](https://www.parkinsons.org.uk/news/positive-results-early-clinical-trial-drug-boosting-cell-batteries-people-parkinsons)
- [EJS ACT-PD recruitment announcement | Cure Parkinson's (Oct 2025)](https://cureparkinsons.org.uk/2025/10/ejs-act-pd-recruitment-announcement/)
- [Largest-ever PD trial opens across UK | UCL News (Oct 2025)](https://www.ucl.ac.uk/news/2025/oct/largest-ever-parkinsons-disease-trial-opens-across-uk)

### Regulatory & Market
- [The UP Study | Health Research Authority](https://www.hra.nhs.uk/planning-and-improving-research/application-summaries/research-summaries/trial-of-ursodeoxycholic-acid-udca-for-pd-the-up-study/)
- [PD Drug Therapies in the Clinical Trial Pipeline: 2024 Update | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307066/)
- [Cure Parkinson's iLCT Programme](https://cureparkinsons.org.uk/research/ilct/)
