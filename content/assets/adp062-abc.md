---
drug_name: "ADP062-ABC"
aliases: ["ADP062"]
target: "SNCA mRNA (alpha-synuclein production inhibition)"
mechanism: "siRNA targeting alpha-synuclein mRNA, conjugated to Alector Brain Carrier (ABC) for transferrin receptor-mediated transcytosis; peripheral dosing achieves CNS-wide alpha-synuclein gene silencing"
modality: "siRNA"
developer: "Alector"
company_type: "biotech"
publicly_traded: true
ticker: "ALEC"
stage: "Preclinical"
status: "Active"
patient_population: "Parkinson's disease (eventually LBD)"
route_of_administration: "SC (expected; peripheral dosing via ABC platform)"
key_biomarkers: ["CSF alpha-synuclein", "SNCA mRNA levels", "alpha-synuclein SAA"]
confidence_rating: "2/10"
next_catalyst: "Preclinical data disclosure or IND timeline announcement"
catalyst_date: "TBD"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# ADP062-ABC

## Summary

ADP062-ABC is Alector's (biotech, ALEC) alpha-synuclein siRNA conjugated to the Alector Brain Carrier (ABC) platform for peripherally dosed CNS gene silencing. Currently at the research stage -- earlier than [[aro-snca|ARO-SNCA]] (Arrowhead/Novartis, preclinical, $2.2B deal) and [[dnl422|DNL422]] (Denali, IND-enabling), both of which target the same SNCA mRNA but via different delivery platforms. ADP062-ABC's distinguishing claim is that the ABC platform enables subcutaneous or IV dosing with homogeneous brain distribution, avoiding the intrathecal delivery that doomed [[ion464|ION464]] (Ionis/Biogen, discontinued). No preclinical data have been publicly disclosed. The critical dependency is the ABC platform itself: its most advanced siRNA program, ADP064-ABC (anti-tau), will serve as the proof-of-concept for ABC-delivered siRNA before ADP062-ABC reaches the clinic. If ADP064-ABC and [[aro-snca|ARO-MAPT]] (Arrowhead's parallel tau siRNA platform validator) both succeed, the alpha-synuclein siRNA space becomes a multi-platform race. If both fail, peripherally dosed CNS siRNA is invalidated and intrathecal approaches like [[ly3962681|LY3962681]] become the default despite their dosing burden.

## Notes

### Science
- Mechanism: anti-alpha-synuclein siRNA that inhibits SNCA mRNA translation and reduces alpha-synuclein protein synthesis, conjugated to Alector Brain Carrier for BBB transcytosis
- ABC platform binds a distinct epitope on the transferrin receptor (TfR) with tunable affinity, enabling receptor-mediated transcytosis from blood to brain parenchyma
- Designed for peripheral dosing (subcutaneous or IV), which represents a major convenience advantage over intrathecal siRNA/ASO delivery if brain penetration is sufficient
- Alpha-synuclein production inhibition is mechanistically upstream of antibody-mediated clearance ([[prasinezumab]]) -- silencing SNCA mRNA prevents new aggregate formation rather than clearing existing aggregates
- SNCA gene duplication and triplication cause familial PD with dose-dependent severity, providing strong genetic validation for production reduction
- GWAS identify SNCA locus as a top PD risk variant in sporadic disease, supporting broader applicability beyond familial PD
- Key question vs. [[aro-snca|ARO-SNCA]]: Arrowhead's TRiM platform uses a distinct conjugate chemistry for CNS delivery; how does ABC TfR-mediated delivery compare in knockdown depth, distribution homogeneity, and durability?
- Key question vs. [[dnl422|DNL422]]: Denali's OTV platform also uses TfR binding (engineered Fc domain) for CNS delivery of an ASO; ADP062 uses siRNA modality -- different cargo, similar shuttle concept
- Open scientific questions: (1) what level of SNCA knockdown is therapeutic vs. toxic? Alpha-synuclein has normal synaptic functions and excessive knockdown may cause harm; (2) does ABC achieve sufficient CNS exposure for meaningful SNCA silencing? (3) durability of siRNA effect with peripheral dosing
- Limited source material -- requires primary research on ABC-siRNA pharmacology, knockdown data, and CNS distribution

### Clinical
No clinical trials initiated. No IND timeline disclosed for ADP062-ABC.

- Listed as "Research" stage on Alector pipeline (earlier than Preclinical)
- The ABC platform's lead siRNA program is ADP064-ABC (anti-tau siRNA for AD/FTD), which is in IND-enabling studies -- this will be the first ABC-siRNA to enter humans and serves as the platform validator
- [[aro-snca|ARO-SNCA]] (Arrowhead/Novartis) and [[dnl422|DNL422]] (Denali) are the closest competitive programs, both further advanced

### Financial
- Alector (NASDAQ: ALEC) had $291.1M cash as of September 30, 2025, with runway estimated through 2027
- No disclosed partnerships or licensing deals specific to ADP062-ABC
- Post-restructuring (October 2025, 49% workforce reduction), Alector is prioritizing AL050 (GCase ERT, IND 2027) and AL137 (anti-amyloid beta, IND 2026) ahead of the siRNA programs
- Comparator deal: Novartis paid $200M upfront / $2.2B total for [[aro-snca|ARO-SNCA]] -- this values a preclinical alpha-synuclein siRNA with a validated delivery platform. ADP062-ABC at research stage with an unvalidated siRNA delivery platform would command significantly less
- ADP062 likely needs external funding or partnership to advance to IND given Alector's constrained resources

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "alpha-synuclein") AND file.name != "adp062-abc"
SORT stage DESC
```

- [[aro-snca|ARO-SNCA]] (Arrowhead/Novartis, preclinical) is the dominant alpha-synuclein siRNA competitor -- $2.2B deal, TRiM platform with ARO-MAPT as near-term clinical validator. ADP062-ABC is significantly behind
- [[dnl422|DNL422]] (Denali, IND-enabling) uses the same TfR-mediated transcytosis concept (OTV platform) but delivers an ASO rather than siRNA -- functionally similar gene silencing approach with a competing delivery shuttle
- [[ly3962681|LY3962681]] (Lilly, Phase 1/2) is an intrathecal ASO -- different delivery route, already in clinic, but burdened by the intrathecal dosing disadvantage that contributed to [[ion464|ION464]] discontinuation
- [[prasinezumab]] (Roche/Prothena, Phase 3) and [[abl301|ABL301]] (ABL Bio/Sanofi) target extracellular alpha-synuclein aggregates via antibodies -- different mechanism (clearance vs. production inhibition)
- ADP062-ABC shares the ABC platform with [[al050-abc|AL050-ABC]] and [[adp065-abc|ADP065-ABC]], creating correlated platform risk: ABC validation or failure affects all three programs

## Analysis

ADP062-ABC is a very early-stage program in a crowded alpha-synuclein silencing landscape. Its competitive position depends entirely on the ABC platform's ability to deliver siRNA cargo across the BBB at therapeutically meaningful levels -- a capability that remains unproven in humans. The program sits behind both [[aro-snca|ARO-SNCA]] (which has a $2.2B Novartis partnership and the TRiM platform) and [[dnl422|DNL422]] (which is in IND-enabling studies with Denali's well-funded OTV platform), making ADP062-ABC at best the third entrant in peripherally dosed alpha-synuclein gene silencing.

The strategic logic for ADP062-ABC is sound: if the ABC platform validates through ADP064-ABC (tau siRNA) or nivisnebart (antibody), Alector can apply the same shuttle to multiple CNS targets including alpha-synuclein. This platform leverage is the core value proposition -- not the alpha-synuclein siRNA itself, which is relatively commodity cargo. However, Alector's post-restructuring resource constraints mean ADP062-ABC is unlikely to advance on Alector's current cash runway without a partner.

**Analytical estimate -- probability of reaching IND within 5 years: 15-25%.** This is our assessment, not from a published source. The reasoning:
- Base rate: research-stage programs at restructured biotechs have ~10-15% chance of reaching IND
- Adjustments upward: well-validated target with strong genetic evidence (+5%), ABC platform has multiple programs providing shared validation (+5%), strong comparator deal (Novartis/Arrowhead) signals market interest in modality (+5%)
- Adjustments downward: research stage (not yet preclinical) (-5%), Alector cash constraints and competing pipeline priorities (-10%), two competitors with more advanced programs and better-funded platforms (-5%)
- Net: ~15-25%

The decision tree for ADP062-ABC depends on multiple external events: (1) if ADP064-ABC (tau siRNA, ABC platform) shows clean CNS knockdown in Phase 1, ABC-siRNA is validated and ADP062 becomes partnerable; (2) if [[aro-snca|ARO-MAPT]] Phase 1/2a validates TRiM, the alpha-synuclein siRNA space becomes hot and ADP062 benefits from sector interest despite being behind; (3) if both platform validators fail, peripherally dosed CNS siRNA is dead and ADP062 is shelved. Alector's most likely path for ADP062 is as a partnered program, using ABC platform validation from other programs to attract a co-development deal.

## References

### Press Releases & Filings
- [Alector Q3 2025 Financial Results and Business Update (Nov 2025)](https://investors.alector.com/news-releases/news-release-details/alector-reports-third-quarter-2025-financial-results-and)
- [Alector Strategic Priorities for 2025 (Jan 2025)](https://investors.alector.com/news-releases/news-release-details/alector-reports-recent-progress-and-outlines-strategic)
- [Alector Pipeline](https://alector.com/pipeline/)

### Key Publications
- Limited source material -- requires primary research. No peer-reviewed publications specific to ADP062-ABC identified.

### Regulatory & Market
- [Alector January 2026 Corporate Presentation | MarketScreener](https://www.marketscreener.com/news/alector-january-2026-corporate-presentation-ce7e59dfd18af12d)
- [Alector Post-Latozinemab Pipeline Assessment | AInvest](https://www.ainvest.com/news/alector-pipeline-resilience-post-latozinemab-failure-assessing-risk-adjusted-long-term-catalyst-potential-2512/)
