---
drug_name: "Gocovri"
aliases: ["ADS-5102", "amantadine extended-release", "amantadine ER", "amantadine DR/ER"]
target: "NMDA receptor / dopamine reuptake transporter"
mechanism: "Extended-release amantadine formulation delivering NMDA receptor antagonism and weak dopamine reuptake inhibition timed to morning peak, reducing levodopa-induced dyskinesia and OFF time"
modality: "small molecule"
developer: "Supernus Pharmaceuticals"
company_type: "biotech"
publicly_traded: true
ticker: "SUPN"
partner: ""
partner_type: ""
stage: "Approved"
status: "Active"
patient_population: "PD patients on levodopa with dyskinesia or OFF episodes"
route_of_administration: "oral"
key_biomarkers: ["UDysRS", "MDS-UPDRS Part IV", "Hauser patient diaries", "ON time without troublesome dyskinesia"]
confidence_rating: ""
next_catalyst: "Generic entry (settled for March 2030)"
catalyst_date: "2030-03-04"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-20
company_link: "[[companies/supernus-pharmaceuticals]]"
---

# Gocovri

## Summary

The only FDA-approved drug for levodopa-induced dyskinesia (LID) in PD. Gocovri is a reformulated extended-release amantadine (274 mg, bedtime dosing) that delivers peak plasma levels in the morning when dyskinesia is worst. Approved August 2017 (LID) with a second indication added for OFF episodes. Originally developed by Adamas Pharmaceuticals (founded 2002, Emeryville CA); acquired by Supernus Pharmaceuticals (biotech, SUPN) in November 2021 for ~$400M upfront + $50M CVRs. Now generating ~$131M/year in net sales (FY2024), growing mid-teens annually. Generic entry settled with Sandoz for March 4, 2030; patent portfolio extends through 2038. The main competitive threat is [[mesdopetam]] (IRLAB Therapeutics), a selective D3 receptor antagonist preparing for Phase 3 that could offer a differentiated MOA without amantadine's CNS side-effect burden — but Gocovri has a decade head start and established physician familiarity.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Supernus Pharmaceuticals (acquirer) |
| Deal Date | November 2021 |
| Upfront | ~$400M ($8.10/share cash) |
| Total (Biobucks) | ~$450M ($8.10 + up to $1.00/share CVRs) |
| Deal Type | Acquisition |

CVR details: $0.50/share payable if Gocovri net sales reach $150M in any four consecutive quarters by end-2024; second $0.50/share if $225M in any four consecutive quarters by end-2025. As of mid-2025, FY2024 net sales were $130.8M — the first CVR threshold was likely not met on a trailing-four-quarter basis.

## Notes

### Science
- Amantadine is an old molecule (1966, originally an antiviral for influenza A). Immediate-release amantadine (Symmetrel) has been used off-label for PD dyskinesia for decades. Gocovri is the ER reformulation with delayed-release pellets designed for bedtime dosing with morning peak
- **Primary mechanism for LID: NMDA receptor antagonism.** Amantadine is an uncompetitive open-channel blocker of NMDA receptors that accelerates channel closure rather than simply blocking current flow. In PD, chronic levodopa causes maladaptive striatal plasticity via overactive corticostriatal glutamatergic signaling — NMDA blockade dampens this hyperexcitability, reducing dyskinesia without worsening parkinsonism
- **Secondary mechanisms:** (1) Weak dopamine reuptake inhibition — increases synaptic DA availability, which may contribute to ON-time extension and anti-OFF effects. (2) Stimulates dopamine release from presynaptic terminals. (3) Weak anticholinergic activity. (4) Anti-inflammatory — reduces microglial activation and increases GDNF expression in astrocytes (preclinical)
- **MOA debate for LID:** The NMDA hypothesis is best supported — dyskinesia is a glutamatergic excess problem, and other NMDA antagonists (e.g., memantine, dextromethorphan) also show anti-dyskinetic effects. The dopaminergic effects are pharmacologically relevant at higher concentrations and likely more important for the OFF-episode indication than for LID
- **Formulation innovation:** The DR/ER capsule contains coated pellets with an initial lag phase followed by slow release. Bedtime administration achieves Tmax ~12 hours post-dose (range 6-20h), aligning peak drug levels with morning wakefulness when dyskinesia peaks. Steady state reached in ~4 days; accumulation ratio 1.2-1.3x
- Key limitation: hallucinations are the most common serious AE (>15% incidence), driven by amantadine's dopaminergic and possibly anticholinergic effects — limits use in patients with PD psychosis

### Clinical

**EASED (Phase 2/3 dose-finding)** | NCT01397422 | N=83 | PD patients with troublesome LID
- **Primary endpoint:** UDysRS change from baseline → significant for 340mg dose
- **Key secondary:** ON time without troublesome dyskinesia increased by 2.7-3.3 hours vs. placebo across dose groups (260, 340, 420mg)
- **Status:** Completed
- **Interpretation:** Established 274mg (340mg amantadine HCl) as the optimal dose. All three doses showed anti-dyskinetic effects; middle dose had best risk-benefit profile

**EASE LID (Phase 3)** | NCT02136914 | N=126 | PD with >=1h/day troublesome dyskinesia, on levodopa
- **Primary endpoint:** UDysRS total score change at week 12 → LS mean -15.9 (ADS-5102) vs. -8.0 (placebo); treatment difference -7.9 [95% CI -12.5 to -3.3], **p<0.001**
- **Key secondary:** ON time without troublesome dyskinesia increased; OFF time decreased. Effects sustained through 25 weeks
- **Status:** Completed (May 2014 - July 2015)
- **Interpretation:** Clean win on primary. Formed one of two pivotal trials for FDA approval

**EASE LID 3 (Phase 3)** | NCT02274766 | N=75 | PD with troublesome LID, on levodopa
- **Primary endpoint:** UDysRS total score change at week 12 → LS mean -20.7 (ADS-5102) vs. -6.3 (placebo); treatment difference -14.4 [95% CI -20.4 to -8.3], **p<0.0001**
- **Key secondary:** Consistent with EASE LID — increased ON time without troublesome dyskinesia, reduced OFF time
- **Status:** Completed
- **Interpretation:** Even larger effect size than EASE LID. Pooled analysis of both Phase 3 trials showed -10.1 point UDysRS difference (p<0.0001)

**EASE LID 2 (Open-label extension)** | N=223 | Long-term safety/durability
- **Primary endpoint:** Safety and tolerability over 2 years
- **Key secondary:** Durable reduction in dyskinesia and OFF time maintained over the study period
- **Status:** Completed
- **Interpretation:** Confirmed long-term efficacy is stable — no tolerance development, which had been a concern with immediate-release amantadine

**OFF-episode study** | Post-approval | PD patients on levodopa with OFF episodes
- **Primary endpoint:** Reduction in OFF time → statistically significant reduction
- **Status:** Completed; FDA approved OFF episode indication (2021)
- **Interpretation:** Broadened label beyond LID to OFF episodes, expanding addressable patient population

### Financial
- **FY2024 net sales:** $130.8M (up 9% YoY from FY2023) [source](https://ir.supernus.com/news-releases/news-release-details/supernus-announces-fourth-quarter-and-full-year-2024-financial)
- **Q3 2025 net sales:** $40.8M (up 15% YoY); H1 2025 trending ~16% growth
- **Annualized run-rate (mid-2025):** ~$145-150M
- **Acquisition economics:** Supernus paid ~$400M for Adamas in 2021. At the time, Gocovri was generating roughly $90-100M/year. At current trajectory, Supernus will have recouped the acquisition price in cumulative Gocovri revenue within ~3-4 years post-close — a clean return
- **CVR status:** First CVR ($0.50/share at $150M trailing-four-quarter sales) appears to have been missed given FY2024 of $130.8M. Second CVR ($0.50/share at $225M) almost certainly not achievable by end-2025
- **Generic risk:** Settlement with Sandoz permits generic entry March 4, 2030. 31 ANDA filers on record. Patent portfolio extends to 2038 but settlement terms govern. Expect meaningful erosion post-2030
- **Supernus total revenue context:** Gocovri is one of four key commercial products (alongside Qelbree/ADHD, Oxtellar XR/Trokendi XR/epilepsy, and APOKYN+ONAPGO/PD). ONAPGO (apomorphine infusion pump) launched April 2025 — another PD product growing rapidly (>750 enrollment forms in first quarter)

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

- **[[mesdopetam]]** (IRLAB Therapeutics) is the primary competitive threat — a selective D3 receptor antagonist entering Phase 3 for LID. Different MOA (dopaminergic D3 antagonism vs. glutamatergic NMDA blockade). Phase 2b showed dose-dependent UDysRS improvement and an anti-OFF signal, but missed primary endpoint (good ON-time). Phase 3 aligned with both FDA and EMA using UDysRS primary endpoint. If approved, would be the first new-MOA LID drug since Gocovri
- **Immediate-release amantadine (generic Symmetrel):** Much cheaper, widely used off-label. Gocovri's advantage is optimized PK (bedtime dosing, morning peak), proven efficacy in controlled trials, and convenience. Many neurologists still prescribe generic IR amantadine TID instead of Gocovri — a commercial headwind
- **OS320 (Osmotica/Amneal):** Immediate-release/extended-release amantadine combination (ALLAY-LID studies). Another reformulation play; not yet approved
- **Deep brain stimulation (DBS):** Surgical alternative for refractory LID. Non-drug competitor for severe cases
- Gocovri's position is defensible until 2030 (generic entry date) but faces erosion from both generic amantadine ER and potentially [[mesdopetam]] if the latter reaches market

## Analysis

Gocovri represents a successful pharmaceutical reformulation strategy — taking an old, well-understood molecule (amantadine, ~60 years old) and optimizing its delivery profile for a specific clinical problem (morning-predominant dyskinesia). The science is straightforward: LID is driven by glutamatergic overactivity in the striatum, NMDA blockade dampens it, and the ER formulation ensures drug levels peak when patients need relief most. Two clean Phase 3 wins, durable OLE data, and a manageable (if notable) side-effect profile earned a legitimate FDA approval in a space with zero prior approved treatments.

Commercially, Gocovri is a modest franchise — $131M in 2024, growing mid-teens — not a blockbuster, but a profitable niche product. The addressable population (25-40% of levodopa-treated PD patients develop LID, ~1.4-2.3M globally in major markets) is large enough to support multiple therapies, which is why [[mesdopetam]]'s Phase 3 program matters. If [[mesdopetam]] succeeds, it would not necessarily displace Gocovri but could split the market — physicians may prefer D3 antagonism in patients with hallucination risk (where amantadine is contraindicated) and stick with Gocovri for others.

**Analytical estimate — Gocovri cumulative lifetime revenue through patent expiration: $1.2-1.5B.** This is our assessment, not from a published source. The reasoning: $131M in FY2024, growing ~15% annually through ~2027 (reaching $175-200M peak), then plateauing as [[mesdopetam]] or competitors enter, followed by sharp decline post-March 2030 generic entry. Total commercial life from 2018 launch to ~2032 effective genericization = ~14 years of meaningful revenue.

The Adamas acquisition at ~$400M looks like a fair-to-good deal for Supernus in retrospect. They acquired a growing, sole-FDA-approved product in a defined niche, with 8+ years of remaining patent protection. The CVR miss (sales not reaching $150M/$225M thresholds) suggests Adamas shareholders had an overly optimistic sales trajectory, but the base deal price was reasonable for the actual revenue trajectory. Supernus's broader PD strategy — combining Gocovri (dyskinesia), APOKYN (rescue injection for OFF), and ONAPGO (continuous apomorphine infusion) — creates a multi-product PD franchise that few other mid-cap biotechs can match.

## References

### Clinical Trials
- [EASED Phase 2/3](https://clinicaltrials.gov/ct2/show/NCT01397422) — NCT01397422
- [EASE LID Phase 3](https://clinicaltrials.gov/ct2/show/NCT02136914) — NCT02136914
- [EASE LID 3 Phase 3](https://clinicaltrials.gov/ct2/show/NCT02274766) — NCT02274766

### Key Publications
- [ADS-5102 for LID in PD (EASE LID) | JAMA Neurology (2017)](https://jamanetwork.com/journals/jamaneurology/fullarticle/2630682)
- [EASE LID 3 results | Movement Disorders (2017)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.27131)
- [Pooled Phase 3 analyses | CNS Drugs (2018)](https://pubmed.ncbi.nlm.nih.gov/29532440/)
- [EASE LID 2: 2-year OLE | J Parkinsons Dis (2020)](https://pubmed.ncbi.nlm.nih.gov/31929122/)
- [Amantadine DR/ER reduces OFF time | npj Parkinson's Disease (2022)](https://www.nature.com/articles/s41531-022-00291-1)
- [Amantadine ER review in LID | Drugs (2018)](https://pubmed.ncbi.nlm.nih.gov/30088203/)
- [Amantadine in PD and movement disorders | Lancet Neurology (2021)](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(21)00249-0/abstract)
- [Amantadine NMDA receptor mechanism | J Neurosci (2005)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6724906/)
- [Amantadine dual neuroprotective action | PMC (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3130082/)

### Press Releases & Filings
- [Adamas Gocovri FDA approval (August 2017)](https://www.genengnews.com/topics/drug-discovery/adamas-gocovri-wins-fda-nod-as-first-pd-treatment-for-levodopa-induced-dyskinesia/)
- [Supernus to acquire Adamas (October 2021)](https://ir.supernus.com/news-releases/news-release-details/supernus-pharmaceuticals-acquire-adamas-pharmaceuticals)
- [Supernus completes Adamas acquisition (November 2021)](https://ir.supernus.com/news-releases/news-release-details/supernus-pharmaceuticals-completes-acquisition-adamas)
- [Adamas settles patent litigation with Sandoz (January 2020)](https://www.globenewswire.com/news-release/2020/01/02/1965715/30654/en/Adamas-Announces-Settlement-of-Patent-Litigation-with-Sandoz-Inc.html)
- [Supernus FY2024 financial results (February 2025)](https://ir.supernus.com/news-releases/news-release-details/supernus-announces-fourth-quarter-and-full-year-2024-financial)
- [Supernus Q3 2025 financial results (November 2025)](https://www.globenewswire.com/news-release/2025/11/04/3180807/19871/en/Supernus-Announces-Third-Quarter-2025-Financial-Results.html)

### Regulatory & Market
- [Gocovri FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/208944s009lbl.pdf)
- [Gocovri patent information | DrugPatentWatch](https://www.drugpatentwatch.com/p/tradename/GOCOVRI)
- [Generic Gocovri availability | Drugs.com](https://www.drugs.com/availability/generic-gocovri.html)
- [Gocovri HCP site](https://www.gocovrihcp.com/)
