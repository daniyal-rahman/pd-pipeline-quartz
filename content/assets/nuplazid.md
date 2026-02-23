---
drug_name: "Nuplazid (pimavanserin)"
aliases: ["pimavanserin", "ACP-103", "ACP-103-020"]
target: "5-HT2A serotonin receptor"
mechanism: "Selective 5-HT2A inverse agonist/antagonist that reduces psychotic symptoms without dopamine D2 blockade, preserving motor function in PD patients"
modality: "small molecule"
developer: "Acadia Pharmaceuticals"
company_type: "biotech"
publicly_traded: true
ticker: "ACAD"
stage: "Approved"
status: "Active"
patient_population: "PD patients with hallucinations and delusions (PD psychosis)"
route_of_administration: "oral"
key_biomarkers: ["SAPS-PD (efficacy)", "QTc interval (safety)"]
next_catalyst: "Pimavanserin patent expiry Q1 2030; remlifanserin (ACP-204) Phase 2 RADIANT readout Aug-Oct 2026"
catalyst_date: "2026 (RADIANT) / 2030 (generics)"
thesis_cluster: "symptomatic"
tags: [pd-pipeline]
date: 2026-02-20
company_link: "[[companies/acadia-pharmaceuticals]]"
---

# Nuplazid (Pimavanserin)

## Summary

The only FDA-approved treatment for Parkinson's disease psychosis (PDP), approved April 2016. Acadia Pharmaceuticals (biotech, ACAD) has grown Nuplazid into a $609M/year franchise (FY2024) with 2025 guidance of $685-695M, on a trajectory toward ~$1B by 2028. The drug works by selectively blocking 5-HT2A receptors without touching dopamine D2 — the critical differentiator in PD where D2 blockade worsens motor symptoms. Acadia attempted label expansion into dementia-related psychosis (DRP) via the HARMONY trial but received two FDA Complete Response Letters (2021, 2022), limiting the drug to the PDP indication. The key competitive dynamics: quetiapine dominates off-label despite weak evidence; clozapine is effective but requires mandatory blood monitoring; [[ly03017|LY03017]] (Luye) and remlifanserin (Acadia's own next-gen 5-HT2A) are the pipeline threats. Patent expiry ~Q1 2030 creates a generics cliff, making the 2026-2029 window critical for Acadia to either expand the franchise or transition revenue to remlifanserin and DAYBUE.

## Notes

### Science
- Selective inverse agonist/antagonist at 5-HT2A receptors (Ki = 0.087 nM) with 40-fold weaker activity at 5-HT2C (Ki = 0.44 nM) and no clinically meaningful affinity for dopamine D2, histamine H1, muscarinic, or adrenergic receptors
- Mechanism: 5-HT2A receptors on cortical pyramidal neurons modulate glutamatergic and dopaminergic signaling in the ventral tegmental area; inverse agonism reduces aberrant serotonin-driven cortical excitation that underlies visual hallucinations and delusions in PDP
- The absence of D2 blockade is the key pharmacological advantage — conventional and most atypical antipsychotics (risperidone, olanzapine, haloperidol) are contraindicated in PDP because D2 antagonism worsens parkinsonism
- Dosing: 34 mg once daily (two 17 mg tablets, or single 34 mg capsule). No titration required. Long half-life: pimavanserin ~57 hours, active N-desmethyl metabolite ~200 hours
- Black box warning: increased mortality in elderly patients with dementia-related psychosis (class-wide antipsychotic warning). QTc prolongation (~5-8 ms at therapeutic doses) — avoid with strong CYP3A4 inhibitors and in patients with QT-prolonging medications
- CYP3A4 is the primary metabolic pathway; dose reduction to 17 mg required with strong CYP3A4 inhibitors; contraindicated with strong CYP3A4 inducers
- [[ly03017|LY03017]] (Luye Pharma) adds 5-HT2C antagonism to the 5-HT2A mechanism, theoretically improving prefrontal dopamine tone and addressing cognitive symptoms that pimavanserin does not — but this dual mechanism is unproven in humans

### Clinical

**ACP-103-006 (Phase 2)** | NCT TBD | N=60 | PD psychosis
- **Primary endpoint:** Safety/efficacy signal → Demonstrated antipsychotic effects without impairing motor function
- **Status:** Completed (2006)
- **Interpretation:** First proof-of-concept for selective 5-HT2A inverse agonism in PDP

**ACP-103-012 (Phase 3)** | NCT00477672 | N=298 | PD psychosis
- **Primary endpoint:** SAPS H+D 20-item score → Failed to reach significance due to unexpectedly large placebo response (42%)
- **Design:** 1:1:1 randomization (placebo vs. 10 mg vs. 40 mg pimavanserin, 6 weeks)
- **Key finding:** 40 mg arm showed clear efficacy signals but could not separate from placebo statistically; 10 mg showed no separation
- **Status:** Completed
- **Interpretation:** Placebo response problem, not drug problem. Led to trial design refinements for the pivotal study

**ACP-103-014 (Phase 3)** | NCT00658567 | N=~300 | PD psychosis
- **Primary endpoint:** Failed to show efficacy
- **Status:** Completed (unpublished; data available via FDA)
- **Interpretation:** Second Phase 3 failure. Combined with -012, Acadia identified trial design variables (placebo lead-in, endpoint specificity) correlating with effect size

**ACP-103-020 (Pivotal Phase 3)** | NCT01174004 | N=199 | PD psychosis (hallucinations + delusions, ≥40 years, ≥1 month stable PD meds)
- **Primary endpoint:** SAPS-PD (9-item PD-adapted scale) → **Statistically significant improvement, p=0.0014, effect size d=0.50**
- **Design:** 6-week, double-blind, placebo-controlled with 2-week non-pharmacological lead-in phase to reduce placebo response
- **Key secondary:** CGI-S, CGI-I, caregiver burden, nighttime sleep, daytime wakefulness — all significantly improved
- **Safety:** Most common AEs: peripheral edema (7% vs. 3% placebo), confusional state (6% vs. 3%)
- **Status:** Completed → Basis for FDA approval April 29, 2016
- **Interpretation:** Third time was the charm. The 2-week placebo lead-in and PD-specific SAPS subscale solved the placebo response problem that sank -012 and -014. Effect size of 0.50 is moderate but clinically meaningful in a population with no approved alternatives

**HARMONY (Phase 3 — DRP label expansion)** | NCT03325556 | N=392 | Dementia-related psychosis (AD, DLB, PDD, vascular, frontotemporal)
- **Primary endpoint:** Time to relapse of psychosis → **HR=0.35, p=0.005** (2.8-fold reduction in relapse risk). Stopped early at pre-planned interim for positive efficacy
- **Design:** Open-label pimavanserin 12 weeks → responders (≥30% SAPS reduction + CGI-I much/very much improved at weeks 8 and 12) randomized 1:1 to pimavanserin or placebo for up to 26 weeks
- **Status:** Completed — but FDA issued two CRLs (April 2021, October 2022)
- **FDA rationale for rejection:** Efficacy appeared driven primarily by the PD-dementia subgroup (already subsumed by PDP indication). Supportive Phase 2 Study-019 had limited interpretability. FDA recommended an additional trial in AD psychosis specifically
- **Interpretation:** Devastating commercial blow. The DRP indication would have expanded the addressable market 5-10x. Acadia's stock fell ~30% on the first CRL. The FDA's objection was specific and targeted: they wanted AD-specific data, not a pooled dementia bucket. Acadia pivoted to developing remlifanserin (ACP-204) specifically for Alzheimer's disease psychosis

### Financial
- **Revenue trajectory (Nuplazid net product sales):**
  - 2017: $125M | 2018: $224M | 2019: $339M | 2020: $442M
  - 2021: $484M | 2022: $517M | 2023: $549M | 2024: $609M
  - 2025 guidance: $685-695M | 2028 target: ~$1B
- **Growth drivers:** Steady volume growth (~5-9% annually) plus modest price increases; new prescriptions accelerating as of Q3 2025
- **Patent expiry:** ~Q1 2030. Generics cliff is the primary financial risk
- **Acadia market cap:** ~$3.8B (Oct 2025); ~60% of enterprise value attributable to Nuplazid franchise
- **No licensing deal:** Nuplazid was developed entirely internally by Acadia. No partner, no milestones, no royalty split — 100% of economics accrue to Acadia
- **DAYBUE (trofinetide):** Acadia's second approved product (Rett syndrome, approved March 2023), projected ~$700M by 2028. Diversifies revenue away from Nuplazid dependence
- **Remlifanserin (ACP-204):** Next-generation 5-HT2A inverse agonist targeting AD psychosis and Lewy body dementia psychosis. Phase 2 RADIANT study readout expected Aug-Oct 2026. Acadia projects ~$4B of $11B total pipeline peak sales opportunity from remlifanserin alone

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[ly03017]] | Phase 1 | Active | Luye Pharma Group | small molecule |
| [[nuplazid]] | Approved | Active | Acadia Pharmaceuticals | small molecule |

- **Quetiapine (off-label):** The most widely prescribed treatment for PDP despite no RCT evidence of efficacy and significant AE burden (sedation, metabolic syndrome, motor worsening at higher doses). Practice inertia and cost (~$0.15/day generic vs. ~$30/day Nuplazid) explain its dominance. MDS guidelines rate quetiapine as only "possibly useful" vs. pimavanserin's "clinically useful"
- **Clozapine (off-label):** Efficacy equivalent or superior to pimavanserin in head-to-head analyses, and the only other agent rated "clinically useful" by MDS. However, mandatory REMS blood monitoring for agranulocytosis severely limits uptake — <2% of PDP patients receive clozapine
- [[ly03017|LY03017]] (Luye Pharma) is the most direct pipeline threat: dual 5-HT2A/5-HT2C mechanism, claims superior cardiac safety, but Phase 1 only and years from market. Luye's commercial strategy likely China-first where pimavanserin is not approved
- [[mesdopetam]] (Ipsen/Cerevel) — D3 antagonist for levodopa-induced dyskinesia, but PDP line extension potential noted in its profile
- **Remlifanserin (ACP-204)** — Acadia's own next-generation 5-HT2A, designed to replace Nuplazid with improved selectivity. Phase 2 RADIANT in AD psychosis (Aug-Oct 2026 readout). If successful, Acadia transitions from Nuplazid to remlifanserin before generics hit; if it fails, the 2030 patent cliff becomes existential
- No other selective 5-HT2A agents in late-stage development for PDP — eplivanserin, pruvanserin, and volinanserin all discontinued. The field's high attrition rate underscores pimavanserin's achievement in reaching market

## Analysis

Nuplazid occupies a rare position: the only approved drug for a well-defined neuropsychiatric indication that affects ~60% of PD patients. Despite this monopoly, real-world penetration remains modest — quetiapine's off-label dominance persists due to cost, familiarity, and the black box warning on pimavanserin that makes prescribers hesitant. The $609M in 2024 sales against an addressable population of ~500,000+ US PDP patients implies significant room for growth even within the current label, but the trajectory is steady rather than explosive.

The HARMONY rejection was the pivotal strategic inflection. Had FDA approved the DRP indication, Nuplazid would have become a multi-billion-dollar franchise targeting ~3M patients with dementia-related psychosis in the US alone. The FDA's specific objection — that HARMONY's efficacy was driven by PD-dementia (already covered) rather than AD psychosis — forced Acadia to develop remlifanserin as a cleaner next-generation molecule designed specifically for the AD psychosis regulatory pathway. This pivot is strategically sound but introduces execution risk: Acadia is now racing to prove remlifanserin before Nuplazid's 2030 patent cliff.

**Analytical estimate — Nuplazid cumulative revenue 2025-2029 (pre-generics): $3.5-4.0B.** This is our assessment, not from a published source. The reasoning: 2025 guidance is $690M; assuming 8-10% annual growth from volume + price → ~$750M (2026), ~$810M (2027), ~$880M (2028), ~$950M (2029). This may be conservative given Acadia's $1B 2028 target, but growth deceleration near patent expiry is typical. Post-2030, generics will erode revenue 70-80% within 2-3 years based on specialty oral precedents.

**Signal analysis:** Acadia's behavior reveals their strategic calculus clearly. The R&D Day in 2025 showcasing nine pipeline programs and $11B peak sales opportunity is a deliberate narrative shift from "Nuplazid company" to "CNS platform company." The remlifanserin timeline (RADIANT readout Aug-Oct 2026) is calibrated to allow a Phase 3 start in 2027, NDA filing ~2029, and approval ~2030 — just as Nuplazid generics arrive. This is a textbook lifecycle management play. If RADIANT succeeds, Acadia has a clean transition path and the stock re-rates on a multi-product thesis. If RADIANT fails, Acadia faces a 2030 revenue cliff with only DAYBUE ($700M projected) as a backstop — the company becomes a ~$5-6B revenue business declining to ~$2-3B, which likely triggers M&A interest from mid-cap pharma.

## References

### Clinical Trials
- [ACP-103-020 Pivotal Phase 3](https://clinicaltrials.gov/ct2/show/NCT01174004) — NCT01174004
- [ACP-103-012 Phase 3](https://clinicaltrials.gov/ct2/show/NCT00477672) — NCT00477672
- [ACP-103-014 Phase 3](https://clinicaltrials.gov/ct2/show/NCT00658567) — NCT00658567
- [HARMONY Phase 3 (DRP)](https://clinicaltrials.gov/ct2/show/NCT03325556) — NCT03325556

### Key Publications
- [Pimavanserin for patients with PD psychosis: Phase 3 trial | The Lancet (2014)](https://www.thelancet.com/article/S0140-6736(13)62106-6/abstract)
- [Trial of Pimavanserin in Dementia-Related Psychosis | NEJM (2021)](https://www.nejm.org/doi/full/10.1056/NEJMoa2034634)
- [Pimavanserin: A Novel Drug Approved to Treat PDP | PMC (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5819716/)
- [On the Discovery and Development of Pimavanserin | PMC (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4172996/)
- [Pimavanserin and Clozapine Outperform Other Atypical Antipsychotics in PDP | NeurologyLive (2024)](https://www.neurologylive.com/view/pimavanserin-clozapine-outperform-other-atypical-antipsychotics-in-treating-parkinson-disease-psychosis)
- [Management of PD psychosis: first-line antipsychotic selection | Expert Opinion (2025)](https://www.tandfonline.com/doi/full/10.1080/14656566.2025.2481205)
- [PD Psychosis Treatment: Review | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11505035/)
- [Pimavanserin StatPearls | NCBI](https://www.ncbi.nlm.nih.gov/books/NBK557712/)

### Press Releases & Filings
- [FDA Approves NUPLAZID (April 2016)](https://acadia.com/en-us/media/news-releases/fda-approves-acadia-pharmaceuticals-nuplazidtm-pimavanserin)
- [Acadia Receives CRL for DRP sNDA (April 2021)](https://acadia.com/en-us/media/news-releases/acadia-pharmaceuticals-receives-complete-response-letter-us-0)
- [FDA Issues Second CRL for Pimavanserin AD Psychosis (2022)](https://www.neurologylive.com/view/fda-issues-second-crl-pimavanserin-treatment-alzheimer-disease-psychosis)
- [Acadia FY2024 Financial Results](https://acadia.com/en-us/media/news-releases/acadia-pharmaceuticals-reports-fourth-quarter-and-full-year-2024)
- [Acadia R&D Day Pipeline Showcase (2025)](https://ir.acadia.com/news-releases/news-release-details/acadia-pharmaceuticals-hosts-inaugural-rd-day-showcasing)
- [Acadia JPM 2026 Business Update](https://acadia.com/en-us/media/news-releases/acadia-pharmaceuticals-provides-business-and-pipeline-updates-at-44th-annual-j-p--morgan-healthcare-conference)

### Regulatory & Market
- [Nuplazid Prescribing Information (FDA Label)](https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/207318lbl.pdf)
- [FDA Medical Review — NDA 207318](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/207318Orig1s000MedR.pdf)
- [Nuplazid Profile | Alzforum](https://www.alzforum.org/therapeutics/nuplazid)
