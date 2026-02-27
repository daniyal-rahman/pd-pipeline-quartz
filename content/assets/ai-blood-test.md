---
drug_name: "AI Blood Test"
aliases: ["UCL Blood Test", "GSL PD Panel", "Plasma Proteomics PD Test"]
target: "8-protein blood biomarker panel (plasma proteomics)"
mechanism: "Machine learning classifier applied to multiplexed mass spectrometry of 8 blood-based protein biomarkers whose concentrations are altered in PD, enabling pre-motor diagnosis up to 7 years before symptom onset"
modality: "diagnostic assay"
developer: "UCL / Guilford Street Laboratories"
company_type: "academic"
publicly_traded: false
partner: "UCLH NHS Foundation Trust"
partner_type: "academic"
stage: "Research"
status: "Active"
patient_population: "Pre-motor individuals (iRBD cohort) and early PD"
route_of_administration: "blood draw (venipuncture)"
key_biomarkers: ["8-protein plasma panel", "alpha-synuclein-associated proteins"]
confidence_rating: "5/10"
next_catalyst: "NHS clinical deployment / prospective validation study"
catalyst_date: "2026-2027"
thesis_cluster: "diagnostics"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/university-college-london]]"
partner_link: "[[companies/uclh-nhs-foundation-trust]]"
---

# AI Blood Test

## Summary

UCL and Guilford Street Laboratories (academic spinout, 2024) have developed a machine learning-based blood test that diagnosed PD with 100% accuracy and predicted conversion in 79% of pre-motor iRBD patients up to 7 years before symptom onset, published in Nature Communications (June 2024). The test analyzes a panel of 8 blood-based protein biomarkers via targeted multiplexed mass spectrometry. GSL secured an NHS partnership with UCLH in January 2025, targeting clinical deployment within 2 years. If prospective validation confirms retrospective accuracy, this becomes a population-level screening tool that fundamentally reshapes the PD therapeutic landscape -- enabling disease-modifying therapies like [[prasinezumab]] and [[aro-snca|ARO-SNCA]] to be tested and deployed at pre-motor stages. If accuracy degrades in larger, more heterogeneous populations, the test may still have value as an enrichment biomarker for clinical trials rather than a standalone diagnostic.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | UCLH NHS Foundation Trust |
| Deal Date | January 2025 |
| Upfront | Not disclosed |
| Total (Biobucks) | Not disclosed |
| Deal Type | Partnership |

## Notes

### Science
- Uses **targeted multiplexed mass spectrometry** to measure concentrations of 8 blood-based protein biomarkers that are differentially expressed in PD patients versus healthy controls
- The specific 8 proteins were identified through comprehensive plasma proteomic screening; the panel captures a multi-pathway signature rather than relying on a single analyte
- Machine learning classifier (trained on the 8-protein expression profile) distinguishes PD patients from controls and identifies a "Parkinson's-like" blood profile in pre-motor individuals
- Key scientific distinction vs. CSF-based diagnostics (e.g., [[asn51|alpha-synuclein SAA]]): blood draw is minimally invasive and scalable to population-level screening, whereas CSF requires lumbar puncture
- The iRBD cohort is a critical design feature -- 75-80% of iRBD patients eventually develop a synucleinopathy, making them a natural prodromal PD enrichment population
- Open question: whether the 8-protein panel captures alpha-synuclein-specific pathology or a broader neurodegeneration signature, which would affect specificity for PD vs. other synucleinopathies (MSA, DLB)
- The team is developing a **simpler blood spot test** (finger-prick format) that could further lower the barrier to screening

### Clinical

**Retrospective Discovery/Validation Study** | No NCT (academic study) | N=207 total | PD patients + iRBD + healthy controls
- **Cohorts:** Recently diagnosed motor PD (n=99), iRBD cohort 1 (n=18), iRBD cohort 2 longitudinal (n=54), healthy controls (n=36)
- **Primary endpoint:** Diagnostic accuracy of 8-protein ML classifier → **100% accuracy** distinguishing PD patients from controls
- **Key secondary:** Predictive accuracy in pre-motor iRBD → **79% classified as PD-like** blood profile; 16 patients confirmed to convert over 10-year follow-up
- **Prediction window:** Up to 7 years before motor symptom onset
- **Status:** Published (Nature Communications, June 2024)
- **Interpretation:** Striking accuracy in a small, well-defined cohort. The 100% figure reflects a retrospective, enriched population -- prospective validation in unselected populations is the critical next step. The 79% iRBD classification rate aligns with the known 75-80% conversion rate, which is reassuring but not independently confirmatory.

No prospective clinical trials registered as of February 2026. NHS deployment through the UCLH-GSL partnership represents the next stage of real-world validation.

### Financial
- **GSL founded 2024** as a UCL Business (UCLB) spinout -- one of 51 spinouts in 5 years from UCLB (which has raised a collective £2.9B)
- **Founders:** Prof. Kevin Mills, Dr. Tomas Baldwin, Dr. Wendy Heywood (all from UCL Great Ormond Street Institute of Child Health)
- **Funding:** EU Horizon 2020 grant, Parkinson's UK, NIHR GOSH Biomedical Research Centre, Szeben-Peto Foundation; GSL completed a follow-on investment round (amount undisclosed)
- **Revenue model:** GSL operates as a CRO providing biomarker services, with the PD diagnostic as a lead clinical product -- dual revenue streams (services + diagnostic commercialization)
- **Market context:** Blood-based PD diagnostics represent a potential multi-billion dollar market if disease-modifying therapies reach approval, as every DMT requires patient identification at the pre-motor or early stage
- **Comparator:** Amprion's CSF-based SAAmplify-aSYN is already commercial (Mayo Clinic partnership), but invasive lumbar puncture limits scalability. A validated blood test would command pricing and volume advantages.

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[ai-blood-test]] | Research | Active | UCL / Guilford Street Laboratories | diagnostic assay |

- The PD diagnostics space is currently dominated by CSF-based alpha-synuclein seed amplification assays (SAA) -- Amprion's SAAmplify is the commercial leader with Mayo Clinic distribution
- PET tracers represent the imaging-based competitor: SynuSight's 18F-FD4 and Merck's MK-7337 aim to visualize alpha-synuclein deposits directly, but PET is expensive ($3,000-5,000/scan) and limited to specialized centers
- The UCL/GSL blood test's advantage is **scalability** -- a standard blood draw processed through mass spectrometry is orders of magnitude cheaper and more accessible than CSF collection or PET imaging
- If validated prospectively, the blood test could serve as a first-line screen that triages patients into confirmatory CSF SAA or PET imaging, creating a tiered diagnostic pathway rather than directly competing with existing modalities
- Key risk: other groups are pursuing blood-based PD biomarkers (including alpha-synuclein SAA in blood, neurofilament light chain panels). First-mover advantage matters but is not decisive if a competitor achieves better specificity in a larger validation

## Analysis

The 100% diagnostic accuracy headline is both the strongest selling point and the greatest source of skepticism. In a retrospective study of 207 individuals drawn from well-characterized research cohorts, perfect classification is achievable because the ML model was trained and validated on the same tightly defined populations. The real test is whether this holds in the wild -- in primary care settings with diverse demographics, comorbidities, medications, and the full spectrum of parkinsonian syndromes that mimic idiopathic PD. The iRBD cohort is a well-chosen validation population (high conversion rate, biologically homogeneous), but it represents the easiest diagnostic challenge, not the hardest.

**Analytical estimate -- Probability of successful prospective validation (maintaining >90% accuracy in a larger NHS cohort): 35-45%.** This is our assessment, not from a published source. The reasoning: Base rate for biomarker panels translating from discovery to clinical-grade diagnostics is ~10-15%. Adjustments upward: mass spectrometry platform is mature and reproducible (+10%), the 8-protein panel captures multiple pathways reducing single-analyte fragility (+5%), NHS partnership provides infrastructure for rapid prospective testing (+5%), iRBD prediction aligns with known conversion rates providing biological plausibility (+10%). Adjustments downward: small sample size (N=207 total, only 99 PD) (-10%), no independent external validation cohort reported (-5%), retrospective design allows overfitting (-5%). Net: ~35-45%.

The strategic significance of this test extends beyond GSL's commercial prospects. Every disease-modifying therapy in the PD pipeline -- from [[prasinezumab]] to [[aro-snca|ARO-SNCA]] to [[bemdaneprocel]] -- faces the same fundamental challenge: identifying patients early enough for intervention to matter. If a validated, scalable blood test can identify pre-motor PD patients, it transforms trial enrollment (smaller trials, shorter duration, cleaner signal) and commercial launch (addressable market expands from diagnosed PD to at-risk populations). The UCLH-GSL NHS partnership is the near-term catalyst; if early NHS deployment data confirms the retrospective findings, GSL becomes a high-value acquisition target for any company with a PD disease-modification program.

The decision tree is asymmetric: if prospective validation succeeds, the diagnostic becomes foundational infrastructure for the entire PD field; if it fails to replicate, the approach may still have utility as a research enrichment tool, but the commercial thesis collapses. Given the current stage (no prospective trial, small retrospective dataset, academic spinout with limited capital), this is a high-potential but early-stage opportunity that requires monitoring rather than immediate action.

## References

### Key Publications
- [Plasma proteomics identify biomarkers predicting Parkinson's disease up to 7 years before symptom onset | Nature Communications (June 2024)](https://www.nature.com/articles/s41467-024-48961-3)

### Press Releases & Filings
- [Blood test could predict Parkinson's seven years before symptoms | UCL News (June 2024)](https://www.ucl.ac.uk/news/2024/jun/blood-test-could-predict-parkinsons-seven-years-symptoms)
- [NHS patients to benefit from state-of-the-art diagnostic tests for Parkinson's & Mitochondrial diseases | UCLH (Jan 2025)](https://www.uclh.nhs.uk/news/nhs-patients-benefit-state-art-diagnostic-tests-parkinsons-mitochondrial-diseases-resulting-uk-first-partnership)
- [UCLH and GSL's partnership brings diagnostics hope for Parkinson's and other diseases | UCLB (Jan 2025)](https://www.uclb.com/2025/01/09/uclh-and-gsls-partnership-brings-diagnostics-hope-for-parkinsons-and-other-diseases/)
- [UCLB spinout GSL to help researchers detect diseases earlier | UCLB (Oct 2024)](https://www.uclb.com/2024/10/14/uclb-spinout-gsl-to-help-researchers-detect-diseases-earlier/)

### Regulatory & Market
- [AI helps detect Parkinson's with 100% accuracy 7 years before symptoms | Interesting Engineering](https://interestingengineering.com/health/new-ai-blood-test-for-parkinson)
- [Blood test could predict Parkinson's seven years before symptoms | ScienceDaily](https://www.sciencedaily.com/releases/2024/06/240618115251.htm)
