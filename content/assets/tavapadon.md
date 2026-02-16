---
drug_name: "Tavapadon"
aliases: ["CVL-751", "PF-06649751"]
target: "dopamine D1/D5 receptor"
mechanism: "Selective D1/D5 dopamine receptor partial agonist that activates direct-pathway motor neurons while avoiding D2/D3-mediated side effects"
modality: "small molecule"
developer: "Cerevel Therapeutics"
company_type: "big pharma"
publicly_traded: true
ticker: "ABBV"
partner: "AbbVie"
partner_type: "big pharma"
stage: "NDA Filed"
status: "Active"
patient_population: "Early PD (monotherapy) and advanced PD with motor fluctuations (adjunctive to levodopa)"
route_of_administration: "oral"
key_biomarkers: ["MDS-UPDRS Parts II+III", "ON time without troublesome dyskinesia", "OFF time"]
confidence_rating: "8/10"
next_catalyst: "FDA PDUFA decision"
catalyst_date: "H1 2026"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/cerevel-therapeutics]]"
partner_link: "[[companies/abbvie]]"
---

# Tavapadon

## Summary

Tavapadon is a first-in-class selective D1/D5 dopamine receptor partial agonist that swept all three pivotal Phase 3 TEMPO trials -- TEMPO-1 and TEMPO-2 as monotherapy in early PD, TEMPO-3 as adjunctive to levodopa in motor fluctuations -- with highly significant primary endpoints (p<0.0001 across trials). AbbVie (big pharma, ABBV) acquired tavapadon via the $8.7B Cerevel Therapeutics takeover (completed August 2024) and filed the NDA in September 2025, with an FDA decision expected H1 2026. The D1/D5 selectivity is the differentiator: unlike existing D2/D3 agonists (pramipexole, ropinirole), tavapadon showed impulse control disorder rates comparable to placebo (1.4% in the OLE) and delivered ON time gains without troublesome dyskinesia. If approved, tavapadon becomes the first new dopamine agonist mechanism in PD in over two decades and could capture significant share from generic D2/D3 agonists in both early and adjunctive settings. If the FDA issues a complete response letter, AbbVie has the resources to address any deficiency, but the clean Phase 3 dataset makes a regulatory rejection unlikely.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | AbbVie |
| Deal Date | December 2023 (announced); August 2024 (closed) |
| Upfront | $8.7B (full acquisition of Cerevel Therapeutics at $45/share) |
| Total (Biobucks) | $8.7B (acquisition, not milestone-based) |
| Deal Type | Acquisition |

## Notes

### Science
- First-in-class selective partial agonist at D1 (Ki = 9 nM) and D5 (Ki = 13 nM) dopamine receptors, with negligible activity at D2 (Ki >= 6,210 nM), D3 (Ki >= 6,720 nM), and D4 (Ki >= 4,870 nM) -- approximately 700-fold selectivity for D1/D5 over D2-family
- Originated at Pfizer (PF-06649751), spun out to Cerevel Therapeutics in 2018 as part of a Bain Capital-backed neuroscience portfolio carve-out, then acquired by AbbVie in 2024
- Partial agonism at D1/D5 activates direct-pathway medium spiny neurons in the striatum, which are the primary motor output pathway. This is the same pathway that levodopa activates, but tavapadon's partial agonism avoids the pulsatile stimulation that drives dyskinesia with chronic levodopa
- Non-catechol scaffold resists COMT and MAO metabolism -- the two enzymes that degrade catecholamines like levodopa and dopamine -- providing a long half-life enabling once-daily oral dosing
- Key mechanistic advantage over D2/D3 agonists: D2/D3 receptors (targeted by pramipexole, ropinirole, rotigotine) are widely distributed in mesolimbic reward circuits, driving impulse control disorders (32% with pramipexole) and excessive daytime sleepiness. D1/D5 receptors are more localized to motor circuits, theoretically decoupling motor benefit from these psychiatric side effects
- Partial agonism prevents receptor desensitization that occurs with full dopamine replacement, potentially extending duration of therapeutic benefit
- Open question: whether D1/D5-selective agonism can match the full motor efficacy of levodopa long-term, or whether it will serve primarily as an early-disease or adjunctive agent

### Clinical

**TEMPO-1 (Phase 3, fixed-dose monotherapy)** | NCT04201093 | N=529 | Early PD (disease duration <3 years, not requiring levodopa)
- **Primary endpoint:** MDS-UPDRS Parts II+III combined score change at week 26 --> Highly significant: placebo +1.8; tavapadon 5 mg -9.7; tavapadon 15 mg -10.2 (p<0.0001 for each dose vs. placebo)
- **Key secondary:** MDS-UPDRS Part II (motor aspects of daily living) -- met in both dose groups
- **Safety:** Consistent with prior trials; majority of AEs mild-to-moderate
- **Status:** Completed (September 2024 topline)
- **Interpretation:** Robust, dose-dependent efficacy as monotherapy. The ~11-point improvement over placebo on MDS-UPDRS II+III is clinically meaningful and competitive with D2/D3 agonists, with a differentiated safety profile.

**TEMPO-2 (Phase 3, flexible-dose monotherapy)** | NCT04223193 | N=304 | Early PD (disease duration <3 years, not requiring levodopa)
- **Primary endpoint:** MDS-UPDRS Parts II+III combined score change at week 26 --> Met with statistical significance (tavapadon 5-15 mg flexible dose vs. placebo)
- **Key secondary:** MDS-UPDRS Part II -- met
- **Status:** Completed (December 2024 topline)
- **Interpretation:** Confirms TEMPO-1 in a flexible-dose design that mirrors real-world prescribing, where clinicians titrate to optimal dose. Both fixed-dose and flexible-dose monotherapy trials positive -- a clean regulatory package.

**TEMPO-3 (Phase 3, adjunctive to levodopa)** | NCT04542499 | N=507 | PD with motor fluctuations on stable levodopa
- **Primary endpoint:** Change in total ON time without troublesome dyskinesia at week 27 --> Tavapadon +1.7 hours vs. placebo +0.6 hours (net +1.1 hours; p<0.0001)
- **Key secondary:** OFF time reduction -- statistically significant in tavapadon arm
- **Status:** Completed (April 2024 topline)
- **Interpretation:** The +1.1 hour ON time gain is clinically meaningful and competitive with other adjunctive therapies (opicapone, safinamide). Critically, the ON time was "without troublesome dyskinesia" -- directly addressing the D2/D3 agonist liability.

**TEMPO-4 (Phase 3, open-label extension)** | NCT TBD | N=ongoing | Rollover from TEMPO-1/2/3 + de novo patients on levodopa
- **Primary endpoint:** Long-term safety and tolerability over 58 weeks (85 total weeks for active rollovers)
- **Key findings:** No new safety signals. Hallucination 6.3%, somnolence 4.6%, hypotension 4.1%, orthostatic hypotension 3.7%, impulse control disorders 1.4%. De novo and crossover patients showed motor improvements consistent with blinded trials.
- **Status:** Ongoing (interim data reported)
- **Interpretation:** The 1.4% ICD rate is the headline number -- dramatically lower than the 25-32% seen with D2/D3 agonists, validating the D1/D5 selectivity hypothesis in long-term treatment.

### Financial
- **Acquisition context:** AbbVie paid $8.7B for all of Cerevel Therapeutics (December 2023 announcement, August 2024 close). Tavapadon was one of several Cerevel assets including emraclidine (schizophrenia) -- the acquisition was not solely for tavapadon
- **Peak sales estimates:** Analyst range of $270M (Citi, conservative) to $1B (Truist Securities, bull case); Mizuho at $532M. Consensus clusters around $500M-$1B
- **Deal accretion:** AbbVie expects the Cerevel acquisition to be accretive to adjusted diluted EPS beginning in 2030
- **Competitive pricing context:** Tavapadon will compete with generic D2/D3 agonists (pramipexole, ropinirole <$50/month) and branded adjunctive agents (opicapone ~$400/month, safinamide ~$700/month). Novel mechanism and differentiated safety profile justify branded pricing, but generic competition on the low end constrains the addressable market
- **AbbVie PD franchise:** AbbVie also markets Duodopa/Vyalev (levodopa/carbidopa intestinal gel/subcutaneous infusion) for advanced PD, creating a portfolio spanning early to late disease. Tavapadon fills the early PD oral treatment gap

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE thesis_cluster = "symptomatic" AND file.name != "tavapadon"
SORT stage DESC
```

- Tavapadon is not a disease-modifying therapy -- it is a novel symptomatic agent competing in the established dopaminergic treatment space. Its competitors are primarily marketed generics (pramipexole, ropinirole, levodopa/carbidopa) rather than pipeline assets
- Key competitive advantage is the D1/D5 selectivity: if the 1.4% ICD rate holds post-approval, tavapadon could displace D2/D3 agonists as first-line dopamine agonist therapy, particularly in patients at risk for impulse control disorders
- In the adjunctive setting, tavapadon's +1.1 hour ON time gain competes with opicapone (+1.0 hour in BIPARK-1), safinamide (+1.4 hours in SETTLE), and istradefylline (+0.7 hours) -- tavapadon is competitive but not clearly superior on efficacy; the differentiation is the safety/tolerability profile
- Disease-modifying candidates like [[prasinezumab]], [[aro-snca|ARO-SNCA]], and [[biib122|BIIB122]] target different aspects of PD pathology and are not direct competitors -- if any succeed, tavapadon would likely be used in combination as the symptomatic backbone therapy
- No other D1/D5-selective agonists are in late-stage development; tavapadon has first-mover advantage in this mechanism class

## Analysis

Tavapadon has the cleanest regulatory path of any asset in this folder -- three positive pivotal trials with highly significant p-values, a novel mechanism with a differentiated safety profile, and the backing of a big pharma with deep regulatory experience. The question is not whether it will be approved (probability is very high) but how large the commercial opportunity will be.

**Analytical estimate -- probability of FDA approval: 90-95%.** This is our assessment, not from a published source. The reasoning: base rate for NDA-stage drugs with positive Phase 3 data is ~85%. Adjustments upward: three-for-three pivotal wins (+5%), first-in-class mechanism with clear differentiation (+3%), no safety signals requiring REMS (+2%). Adjustments downward: standard NDA review risk (manufacturing, labeling, CMC issues) (-3%). Net: ~90-95%.

The commercial question is more nuanced. Tavapadon enters a market with cheap, effective generics (pramipexole, ropinirole) that have decades of clinical familiarity. Neurologists will need to be convinced that the D1/D5 safety advantage -- particularly the low ICD rate -- justifies branded pricing over generics. The TEMPO-4 OLE data showing 1.4% ICD vs. 25-32% for D2/D3 agonists is compelling, but this was not a head-to-head comparison. Post-marketing real-world evidence will be critical for commercial uptake. The adjunctive (TEMPO-3) indication may actually be the easier commercial sell, as patients with motor fluctuations already on levodopa are seeking additional ON time without adding dyskinesia risk -- a gap that tavapadon fills cleanly.

**Signal analysis:** AbbVie's $8.7B acquisition of Cerevel was a portfolio bet on neuroscience, not a tavapadon-specific bet. Emraclidine (schizophrenia) was arguably the higher-value asset in the deal. This means tavapadon does not need to justify the entire acquisition price -- a $500M-$1B peak sales asset is accretive within a multi-asset portfolio. AbbVie's rapid progression from acquisition close (August 2024) to NDA filing (September 2025) -- barely 13 months -- signals confidence in the data package and a well-run clinical-to-regulatory handoff. The decision tree is straightforward: FDA approval in H1 2026 leads to commercial launch, with the real contest being market penetration against generics. A complete response letter would delay but likely not kill the program given the strength of the Phase 3 data.

## References

### Clinical Trials
- [TEMPO-1 Phase 3](https://clinicaltrials.gov/ct2/show/NCT04201093) -- NCT04201093
- [TEMPO-2 Phase 3](https://clinicaltrials.gov/ct2/show/NCT04223193) -- NCT04223193
- [TEMPO-3 Phase 3](https://clinicaltrials.gov/ct2/show/NCT04542499) -- NCT04542499

### Key Publications
- [Rationale and Development of Tavapadon, a D1/D5-Selective Partial Dopamine Agonist for PD | CNS Drugs (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10909821/)
- [Emerging Clinical Role of Tavapadon, a Novel Dopamine Partial Agonist, in PD | Diseases (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12468602/)
- [Efficacy and Safety of Tavapadon Adjunctive to Levodopa (TEMPO-3) | Neurology (2024)](https://www.neurology.org/doi/10.1212/WNL.0000000000208468)

### Press Releases & Filings
- [AbbVie Submits NDA for Tavapadon (Sep 2025)](https://news.abbvie.com/2025-09-26-AbbVie-Submits-New-Drug-Application-to-U-S-FDA-for-Tavapadon-for-the-Treatment-of-Parkinsons-Disease)
- [AbbVie TEMPO-1 Positive Topline Results (Sep 2024)](https://news.abbvie.com/2024-09-26-AbbVie-Announces-Positive-Topline-Results-from-Phase-3-TEMPO-1-Trial-Evaluating-Tavapadon-as-a-Monotherapy-for-Parkinsons-Disease)
- [AbbVie TEMPO-2 Positive Topline Results (Dec 2024)](https://news.abbvie.com/2024-12-09-AbbVie-Announces-Positive-Topline-Results-for-the-Phase-3-TEMPO-2-Trial-Evaluating-Tavapadon-as-a-Monotherapy-for-Parkinsons-Disease)
- [Cerevel TEMPO-3 Positive Topline Results (Apr 2024)](https://news.abbvie.com/2024-04-18-Cerevel-Therapeutics-Announces-Positive-Topline-Results-for-Tavapadon-in-Phase-3-Adjunctive-Trial-for-People-Living-with-Parkinsons-Disease)
- [AbbVie Completes Acquisition of Cerevel Therapeutics (Aug 2024)](https://news.abbvie.com/2024-08-01-AbbVie-Completes-Acquisition-of-Cerevel-Therapeutics)
- [AbbVie to Acquire Cerevel Therapeutics (Dec 2023)](https://www.prnewswire.com/news-releases/abbvie-to-acquire-cerevel-therapeutics-in-transformative-transaction-to-strengthen-neuroscience-pipeline-302008134.html)
- [Tavapadon Profile | Alzforum](https://www.alzforum.org/therapeutics/tavapadon)

### Regulatory & Market
- [Previewing Expected FDA Decisions in Neurology for 2026 | NeurologyLive](https://www.neurologylive.com/view/previewing-expected-fda-decisions-in-neurology-for-2026)
- [New PD Drug Tavapadon Submitted for FDA Review | MJFF](https://www.michaeljfox.org/news/new-parkinsons-drug-tavapadon-submitted-fda-review)
- [Tavapadon Market Size, Forecast, and Emerging Insight | DelveInsight](https://www.delveinsight.com/blog/parkinsons-disease-treatment-market)
- [Tavapadon Molecule Profile | Drug Hunter](https://drughunter.com/molecule/tavapadon-cvl-751-pf-06649751)
