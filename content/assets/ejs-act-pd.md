---
drug_name: "EJS ACT-PD Platform"
aliases: ["Edmond J Safra Accelerating Clinical Trials in Parkinson's Disease", "ACT-PD"]
target: "multiple (AT1R / PGK1 / TUDCA-mitochondria)"
mechanism: "Multi-arm multi-stage platform trial testing repurposed drugs for disease modification: telmisartan (AT1R blocker reducing neuroinflammation via brain renin-angiotensin system), terazosin (PGK1 activator enhancing glycolysis and neuronal ATP), and UDCA (mitochondrial rescue)"
modality: "platform"
developer: "UCL / MRC Clinical Trials Unit"
company_type: "academic"
publicly_traded: false
partner: "Cure Parkinson's / Parkinson's UK / MJFF / Van Andel Institute"
partner_type: "academic"
stage: "Phase 3"
status: "Active"
patient_population: "Adults aged 30+ with clinical PD diagnosis on dopaminergic therapy"
route_of_administration: "oral"
key_biomarkers: ["MDS-UPDRS Parts 1 & 2", "wearable sensor data", "molecular biomarkers (MJFF sub-study)"]
confidence_rating: "4/10"
next_catalyst: "Interim futility analysis (first arm)"
catalyst_date: "2028-2029"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/university-college-london]]"
partner_link: "[[companies/cure-parkinsons]]"
---

# EJS ACT-PD Platform

## Summary

EJS ACT-PD (Edmond J Safra Accelerating Clinical Trials in Parkinson's Disease) is the world's largest PD trial -- a Phase 3 multi-arm multi-stage (MAMS) platform run by UCL's MRC Clinical Trials Unit (academic) with co-chief investigators Prof. Thomas Foltynie and Prof. Camille Carroll. Funded at GBP 26M by an MRC/NIHR partnership, Cure Parkinson's, MJFF, Parkinson's UK, and others, the trial began recruiting in October 2025 across 40+ UK sites with a target of 1,600 participants (400 per arm). The first two arms test repurposed generics -- telmisartan (AT1R blocker) and terazosin (PGK1 activator) -- against a shared placebo, with ursodeoxycholic acid (UDCA) planned as a third arm in 2026. The primary endpoint is a 30% reduction in rate of progression on MDS-UPDRS Parts 1 & 2 combined over 36 months. The MAMS design allows ineffective arms to be dropped at interim analysis and new arms to be added, potentially cutting drug assessment timelines by ~25% (~3 years) vs. sequential standalone trials. If any arm demonstrates disease modification, it would be the first validated neuroprotective therapy in PD and a landmark for the repurposed-drug approach championed by Cure Parkinson's iLCT programme. If all arms fail, it reinforces the pattern seen with [[exenatide]] -- that strong epidemiological and preclinical signals for repurposed generics do not survive Phase 3 testing -- and redirects capital toward novel mechanisms like [[dapansutrile|NLRP3 inhibition]], [[bhv-8000|Trk-B activation]], and [[nrg5051|mPTP inhibition]].

## Notes

### Science

**Platform Design (MAMS)**
- Multi-arm multi-stage design allows multiple drugs to be tested against a single shared placebo arm, reducing the total patients required vs. running individual trials and enabling direct cross-arm comparisons
- Interim futility analyses can drop underperforming arms early, redirecting resources to new candidates -- the trial is designed to continuously cycle treatments through the platform
- Drug candidates are selected via Cure Parkinson's international Linked Clinical Trials (iLCT) committee, a panel of 20-30 PD experts who have evaluated 239 drug dossiers and 171 unique agents since 2012, scoring candidates on preclinical evidence, epidemiological data, safety profile, and mechanistic plausibility
- This is the first MAMS platform trial in PD, adapting a methodology proven in oncology (e.g., STAMPEDE in prostate cancer) and COVID-19 (RECOVERY trial, also run by UK academic trialists)

**Arm 1: Telmisartan (AT1R blocker)**
- Angiotensin II type 1 receptor (AT1R) antagonist, currently approved as an oral antihypertensive (generic)
- The brain renin-angiotensin system (RAS) is implicated in PD pathogenesis: AT1R activation promotes microglial activation, oxidative stress, and dopaminergic neurodegeneration. High AT1R expression marks the most vulnerable neuronal populations in human PD
- AT1R activation directly promotes neuronal and glial alpha-synuclein aggregation and transmission (Nature npj Parkinson's Disease, 2024) -- blocking AT1R could interrupt a key upstream driver of synuclein pathology
- Telmisartan also activates PPAR-gamma, providing additional anti-inflammatory and neuroprotective effects beyond pure AT1R blockade
- In MPTP mouse models, telmisartan protected mitochondrial function, prevented neuronal apoptosis, attenuated dopaminergic degeneration, and preserved gait via Akt/GSK3-beta/PGC1-alpha signaling
- Telmisartan also reduced alpha-synuclein levels and increased BDNF and GDNF expression in preclinical models
- Clinical advantage: decades of human safety data, oral dosing, generic availability, and well-characterized PK/PD
- Key uncertainty: whether systemically administered telmisartan achieves sufficient brain concentrations, as AT1R blockade in the periphery (blood pressure lowering) may limit tolerability at doses needed for CNS effects

**Arm 2: Terazosin (PGK1 activator / alpha-1 blocker)**
- Alpha-1 adrenergic receptor antagonist, currently approved for benign prostatic hyperplasia (BPH) and hypertension (generic)
- The PD-relevant mechanism is independent of alpha-1 blockade: terazosin binds and activates phosphoglycerate kinase 1 (PGK1), a rate-limiting glycolytic enzyme, enhancing cellular ATP production
- PGK1 activation is particularly relevant in PD because dopaminergic neuron axons are exceptionally energy-demanding -- even a small boost to glycolytic ATP supply can sustain axonal function when glucose availability is compromised
- DJ-1, a protein whose loss-of-function causes autosomal recessive PD (PARK7), is a necessary partner for PGK1 -- DJ-1 impairment reduces PGK1 activity, and terazosin partially rescues this deficit, providing direct genetic validation for the target
- Epidemiological evidence from three independent databases (Truven MarketScan, Danish Nationwide Health Registries, Optum Research) shows reduced PD risk in terazosin users vs. tamsulosin users (an alpha-1 blocker that does not activate PGK1), and slowed motor progression in PD patients already taking terazosin (PPMI database)
- Preclinical neuroprotection demonstrated in toxin-induced and genetic PD models across mice, rats, flies, and iPSC-derived neurons
- A pilot dose-finding study in PD patients confirmed target engagement (PGK1 activation) and adequate safety
- Key uncertainty: whether the magnitude of PGK1 activation achievable with terazosin (a partial activator originally designed for alpha-1 blockade) is sufficient for clinical neuroprotection, or whether next-generation PGK1-optimized analogs would be required

**Arm 3 (planned 2026): Ursodeoxycholic acid (UDCA)**
- Bile acid derivative currently approved for primary biliary cholangitis and gallstone dissolution (generic)
- Proposed neuroprotective mechanism via mitochondrial rescue -- improves mitochondrial membrane potential, reduces oxidative stress, and has anti-apoptotic effects
- Previously tested in PD in a small Phase 2 trial (UP study) led by the Sheffield group, with positive biomarker signals on mitochondrial function
- Planned addition to the platform in 2026 as the third treatment arm

### Clinical

**EJS ACT-PD (Phase 3 MAMS)** | ISRCTN17799294 | N=1,600 (400 per arm) | Adults 30+ with PD on dopaminergic therapy
- **Primary endpoint:** 30% reduction in rate of progression on MDS-UPDRS Parts 1 & 2 combined over 36 months
- **Key secondary:** Wearable technology-derived motor/gait measures (MJFF-funded sub-study); molecular biomarkers predictive of treatment response (MJFF-funded sub-study); quality of life; health economic outcomes
- **Design:** Randomised, double-blind, placebo-controlled, multi-arm multi-stage. Each treatment arm tested against the shared placebo. Interim futility analyses enable dropping ineffective arms and adding new ones
- **Sites:** 40+ hospitals across England, Wales, Scotland, and Northern Ireland; initial recruiting sites at UCLH (London) and Clinical Ageing Research Unit (Newcastle); remaining sites planned to open by mid-2026
- **Investigators:** Prof. Thomas Foltynie (UCL Queen Square, co-chief investigator), Prof. Camille Carroll (Newcastle University, co-chief investigator), Prof. Sonia Gandhi (UCL/Francis Crick Institute, innovation programme co-lead)
- **Visit schedule:** First visit in-person (~2 hours); subsequent visits every 6 months, in-person or remote (~30 min to 2 hours); 10 appointments + 3 phone calls over 36 months
- **Recruitment:** Began October 2025; 3 sites active as of early 2026; target recruitment completion ~September 2029
- **Funding duration:** August 2024 to July 2031
- **Status:** Actively recruiting
- **Interpretation:** The MAMS design is the trial's core innovation -- it can test 3+ drugs in the time and cost of one conventional Phase 3, and the shared placebo reduces total patient burden. MDS-UPDRS Parts 1 & 2 (non-motor and motor experiences of daily living) as primary endpoint avoids the in-clinic examiner variability of Part III and may better capture meaningful patient-reported disease progression. The 36-month duration is appropriate for disease modification. The repurposed-drug approach enables immediate GMP drug supply (all arms are cheap, widely manufactured generics) but limits commercial incentive -- no pharma company owns or will own the PD indication for these molecules.

**Terazosin Pilot Study** | NCT04386187 | N=unknown | PD patients
- **Primary endpoint:** Target engagement (PGK1 activation) and safety
- **Key finding:** Confirmed PGK1 target engagement at clinically tolerable doses
- **Status:** Completed
- **Interpretation:** Provided the mechanistic bridge between epidemiological data and the Phase 3 arm in EJS ACT-PD

### Financial
- **Total programme budget: GBP 26M** (~$33M) -- the largest non-pharma-funded PD trial in history
- **Funders:** MRC/NIHR partnership (UK government), Cure Parkinson's, MJFF, Parkinson's UK, The John Black Charitable Foundation, The Gatsby Charitable Foundation, Van Andel Institute
- **Named after:** Edmond J. Safra Foundation (major philanthropic donor)
- **Cost advantage:** All treatment arms are off-patent generics costing pennies per dose -- eliminates drug supply costs and enables indefinite treatment if efficacy is demonstrated
- **No commercial sponsor:** Unlike company-sponsored Phase 3 trials (typically $200-500M), this trial is funded entirely by government and nonprofit sources. No pharma company has licensed or co-developed any arm for PD
- **Context:** Cure Parkinson's has a track record funding academic disease-modification trials -- the [[exenatide]] Phase 3 (Exenatide-PD3, failed 2025), the [[ambroxol]] Phase 3 (ASPro-PD, ongoing), the [[lixisenatide]] Phase 3 (in planning), and the [[dapansutrile]] Phase 2 (DAPA-PD, recruiting). The MAMS design is explicitly intended to improve the economics of this model by sharing infrastructure across multiple arms
- **No peak sales estimates applicable** -- these are generic drugs with no patent exclusivity; even if efficacy is demonstrated, the commercial pathway would require regulatory approval followed by generic prescribing, not a branded launch

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[sargramostim]] | Phase 1b | Active | University of Nebraska Medical Center (Howard Gendelman) | recombinant protein (cytokine) |
| [[vgn-r09b]] | Phase 1/2 | Active | Shanghai Vitalgen BioPharma | AAV gene therapy |
| [[liraglutide]] | Phase 2 | Active | Academic (Cedars-Sinai / Cure Parkinson's) | small molecule |
| [[lixisenatide]] | Phase 2 | Active | Toulouse University Hospital (academic) | small molecule |
| [[pt320]] | Phase 2 | Failed | Peptron | small molecule |
| [[semaglutide]] | Phase 2 | Active | Novo Nordisk / Osaka University | small molecule |
| [[exenatide]] | Phase 3 | Failed | UCL (Tom Foltynie) | small molecule |

- EJS ACT-PD competes in the broader "neuroprotection via repurposed drugs" space alongside [[exenatide]] (failed Phase 3), [[lixisenatide]] (positive Phase 2, Phase 3 planned), [[semaglutide]] (Phase 2 ongoing), [[ambroxol]] (Phase 3 ongoing), and [[nicotinamide-riboside]] (Phase 3 results pending)
- The telmisartan arm's AT1R/neuroinflammation hypothesis overlaps mechanistically with other anti-inflammatory approaches: [[dapansutrile]] (NLRP3 inhibition), [[selnoflast]] (Roche NLRP3 inhibitor), and [[vtx3232]] (Ventus NLRP3 inhibitor), though the specific AT1R/RAS pathway is distinct
- The terazosin arm's bioenergetic/glycolysis hypothesis aligns with the broader mitochondrial/energy metabolism cluster: [[nrg5051]] (mPTP inhibition), [[nicotinamide-riboside]] (NAD+ replenishment), and [[mtx325]] (USP30 inhibition), though PGK1 activation via glycolysis enhancement is a unique mechanism
- The planned UDCA arm addresses mitochondrial rescue, directly competing with [[nrg5051]] and the NAD+ pathway drugs
- **Key competitive distinction:** EJS ACT-PD tests cheap generics via nonprofit funding, while most competitors are proprietary molecules backed by pharma economics. If a generic succeeds, it is immediately available globally at minimal cost -- transformative for patients but commercially irrelevant for drug companies. This creates an unusual dynamic where success in EJS ACT-PD would not directly threaten proprietary programs (which target different mechanisms) but would validate the disease-modification concept and potentially accelerate regulatory acceptance of other agents
- The MAMS design itself is a competitive advantage in throughput -- it can evaluate multiple hypotheses simultaneously, while each competitor runs standalone trials requiring separate infrastructure
- Prof. Thomas Foltynie, co-chief investigator, previously led the [[exenatide]] programme from Phase 2 through Phase 3. His willingness to lead a new platform after the exenatide failure, selecting entirely different mechanisms, suggests scientific conviction in the iLCT drug selection process rather than persistence with a failed hypothesis

## Analysis

EJS ACT-PD is a structurally important trial regardless of whether any individual arm succeeds. The MAMS platform design -- proven in oncology and infectious disease but novel in neurodegeneration -- addresses the fundamental throughput problem in PD drug development: testing one drug at a time in 3-5 year Phase 3 trials against a disease with no validated surrogate endpoints means decades of sequential failures before finding a winner. By running arms in parallel with shared infrastructure and placebo, the platform compresses this timeline and reduces per-drug cost. If the platform itself proves operationally viable (recruitment, retention, data quality), it becomes reusable infrastructure for the entire PD field, independent of whether telmisartan or terazosin works.

**Analytical estimate -- Probability that any single arm demonstrates disease modification: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: repurposed drugs in PD disease-modification trials have a 0% success rate to date ([[exenatide]] Phase 3 failed, isradipine Phase 3 failed, creatine Phase 3 failed, coenzyme Q10 Phase 3 failed, inosine Phase 3 failed)
- Adjustments upward for telmisartan: strong preclinical package including alpha-synuclein aggregation mechanism (+3%), novel pathway not previously tested in PD Phase 3 (+3%), PPAR-gamma dual activity (+2%)
- Adjustments upward for terazosin: epidemiological evidence across three independent databases (+5%), genetic validation via DJ-1/PGK1 link (+5%), pilot study confirming target engagement (+3%)
- Adjustments downward: epidemiological associations have never translated to positive Phase 3 results in PD (-5%), blood pressure lowering may limit tolerable dose and CNS exposure (-3%), 36-month endpoint requires sustained effect magnitude (-3%)
- Net per arm: ~10-15% (terazosin slightly higher than telmisartan due to genetic validation and epidemiological depth)

**Analytical estimate -- Probability that the platform generates at least one positive arm across its lifetime (including future arms): 25-35%.** This is our assessment, not from a published source. The reasoning: the MAMS design is explicitly built to cycle through multiple candidates; if the first two fail, the infrastructure persists for UDCA and subsequent arms. Over 5-10 arms tested, even with per-arm success rates of 10-15%, the cumulative probability of at least one hit rises meaningfully.

**Signal analysis:** The funding consortium is the most important signal. GBP 26M from government (MRC/NIHR), four major PD charities, and two foundations represents the largest coordinated bet on disease modification outside of pharma. This consortium previously funded [[exenatide]] Phase 3 -- they saw that fail and chose to invest more, not less, in a platform designed to test drugs faster. The selection of telmisartan and terazosin by the iLCT committee (which evaluated 239 dossiers) over other repurposing candidates signals that these two drugs had the strongest combined evidence packages. The co-chief investigators (Foltynie, Carroll) and innovation lead (Gandhi at the Francis Crick Institute) represent top-tier UK neuroscience leadership. The embedded MJFF sub-studies on wearables and molecular biomarkers ensure the platform generates value even if the drugs fail -- by validating digital endpoints and identifying biological predictors of treatment response for future trials.

The decision tree is asymmetric. If an arm succeeds: a generic drug, costing pennies, becomes the first disease-modifying PD therapy -- this would be one of the most impactful clinical results in neurology and would reshape the regulatory and scientific landscape for every other disease-modification program ([[prasinezumab]], [[aro-snca]], [[biib122]], [[pariceract]]). If all arms fail: the platform infrastructure persists, the MAMS methodology is validated or refined, and the field gains definitive negative data on AT1R blockade and PGK1 activation -- closing two hypotheses cleanly rather than leaving them in the ambiguous "underpowered Phase 2" zone that has plagued PD for decades.

## References

### Clinical Trials
- [EJS ACT-PD](https://www.isrctn.com/ISRCTN17799294) -- ISRCTN17799294
- [Terazosin Pilot Study](https://clinicaltrials.gov/ct2/show/NCT04386187) -- NCT04386187

### Key Publications
- [Treatment Selection and Prioritization for the EJS ACT-PD MAMS Trial Platform | Movement Disorders (2025)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.30190)
- [Outcome Measures for Disease-Modifying Trials in PD: Consensus Paper by the EJS ACT-PD MAMS Trial Initiative | J Parkinsons Dis (2023)](https://pubmed.ncbi.nlm.nih.gov/37545260/)
- [Angiotensin type 1 receptor activation promotes neuronal and glial alpha-synuclein aggregation and transmission | npj Parkinson's Disease (2024)](https://www.nature.com/articles/s41531-024-00650-0)
- [Telmisartan Protects Mitochondrial Function in MPTP Mouse Model via Akt/GSK3-beta/PGC1-alpha | J Integr Neurosci (2024)](https://pubmed.ncbi.nlm.nih.gov/38419447/)
- [Involvement of PPAR-gamma in neuroprotective effects of telmisartan in MPTP model | J Neuroinflammation (2012)](https://jneuroinflammation.biomedcentral.com/articles/10.1186/1742-2094-9-38)
- [Telmisartan attenuates MPTP-induced dopaminergic degeneration via alpha-synuclein and neurotrophic factors | Neuropharmacology (2013)](https://pubmed.ncbi.nlm.nih.gov/23747572/)
- [The application of telmisartan in central nervous system disorders | Pharmacol Rep (2025)](https://link.springer.com/article/10.1007/s43440-025-00737-2)
- [Glycolysis-enhancing alpha-1 antagonists modify cognitive symptoms in PD | npj Parkinson's Disease (2023)](https://www.nature.com/articles/s41531-023-00477-1)
- [A Pilot to Assess Target Engagement of Terazosin in PD | Mov Disord (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8862665/)
- [Terazosin Analogs Targeting PGK1 as Neuroprotective Agents | Front Chem (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360532/)
- [A model for stimulation of enzyme activity by a competitive inhibitor: terazosin and PGK1 | PNAS (2024)](https://www.pnas.org/doi/abs/10.1073/pnas.2318956121)

### Press Releases & Filings
- [EJS ACT-PD, the world's largest clinical trial for Parkinson's, is now recruiting | Cure Parkinson's (Oct 2025)](https://cureparkinsons.org.uk/2025/10/ejs-act-pd-recruitment-announcement/)
- [Largest-ever Parkinson's disease trial opens across UK | UCL News (Oct 2025)](https://www.ucl.ac.uk/news/2025/oct/largest-ever-parkinsons-disease-trial-opens-across-uk)
- [Largest ever Parkinson's research trial is starting now | Parkinson's UK (Oct 2025)](https://www.parkinsons.org.uk/news/2025/largest-ever-parkinsons-research-trial-starting-now)
- [Largest-ever PD trial opens across UK | MRC Clinical Trials Unit at UCL (Oct 2025)](https://www.mrcctu.ucl.ac.uk/news/news-stories/2025/october/largest-ever-parkinson-s-disease-trial-opens-across-uk/)
- [New UK platform trial to test repurposed therapies for Parkinson's | Parkinson's News Today (2025)](https://parkinsonsnewstoday.com/news/new-uk-platform-trial-test-repurposed-therapies-parkinsons/)
- [EJS ACT-PD FAQs | Cure Parkinson's (Oct 2025)](https://cureparkinsons.org.uk/wp-content/uploads/2025/10/EJS-ACT-PD-FAQs-for-charity-co-branding_22Oct2025.pdf)
- [EJS ACT-PD project page | Cure Parkinson's](https://cureparkinsons.org.uk/research/research-projects/ejs-act-pd/)
- [EJS ACT-PD | MRC Clinical Trials Unit at UCL](https://www.mrcctu.ucl.ac.uk/studies/all-studies/e/ejs-act-pd/)
- [EJS ACT-PD | Parkinson's UK](https://www.parkinsons.org.uk/research/projects/edmond-j-safra-accelerating-clinical-trials-parkinsons-ejs-act-pd)

### Regulatory & Market
- [PD Drug Therapies in the Clinical Trial Pipeline: 2024 Update | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307066/)
- [Cure Parkinson's iLCT Programme](https://cureparkinsons.org.uk/research/ilct/)
- [2026 Research Progress and Outlook | Cure Parkinson's](https://cureparkinsons.org.uk/2026/01/2026-research-progress/)
