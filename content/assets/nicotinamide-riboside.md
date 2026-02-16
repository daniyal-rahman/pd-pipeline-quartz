---
drug_name: "Nicotinamide Riboside"
aliases: ["NR", "Niagen", "nicotinamide riboside chloride"]
target: "NAD+ metabolism / mitochondrial bioenergetics"
mechanism: "Oral NAD+ precursor (vitamin B3 form) that boosts neuronal NAD+ levels, rescuing mitochondrial bioenergetic deficits, enhancing mitophagy, lysosomal and proteasomal function, and reducing neuroinflammation"
modality: "small molecule"
developer: "Neuro-SysMed / Haukeland University Hospital"
company_type: "academic"
publicly_traded: false
partner: "Niagen Bioscience"
partner_type: "biotech"
stage: "Phase 3"
status: "Active"
patient_population: "Early PD (within 2 years of diagnosis)"
route_of_administration: "oral"
key_biomarkers: ["cerebral NAD+ (31P-MRS)", "FDG-PET cerebral metabolism", "inflammatory cytokines (serum/CSF)", "MDS-UPDRS"]
confidence_rating: "4/10"
next_catalyst: "NOPARK Phase 3 results publication"
catalyst_date: "2025-2026"
thesis_cluster: "mitophagy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Nicotinamide Riboside

## Summary

Nicotinamide riboside (NR) is a repurposed vitamin B3 supplement being tested as a disease-modifying NAD+ replenishment therapy for PD, originating from academic work at Neuro-SysMed / Haukeland University Hospital (Bergen, Norway) under Prof. Charalampos Tzoulis. The Phase 1 NADPARK trial (N=30, Cell Metabolism 2022) showed NR increased cerebral NAD+ levels, altered brain metabolism on FDG-PET, and reduced inflammatory cytokines -- but clinical benefit was mild and variable. The Phase 3 NOPARK trial (NCT03568968, N=400, 12 sites across Norway) completed enrollment and dosing in June 2025, with results expected but not yet published as of February 2026. In July 2025, Niagen Bioscience (formerly ChromaDex, NASDAQ: NAGE) licensed worldwide exclusive commercial rights from Haukeland, creating a subsidiary (NAD Pharmaceuticals) to pursue EU CMA/accelerated approval. If NOPARK shows statistically significant slowing on total MDS-UPDRS, it would be the first metabolic/mitochondrial therapy to demonstrate disease modification in PD and would validate NAD+ depletion as a druggable node -- a major boost to the broader mitophagy thesis pursued by [[nrg5051|NRG5051]], [[mtx325|MTX325]], [[vb-23|VB-23]], and [[stealth-bio|bevemipretide]]. If NOPARK is negative, it extends the unbroken string of mitochondrial supplement failures (CoQ10, MitoQ) and shifts capital further toward mechanistically targeted approaches like PINK1 activation ([[progenra-pink1]]) and USP30 inhibition ([[mtx325]], [[vb-23]]).

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Niagen Bioscience (fka ChromaDex) |
| Deal Date | July 2025 |
| Upfront | Not disclosed |
| Total (Biobucks) | Not disclosed |
| Deal Type | Licensing/co-development |

## Notes

### Science
- NR is a naturally occurring form of vitamin B3 and a direct precursor to NAD+ via the nicotinamide riboside kinase (NRK) salvage pathway -- oral NR supplementation bypasses the rate-limiting enzyme NAMPT in the de novo NAD+ synthesis pathway
- NAD+ levels are depleted in PD brains (post-mortem studies), and NAD+ is essential for mitochondrial complex I function, sirtuin-mediated stress responses, and PARP-dependent DNA repair -- all processes implicated in dopaminergic neuron vulnerability
- In the NADPARK Phase 1 trial, NR upregulated transcription of genes related to mitochondrial respiration, lysosomal function, and proteasomal clearance -- suggesting a multi-pathway mechanism rather than simple bioenergetic rescue
- NR also decreased inflammatory cytokines in both serum and CSF, connecting the NAD+ depletion hypothesis to the neuroinflammation axis
- Key scientific concern: cerebral NAD+ augmentation was **variable** across patients in NADPARK -- some showed robust increases, others did not, suggesting pharmacogenomic or blood-brain barrier variability that may dilute efficacy in a large trial
- Preclinical validation: NR rescued mitochondrial defects and neuronal loss in iPSC-derived dopaminergic neurons from GBA1-mutant PD patients and in Drosophila PINK1 mutant models (Cell Reports 2018)
- Mechanistic distinction vs. other mitophagy assets: NR works upstream by boosting the cellular NAD+ pool that fuels mitochondrial quality control, whereas [[mtx325|MTX325]] and [[vb-23|VB-23]] enhance mitophagy by inhibiting USP30, [[nrg5051|NRG5051]] prevents mitochondrial pore opening, and [[progenra-pink1]] directly activates PINK1 kinase -- these are complementary rather than competitive mechanisms
- Open question: is NAD+ depletion a cause or consequence of PD neurodegeneration? If downstream, NR supplementation may provide symptomatic metabolic support without altering disease trajectory

### Clinical

**NADPARK (Phase 1)** | NCT03816020 | N=30 | Newly diagnosed, treatment-naive PD
- **Primary endpoint:** Safety/tolerability and cerebral NAD+ change (31P-MRS) --> NR well tolerated; significant but variable increase in cerebral NAD+ levels
- **Key secondary:** FDG-PET showed altered cerebral metabolism in NAD+ responders, associated with mild clinical improvement; inflammatory cytokine reduction in serum and CSF; transcriptional upregulation of mitochondrial, lysosomal, proteasomal pathways
- **Status:** Completed (30-day treatment)
- **Interpretation:** Proof-of-concept that oral NR can reach the CNS and alter brain metabolism, but 30-day duration and N=30 are far too small for clinical conclusions. The variability in NAD+ response is concerning for Phase 3 powering.

**NR-SAFE (Phase 1)** | NCT05344404 | N=20 | PD patients
- **Primary endpoint:** Safety/tolerability of high-dose NR (3000 mg/day, i.e., 1500 mg BID) for 4 weeks --> No moderate or severe adverse events; all 42 AEs were mild
- **Key secondary:** Up to 5-fold increase in blood NAD+ at 3000 mg/day; mild but significant homocysteine increase that stabilized; no methyl pool depletion; MDS-UPDRS improvement (but potential levodopa timing confound)
- **Status:** Completed (April-July 2022, Haukeland University Hospital)
- **Interpretation:** Established that NR dosing can be safely extended to 3000 mg/day, providing headroom above the 1000 mg/day NOPARK dose. The homocysteine signal requires monitoring in longer trials.

**NOPARK (Phase 3)** | NCT03568968 | N=400 | Early PD (within 2 years of diagnosis)
- **Primary endpoint:** Between-group difference (NR 1000 mg/day vs. placebo) in change of total MDS-UPDRS from baseline to week 52
- **Design:** Randomized, double-blind, placebo-controlled; 12 sites across Norway; NR 500 mg BID for 52 weeks
- **Status:** Fully enrolled; dosing completed June 2025; results expected by end of 2025 (not yet published as of February 2026)
- **Interpretation:** This is the definitive trial for NR in PD. N=400 is well-powered for a large effect size but may be underpowered if the treatment effect is modest (e.g., 15-20% slowing). The 52-week duration is standard for PD disease modification trials. The all-comers early PD population (not enriched for mitochondrial dysfunction biomarkers) may introduce heterogeneity that dilutes any real signal -- a lesson the prasinezumab program learned with its levodopa subgroup enrichment in PADOVA.

**N-DOSE (Dose Optimization)** | NCT05589766 | N=TBD | PD patients
- **Status:** Dose-finding study to optimize NR dosing for future development
- **Interpretation:** Suggests the academic team is preparing for post-NOPARK development regardless of the Phase 3 outcome, or hedging that the 1000 mg/day dose may be suboptimal.

### Financial
- **Academic origin:** NOPARK was government-funded through KLINBEFORSK (Norwegian national program for clinical treatment research), Regional Health Authority of Western Norway, and Research Council of Norway -- no pharma sponsor during Phase 3
- **Niagen Bioscience license (July 2025):** Worldwide exclusive commercial rights to NR for PD; financial terms not disclosed. Niagen Bioscience (NASDAQ: NAGE, formerly ChromaDex) renamed from ChromaDex in March 2025 and created NAD Pharmaceuticals subsidiary specifically for this program
- **NAGE market cap:** Niagen Bioscience is a consumer supplement company (~$300M market cap) pivoting toward pharmaceutical development -- this is NOT a typical pharma partner and raises questions about clinical development and regulatory execution capability
- **NR is commercially available:** Niagen/Tru Niagen is sold as an OTC supplement in the US, creating a unique commercial dynamic -- patients can self-treat regardless of regulatory approval, which both validates demand and undermines pricing power
- **Patent position:** Tzoulis and Dolle (Haukeland) filed patent applications for NR use in PD (US20240366648A1, via Vestlandets Innovasjonsselskap AS); Niagen Bioscience holds Niagen compound patents
- **Cost comparison:** NR as a supplement costs ~$40-60/month; pharmaceutical-grade pricing for a PD indication would need to be dramatically higher to support regulatory investment, but payer pushback would be intense for a supplement-adjacent molecule
- **Deal signal:** The licensing deal occurring pre-publication of NOPARK results suggests either (a) Niagen Bioscience is betting on the science regardless of specific results, (b) there is informal knowledge of positive signals, or (c) the company views regulatory exclusivity as valuable even with modest efficacy data

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "mitochond") AND file.name != "nicotinamide-riboside"
SORT stage DESC
```

- NR is mechanistically distinct from other mitophagy-cluster assets: it works upstream by replenishing the NAD+ pool, while [[mtx325|MTX325]] and [[vb-23|VB-23]] (USP30 inhibitors) and [[progenra-pink1]] (PINK1 activator) target specific nodes in the mitophagy machinery, and [[nrg5051|NRG5051]] (mPTP inhibitor) prevents mitochondrial permeability transition
- These approaches are potentially complementary rather than competitive -- NAD+ repletion could theoretically enhance the efficacy of PINK1 activation or USP30 inhibition by providing the bioenergetic substrate for improved mitophagy
- [[stealth-bio|Bevemipretide (SBT-272)]] targets cardiolipin/inner mitochondrial membrane stability, another complementary but distinct mechanism
- Key competitive vulnerability: NR is a supplement, not a novel chemical entity. If NOPARK is positive, any NR manufacturer could market the supplement for "mitochondrial health" without a PD indication -- Niagen Bioscience's moat depends entirely on regulatory exclusivity and physician-directed prescribing
- Historical context for mitochondrial supplements in PD: CoQ10 failed Phase 3 (QE3 trial, negative); MitoQ failed Phase 2 (negative); idebenone failed. NR would need to break this pattern of supplement-class failures to be credible
- If NOPARK succeeds, it validates the upstream NAD+ depletion hypothesis and creates a rising tide for the entire mitophagy cluster -- proving that improving mitochondrial function can slow PD progression increases confidence in more targeted approaches like [[mtx325]] and [[progenra-pink1]]

## Analysis

The NR/NOPARK program sits at an unusual intersection: academic-led, supplement-derived, and now licensed by a consumer health company pivoting to pharma. The scientific rationale is biologically coherent -- NAD+ depletion in PD is well-documented, and the Phase 1 NADPARK data showing cerebral NAD+ augmentation with downstream metabolic and anti-inflammatory effects is a genuine proof-of-concept. But biological coherence has not been sufficient for mitochondrial approaches in PD. CoQ10, MitoQ, and idebenone all had reasonable mechanistic rationale and all failed in controlled trials.

**Analytical estimate -- Phase 3 success probability: 15-20%.** This is our assessment, not from a published source. The reasoning:
- Base rate: 0/3 mitochondrial supplement-class therapies have succeeded in PD Phase 3 --> starting point ~10%
- Adjustments upward: NADPARK showed measurable cerebral NAD+ augmentation and metabolic change (+5%), preclinical iPSC/Drosophila validation in genetic PD models (+3%), multi-pathway mechanism (mitochondrial + lysosomal + anti-inflammatory) is more comprehensive than CoQ10/MitoQ which were purely antioxidant (+5%), large N=400 trial with 52-week duration is adequately powered for moderate effect sizes (+3%), clean safety profile across NADPARK and NR-SAFE (+2%)
- Adjustments downward: variable CNS NAD+ response in NADPARK -- non-responders will dilute signal (-5%), all-comers population not enriched for mitochondrial dysfunction (-5%), 1000 mg/day dose may be suboptimal given NR-SAFE showed higher doses are safe (-3%), supplement-class molecule competing with OTC availability (-2%), no companion diagnostic to identify likely responders (-3%)
- Net: ~15-20%

**Signal analysis:**
- The Niagen Bioscience licensing deal (July 2025) pre-dates NOPARK publication but post-dates trial completion (June 2025). This timing is notable. If the company had no signal on results, licensing an unproven supplement-in-PD would be a highly speculative bet. The more likely interpretation is that informal discussions with the academic team provided some directional signal -- though this is speculative.
- The academic team's parallel pursuit of NR-SAFE (high-dose safety) and N-DOSE (dose optimization) suggests they are building a development platform for NR in PD regardless of the specific NOPARK outcome -- either they expect positive results and are preparing for next steps, or they believe dose optimization may rescue a marginal result.
- Niagen Bioscience is a supplement company with no history of running regulatory clinical trials. If NOPARK is positive, the most likely commercial path is sublicensing to a pharma partner for regulatory development, not Niagen Bioscience executing it independently. The NAD Pharmaceuticals subsidiary may be a vehicle for partnering.
- The biggest strategic question: even if NOPARK is positive, can a pharmaceutical NR product command premium pricing when the same molecule is available OTC as Tru Niagen for $40-60/month? The answer depends entirely on regulatory exclusivity, physician prescribing patterns, and whether payers will cover a pharmaceutical-grade version. This is a fundamentally different commercial model than a novel chemical entity.

If NOPARK is positive, the implications for the mitophagy cluster are substantial: it would validate mitochondrial bioenergetic rescue as disease-modifying in PD, providing a tailwind for [[nrg5051]], [[mtx325]], [[vb-23]], [[progenra-pink1]], and [[stealth-bio]]. If negative, it adds to the graveyard of mitochondrial supplements in PD and -- fairly or not -- increases skepticism toward the entire mitophagy thesis, even though targeted mitophagy enhancement (PINK1, USP30) is mechanistically distinct from NAD+ supplementation.

## References

### Clinical Trials
- [NOPARK Phase 3](https://clinicaltrials.gov/study/NCT03568968) -- NCT03568968
- [NADPARK Phase 1](https://clinicaltrials.gov/study/NCT03816020) -- NCT03816020
- [NR-SAFE Phase 1](https://clinicaltrials.gov/study/NCT05344404) -- NCT05344404
- [N-DOSE](https://clinicaltrials.gov/study/NCT05589766) -- NCT05589766

### Key Publications
- [The NADPARK study: A randomized phase I trial of nicotinamide riboside supplementation in Parkinson's disease | Cell Metabolism (March 2022)](https://pubmed.ncbi.nlm.nih.gov/35235774/)
- [NR-SAFE: a randomized, double-blind safety trial of high dose nicotinamide riboside in Parkinson's disease | Nature Communications (Nov 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10684646/)
- [The NAD+ Precursor Nicotinamide Riboside Rescues Mitochondrial Defects and Neuronal Loss in iPSC and Fly Models of Parkinson's Disease | Cell Reports (2018)](https://pubmed.ncbi.nlm.nih.gov/29874584/)
- [From NADPARK to NOPARK | Science of Parkinson's (March 2022)](https://scienceofparkinsons.com/2022/03/11/nad-2/)

### Press Releases & Filings
- [Niagen Bioscience Secures Exclusive License for NR as PD Therapy (July 2025)](https://www.businesswire.com/news/home/20250708472670/en/Niagen-Bioscience-Secures-Exclusive-License-to-Develop-and-Commercialize-its-NAD-Precursor-Patented-Nicotinamide-Riboside-Niagen-as-a-Potential-Parkinsons-Disease-Therapy-in-Agreement-with-Haukeland-University-Hospital-in-Bergen-Norway)
- [ChromaDex Renamed to Niagen Bioscience, Ticker NAGE (March 2025)](https://www.businesswire.com/news/home/20250319662388/en/ChromaDex-Evolves-Into-Niagen-Bioscience-Marking-a-New-Era-of-Uncovering-the-Potential-of-NAD-With-Precision-Science)
- [NOPARK Study Page | Neuro-SysMed / Haukeland University Hospital](https://www.helse-bergen.no/en/neuro-sysmed-english/clinical-studies-at-neuro-sysmed/parkinsons--clinical-studies/the-nopark-study/)
- [2026 Research Progress | Cure Parkinson's](https://cureparkinsons.org.uk/2026/01/2026-research-progress/)

### Regulatory & Market
- [VIS Patent Application US20240366648A1 -- Nicotinamide riboside for PD](https://patents.google.com/patent/US20240366648A1)
- [Niagen Bioscience Investor Relations](https://investors.niagenbioscience.com/overview/default.aspx)
