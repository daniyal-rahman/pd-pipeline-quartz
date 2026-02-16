---
drug_name: "Exenatide"
aliases: ["Bydureon", "Byetta", "Exenatide-PD3"]
target: "GLP-1 receptor (neuroprotection/repurposed)"
mechanism: "GLP-1 receptor agonist — originally a diabetes drug, repurposed for potential neuroprotective effects via anti-inflammatory, anti-apoptotic, and neurotrophic signaling"
modality: "small molecule"
developer: "UCL (Tom Foltynie)"
company_type: "academic"
publicly_traded: false
partner: "AstraZeneca (originator of exenatide)"
partner_type: "big pharma"
stage: "Phase 3"
status: "Failed"
patient_population: "Moderate PD on stable dopaminergic therapy"
route_of_administration: "SC (weekly injection)"
key_biomarkers: ["DaT-SPECT", "CSF exenatide levels", "MDS-UPDRS Part III (OFF)"]
confidence_rating: "1/10"
next_catalyst: "Subgroup analyses (glucose metabolism markers) and implications for next-gen GLP-1 agonists"
catalyst_date: "2025-2026"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/university-college-london]]"
partner_link: "[[companies/astrazeneca]]"
---

# Exenatide

## Summary

Exenatide (Bydureon), a GLP-1 receptor agonist originally developed by AstraZeneca for type 2 diabetes, was the first GLP-1 drug to reach Phase 3 in Parkinson's disease. The Exenatide-PD3 trial (UCL, academic-led) published negative results in The Lancet in February 2025: no benefit on motor progression (p=0.47), no DaT-SPECT signal, and low CSF penetration — a definitive failure after 15 years of development from open-label proof-of-concept through Phase 3. This result is critical landscape context because it was the largest and longest GLP-1 agonist trial in PD (N=194, 96 weeks) and directly challenges the earlier positive Phase 2 signal (Lancet 2017). The field now pivots to next-generation GLP-1 agonists with better brain penetration — lixisenatide showed a positive Phase 2 signal (LIXIPARK, NEJM 2024), and semaglutide and NLY01 trials are ongoing. For the broader disease-modification landscape, the exenatide failure reinforces that mechanism-of-action plausibility and open-label signals do not survive rigorous Phase 3 testing, a pattern also seen in [[cinpanemab]] and [[buntanetap]].

## Notes

### Science
- GLP-1 receptor agonists activate a G-protein-coupled receptor expressed on neurons and glia, triggering downstream anti-inflammatory (reduced microglial activation), anti-apoptotic (Bcl-2 upregulation), and neurotrophic (BDNF, GDNF-like) signaling cascades
- Preclinical rationale was strong: exenatide protected dopaminergic neurons in MPTP and 6-OHDA rodent models of PD, reduced alpha-synuclein aggregation, and improved mitochondrial function
- The core pharmacological problem is **brain penetration**: exenatide is a 39-amino-acid peptide with limited BBB crossing. CSF analysis from PD3 confirmed only low levels reached the CNS — a possible explanation for the Phase 3 failure despite the target being biologically relevant
- Exenatide is a first-generation GLP-1 agonist (exendin-4 based). Newer agents like lixisenatide, semaglutide, and NLY01 (PEGylated exendin-4 designed for enhanced CNS penetration) may have different pharmacokinetic profiles in the brain
- Key distinction from disease-specific targets: GLP-1 agonism is a broadly neuroprotective strategy, not targeting a PD-specific pathology like alpha-synuclein or LRRK2. This means the effect size, if any, may be modest and require very large trials to detect
- Epidemiological data from diabetes registries suggested reduced PD incidence in GLP-1 agonist users — but confounding (diabetes itself, healthy-user bias) makes causal inference difficult

### Clinical

**Exenatide-PD (Open-Label Proof of Concept)** | NCT TBD | N=45 | Moderate PD
- **Primary endpoint:** Safety/tolerability and MDS-UPDRS changes → Exenatide group improved by 2.7 points vs. 2.2-point decline in controls (p=0.037)
- **Key secondary:** Effects persisted 12 months after drug cessation — 5.6-point advantage on MDS-UPDRS III motor subscale and 5.3-point advantage on Mattis DRS-2 cognitive scale
- **Status:** Completed (2013, published in J Clin Invest)
- **Interpretation:** Open-label, non-blinded design introduced substantial placebo/expectation bias. The persistence of effect post-washout was the key argument for disease modification rather than symptomatic benefit. Generated enormous excitement but, in retrospect, did not survive rigorous blinded replication.

**Exenatide-PD (Phase 2)** | NCT01971242 | N=62 | Moderate PD on stable medication
- **Primary endpoint:** MDS-UPDRS Part III OFF-medication at 60 weeks (48 weeks treatment + 12-week washout) → Adjusted difference of 3.5 points favoring exenatide (p=0.0318)
- **Key secondary:** DaT-SPECT — no significant difference. Cognitive and non-motor measures — no significant differences
- **Status:** Completed (2017, published in The Lancet)
- **Interpretation:** The motor signal survived blinding and washout, which was the strongest evidence for disease modification at the time. However, the effect was confined to a single endpoint (motor OFF score), with no biomarker or imaging confirmation. Sample size (N=62) was underpowered to distinguish small real effects from noise. This result motivated the Phase 3 investment.

**Exenatide-PD3 (Phase 3)** | NCT04232969 | N=194 | Moderate PD on stable dopaminergic therapy
- **Primary endpoint:** MDS-UPDRS Part III OFF-medication at 96 weeks → Exenatide worsened by 5.7 points (SD 11.2) vs. placebo worsened by 4.5 points (SD 11.4); adjusted coefficient 0.92 [95% CI -1.56 to 3.39], **p=0.47**
- **Key secondary:** DaT-SPECT imaging — no difference between groups. No benefit on any secondary or exploratory endpoint
- **CSF analysis:** Low exenatide levels detected in CSF, suggesting limited brain penetration
- **Safety:** Exenatide was safe and well tolerated; no new safety signals. GI side effects consistent with GLP-1 class
- **Status:** Completed summer 2024; published February 2025 in The Lancet
- **Interpretation:** Definitive negative result. Not a borderline miss — the direction of the primary endpoint numerically favored placebo. The low CSF penetration finding provides a pharmacological explanation: the drug may simply not have reached the target in sufficient concentrations. This does not invalidate GLP-1 receptor agonism as a PD strategy, but it does invalidate exenatide specifically as the vehicle.

### Financial
- **Funding:** Exenatide-PD3 was funded by the UK National Institute for Health and Care Research (NIHR), Cure Parkinson's, and the Van Andel Institute — entirely non-commercial
- **AstraZeneca role:** Originator of exenatide (marketed as Bydureon/Byetta for diabetes), provided drug supply but did not fund or sponsor the PD trials. AstraZeneca has no active PD pipeline stake in exenatide
- **No commercial PD development path:** As a generic-eligible diabetes drug, exenatide has no patent-protected commercial future in PD even if it had succeeded. The trials were academically motivated, not commercially driven
- **Market impact on GLP-1 landscape:** The failure created a brief narrative headwind for GLP-1 agonists in neurodegeneration, but the field quickly differentiated: lixisenatide's positive LIXIPARK Phase 2 (NEJM 2024) and Novo Nordisk's semaglutide Alzheimer's trials (EVOKE) sustained investor interest in the broader GLP-1-for-neurodegeneration thesis
- **Estimated cost:** Phase 3 trial cost was likely in the range of $15-25M (academic-led, UK NHS infrastructure, relatively small N=194), modest by pharma standards

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "GLP-1") AND file.name != "exenatide"
SORT stage DESC
```

- The GLP-1 agonist field in PD now includes multiple agents at various stages: **lixisenatide** (positive Phase 2, LIXIPARK, Meissner et al. NEJM 2024 — 3.08-point advantage on MDS-UPDRS III, p=0.007, but high nausea at 46%), **NLY01** (Neuraly, PEGylated exendin-4 designed for CNS penetration — Phase 2 missed primary but showed signal in patients <60, dose-related), and **semaglutide** (Phase 2, NCT03659682, Oslo — ongoing)
- Key competitive question is **brain penetration**: exenatide's failure may be pharmacokinetic, not mechanistic. Agents engineered for better CNS access (NLY01) or with intrinsically different PK profiles (lixisenatide, semaglutide) may succeed where exenatide failed
- Lixisenatide's LIXIPARK success creates the strongest counterpoint to exenatide's failure — both are GLP-1 agonists but lixisenatide showed a 2-month washout-persistent motor benefit, suggesting the target is valid even if this specific drug is not
- The broader disease-modification competitive set includes [[prasinezumab]] (alpha-synuclein antibody, Phase 3), [[biib122|BIIB122]] (LRRK2 inhibitor, Phase 3), and [[pariceract]] (GBA1 activator, Phase 2) — exenatide's failure narrows the "non-target-specific neuroprotection" approach and increases relative attractiveness of genetically validated, target-specific strategies

## Analysis

The exenatide-PD3 failure is one of the most instructive negative results in the PD disease-modification field. The trajectory — exciting open-label data (2013), encouraging Phase 2 (2017), definitive Phase 3 failure (2025) — recapitulates a pattern seen repeatedly in neurodegeneration: early signals inflated by small samples, open-label bias, and single-endpoint positivity do not survive adequately powered blinded trials. The parallel to [[cinpanemab]] (positive Phase 1 biomarker data, clean Phase 2 failure) is direct.

The CSF penetration finding is the most important mechanistic takeaway. If exenatide simply did not reach the brain in sufficient concentrations, then the Phase 3 failure is about drug delivery, not about the GLP-1 target. This preserves the thesis for next-generation agents. Lixisenatide's LIXIPARK Phase 2 success (NEJM 2024) supports this interpretation — a structurally different GLP-1 agonist showed a motor benefit that persisted through washout, the hallmark of disease modification rather than symptomatic effect. However, LIXIPARK was also small (N=156) and only 12 months, and the 46% nausea rate raises questions about unblinding.

**Analytical estimate — probability that any GLP-1 agonist achieves Phase 3 success in PD within the next 5 years: 15-20%.** This is our assessment, not from a published source. The reasoning: base rate for disease-modifying PD drugs reaching Phase 3 success is very low (<5%); adjustment upward for lixisenatide Phase 2 signal (+10%), strong preclinical rationale across multiple models (+5%), epidemiological signal from diabetes registries (+5%); adjustment downward for exenatide Phase 3 failure (-10%), brain penetration uncertainty for all peptide-based GLP-1 agonists (-5%), historical pattern of Phase 2 signals not replicating in PD Phase 3 (-5%). The semaglutide trials will be the next definitive test, as semaglutide has demonstrated greater BBB penetration in preclinical models than exenatide.

For the broader PD landscape, exenatide's failure reinforces the case for target-specific strategies — [[biib122|LRRK2 inhibition]], [[pariceract|GBA1 activation]], [[prasinezumab|alpha-synuclein immunotherapy]] — over broadly neuroprotective approaches. The GLP-1 story is not over, but the bar for the next Phase 3 entrant has risen: any program will need to demonstrate adequate CSF exposure and a cleaner biomarker signal before committing to a large trial.

## References

### Clinical Trials
- [Exenatide-PD3 Phase 3](https://clinicaltrials.gov/study/NCT04232969) — NCT04232969
- [Exenatide-PD Phase 2](https://clinicaltrials.gov/ct2/show/NCT01971242) — NCT01971242

### Key Publications
- [Exenatide once a week versus placebo as a potential disease-modifying treatment for people with Parkinson's disease (PD3 Phase 3) | The Lancet (Feb 2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02808-3/fulltext)
- [Exenatide once weekly versus placebo in Parkinson's disease (Phase 2) | The Lancet (Aug 2017)](https://pubmed.ncbi.nlm.nih.gov/28781108/)
- [Exenatide and the treatment of patients with Parkinson's disease (Open-Label) | J Clin Invest (2013)](https://pubmed.ncbi.nlm.nih.gov/23728174/)
- [Motor and cognitive advantages persist 12 months after exenatide exposure in Parkinson's disease | J Parkinson's Disease (2014)](https://pubmed.ncbi.nlm.nih.gov/24662192/)
- [First phase 3 trial of GLP-1 receptor agonist for neurodegeneration (Editorial) | The Lancet (2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)00161-8/abstract)
- [Trial of Lixisenatide in Early Parkinson's Disease (LIXIPARK) | NEJM (2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2312323)
- [Safety, tolerability, and efficacy of NLY01 in early untreated Parkinson's disease | Lancet Neurol (2023)](https://pubmed.ncbi.nlm.nih.gov/38101901/)
- [Post hoc analysis of the Exenatide-PD trial — Factors that predict response | Eur J Neurosci (2018)](https://pubmed.ncbi.nlm.nih.gov/30070753/)
- [Exenatide-PD3 study protocol | BMJ Open (2021)](https://pubmed.ncbi.nlm.nih.gov/34049922/)

### Press Releases & Filings
- [GLP-1 drug shows little benefit for people with Parkinson's disease | UCL News (Feb 2025)](https://www.ucl.ac.uk/news/2025/feb/glp-1-drug-shows-little-benefit-people-parkinsons-disease)
- [Exenatide-PD3 results published | Cure Parkinson's (Feb 2025)](https://cureparkinsons.org.uk/2025/02/exenatide-pd3-results-published/)
- [The Phase 3 Exenatide results | Cure Parkinson's (Mar 2025)](https://cureparkinsons.org.uk/2025/03/exenatide3/)
- [Results from the phase 3 trial of exenatide published | Parkinson's UK (2025)](https://www.parkinsons.org.uk/news/2025/results-phase-3-trial-exenatide-published)
- [Exenatide, a GLP-1 Drug, Shows No Impact on Parkinson's Symptoms | MJFF (2025)](https://www.michaeljfox.org/news/exenatide-glp-1-drug-shows-no-impact-parkinsons-symptoms)
- [AstraZeneca's diabetes drug fails to slow Parkinson's progression in UCL trial | Clinical Trials Arena](https://www.clinicaltrialsarena.com/news/astrazeneca-diabetes-drug-fails-to-slow-parkinsons-progression-in-ucl-trial/)

### Regulatory & Market
- [After the recent exenatide results, what's next in Parkinson's disease research? | Van Andel Institute (2025)](https://www.vai.org/article/after-the-recent-exenatide-results-whats-next-in-parkinsons-disease-research-and-clinical-trials/)
- [GLP-1 receptor agonists in Parkinson's disease: systematic review with meta-analysis | PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12374370/)
