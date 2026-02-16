---
drug_name: "CSM-101"
aliases: ["Casma TRPML1 agonist"]
target: "TRPML1 (lysosomal ion channel)"
mechanism: "First-in-class oral small molecule TRPML1 agonist that restores lysosomal function by activating the TRPML1 cation channel, enhancing clearance of toxic lipids and alpha-synuclein aggregates"
modality: "small molecule"
developer: "Casma Therapeutics"
company_type: "startup"
publicly_traded: false
partner: ""
partner_type: ""
stage: "IND-enabling"
status: "Active"
patient_population: "Gaucher's disease with PD (GD-PD); expansion to GBA-PD and idiopathic PD"
route_of_administration: "oral"
key_biomarkers: ["glucosylsphingosine", "alpha-synuclein levels", "neuromelanin"]
confidence_rating: "4/10"
next_catalyst: "IND filing with FDA"
catalyst_date: "H1 2026"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# CSM-101 (Casma TRPML1 Agonist)

## Summary

CSM-101 is a first-in-class oral TRPML1 agonist from Casma Therapeutics (startup, private) that restores lysosomal function to clear toxic lipids and alpha-synuclein, nominated as development candidate in June 2025 with IND planned H1 2026. Initial target indication is Gaucher's disease patients with Parkinson's (GD-PD), with planned expansion into GBA-associated PD and eventually idiopathic PD -- positioning it as a lysosomal-function approach orthogonal to direct GCase activation seen with [[pariceract]] and [[ambroxol]]. Preclinical data showed 30% alpha-synuclein reduction and dopaminergic neuron preservation in a hA53T rat model, plus improved survival in Gaucher's models. If the IND clears and early clinical data in genetically defined GD-PD patients shows biomarker movement on glucosylsphingosine and alpha-synuclein, this validates TRPML1 as a druggable node in the lysosomal pathway and differentiates from the GCase-focused approaches; if the IND is delayed or early tolerability/CNS exposure disappoints, the lean company (~11 employees post-restructuring) may lack runway to iterate.

## Notes

### Science
- TRPML1 (Transient Receptor Potential channel Mucolipin 1) is a non-selective lysosomal cation channel permeable to Ca2+, Fe2+, and Zn2+ that regulates lysosomal pH, autophagosome maturation, and cellular waste clearance
- CSM-101 activates TRPML1 to restore lysosomal function -- mechanistically upstream of GCase itself. While [[pariceract]] and [[ambroxol]] directly stabilize or chaperone the GCase enzyme, CSM-101 enhances overall lysosomal homeostasis including but not limited to GCase-dependent pathways
- In GBA-mutant cells, TRPML1 dysfunction leads to impaired degradation and accumulation of glucosylsphingosine and glucosylceramide (toxic lipids), which in turn impairs alpha-synuclein clearance and triggers neuroinflammation
- Published literature shows TRPML1 agonism (via tool compound ML-SA1) facilitates clearance of alpha-synuclein aggregates by promoting autophagosome maturation -- the late steps of autophagy
- Key differentiator: oral, brain-penetrant small molecule targeting lysosomal function broadly, not restricted to GCase mutation carriers. The mechanism could apply to idiopathic PD where lysosomal dysfunction occurs without GBA mutations
- Competitive mechanism: Merck acquired Calporta Therapeutics ($576M, 2019) and Caraway Therapeutics ($610M biobucks, 2023), both targeting TRPML1. Merck's sustained investment validates the target but means Casma faces a big pharma competitor on the same target
- Open question: whether TRPML1 agonism provides sufficient therapeutic benefit beyond what GCase activators achieve in GBA-PD patients, and whether the broader lysosomal activation creates off-target toxicity risks (e.g., in non-CNS lysosomal compartments)

### Clinical

No clinical trials initiated. CSM-101 is in IND-enabling studies.

**Preclinical data (GBA1 Meeting 2025 and MDS International Congress 2025):**
- **Gaucher's disease models (CBE mouse):** CSM-101 significantly reduced glucosylsphingosine levels in primary cortical neurons and significantly delayed premature lethality in CBE-treated mice
- **PD model (hA53T rat):** Rats with unilateral alpha-synuclein (hA53T) overexpression in substantia nigra received 6 weeks of CSM-101 treatment. Alpha-synuclein levels reduced by 30%; tyrosine hydroxylase-positive (TH+) dopaminergic neurons preserved
- **GBA-PD and idiopathic PD models:** CSM-101 reversed pathological phenotypes, lowered toxic alpha-synuclein levels, and preserved dopaminergic neurons
- **PK/Safety:** High CNS exposure demonstrated; well tolerated in rodent studies with favorable pharmacokinetic and safety profiles
- **IND filing:** Planned H1 2026 with the US FDA

### Financial
- **Total raised:** ~$155-183M across three rounds (Series A: $58.5M in 2018 led by Third Rock Ventures; Series B: $50M in 2020; Series C: $46M in November 2022)
- **Key investors:** Third Rock Ventures (founder/lead), Amgen Ventures, Astellas Venture Management, Eisai, Euclidean Capital, Mirae Asset Capital, Ono Venture Investment, Eventide Asset Management, Schroders Capital, The Column Group
- **Strategic investor signal:** Amgen, Astellas, Eisai, and Ono all participated in Series C -- four pharma strategics in a single round is notable validation of the autophagy/lysosomal thesis
- **Restructuring:** Company cut most staff, now operating with ~11 employees as of late 2025. CEO Frank Gentile (former COO, promoted January 2023) is leading a lean operation focused on getting CSM-101 to IND
- **Runway concern:** With $46M raised in November 2022 and significant headcount reduction, the company appears to have extended runway by cutting burn rate. IND-enabling studies and a Phase 1 trial will likely require additional capital
- **Comparable deals:** Merck's acquisitions of Calporta ($576M, 2019) and Caraway ($610M biobucks, 2023) -- both TRPML1 programs -- establish a valuation benchmark. If CSM-101 generates clinical data, Casma could be an acquisition target at a similar scale

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "GBA1") AND file.name != "casma-trpml1"
SORT stage DESC
```

- CSM-101 targets lysosomal function via TRPML1 rather than GCase directly, making it mechanistically distinct from [[pariceract]] (allosteric GCase activator, Phase 2b) and [[ambroxol]] (GCase chaperone, Phase 2). It could be complementary or competitive depending on clinical data
- **Merck (big pharma)** is the primary competitive threat: acquired both Calporta (2019) and Caraway (2023), both TRPML1-focused. Merck's programs are not publicly disclosed in detail, but the $1.2B+ total investment across two acquisitions signals deep commitment. Casma's competitive position depends on whether CSM-101 has differentiated pharmacology vs. Merck's internal TRPML1 compounds
- The GBA-PD patient population is well-defined genetically (5-15% of PD patients carry GBA1 variants), enabling enrichment strategies that reduce trial size and increase probability of detecting signal
- If [[pariceract]] succeeds in Phase 2b, it validates the lysosomal/GCase pathway broadly and supports TRPML1 agonism as a complementary or second-generation approach. If [[pariceract]] fails, it raises questions about whether lysosomal restoration is sufficient for disease modification -- though CSM-101's broader lysosomal mechanism could still differentiate

## Analysis

CSM-101 represents a scientifically interesting but high-risk early-stage bet on lysosomal function restoration via a novel target. The TRPML1 mechanism sits upstream of GCase in the lysosomal pathway, theoretically offering broader lysosomal correction than enzyme-specific approaches. The preclinical package -- 30% alpha-synuclein reduction, dopaminergic neuron preservation, improved survival in Gaucher's models -- is encouraging but standard for IND-enabling programs. The real test is whether these effects translate to measurable biomarker changes in humans.

**Analytical estimate -- Probability of reaching Phase 2 with positive biomarker data: 15-20%.** This is our assessment, not from a published source. The reasoning:
- Base rate: ~60% of IND applications are accepted, ~50% of Phase 1 trials succeed on safety -> ~30% chance of reaching Phase 2
- Adjustments upward: genetically defined initial population with clear biomarkers (glucosylsphingosine) reduces heterogeneity (+5%), strong preclinical CNS penetration data (+5%), validated target via Merck's repeat investment (+5%)
- Adjustments downward: company has ~11 employees and may lack operational capacity for clinical execution (-10%), no disclosed partnership for clinical development (-5%), Merck's parallel programs could preempt (-5%), novel target with no clinical validation in any indication (-5%)
- Net: ~15-20%

**Signal analysis:** The company's restructuring from ~38 employees to ~11 while maintaining IND-enabling momentum is a double-edged signal. On one hand, it demonstrates disciplined capital allocation -- CSM-101 survived the cut as the sole priority. On the other, a startup running IND-enabling studies and planning a clinical trial with 11 people is operationally fragile. The four pharma strategic investors (Amgen, Astellas, Eisai, Ono) in the Series C suggest potential acquirers or partners if data warrants. Merck's $1.2B+ total investment in TRPML1 via two acquisitions is the strongest external validation of the target, but also means Casma is racing against a well-funded big pharma competitor on the same mechanism. The most likely positive outcome is Casma generating enough clinical data to attract an acquisition or partnership, similar to how Merck acquired Caraway for $610M at a preclinical stage.

## References

### Key Publications
- [TRPML1 Agonists Cognitive Vitality Report | Alzheimer's Drug Discovery Foundation (April 2025)](https://www.alzdiscovery.org/uploads/cognitive_vitality_media/TRPML1_Agonists.pdf)
- [Activated Endolysosomal Cation Channel TRPML1 Facilitates Maturation of alpha-Synuclein-Containing Autophagosomes | Frontiers in Cellular Neuroscience (2022)](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2022.861202/full)
- [The activation of Mucolipin TRP channel 1 (TRPML1) protects motor neurons by promoting autophagic clearance | Scientific Reports (2019)](https://www.nature.com/articles/s41598-019-46708-5)
- [Discovery and characterization of novel TRPML1 agonists | Bioorganic & Medicinal Chemistry Letters (2023)](https://www.sciencedirect.com/science/article/abs/pii/S0960894X23004730)

### Press Releases & Filings
- [Casma Therapeutics Nominates CSM-101 as a Development Candidate for Rare and Common Forms of PD (June 5, 2025)](https://www.casmatx.com/2025/06/05/casma-therapeutics-nominates-csm-101-as-a-development-candidate-for-the-treatment-of-rare-and-common-forms-of-parkinsons-disease/)
- [Casma Therapeutics Raises $46.0M in Series C Funding (November 2022)](https://www.casmatx.com/2022/11/15/casma-therapeutics-raises-46-0-m-in-series-c-funding/)
- [Third Rock Ventures Launches Casma Therapeutics with $58.5M Investment (May 2018)](https://www.casmatx.com/third-rock-ventures-launches-casma-therapeutics-with-58-point-5-million-dollar-investment/)
- [Merck to Acquire Caraway Therapeutics (November 2023)](https://www.merck.com/news/merck-to-acquire-caraway-therapeutics-inc/)
- [Merck Acquires Caraway for up to $610M | Fierce Biotech](https://www.fiercebiotech.com/biotech/merck-seals-610m-biobucks-deal-acquire-preclinical-neurodegenerative-biotech-caraway)

### Conference Abstracts
- [CSM-101 is a Small Molecule Agonist of TRPML1 for Parkinson's-Related Disorders | MDS International Congress 2025](https://www.mdsabstracts.org/abstract/csm-101-is-a-small-molecule-agonist-of-trpml1-for-parkinsons-related-disorders/)

### Regulatory & Market
- [Assessing TRPML1 Agonists in GBA Parkinson's Disease | MJFF Grant](https://www.michaeljfox.org/grant/assessing-trpml1-agonists-gba-parkinsons-disease)
- [Casma Takes a New Therapeutic Approach to Neurodegeneration | Drug Discovery World (June 2025)](https://www.ddw-online.com/casma-takes-a-new-therapeutic-approach-to-neurodegeneration-35363-202506/)
- [Casma to Develop CSM-101 as Treatment for Parkinson's | Parkinson's News Today](https://parkinsonsnewstoday.com/news/casma-develop-csm-101-treatment-parkinsons/)
