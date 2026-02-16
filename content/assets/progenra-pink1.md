---
drug_name: "Progenra PINK1 activator (lead undisclosed)"
aliases: ["Progenra PINK1/Parkin molecular glue program"]
target: "PINK1 kinase (activation of mutant and wild-type forms)"
mechanism: "small molecule PINK1 activator that restores kinase function in pathogenic PINK1 mutant variants, reactivating mitochondrial stress sensing and PINK1/Parkin-mediated mitophagy to clear damaged mitochondria"
modality: "small molecule (molecular glue)"
developer: "Progenra"
company_type: "startup"
publicly_traded: false
partner: ""
partner_type: ""
stage: "Preclinical"
status: "Active"
patient_population: "Familial/early-onset PD with PINK1 mutations (5-10% of inherited PD); potential extension to idiopathic PD with mitochondrial dysfunction"
route_of_administration: "Undisclosed (oral expected given small molecule modality and need for CNS penetration)"
key_biomarkers: ["pSer65-ubiquitin (pS65Ub)", "mitophagy flux markers", "PINK1 kinase activity", "mitochondrial membrane potential"]
confidence_rating: "4/10"
next_catalyst: "Completion of comparative activity studies vs. MTK-458; IND-enabling preclinical toxicity studies"
catalyst_date: "2027 (first-in-human target per company, from July 2025 announcement)"
thesis_cluster: "mitophagy"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/progenra]]"
---

# Progenra PINK1 Activator Program

## Summary

Progenra (private, Malvern PA, founded 2005) is developing first-in-class small molecule PINK1 kinase activators to treat familial and early-onset Parkinson's disease caused by loss-of-function PINK1 mutations. The program leverages Progenra's UbiPro platform -- a high-throughput screening toolbox for the ubiquitin proteasome system (UPS) encompassing >700,000 drug-like small molecules -- to identify molecular glues that restore PINK1 kinase activity and reactivate mitophagy. In a July 2025 press release, Progenra claimed their lead candidate demonstrates "exceptional potency -- over 20 times more active than AbbVie's clinical-stage molecule" (referring to [[abbv-1088]] / MTK-458), with "robust efficacy in preclinical studies." The program has received two MJFF grants: a 2018 Therapeutic Pipeline Award and a 2025 grant specifically for PINK1 activators. No VC funding rounds have been disclosed; the company appears to be grant-funded and bootstrapped. Progenra targets first-in-human studies within two years of the July 2025 announcement (i.e., ~2027).

## Notes

### Science
- PINK1 (PTEN-induced kinase 1) is a mitochondrial kinase that senses mitochondrial damage and phosphorylates ubiquitin at Ser65, which in turn recruits and activates the E3 ligase Parkin to ubiquitinate outer mitochondrial membrane proteins, triggering selective autophagy of damaged mitochondria (mitophagy)
- Loss-of-function mutations in PINK1 and Parkin together account for 5-10% of hereditary early-onset PD cases; these mutations prevent cells from clearing dysfunctional mitochondria, leading to dopaminergic neuron death
- Progenra's key scientific claim (July 2025): specific pathogenic PINK1 mutations found in PD patients can be pharmacologically reactivated with small molecules, restoring their ability to sense mitochondrial stress and initiate mitophagy -- this was "previously considered impossible" for loss-of-function variants
- The compound removes protein aggregates and generates new mitochondria, suggesting both clearance and biogenesis effects
- Progenra also has a separate but related Parkin activation / molecular glue program; BIO-2007817 (developed by Biogen, published in Nature Communications 2024) is a distinct molecular glue that activates Parkin by gluing phospho-ubiquitin to the RING0 zinc-finger domain and partially rescues Parkin EOPD mutants R42P and V56E -- Progenra's PINK1 program acts upstream of this, on the kinase itself
- The UbiPro platform has been used to discover molecular glues, DUB inhibitors, E3 ligase modulators, and PROTAC ligands across oncology, neurodegeneration, and inflammation
- Progenra also pursues tau aggregate degraders for Alzheimer's and anti-inflammatory molecular glues (psoriasis, asthma models) -- these are secondary programs
- The 2025 MJFF grant objectives explicitly include establishing comparative activity between Progenra's PINK1 activators and MTK-458 (the published comparator compound from AbbVie/Mitokinin), evaluating drug efficacy in biochemical, human cell, and mouse cell models, and assessing effectiveness on PINK1 variants using pSer65Ub as a biomarker
- Open question: what specific PINK1 mutations does the compound rescue? The press release references "pathogenic PINK1 mutations found in Parkinson's patients" broadly but does not enumerate the variants tested. This matters because there are >70 known pathogenic PINK1 mutations with different structural consequences

### Clinical
No clinical trials initiated. The program is in preclinical stage.

- Company-stated goal: first-in-human studies within 2 years of July 2025 announcement (~mid-2027)
- Following current MJFF grant milestones, next steps include: preclinical toxicity studies, long-term safety evaluations, drug manufacturing optimization, and clinical trial advancement
- No NCT numbers; no disclosed animal model efficacy data
- The 20x potency claim vs. AbbVie's clinical-stage molecule has not been published in a peer-reviewed paper as of February 2026 -- it appears only in company press releases and the BIO 2026 exhibitor profile
- **Analytical estimate: the 2027 FIH timeline is aggressive for a grant-funded company with no disclosed VC backing. Base rate for grant-funded preclinical programs reaching IND on stated timeline is ~20-30%. This is our assessment, not from a published source.**

### Financial
- **MJFF Therapeutic Pipeline Award (2018):** amount undisclosed; funded small molecule drug discovery targeting UPS enzymes for PD
- **MJFF PINK1 Activators Grant (2025):** amount undisclosed; PIs: Kumar Suresh PhD and Tauseef R. Butt PhD; funds comparative studies vs. MTK-458, efficacy in cell models, PINK1 variant assessment
- **VC funding:** None disclosed. No rounds listed on Crunchbase, CB Insights, or Tracxn
- **Total known funding:** Two MJFF grants (amounts undisclosed) + unspecified prior capital. CEO Tauseef Butt has been "instrumental in raising ~$175 million capital" across his career, but this figure appears to encompass Progenra's entire history since 2005, including non-PD programs and possibly contract research revenue
- Company founded 2005; headquarters in Malvern, PA
- Exhibited at BIO International Convention 2025 (Boston) and 2026 (San Diego, June 22-25)
- No disclosed valuation; private company structure

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE (contains(target, "PINK1") OR contains(target, "mitophagy") OR contains(target, "Parkin") OR contains(target, "USP30") OR contains(thesis_cluster, "mitophagy"))
AND file.name != "progenra-pink1"
SORT stage DESC
```

**PINK1/Parkin/Mitophagy Competitive Landscape (as of Feb 2026):**

| Company | Asset | Target | Stage | Differentiation |
|---------|-------|--------|-------|-----------------|
| AbbVie (ex-Mitokinin) | [[abbv-1088]] (MTK-458 derivative) | PINK1 stabilizer | Phase 1 (completed SAD; MAD active) | Most advanced PINK1 program; acquired for $110M + $545M milestones; stabilizes active PINK1 complex rather than reactivating mutants |
| Mission Therapeutics | MTX325 | USP30 inhibitor | Phase 1b (starting H1 2026) | USP30 inhibition is downstream of PINK1/Parkin; Phase 1a completed with PET-confirmed brain penetration; $13.3M raise + $5.2M MJFF grant |
| Vincere Biosciences | USP30 inhibitor (undisclosed) | USP30 inhibitor | IND-enabling | $5M MJFF grant (Nov 2025); planned Phase 1 in 2026; >800 molecules synthesized |
| Progenra | PINK1 activator (this asset) | PINK1 activator | Preclinical | Claims 20x potency vs. MTK-458; rescues mutant PINK1; grant-funded |
| Biogen (research) | BIO-2007817 | Parkin molecular glue | Research tool | Published in Nature Communications 2024; rescues Parkin mutants R42P, V56E; research-stage compound |

- **Key distinction vs. [[abbv-1088]]:** AbbVie/Mitokinin's MTK-458 stabilizes the active form of wild-type PINK1 on damaged mitochondria, amplifying normal PINK1 signaling. Progenra claims to reactivate loss-of-function PINK1 mutant variants -- a fundamentally different (and more ambitious) pharmacological claim. If validated, Progenra's approach would address the genetic root cause in PINK1-mutation carriers, while AbbVie's approach is broader (applicable to idiopathic PD where wild-type PINK1 signaling is suboptimal)
- **USP30 inhibitors (Mission, Vincere)** work downstream: USP30 removes ubiquitin from mitochondrial substrates, opposing the PINK1/Parkin pathway. Inhibiting USP30 lowers the threshold for mitophagy without requiring PINK1 or Parkin activity -- potentially applicable even in PINK1/Parkin-null patients, which is a theoretical advantage over PINK1 activators
- **Broader context:** per Mission Therapeutics' Nature Reviews Drug Discovery article (Jan 2025), each of the top 10 pharma companies has some level of mitophagy R&D ongoing. Other entrants include Pretzel Therapeutics (Arch Venture Partners) and Capacity Bio (RA Capital)
- A 2025 Science Advances publication raised caution: putative PINK1/Parkin activators (including MTK-458 and FB231) were shown to lower the threshold for mitophagy rather than directly activating the pathway, working by "sensitizing cells to mitochondrial stress" -- this mechanistic nuance may apply to Progenra's compounds and warrants scrutiny

## Leadership

| Role | Name |
|------|------|
| President & CEO, Co-Founder | Tauseef R. Butt, PhD (University of Glasgow; ex-NIH, ex-SmithKline/GSK; Adjunct Prof, UPenn Medical School & Drexel) |
| VP of Research & Development | Kumar Suresh, PhD (Indian Institute of Science; postdoc UPenn; >40 publications; leads medicinal chemistry and drug discovery) |
| Scientific Advisory Board | Magid Abou-Gharbia, PhD, FRSC (Temple University; ex-Wyeth SVP; 10 marketed drugs) |

## Analysis

Progenra's PINK1 activator program occupies an intriguing but high-risk position in the mitophagy competitive landscape. The headline claim -- 20x potency vs. AbbVie's clinical-stage PINK1 molecule -- is attention-grabbing but unverified in peer-reviewed literature as of February 2026. The claim that loss-of-function PINK1 mutants can be pharmacologically reactivated is scientifically ambitious; if validated, it would represent a genuine precision medicine approach for the ~5-10% of hereditary PD cases caused by PINK1 mutations. However, the addressable population is small (precision PINK1-mutation PD), the data is entirely preclinical and unpublished, and the company has no disclosed VC backing.

**Analytical estimate -- probability of reaching Phase 1 by 2027 as stated: ~15-25%. This is our assessment, not from a published source. The reasoning:** Progenra is grant-funded with no disclosed VC investment, which severely limits the capital available for IND-enabling studies, GMP manufacturing, and regulatory filings. The typical cost from late preclinical to IND is $5-15M, and MJFF grants alone are unlikely to cover this. The company has been operating since 2005 with deep UPS expertise but has not advanced any program to clinical stage in 20 years. Against this: the MJFF grants provide credibility and structured milestones, the team has genuine domain expertise (Butt and Suresh have decades in ubiquitin biology), and the 20x potency claim, if real, would attract partnership or acquisition interest from pharma companies active in the mitophagy space. The most likely path to clinical development is a licensing deal or acquisition by a larger company with PD pipeline interest.

**Key risk factors:**
1. No peer-reviewed publication of the PINK1 activator compound or its potency data
2. No disclosed animal model efficacy data (neurodegeneration, dopaminergic neuron protection)
3. No evidence of BBB penetration for the lead compound
4. Grant-funded operations with no visible path to the $5-15M+ needed for IND-enabling studies
5. 20-year-old company that has not previously advanced any compound to clinical stage
6. The Science Advances (2025) finding that PINK1/Parkin activators may work by sensitizing cells to stress rather than direct pathway activation -- if this applies to Progenra's compounds, the therapeutic window and safety profile become critical unknowns

**What would change the thesis:**
- Peer-reviewed publication confirming the 20x potency claim and mutant PINK1 reactivation
- Licensing deal or partnership with a pharma company (e.g., if AbbVie, which paid $110M for Mitokinin, acquires or partners with Progenra for a differentiated PINK1 approach)
- VC financing round (Series A) providing IND-enabling capital
- Disclosed in vivo data showing neuroprotection in PINK1-mutant animal models
- Positive readout from AbbVie's [[abbv-1088]] Phase 1 validating PINK1 as a druggable target (rising tide lifts all boats in the pathway)

## References

### Press Releases & Filings
- [A New Parkinson's Disease Drug Function in Inherited form of Parkinson's Disease -- Progenra Press Release (June 2025)](https://progenra.com/press-releases/a-new-parkinsons-disease-drug-function-in-inherited-form-of-parkinsons-disease/)
- [A New Drug by Progenra Inc. Functions in Parkinson's Disease -- BusinessWire (July 2025)](https://www.businesswire.com/news/home/20250709934751/en/A-New-Drug-by-Progenra-Inc.-Functions-in-Parkinsons-Disease)
- [Progenra Inc. Receives Therapeutic Pipeline Award from MJFF (Dec 2018)](https://www.businesswire.com/news/home/20181218005826/en/Progenra-Inc.-Receives-Therapeutic-Pipeline-Award-from-The-Michael-J.-Fox-Foundation-for-Parkinson%E2%80%99s-Research-and-Drug-Development)

### MJFF Grants
- [PINK1 Activators for Treating Parkinson's Disease -- MJFF Grant Page (2025)](https://www.michaeljfox.org/grant/pink1-activators-treating-parkinsons-disease)
- [Parkinson's Disease Therapeutics Pipeline Program -- MJFF](https://www.michaeljfox.org/grant/parkinsons-disease-therapeutics-pipeline-program)

### Publications
- [Activation of parkin by a molecular glue -- Nature Communications (2024)](https://www.nature.com/articles/s41467-024-51889-3) -- BIO-2007817 Parkin molecular glue (Biogen; related but distinct from Progenra's PINK1 program)
- [A molecular glue for PRKN/parkin -- Autophagy (2024)](https://pubmed.ncbi.nlm.nih.gov/39699041/) -- Commentary on BIO-2007817
- [Pharmacological PINK1 activation ameliorates Pathology in Parkinson's Disease models -- Nature (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11100876/) -- MTK-458 preclinical data (AbbVie/Mitokinin)
- [Putative PINK1/Parkin activators lower the threshold for mitophagy by sensitizing cells to mitochondrial stress -- Science Advances (2025)](https://www.science.org/doi/10.1126/sciadv.ady0240) -- Mechanistic caution on PINK1/Parkin activator class
- [The Ubiquitin Proteasome System as a Therapeutic Area in Parkinson's Disease -- PubMed (2023)](https://pubmed.ncbi.nlm.nih.gov/36739586/) -- Progenra-affiliated review

### Media Coverage
- [Progenra Breakthrough Offers New Hope for Parkinson's Disease and Beyond -- MyChesCo](https://www.mychesco.com/a/news/health-medical/research/progenra-breakthrough-offers-new-hope-for-parkinsons-disease-and-beyond/)
- [Parkinson's Research at Progenra Supported by MJ Fox Foundation Award -- Parkinson's News Today (2018)](https://parkinsonsnewstoday.com/news/michael-j-fox-foundation-grants-therapeutic-pipeline-award-support-progenra-work/)

### Company
- [Progenra website](https://progenra.com/)
- [Progenra Management Team](https://progenra.com/about/management/)
- [Progenra Therapeutic Areas](https://progenra.com/therapeutic-focus/therapeutic-areas/)
- [Progenra UbiPro Platform](https://progenra.com/therapeutic-focus/rd-platform/)
- [Progenra -- BIO International Convention 2026 Exhibitor Profile](https://convention.bio.org/exhibitors/progenra-inc)

### Competitive Context
- [AbbVie Exercises Exclusive Right to Acquire Mitokinin (Oct 2023)](https://news.abbvie.com/2023-10-05-AbbVie-Exercises-Exclusive-Right-to-Acquire-Mitokinin,-Further-Strengthening-Neuroscience-Pipeline)
- [Mission Therapeutics raises $13.3M for MTX325 Phase 1b (Oct 2025)](https://missiontherapeutics.com/mission-therapeutics-raises-13-3-million-to-progress-first-in-class-parkinsons-disease-candidate-mtx325-through-clinical-trials/)
- [Vincere Biosciences Awarded $5M from MJFF (Nov 2025)](https://www.prnewswire.com/news-releases/vincere-biosciences-awarded-5-million-from-the-michael-j-fox-foundation-to-advance-parkinsons-therapeutic-toward-clinical-trials-302617918.html)
