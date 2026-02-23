---
drug_name: "Lixisenatide"
aliases: ["Adlyxin", "Lyxumia"]
target: "GLP-1 receptor (neuroprotection via insulin signaling, anti-neuroinflammation)"
mechanism: "GLP-1 receptor agonist repurposed from diabetes; activates PI3K/Akt and cAMP/PKA signaling to reduce neuroinflammation, oxidative stress, and alpha-synuclein accumulation"
modality: "small molecule"
developer: "Toulouse University Hospital (academic)"
company_type: "academic"
publicly_traded: false
partner: "Sanofi (drug supply)"
partner_type: "big pharma"
stage: "Phase 2"
status: "Active"
patient_population: "Early PD (<3 years from diagnosis), on stable symptomatic therapy, no motor complications"
route_of_administration: "SC (daily injection)"
key_biomarkers: ["MDS-UPDRS Part III", "DaT-SPECT"]
confidence_rating: "5/10"
next_catalyst: "Phase 3 trial initiation (Cure Parkinson's-led)"
catalyst_date: "2026-2027"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/toulouse-university-hospital]]"
partner_link: "[[companies/sanofi]]"
---

# Lixisenatide

## Summary

The LixiPark Phase 2 trial (NEJM, April 2024) is the first GLP-1 receptor agonist to show statistically significant slowed motor progression in PD: 3.08-point difference on MDS-UPDRS Part III vs. placebo (p=0.007) at 12 months, with the lixisenatide group essentially flat (-0.04) while placebo worsened (+3.04). The 2-month washout data showed persistent separation, raising the possibility of disease modification rather than symptomatic benefit. However, 46% nausea and 13% vomiting are significant tolerability hurdles, and secondary endpoints did not consistently support the primary. Critically, the closely related GLP-1 agonist exenatide failed its Phase 3 trial (Lancet, Feb 2025), casting doubt on the class thesis. Cure Parkinson's and the Toulouse/Bordeaux investigators (Profs. Olivier Rascol and Wassilios Meissner) are planning a Phase 3. If that trial confirms disease modification, lixisenatide becomes a repurposed, low-cost, first-in-class PD disease-modifying therapy. If it fails, the GLP-1 class for PD is likely exhausted alongside the exenatide and [[abl301|NLY01]] failures.

## Notes

### Science
- GLP-1 receptor agonists activate PI3K/Akt/mTORC1, cAMP/PKA, MEK/ERK, and CREB/BDNF signaling pathways in neurons, producing neuroprotection through multiple mechanisms: reduced neuroinflammation, decreased oxidative stress, enhanced mitochondrial function, improved insulin sensitivity, and reduced alpha-synuclein accumulation
- Lixisenatide is a synthetic 44-amino-acid peptide (exendin-4 analogue) originally developed by Zealand Pharma and licensed to Sanofi; approved for type 2 diabetes as Adlyxin (US, 2016) and Lyxumia (EU, 2013), though Sanofi has since discontinued marketing in both markets (US 2023, EU withdrawn Dec 2025) due to competitive pressure from longer-acting GLP-1 agents
- Key differentiator vs. exenatide: lixisenatide has higher GLP-1R binding affinity and different pharmacokinetics (once-daily vs. once-weekly for extended-release exenatide). Whether the pharmacokinetic profile matters for CNS effects is an open question — continuous vs. pulsatile receptor stimulation may produce different neuroprotective responses
- The neuroprotection hypothesis is target-agnostic for PD subtype — GLP-1R agonists should theoretically benefit all PD patients regardless of genetic background, unlike [[biib122|LRRK2]] or [[pariceract|GBA1]] approaches that target genetic subpopulations
- Open question: does the drug cross the blood-brain barrier in sufficient concentrations? Preclinical data suggests CNS penetration but human CSF data from LixiPark has not been published. The mechanism may also work partly through peripheral effects (gut-brain axis, vagal nerve signaling, systemic inflammation reduction)
- Epidemiological studies have shown reduced PD incidence in type 2 diabetes patients taking GLP-1 agonists, providing population-level support for the neuroprotection hypothesis

### Clinical

**LixiPark (Phase 2)** | NCT03439943 | N=156 | Early PD (<3 years, on stable symptomatic therapy)
- **Primary endpoint:** Change from baseline in MDS-UPDRS Part III (motor) at 12 months, assessed in the on-medication state → **Lixisenatide -0.04 vs. placebo +3.04; difference 3.08 [95% CI 0.86-5.30], p=0.007**
- **Key secondary:** After 2-month washout (14 months), off-medication MDS-UPDRS Part III scores were 17.7 (lixisenatide) vs. 20.6 (placebo) — persistent separation suggestive of disease modification, though not formally tested for significance. Other secondary endpoints (non-motor symptoms, quality of life) did not consistently support the primary finding
- **Safety:** Nausea in 46% and vomiting in 13% of lixisenatide participants — GI side effects were the main tolerability concern. No serious safety signals. Dose titration over 14 days (10 mcg to 20 mcg daily)
- **Status:** Completed. Published NEJM April 2024 (Meissner et al.)
- **Interpretation:** First positive Phase 2 for any GLP-1 agonist in PD. The primary endpoint hit with p=0.007 is robust. The washout data is provocative for disease modification but the 2-month washout may be insufficient to fully exclude long-lasting symptomatic effects. The disconnect between a strong motor primary and inconsistent secondaries is a concern. Trial was relatively small (N=156) and conducted at 21 French sites of the NS-Park network — needs replication at scale

### Financial
- **LixiPark was an investigator-initiated trial** funded by the French Ministry of Health and Cure Parkinson's (UK charity), with support from the Van Andel Institute. Sanofi provided lixisenatide and placebo but was not the sponsor and holds no PD-specific development obligations
- **No commercial deal exists for PD indication.** Lixisenatide is off-patent or near off-patent; Sanofi has withdrawn it from the diabetes market in both the US (2023) and EU (Dec 2025). This means a Phase 3 for PD would likely need public/philanthropic funding or a new commercial partner willing to pursue a repurposed generic
- **Cure Parkinson's** is the key funding organization driving Phase 3 planning — they funded the original LixiPark trial and the exenatide Phase 3
- **Cost advantage:** If approved for PD, a repurposed small molecule peptide with expired/expiring patents could be dramatically cheaper than biologics or gene therapies — potentially $5,000-10,000/year vs. $50,000-200,000+ for novel disease-modifying therapies
- **Comparison:** The exenatide Phase 3 (Exenatide-PD3) was also Cure Parkinson's-funded and ran at academic sites — the same infrastructure would likely be leveraged for a lixisenatide Phase 3

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[liraglutide]] | Phase 2 | Active | Academic (Cedars-Sinai / Cure Parkinson's) | small molecule |
| [[lixisenatide]] | Phase 2 | Active | Toulouse University Hospital (academic) | small molecule |
| [[nly01]] | Phase 2 | Active | Neuraly (D&D Pharmatech) | small molecule |
| [[pt320]] | Phase 2 | Failed | Peptron | small molecule |
| [[semaglutide]] | Phase 2 | Active | Novo Nordisk / Osaka University | small molecule |
| [[exenatide]] | Phase 3 | Failed | UCL (Tom Foltynie) | small molecule |

- Lixisenatide is the **only GLP-1 agonist with a positive PD trial** — the class landscape is otherwise negative or inconclusive:
  - **Exenatide** (AstraZeneca/Bydureon): Phase 3 Exenatide-PD3 trial (N=194, 96 weeks) **failed** — no difference vs. placebo on MDS-UPDRS Part III off-medication (Lancet, Feb 2025). This is the single biggest risk factor for the lixisenatide thesis
  - **NLY01** (Neuraly): Phase 2 (N=255) overall **negative** on MDS-UPDRS Parts II+III at 36 weeks, though a post-hoc subgroup in patients <60 showed ~5-point improvement (p<0.01)
  - **Liraglutide** (Novo Nordisk/Victoza): Phase 2 (N=63) showed improvement in non-motor symptoms and quality of life but **no significant motor benefit** on MDS-UPDRS Part III
  - **Semaglutide** (Novo Nordisk/Ozempic): Phase 2 in PD ongoing (NCT03659682); failed Phase 3 in Alzheimer's (EVOKE/EVOKE+), weakening the broader neurodegeneration thesis for GLP-1 agents
- The competitive dynamics are unusual: lixisenatide competes within its own drug class rather than against other PD targets. Success or failure will be read as a class effect signal by the field
- If lixisenatide Phase 3 succeeds: validates GLP-1R as PD target, raises questions about why exenatide failed (pharmacokinetic differences? population selection?), opens door for next-gen GLP-1 agents designed for CNS
- The disease modification thesis is distinct from the symptomatic approaches ([[tavapadon]], [[mesdopetam]], [[p2b001|P2B001]]) and orthogonal to genetic PD targets ([[biib122|LRRK2]], [[pariceract|GBA1]])

## Analysis

Lixisenatide sits at a pivotal and paradoxical position in PD drug development. It produced the cleanest positive Phase 2 result of any disease-modifying candidate in PD in recent years — a statistically significant primary endpoint in a well-designed, placebo-controlled trial published in the NEJM. Yet it faces a headwind that no other positive Phase 2 asset confronts: a closely related molecule (exenatide) failed definitively in Phase 3 just months later. The question is whether lixisenatide's positive result reflects a genuine pharmacological distinction or whether it was a Phase 2 statistical artifact that will not replicate.

**Analytical estimate — Phase 3 success probability: 20-25%.** This is our assessment, not from a published source. The reasoning:
- Base rate: GLP-1 agonists in PD Phase 2 have a 1/4 positive rate (lixisenatide only); exenatide failed Phase 3 → starting point ~15%
- Adjustments upward: strong primary endpoint p-value of 0.007 (+5%), washout data suggesting disease modification (+5%), biologically plausible multi-pathway mechanism (+5%), published in NEJM (rigorous peer review) (+3%)
- Adjustments downward: exenatide Phase 3 failure in same class (-10%), small Phase 2 sample (N=156) (-5%), secondary endpoints inconsistent with primary (-3%), 46% nausea raising unblinding risk (-3%), academic sponsor without pharma resources for optimal Phase 3 design (-2%)
- Net: ~20-25%

**Signal analysis:**
- Sanofi's non-involvement is telling. They originated the molecule, supplied drug for the trial, but have not pursued the PD indication. This likely reflects commercial calculus (off-patent molecule, no exclusivity) rather than scientific skepticism, but it means Phase 3 must be funded through non-traditional channels — Cure Parkinson's, government grants, and philanthropic capital. This creates execution risk that company-sponsored programs do not face.
- The exenatide failure is the central interpretive challenge. Optimists argue that lixisenatide's pharmacokinetic profile (daily dosing, higher receptor affinity) produces a different biological effect than weekly exenatide. Pessimists note that if the mechanism is the same GLP-1R activation, pharmacokinetic differences should not fundamentally alter the outcome. The exenatide trial also used a different population (moderate PD, longer disease duration) and assessed off-medication scores, complicating direct comparison.
- The tolerability profile (46% nausea) is manageable for a disease-modifying therapy in a progressive neurodegenerative disease, but it creates a practical unblinding risk in trials — participants who experience nausea may correctly guess they are on active drug, potentially influencing subjective motor assessments. A Phase 3 design would need to address this, possibly through active placebo or GI symptom masking.
- If positive, lixisenatide's economic profile as a repurposed, potentially generic molecule could be transformative for PD patients globally — high accessibility and low cost. However, the lack of patent protection also means limited commercial incentive, which may slow adoption and marketing compared to proprietary disease-modifying therapies like [[prasinezumab]].

## References

### Clinical Trials
- [LixiPark Phase 2](https://clinicaltrials.gov/study/NCT03439943) — NCT03439943

### Key Publications
- [Trial of Lixisenatide in Early Parkinson's Disease | NEJM (April 2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2312323)
- [Exenatide Phase 3 in Parkinson's Disease | The Lancet (Feb 2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02808-3/fulltext)
- [Safety, tolerability, and efficacy of NLY01 in early untreated PD | PubMed](https://pubmed.ncbi.nlm.nih.gov/38101901/)
- [GLP-1 receptor agonists in Parkinson's disease: systematic review with meta-analysis | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12374370/)
- [GLP-1 class drugs show protective effects in PD and AD clinical trials | Neuropharmacology (2024)](https://www.sciencedirect.com/science/article/pii/S0028390824001217)
- [Neuroprotective effects of GLP-1 in Alzheimer's and Parkinson's | Frontiers Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.970925/full)

### Press Releases & Filings
- [Phase 2 trial results of lixisenatide published | Cure Parkinson's (April 2024)](https://cureparkinsons.org.uk/2024/04/phase-2-trial-results-of-lixisenatide-published/)
- [Results of Parkinson's Trial for Diabetes Drug Lixisenatide | MJFF](https://www.michaeljfox.org/news/results-parkinsons-trial-diabetes-drug-lixisenatide-published)
- [LixiPark trial overview | Movement Disorders Society](https://www.movementdisorders.org/Moving-Along/2024-issue3/LIXIPARK)
- [Lixisenatide profile | Alzforum](https://www.alzforum.org/therapeutics/lixisenatide)
- [Exenatide-PD3 results published | Cure Parkinson's (Feb 2025)](https://cureparkinsons.org.uk/2025/02/exenatide-pd3-results-published/)
- [First phase 3 trial of GLP-1R agonist for neurodegeneration (editorial) | The Lancet (2025)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)00161-8/abstract)

### Regulatory & Market
- [Sanofi FDA Approval of Adlyxin (July 2016)](https://www.news.sanofi.us/2016-07-27-Sanofi-Receives-FDA-Approval-of-AdlyxinTM-for-Treatment-of-Adults-with-Type-2-Diabetes)
- [Lyxumia EU marketing authorisation withdrawal | EMA (Dec 2025)](https://www.ema.europa.eu/en/medicines/human/EPAR/lyxumia)
