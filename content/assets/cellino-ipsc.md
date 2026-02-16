---
drug_name: "Cellino iPSC Platform (MGH)"
aliases: ["Cellino Nebula", "Cellino Foundry", "NCT06687837"]
target: "dopaminergic neuron replacement (autologous iPSC-derived DA progenitors)"
mechanism: "AI-driven autonomous iPSC manufacturing platform (Nebula) producing patient-specific midbrain dopaminergic progenitors from skin-derived fibroblasts, transplanted bilaterally into the putamen"
modality: "platform"
developer: "Cellino Biotech"
company_type: "startup"
publicly_traded: false
partner: "Mass General Brigham"
partner_type: "academic"
stage: "Phase 1"
status: "Active"
patient_population: "Advanced PD with motor fluctuations, on stable levodopa/dopamine agonists"
route_of_administration: "intracranial (bilateral stereotactic injection into putamen)"
key_biomarkers: ["18F-DOPA PET (graft survival)", "MDS-UPDRS Part III", "CT/MRI safety imaging"]
confidence_rating: "3/10"
next_catalyst: "Phase 1 safety/feasibility data from MGH trial"
catalyst_date: "2027"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-16
company_link: "[[companies/cellino-biotech]]"
partner_link: "[[companies/mass-general-brigham]]"
---

# Cellino iPSC Platform (MGH)

## Summary

Cellino Biotech (startup, private) is a manufacturing platform company deploying its AI-driven Nebula system to produce autologous iPSC-derived dopaminergic neurons for a Phase 1 Parkinson's trial (NCT06687837, N=8) led by neurosurgeon Jeffrey Schweitzer at Massachusetts General Hospital. The Cellino Foundry -- the first hospital-based autonomous iPSC manufacturing facility in the US, launched February 2025 -- uses closed-cassette laser cell management and deep learning to automate iPSC reprogramming, expansion, and differentiation, addressing the manufacturing scalability bottleneck that limits all autologous cell therapies. This program is distinct from the parallel NRI/McLean trial ([[autologous-mdaps]], NCT06422208, N=6) at Brigham and Women's Hospital, though both originate from the same scientific lineage (Schweitzer/Isacson, NEJM 2020). If the Cellino platform demonstrates reproducible, cost-effective manufacturing across 8 patients and clinical safety is confirmed, it validates decentralized autologous iPSC manufacturing as commercially viable -- potentially transforming the economics of [[anpd001|ANPD001]], [[ux-da001|UX-DA001]], and the broader autologous cell therapy field. If manufacturing variability persists or costs remain prohibitive despite automation, the field consolidates around allogeneic approaches like [[bemdaneprocel]].

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Mass General Brigham (GCTI) |
| Deal Date | February 2025 |
| Upfront | Undisclosed |
| Total (Biobucks) | Undisclosed |
| Deal Type | Partnership |

## Notes

### Science
- Cellino's Nebula platform combines three technologies: (1) label-free optical imaging to monitor cell state in real time, (2) high-speed laser cell management that uses laser-generated bubbles to precisely remove unwanted or undifferentiated cells, and (3) deep learning algorithms that automate reprogramming, expansion, and differentiation decisions within a closed cassette format
- The closed-cassette design eliminates manual handling -- a major source of contamination and batch-to-batch variability in traditional iPSC manufacturing. The system is designed to be deployable at hospital sites ("point-of-care manufacturing") rather than requiring centralized GMP facilities
- The Parkinson's application takes patient skin fibroblasts, reprograms them into iPSCs, differentiates them into midbrain dopaminergic progenitors (mDAPs) with substantia nigra pars compacta (A9-type) phenotype, and delivers them into the putamen bilaterally
- The autologous approach eliminates immunosuppression entirely -- a meaningful clinical advantage given that chronic immunosuppression carries infection, malignancy, and metabolic risks in an elderly PD population
- Core scientific question: can automated manufacturing solve the inter-patient variability problem? The Cell Stem Cell 2025 preclinical study (Kim, Isacson et al.) showed 1-of-4 patient iPSC lines failed to produce efficacious mDAPs despite meeting in vitro quality criteria -- automated manufacturing may improve consistency but cannot eliminate biological variability inherent to individual donor cells
- The Nebula platform uses a "Cellinoverse" digital simulation environment to model biomanufacturing behavior in silico before running physical processes, potentially enabling predictive quality control
- Founded 2017 by Nabiha Saklayen (CEO, Harvard PhD in physics/laser optics), Marinna Madrid (CTO, Harvard PhD in applied physics), and Matthias Wagner -- the core technology originated from laser-based intracellular delivery research at Harvard

### Clinical

**Schweitzer MGH Phase 1** | NCT06687837 | N=8 | Advanced PD on stable levodopa/dopamine agonists
- **Design:** Open-label, dose-escalation with two arms: Group I (4 million autologous dopaminergic cells, bilateral) and Group II (8 million cells, bilateral)
- **Primary endpoint:** Safety and tolerability of autologous mDAP transplantation -- adverse events, neuroimaging (CT, MRI) monitoring over 2 years
- **Key secondary:** 18F-DOPA PET (graft survival), MDS-UPDRS assessments, clinical improvement monitoring
- **Procedure:** Fibroblast-derived autologous iPSC-mDAPs transplanted bilaterally into putamen; no immunosuppression
- **PI:** Jeffrey Schweitzer, MD, PhD (George A. Lopez, MD Endowed Chair in Neurosurgery, MGH)
- **Manufacturing:** Cellino Nebula platform at the MGH-based iPSC Foundry
- **Cell production timeline:** 4-8 weeks per patient from fibroblast collection to transplant-ready product
- **Follow-up:** 2 years with regular clinical and imaging assessments
- **Status:** Recruiting as of late 2024/early 2025
- **Interpretation:** The dose-escalation design (4M vs. 8M cells) directly addresses a key question from the field: whether higher cell doses improve engraftment and clinical outcomes. The 8-patient enrollment is slightly larger than the parallel NRI trial (N=6), and the manufacturing automation via Cellino's Nebula platform is the key differentiator -- this trial is as much a test of the manufacturing platform as it is of the cell therapy itself

**Schweitzer Single-Patient Proof-of-Concept** | No NCT | N=1 | Published NEJM May 2020
- **Key results:** MDS-UPDRS Part III improved from 38 to 29 at 24 months; off-time decreased from 3 hrs/day to 1 hr/day; 18F-DOPA PET confirmed graft survival; no immunosuppression, no graft-induced dyskinesia
- **Status:** Completed
- **Interpretation:** Landmark first-in-human demonstration that autologous iPSC-DA neurons can survive in the human brain. This case underpins the scientific rationale for both the MGH trial and the parallel [[autologous-mdaps|NRI trial]]. Note that manufacturing for this case used traditional manual methods, not Cellino's platform

### Financial
- **Total raised:** ~$105M+ across Series A ($80M, January 2022, led by Leaps by Bayer) and ARPA-H grant ($25M, September 2024), plus undisclosed seed funding. Key investors: Leaps by Bayer, 8VC, Khosla Ventures, Engine Ventures
- **ARPA-H award:** Up to $25M from the Advanced Research Projects Agency for Health, the first project funded by the Scalable Solutions Mission Office -- positioned the Nebula platform as a national security/health infrastructure priority
- **Bayer connection:** Leaps by Bayer led the Series A. Bayer also owns BlueRock Therapeutics ([[bemdaneprocel]]). This creates an unusual strategic position where Bayer has invested in both the leading allogeneic (BlueRock) and the leading autologous manufacturing platform (Cellino) -- hedging modality risk
- **Company valuation:** Not publicly disclosed; PitchBook profile exists but behind paywall
- **Revenue model:** Cellino is a platform company, not a therapeutic developer. Revenue would come from manufacturing partnerships, Foundry deployments, and per-patient manufacturing fees. The MGH partnership is the first clinical deployment
- **COGS thesis:** Autologous cell therapy COGS with traditional manufacturing estimated at $100K+ per patient (analogous to CAR-T). Cellino's value proposition is that autonomous manufacturing in a closed cassette can reduce this to commercially viable levels -- no published estimates yet
- **Competitive funding context:** Cellino's $105M+ is well-capitalized for a platform company but modest compared to therapeutic developers: [[anpd001|Aspen Neuroscience]] ($280M+ total), [[bemdaneprocel|BlueRock/Bayer]] ($1B+ acquisition)

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "dopaminergic neuron replacement") AND file.name != "cellino-ipsc"
SORT stage DESC
```

- [[bemdaneprocel]] (BlueRock/Bayer) is the overall cell therapy leader: allogeneic ESC-derived, Phase 3 (exPDite-2, N~102), FDA RMAT + Fast Track. Allogeneic manufacturing scales inherently better than autologous but requires lifelong immunosuppression -- an open long-term safety question
- [[anpd001|ANPD001]] (Aspen Neuroscience) is the most direct competitor: also autologous iPSC-derived, further along clinically (ASPIRO Phase 1/2a, 6-month data showing 45% MDS-UPDRS Part III improvement), and developing its own automated manufacturing. Cellino could theoretically serve as a manufacturing partner for programs like ANPD001 if the platform proves superior
- [[autologous-mdaps]] (NRI/McLean/Oryon) is the parallel academic trial using the same Schweitzer/Isacson science but traditional (non-automated) manufacturing at BWH. The two trials together constitute a natural experiment comparing automated (Cellino) vs. manual manufacturing of the same fundamental cell product
- [[ux-da001|UX-DA001]] (UniXell) is China's autologous iPSC entry -- uses blood-derived (not skin-derived) iPSCs, which may have different reprogramming kinetics relevant to automated platforms
- [[kyoto-ipsc|Kyoto iPSC-DA]] and [[stem-pd|STEM-PD]] represent the allogeneic iPSC and ESC alternatives, respectively
- Cellino's unique competitive position is as a manufacturing enabler rather than a therapeutic competitor -- if the Nebula platform works, it could power multiple autologous programs rather than competing with them

## Analysis

Cellino occupies a distinct niche in the PD cell therapy landscape: it is primarily a manufacturing platform company that has chosen Parkinson's as its first clinical proof-of-concept. The MGH trial (NCT06687837) is therefore a dual test -- of both the autologous iPSC-derived dopaminergic cell therapy itself and of the Nebula autonomous manufacturing platform that produces it. This makes the trial's implications broader than any single therapeutic asset.

**Analytical estimate -- Platform validation probability: 40-50%; clinical success probability (safety): 65-70%.** This is our assessment, not from a published source. The reasoning: For platform validation, the base rate for novel manufacturing platforms successfully producing clinical-grade cell products at first deployment is moderate (~50%). Adjustments upward: $25M ARPA-H backing signals government-level technical diligence (+5%), and the underlying biology is validated by the Schweitzer NEJM 2020 case (+5%). Adjustments downward: no published manufacturing data from the Nebula platform in human iPSCs (-5%), the biological variability problem (Cell Stem Cell 2025, 1-of-4 lines failing) may not be solvable by manufacturing automation alone (-5%). For clinical safety, the autologous approach has a clean track record from the N=1 case and the parallel NRI trial (3 of 6 dosed without reported safety issues), yielding a high baseline.

**Signal analysis:** The Bayer dual investment is the most strategically significant data point. Leaps by Bayer led Cellino's $80M Series A while Bayer owns BlueRock outright. This is not contradictory -- it is a deliberate hedging strategy. If allogeneic approaches face long-term immune rejection issues (a real possibility given that immunosuppression in elderly PD patients carries significant morbidity), Bayer has the autologous manufacturing infrastructure already funded. Conversely, if autologous proves too expensive or variable, Bayer has BlueRock as the primary asset. The $25M ARPA-H award further validates the platform thesis -- ARPA-H funding signals that the US government views decentralized cell therapy manufacturing as a strategic priority beyond any single disease indication.

The key question for Cellino is not whether the cells work (the Schweitzer/Isacson science is well-validated) but whether automated manufacturing can solve the three fundamental problems of autologous cell therapy: (1) cost (can per-patient COGS drop from $100K+ to a commercially viable level?), (2) consistency (can automation reduce the inter-patient failure rate below the 25% preclinical benchmark?), and (3) speed (can the 4-8 week manufacturing timeline be compressed?). The MGH trial will provide the first real-world data on all three questions. If the answers are favorable, Cellino becomes an essential infrastructure layer for the entire autologous cell therapy field -- not just in PD but across diabetes, cardiovascular disease, and macular degeneration. If not, the autologous paradigm remains a boutique academic exercise.

## References

### Clinical Trials
- [Schweitzer MGH Phase 1](https://clinicaltrials.gov/study/NCT06687837) -- NCT06687837
- [NRI Phase 1 (parallel trial)](https://clinicaltrials.gov/study/NCT06422208) -- NCT06422208

### Key Publications
- [Personalized iPSC-Derived Dopamine Progenitor Cells for Parkinson's Disease | NEJM (May 2020)](https://www.nejm.org/doi/full/10.1056/NEJMoa1915872)
- [Pre-clinical safety and efficacy of human iPSC-derived products for autologous cell therapy in PD | Cell Stem Cell (Mar 2025)](https://www.cell.com/cell-stem-cell/abstract/S1934-5909(25)00006-2)
- [Human autologous iPSC-derived dopaminergic progenitors restore motor function in PD models | JCI (Nov 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6994130/)
- [Making personalized, autologous cell therapies accessible: Interview with Cellino Biotech | Regen Med (2022)](https://www.tandfonline.com/doi/full/10.2217/rme-2022-0027)

### Press Releases & Filings
- [Cellino Launches U.S.'s First Nebula-Powered iPSC Foundry for Scalable Autologous Biomanufacturing | BusinessWire (Feb 2025)](https://www.businesswire.com/news/home/20250224202433/en/Cellino-Launches-U.S.s-First-Nebula-Powered-iPSC-Foundry-for-Scalable-Autologous-Biomanufacturing)
- [Clinical Trial Tests Novel Stem-Cell Treatment for Parkinson's Disease | Mass General Brigham (Mar 2025)](https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/clinical-trial-novel-stem-cell-treatment-for-parkinsons)
- [Cellino Awarded $25M in Funding from ARPA-H | BusinessWire (Sep 2024)](https://www.businesswire.com/news/home/20240910871353/en/Cellino-Awarded-$25M-in-Funding-from-the-Advanced-Research-Projects-Agency-for-Health-ARPA-H)
- [Bayer leads $80M funding round for Cellino | Fierce Pharma (Jan 2022)](https://www.fiercepharma.com/manufacturing/bayer-leads-80-million-series-a-investment-betting-cellino-biotech-s-cell-therapy)
- [Cellino launches stem cell Foundry at Mass General | Regen Report (Mar 2025)](https://theregenreport.com/2025/03/04/cellino-launches-stem-cell-foundry-at-mass-general/)
- [Cellino wins $25M federal grant | Fierce Pharma](https://www.fiercepharma.com/manufacturing/cellino-wins-25m-federal-grant-develop-advanced-bio-manufacturing-tech)
