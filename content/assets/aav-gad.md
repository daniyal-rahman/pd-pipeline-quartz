---
drug_name: "AAV-GAD"
aliases: ["AAV2-GAD", "MGT-GAD", "AAV-GAD65/67"]
target: "subthalamic nucleus GABAergic inhibition (GAD65/GAD67)"
mechanism: "AAV2-delivered glutamic acid decarboxylase gene therapy to the STN, restoring GABAergic inhibition to normalize overactive subthalamic output"
modality: "AAV gene therapy"
developer: "MeiraGTx"
company_type: "biotech"
publicly_traded: true
ticker: "MGTX"
partner: "Hologen"
partner_type: "biotech"
stage: "Phase 2"
status: "Active"
patient_population: "Moderate PD not adequately controlled on anti-parkinsonian medications"
route_of_administration: "intracranial (bilateral MRI-guided stereotactic injection to STN)"
key_biomarkers: ["FDG-PET metabolic network", "UPDRS Part 3 OFF score", "PDQ-39"]
confidence_rating: "6/10"
next_catalyst: "exPDite-2 Phase 3 initiation and enrollment"
catalyst_date: "2025-2026 (initiation); ~2027-2028 (readout)"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/meiragtx]]"
partner_link: "[[companies/hologen]]"
---

# AAV-GAD

## Summary

AAV-GAD is the most clinically advanced gene therapy for Parkinson's disease, with 58 patients treated across three independent sham-controlled studies and an FDA RMAT designation (May 2025). MeiraGTx (biotech, MGTX) acquired the program from Vector Neurosciences (originally developed by Neurologix) and demonstrated an 18-point UPDRS Part 3 OFF improvement at high dose in the MGT-GAD-025 bridging study (p=0.03 vs. sham). The Hologen AI collaboration ($430M total; $200M upfront + $230M JV capital) fully funds Phase 3 (exPDite-2, N=102) and commercialization, with Hologen's AI identifying disease-modifying brain circuitry changes that may differentiate AAV-GAD from purely symptomatic DBS. If exPDite-2 meets its primary endpoint (ON time without troublesome dyskinesia at 78 weeks), AAV-GAD becomes the first approved gene therapy for PD and validates intracranial GABAergic modulation as an alternative to DBS hardware. If it fails, the intracranial gene therapy surgical barrier proves too high relative to benefit, and symptomatic innovation shifts to less invasive approaches like [[cavgene|CavGene's striatal RNAi]].

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Hologen |
| Deal Date | March 2025 |
| Upfront | $200M |
| Total (Biobucks) | $430M ($200M cash + $230M JV committed capital) |
| Deal Type | Partnership |

## Notes

### Science
- Delivers a 1:1 mixture of two AAV2 vectors encoding **GAD-65 and GAD-67** isoforms (the two forms of glutamic acid decarboxylase) under CMV enhancer-chicken beta-actin promoter regulation, injected bilaterally into the subthalamic nucleus
- In PD, dopaminergic neuron loss in the substantia nigra removes inhibitory GABAergic input to the STN, causing STN hyperactivity that drives the cardinal motor symptoms (rigidity, bradykinesia, tremor). AAV-GAD restores local GABA production to normalize STN output -- functionally similar to subthalamic deep brain stimulation (DBS)
- Key molecular distinction vs. DBS: AAV-GAD induces formation of **new polysynaptic pathways** connecting the STN to cortical motor regions, demonstrated on FDG-PET metabolic network analysis. This is a biological remodeling effect that DBS hardware does not produce
- Hologen AI analysis of Phase 2 sham-controlled data identified **disease-modifying changes in brain circuitry** and potentially **protective changes in the substantia nigra** and regions involved in cognition and mood -- if validated in Phase 3, this would distinguish AAV-GAD from symptomatic-only interventions
- Open questions: (1) Is the 18-point UPDRS improvement durable beyond 6 months at MeiraGTx's manufacturing-process dose? The original Neurologix Phase 2 showed benefit at 12 months but modest effect size (23% vs. 12% sham, compared to 41% for DBS). (2) Can AI-identified disease modification signals be reproduced in a larger cohort? (3) Does bilateral injection carry acceptable surgical risk at scale?
- Unlike [[cavgene|CavGene's CaV1.3 approach]] which targets dyskinesia, AAV-GAD targets the underlying STN hyperactivity driving core motor symptoms

### Clinical

**Phase 1 (Neurologix)** | NCT00195143 | N=12 | Advanced PD
- **Primary endpoint:** Safety/tolerability of unilateral STN AAV-GAD injection at three dose levels
- **Key secondary:** Improvement in UPDRS motor scores on treated side; FDG-PET showed reduced thalamic glucose utilization and normalized motor network metabolic activity
- **Status:** Completed (2003-2005)
- **Interpretation:** First-in-human proof of concept; unilateral injection showed lateralized improvement and metabolic normalization correlating with clinical benefit

**Phase 2 (Neurologix)** | NCT00643890 | N=45 | Advanced PD
- **Primary endpoint:** UPDRS Part 3 OFF score at 6 months → Significant improvement (8.1-point decrease vs. 4.7-point sham, p<0.05)
- **Key secondary:** Clinical benefit persisted at 12 months in long-term follow-up
- **Safety:** Well tolerated; no SAEs attributed to therapy
- **Status:** Completed (published Lancet Neurology 2011)
- **Interpretation:** First sham-controlled gene therapy trial to show significant motor benefit in PD. Effect size (23% improvement) was modest vs. DBS (41%). Neurologix planned Phase 3 but went bankrupt in 2012. FDG-PET data published in 2018 revived interest and led to MeiraGTx acquisition.

**MGT-GAD-025 (Phase 1/2 Bridging Study, MeiraGTx)** | NCT05603312 | N=14 | Moderate PD
- **Primary endpoint:** UPDRS Part 3 OFF score at 26 weeks → High-dose group: **18-point improvement** from baseline (p=0.03); low-dose: not significant; sham: not significant
- **Key secondary:** PDQ-39 quality of life — high dose: 8-point improvement (p=0.02); low dose: 6-point improvement (p=0.04); sham: 0.2-point worsening (not significant)
- **Safety:** No SAEs related to AAV-GAD; 58 total patients treated across all studies with clean safety profile
- **Status:** Completed (topline data October 2024)
- **Interpretation:** Bridging study confirmed that MeiraGTx's commercial-process-manufactured AAV-GAD replicates and exceeds the original Neurologix results. The 18-point improvement is substantially larger than the original Phase 2 (8.1 points), likely reflecting dose optimization and bilateral delivery. This data package supported RMAT designation and the Hologen deal.

**Long-term Follow-up** | NCT05894343 | N=14 (from MGT-GAD-025) | Moderate PD
- **Primary endpoint:** 5-year safety and durability monitoring post-treatment
- **Status:** Active, enrolling
- **Interpretation:** Critical for establishing durability of gene therapy effect -- a key advantage over DBS (which requires battery replacement and hardware maintenance)

**exPDite-2 (Phase 3)** | NCT06944522 | N=102 | Moderate PD
- **Primary endpoint:** Change in ON time without troublesome dyskinesia over 78 weeks
- **Key secondary:** UPDRS motor scores; disease modification biomarkers (FDG-PET metabolic network, substantia nigra imaging)
- **Status:** Planned; site engagement underway globally; initiation expected late 2025/early 2026
- **Interpretation:** Sham-controlled pivotal study. The switch from UPDRS OFF score to ON time without troublesome dyskinesia as primary endpoint reflects FDA guidance and broader clinical relevance. If positive, RMAT designation enables accelerated approval pathway.

### Financial
- **Hologen deal structure:** $200M upfront cash to MeiraGTx + $230M committed capital into joint venture (Hologen Neuro AI Limited). MeiraGTx retains **30% ownership** of JV while leading all clinical development and manufacturing. Hologen also obtains minority stake in MeiraGTx's manufacturing subsidiary
- **Cash receipt timing:** $23M of $200M received post-UK FDI clearance (Q2 2025); remainder expected Q3 2025
- **MGTX stock reaction:** +17-29% on Hologen deal announcement (March 2025); market cap ~$619M
- **Stock reaction on Phase 2 data:** MGTX rose on October 2024 bridging study topline data
- **RMAT designation** (May 2025) provides expedited development pathway, rolling review, and priority review eligibility -- significant regulatory de-risking
- **Deal signal:** Hologen committing $430M to a single-asset partnership is extraordinary for a gene therapy with only 14 patients in the most recent study. The AI angle (Hologen's LMMs applied to brain imaging data) is a differentiator but also introduces execution risk around a non-traditional partner
- **Historical context:** Neurologix went bankrupt in 2012 attempting Phase 3 alone -- the Hologen capital solves the funding gap that killed the program a decade ago
- **Manufacturing:** MeiraGTx is vertically integrated with wholly-owned manufacturing facilities, producing AAV-GAD with a commercial platform process. Manufacturing supply agreements with the JV provide revenue stream independent of clinical outcome

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[eladocagene]] | Approved (AADC deficiency); Phase 1b completed (PD — terminated) | Active (AADC deficiency); Discontinued (PD) | PTC Therapeutics | AAV gene therapy |
| [[cavgene]] | Preclinical | Active | CavGene Therapeutics | AAV gene therapy |
| [[lario-cav23]] | Preclinical | Active | Lario Therapeutics | small molecule |
| [[otsuka-program]] | Preclinical | Active | Otsuka Pharmaceutical | Undisclosed |
| [[lu-af28996]] | Phase 1 | Active | Lundbeck | small molecule |
| [[ly03017]] | Phase 1 | Active | Luye Pharma Group | small molecule |
| [[irl757]] | Phase 1b | Active | IRLAB Therapeutics | small molecule |
| [[ser-252]] | Phase 1b | Active | Serina Therapeutics | small molecule |
| [[appello-mglu4]] | Phase 1/2 | Active | Appello Pharmaceuticals | small molecule |
| [[dive-inbrain]] | Phase 1/2 | Active | InBrain Pharma | device-aided therapy (drug/device combination) |
| [[vgn-r09b]] | Phase 1/2 | Active | Shanghai Vitalgen BioPharma | AAV gene therapy |
| [[aav-gad]] | Phase 2 | Active | MeiraGTx | AAV gene therapy |
| [[addex-program]] | Phase 2 | Deprioritized | Addex Therapeutics | small molecule |
| [[blarcamesine]] | Phase 2 | Active | Anavex Life Sciences | small molecule |
| [[glovadalen]] | Phase 2 | Active | UCB | small molecule |
| [[mesdopetam]] | Phase 3 | Active | IRLAB Therapeutics | small molecule |
| [[p2b001]] | Phase 3 | Active | Pharma Two B | small molecule |
| [[solangepras]] | Phase 3 | Active | Cerevance | small molecule |
| [[nd0612]] | NDA Filed | Active | NeuroDerm | small molecule |
| [[tavapadon]] | NDA Filed | Active | Cerevel Therapeutics | small molecule |
| [[apokyn]] | Approved | Active | Supernus Pharmaceuticals | small molecule |
| [[carbidopa-levodopa]] | Approved | Active | Multiple (generic) | small molecule |
| [[crexont]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[duopa]] | Approved | Active | AbbVie | drug-device combination |
| [[gocovri]] | Approved | Active | Supernus Pharmaceuticals | small molecule |
| [[ipx203]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[neupro]] | Approved | Active | UCB | small molecule |
| [[nuplazid]] | Approved | Active | Acadia Pharmaceuticals | small molecule |
| [[rytary]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[vyalev]] | Approved | Active | AbbVie | drug-device combination |

- **vs. Deep Brain Stimulation (DBS):** DBS is the established standard for moderate-advanced PD motor symptoms (41% UPDRS improvement at 6 months). AAV-GAD offers a potential one-time treatment vs. permanent hardware with battery replacements, programming visits, and infection risk. However, DBS is reversible and adjustable; AAV-GAD is a permanent intervention. The disease-modification signal (brain circuitry remodeling, substantia nigra protection) would be the decisive differentiator if confirmed
- **vs. [[cavgene|CavGene (CaV1.3 RNAi)]]:** Both are intracranial AAV gene therapies but target different problems -- AAV-GAD addresses core motor symptoms via STN modulation, while CavGene targets levodopa-induced dyskinesia via striatal calcium channel silencing. Complementary rather than competitive; CavGene is years behind in preclinical
- **vs. AADC gene therapy (PTC Therapeutics/Neurocrine):** AADC gene therapy (eladocagene exuparvovec) delivers the enzyme converting L-DOPA to dopamine in the putamen. Approved in EU for AADC deficiency; in PD trials for patients with motor fluctuations. Different mechanism -- AADC enhances levodopa response while AAV-GAD modulates basal ganglia circuitry independent of dopamine
- **vs. GDNF/neurturin gene therapy (AB-1005/AskBio):** Neurotrophic factor gene therapies aim to rescue/regenerate dopaminergic neurons. Multiple prior failures (Ceregene's CERE-120 neurturin Phase 2 missed). AB-1005 (GDNF, Phase 2) takes the neuroprotective approach. AAV-GAD's circuit-modulation mechanism avoids the challenge of neurotrophic factor diffusion and retrograde transport
- The intracranial delivery requirement is the shared limitation across all PD gene therapies -- any IV-deliverable gene therapy (e.g., Voyager's BBB-crossing AAV capsids for GBA1) would be a paradigm shift that makes surgical approaches less attractive

## Analysis

AAV-GAD occupies a unique niche in the PD landscape: it is a symptomatic gene therapy with emerging disease-modification signals, backed by the longest clinical dataset of any PD gene therapy program (first patient dosed 2003, 58 patients treated, >20 years of safety follow-up from original cohorts). The program's resurrection from Neurologix bankruptcy through MeiraGTx acquisition to a $430M AI partnership is itself a signal -- the biological data was compelling enough to attract capital twice after corporate failure.

**Analytical estimate -- Phase 3 success probability: 40-50%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Gene therapy pivotal trials in CNS have ~30% historical success rate
- Adjustments upward: Consistent efficacy across three independent sham-controlled studies (+10%), RMAT designation reflecting FDA engagement (+5%), 18-point UPDRS improvement is clinically meaningful and well above sham (+10%), clean safety in 58 patients over 20+ years (+5%), endpoint switch to ON time (more patient-relevant, potentially easier to detect) (+5%)
- Adjustments downward: Small bridging study (N=14) may not predict Phase 3 effect size (-10%), surgical procedure introduces placebo/sham response variability (-5%), modest effect size in original Phase 2 relative to DBS (-5%), Hologen is a non-traditional pharma partner with execution risk (-5%)
- Net: ~40-50%

**Signal analysis:**
- The Hologen deal structure reveals MeiraGTx's strategic calculation: retain 30% of the JV (preserving upside) while offloading the $200-300M Phase 3 cost to a partner. The $200M upfront exceeds MeiraGTx's entire market cap at the time of deal rumors, suggesting Hologen sees a path to blockbuster value. However, Hologen is an AI company, not a pharma company -- their ability to support regulatory filings, commercial launch, and physician education for a surgical gene therapy is unproven.
- The AI-identified disease-modification signal is both the most exciting and most risky element. If Hologen's multi-modal foundation models genuinely detected substantia nigra protection in sham-controlled Phase 2 data, AAV-GAD moves from "symptomatic gene therapy" to "disease-modifying gene therapy" -- a category with no approved products. But AI-derived biomarker claims in small datasets (N=14) require extraordinary validation.
- RMAT designation is a meaningful regulatory signal. FDA grants RMAT only when preliminary clinical evidence indicates the therapy may offer substantial improvement over existing treatments for serious conditions. The designation provides access to early interactions with FDA, rolling review, and priority review -- potentially shaving 1-2 years off the path to approval.
- Decision tree: If exPDite-2 positive on ON time endpoint, AAV-GAD likely files for accelerated approval under RMAT, becoming the first gene therapy approved for PD. Manufacturing at MeiraGTx's own facilities enables controlled launch. If negative, the intracranial gene therapy modality for PD symptomatic control faces serious headwinds, and the DBS standard of care remains unchallenged. In the failure scenario, the AI disease-modification claims become the last lever -- if substantia nigra protection data are compelling even with a missed primary, a second pivotal study focused on disease modification could be considered.

## References

### Clinical Trials
- [Phase 1 (Neurologix)](https://clinicaltrials.gov/ct2/show/NCT00195143) -- NCT00195143
- [Phase 2 (Neurologix)](https://clinicaltrials.gov/ct2/show/NCT00643890) -- NCT00643890
- [MGT-GAD-025 Phase 1/2 Bridging](https://clinicaltrials.gov/ct2/show/NCT05603312) -- NCT05603312
- [Long-term Follow-up](https://clinicaltrials.gov/ct2/show/NCT05894343) -- NCT05894343
- [exPDite-2 Phase 3](https://clinicaltrials.gov/ct2/show/NCT06944522) -- NCT06944522

### Key Publications
- [AAV2-GAD gene therapy for advanced PD: sham-surgery controlled, randomised trial | Lancet Neurology (2011)](https://pubmed.ncbi.nlm.nih.gov/21419704/)
- [Long-term follow-up of randomized AAV2-GAD gene therapy trial for PD | JCI Insight (2017)](https://pubmed.ncbi.nlm.nih.gov/28405611/)
- [Safety and tolerability of AAV-GAD gene therapy: Phase I trial | Lancet (2007)](https://pubmed.ncbi.nlm.nih.gov/17586305/)
- [Subthalamic GAD gene therapy: changes in motor function and cortical metabolism | PNAS (2006)](https://pubmed.ncbi.nlm.nih.gov/16835631/)

### Press Releases & Filings
- [MeiraGTx positive data from MGT-GAD-025 bridging study (Oct 2024)](https://investors.meiragtx.com/news-releases/news-release-details/meiragtx-announces-positive-data-randomized-sham-controlled)
- [MeiraGTx RMAT designation for AAV-GAD (May 2025)](https://investors.meiragtx.com/news-releases/news-release-details/meiragtx-granted-fda-regenerative-medicine-advanced-therapy-0)
- [MeiraGTx-Hologen strategic collaboration (March 2025)](https://investors.meiragtx.com/news-releases/news-release-details/meiragtx-enters-strategic-collaboration-hologen-ai-expedite)
- [MeiraGTx Q3 2025 financial results](https://investors.meiragtx.com/news-releases/news-release-details/meiragtx-reports-third-quarter-2025-financial-and-operational)
- [MeiraGTx acquisition of Vector Neurosciences](https://investors.meiragtx.com/news-releases/news-release-details/meiragtx-announces-acquisition-vector-neurosciences-gains-phase)
- [Hologen AI commits $430M to MeiraGTx PD gene therapy | Fierce Biotech](https://www.fiercebiotech.com/biotech/hologen-ai-commits-430m-help-take-meiragtxs-parkinsons-gene-therapy-forward)

### Regulatory & Market
- [AAV-GAD profile | Alzforum](https://www.alzforum.org/therapeutics/aav-gad)
- [MeiraGTx Parkinson's disease program page](https://meiragtx.com/programs-pipeline/parkinsons-disease/)
- [MeiraGTx stock surges on Hologen AI deal | Benzinga](https://www.benzinga.com/25/03/44302928/meiragtx-collaborates-with-hologen-ai-to-expedite-development-of-parkinsons-candidate-stock-surges)
