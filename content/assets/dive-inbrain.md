---
drug_name: "A-dopamine (anaerobic dopamine)"
aliases: ["DIVE-I", "ICV A-dopamine", "intracerebroventricular dopamine"]
target: "dopamine replacement (direct CNS delivery)"
mechanism: "Continuous intracerebroventricular infusion of anaerobic dopamine via implanted pump and catheter into the third ventricle, bypassing the blood-brain barrier and peripheral metabolism to restore striatal dopamine levels"
modality: "device-aided therapy (drug/device combination)"
developer: "InBrain Pharma"
company_type: "startup"
publicly_traded: false
partner: "Tricumed / Flowonix (pump manufacturers)"
partner_type: ""
stage: "Phase 1/2"
status: "Active"
patient_population: "Advanced PD with L-dopa-related motor complications (freezing, dyskinesia)"
route_of_administration: "intracerebroventricular (via implanted abdominal pump + subcutaneous catheter to third ventricle)"
key_biomarkers: ["wrist-worn actimetry (motor state monitoring)", "ON time without dyskinesia", "L-dopa equivalent daily dose"]
confidence_rating: "5/10"
next_catalyst: "DEEP-DIVE Phase 3 initiation"
catalyst_date: "2026-2027"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/inbrain-pharma]]"
partner_link: "[[companies/tricumed-flowonix]]"
---

# A-dopamine (DIVE-I / InBrain Pharma)

## Summary

InBrain Pharma (startup, Lille, France) completed the Phase 1/2 DIVE-I trial demonstrating that continuous intracerebroventricular infusion of anaerobic dopamine (A-dopamine) is safe and significantly reduces L-dopa-related motor complications in advanced PD, with results published in Nature Medicine (January 2025). The Phase 2 crossover showed a 4.4-hour gain in ON time without dyskinesia and a 60% reduction in oral L-dopa dose (p=0.027 on primary endpoint), with all nine Phase 2 completers continuing into long-term follow-up now extending to 4.5 years. In July 2025, the EMA issued a positive opinion supporting advancement to a single pivotal Phase 3 trial (DEEP-DIVE), a 170-patient, randomized, double-blind, placebo-controlled study planned across Europe and the US. If DEEP-DIVE succeeds, A-dopamine would represent a paradigm shift in advanced PD management — direct brain dopamine replacement rather than prodrug conversion or electrical neuromodulation — with projected approvals in 2031-2032. If it fails, the invasive surgical requirement (pump implantation + ventricular catheter) will have been a significant burden on a small patient cohort for no benefit, and the field remains anchored to DBS, [[nd0612|subcutaneous levodopa infusion]], and intestinal gel pumps.

## Notes

### Science
- Addresses a 60-year-old challenge: dopamine itself cannot be given orally (rapid peripheral metabolism, oxidative instability) or IV (does not cross the blood-brain barrier). A-dopamine solves oxidative degradation by preparing dopamine under anaerobic conditions (replacing oxygen with CO2/nitrogen), creating a stable formulation for direct CNS delivery
- A telemetry-controlled intra-abdominal pump (Tricumed Siromedes or Flowonix Prometra) is surgically implanted and connected via a subcutaneous catheter tunneled through the right frontal horn into the third ventricle, near the striatum — the primary site of dopaminergic denervation in PD
- Key distinction vs. oral L-dopa: bypasses the need for aromatic L-amino acid decarboxylase (AADC) conversion, which is progressively lost as dopaminergic neurons degenerate — this means efficacy should be maintained even in late-stage disease when L-dopa response narrows
- Key distinction vs. DBS: pharmacological neuromodulation rather than electrical; targets the neurochemical deficit directly rather than modulating downstream circuit activity. DBS improves symptoms but does not address the dopamine deficit itself
- Key distinction vs. Duodopa/LCIG: delivers dopamine directly to the brain rather than to the intestine; avoids gastrointestinal complications (stoma site infections, tube dislodgement) that plague intestinal gel infusion
- Open questions: long-term ventricular catheter safety (infection, displacement, CSF dynamics), whether continuous ICV dopamine causes receptor desensitization over years, and whether this approach is scalable to the broader advanced PD population beyond the ~10-15% who are refractory to current device-aided therapies
- Founded on research by Professors David Devos and Caroline Moreau at the University of Lille (INSERM UMR-S 1172), licensed exclusively from SATT Nord

### Clinical

**DIVE-I Phase 1 (open-label safety)** | NCT04332276 | N=12 | Advanced PD with L-dopa motor complications
- **Primary endpoint:** Safety/tolerability of ICV A-dopamine → No serious adverse events attributed to A-dopamine
- **Key findings:** Dose-dependent motor improvement; transient side effects similar to oral L-dopa profile; no dyskinesia observed even at high doses
- **Status:** Completed
- **Interpretation:** Established that graphene — rather, that anaerobic dopamine delivered intracerebroventricularly is safe and tolerable, clearing the path for efficacy assessment

**DIVE-I Phase 2 (randomized, controlled, open-label, crossover)** | NCT04332276 | N=9 (of the 12 Phase 1 patients) | Advanced PD with motor complications
- **Primary endpoint:** Percentage of 24-hour periods with inadequate motor symptom control (dyskinesia or bradykinesia), measured by wrist-worn actimetry → **Median within-patient reduction of 10.4% (p=0.027)**
- **Key secondary:** Average gain of **4.4 hours of ON time without dyskinesia per day**; **6.6 hours of functional autonomy per 24-hour period**; **60% reduction in daily L-dopa equivalent dose**
- **Design:** 1 month of A-dopamine vs. 1 month of optimized oral antiparkinsonian therapy (crossover)
- **Status:** Completed; published in Nature Medicine (January 2025)
- **Interpretation:** Statistically significant primary endpoint in a small but well-designed crossover study. The magnitude of ON time gain (4.4 hours) is clinically meaningful and competitive with DBS and Duodopa. All 9 Phase 2 completers chose to continue treatment — a strong qualitative signal.

**DIVE-I Long-Term Follow-Up (open-label extension)** | NCT04332276 | N=9 | Continuing from Phase 2
- **Key findings:** Sustainable motor control effect at 4.5 years; excellent long-term safety profile; no serious device-related adverse events
- **Status:** Completed September 30, 2025; data presented at MDS 2025 (Honolulu, October 2025)
- **Interpretation:** 4.5-year durability data is remarkable for a device-aided therapy in this population. Sustained benefit without apparent tolerance development partially addresses the receptor desensitization concern.

**DEEP-DIVE (Phase 3, planned)** | NCT TBD | N=170 | Advanced PD with L-dopa motor complications
- **Design:** Randomized, double-blind, placebo-controlled (saline infusion), parallel-group, adaptive design; 24-week double-blind phase + 52-week open-label extension
- **Regulatory:** Positive EMA scientific advice (July 2025) validating single pivotal trial strategy for centralized European marketing authorization
- **Geography:** Europe and United States
- **Status:** Planned; clinical batches in production; trial initiation targeted 2026-2027
- **Interpretation:** EMA acceptance of a single pivotal trial is a meaningful de-risking event — reduces cost and timeline vs. requiring two Phase 3 studies. The adaptive design allows sample size re-estimation, adding flexibility.

### Financial
- **Total raised:** Approximately $6.6M (per PitchBook), though other sources report ~$3.1-3.2M — discrepancy likely reflects grant funding vs. equity rounds
- **Key investors:** France Parkinson (equity stake, amount undisclosed), Finovam Gestion, Nord France Amorçage, Fondation de l'Universite de Lille, Eurasante
- **Recent funding:** EUR 1.8M from France 2030's "First Factory" initiative (PERCEPAR project, May 2025) to industrialize anaerobic dopamine production
- **No pharma partner:** InBrain Pharma is actively seeking CRO and pharma partners to support the DEEP-DIVE Phase 3 trial in EU and US (per GlobalData reporting)
- **Funding gap:** The company's total raised to date is far below what a 170-patient, multi-center, transatlantic Phase 3 would cost (likely EUR 30-60M+). A significant partnership or Series A/B will be required before DEEP-DIVE can launch
- **Context:** France Parkinson (a patient advocacy nonprofit) taking an equity stake is unusual and signals the strength of patient community conviction, but the company remains very early-stage financially relative to its clinical ambitions

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[sana-program]] | Preclinical | Deprioritized | Sana Biotechnology | cell therapy (iPSC allogeneic) |
| [[alc01]] | Phase 1 | Active | iCamuno Biotherapeutics | cell therapy (iPSC allogeneic) |
| [[autologous-mdaps]] | Phase 1 | Active | McLean Hospital / Neuroregeneration Research Institute (NRI) | cell therapy (iPSC autologous) |
| [[cellino-ipsc]] | Phase 1 | Active | Cellino Biotech | platform |
| [[lu-af28996]] | Phase 1 | Active | Lundbeck | small molecule |
| [[rndp-001]] | Phase 1 | Active | Kenai Therapeutics | cell therapy (iPSC allogeneic) |
| [[ux-da001]] | Phase 1 | Active | UniXell Biotechnology | cell therapy (iPSC autologous) |
| [[ser-252]] | Phase 1b | Active | Serina Therapeutics | small molecule |
| [[anpd001]] | Phase 1/2 | Active | Aspen Neuroscience | cell therapy (iPSC autologous) |
| [[dive-inbrain]] | Phase 1/2 | Active | InBrain Pharma | device-aided therapy (drug/device combination) |
| [[kyoto-ipsc]] | Phase 1/2 | Active | CiRA (Kyoto University) / Sumitomo Pharma | cell therapy (iPSC allogeneic) |
| [[nouvneu001]] | Phase 1/2 | Active | iRegene Therapeutics | cell therapy (iPSC allogeneic) |
| [[sizhe-biopharma]] | Phase 1/2 | Active | XellSmart / Shize Bio (士泽生物) | cell therapy (iPSC allogeneic) |
| [[stem-pd]] | Phase 1/2 | Active | Lund University / University of Cambridge | cell therapy (ESC) |
| [[ted-a9]] | Phase 1/2 | Active | S.BIOMEDICS | cell therapy (ESC) |
| [[vgn-r09b]] | Phase 1/2 | Active | Shanghai Vitalgen BioPharma | AAV gene therapy |
| [[cbt-npc]] | Phase 2 | Active | CHA Biotech | cell therapy (ESC) |
| [[glovadalen]] | Phase 2 | Active | UCB | small molecule |
| [[bemdaneprocel]] | Phase 3 | Active | BlueRock Therapeutics | cell therapy (ESC) |
| [[mesdopetam]] | Phase 3 | Active | IRLAB Therapeutics | small molecule |
| [[p2b001]] | Phase 3 | Active | Pharma Two B | small molecule |
| [[raguneprocel]] | NDA Filed | Active | Sumitomo Pharma / RACTHERA | cell therapy (iPSC allogeneic) |
| [[tavapadon]] | NDA Filed | Active | Cerevel Therapeutics | small molecule |
| [[ipx203]] | Approved | Active | Amneal Pharmaceuticals | small molecule |

- The competitive set for A-dopamine is **device-aided therapies (DATs) for advanced PD**, not disease-modifying agents. Direct comparators: DBS (Medtronic, Abbott, Boston Scientific — all approved), Duodopa/LCIG (AbbVie — approved), subcutaneous apomorphine infusion (Britannia — approved), and [[nd0612|ND0612]] (NeuroDerm/Mitsubishi Tanabe — subcutaneous levodopa/carbidopa infusion)
- Key advantage over DBS: pharmacological mechanism directly addresses dopamine deficit rather than modulating circuits electrically. DBS can cause speech/gait side effects from stimulation of adjacent structures; A-dopamine avoids this
- Key advantage over Duodopa/LCIG: avoids GI tract entirely — no jejunal tube, no stoma complications, no tube displacement issues that limit Duodopa adherence
- Key disadvantage vs. all competitors: requires neurosurgical catheter placement into the third ventricle — more invasive than subcutaneous approaches like [[nd0612|ND0612]] or subcutaneous apomorphine
- [[nd0612|ND0612]] is the most direct competitive threat — also a continuous levodopa delivery system but administered subcutaneously (no surgery), albeit with lower CNS bioavailability. If ND0612 provides "good enough" motor control for most advanced PD patients, A-dopamine's addressable market narrows to the most refractory cases
- The 4.4-hour ON time gain is competitive with published DBS and Duodopa data, but head-to-head comparisons do not exist and trial populations differ significantly

## Analysis

A-dopamine represents a conceptually elegant solution to a well-defined problem: in advanced PD, the therapeutic window for oral L-dopa narrows as AADC-expressing neurons are lost, leading to unpredictable ON/OFF fluctuations and dose-limiting dyskinesia. By delivering dopamine itself directly to the ventricular system near the striatum, A-dopamine bypasses both the blood-brain barrier and the failing enzymatic conversion step. The DIVE-I Phase 1/2 data is genuinely impressive — the 4.4-hour ON time gain, 60% L-dopa dose reduction, and statistically significant primary endpoint (p=0.027) in a small but well-controlled crossover study represent strong clinical signals. The 4.5-year follow-up durability data, with all patients continuing, adds confidence.

**Analytical estimate — Phase 3 success probability: 35-45%.** This is our assessment, not from a published source. The reasoning:
- Base rate: device-aided therapies in advanced PD have relatively high Phase 3 success rates (~50-60%) because the patient population is well-defined and endpoints are clinically obvious
- Adjustments upward: strong Phase 1/2 efficacy signal with statistical significance (+10%), 4.5-year durability data (+5%), EMA acceptance of single pivotal trial design (+5%), well-understood pharmacology of dopamine itself (+5%)
- Adjustments downward: very small Phase 2 sample (N=9 evaluable, -10%), open-label crossover design in Phase 2 introduces bias (-5%), surgical invasiveness may limit enrollment/compliance in Phase 3 (-5%), underfunded company may not execute a 170-patient transatlantic trial without a major partner (-10%)
- Net: ~35-45%

The critical bottleneck is not science but funding. InBrain Pharma has raised roughly EUR 5-7M total — orders of magnitude below what a Phase 3 of this complexity requires. The EMA positive opinion is a valuable regulatory asset that should help attract a pharma partner or significant investment round, but the company's financial trajectory must change dramatically before DEEP-DIVE can launch. The absence of a pharma partner to date, despite a Nature Medicine publication and EMA validation, raises questions about whether the surgical invasiveness of the approach limits its commercial attractiveness to potential licensors.

If DEEP-DIVE succeeds, A-dopamine carves out a meaningful niche in the most refractory advanced PD patients — those failing DBS and/or intestinal gel infusion. The addressable population is small (perhaps 10-15% of advanced PD patients eligible for DATs), but the severity of unmet need in this group is extreme. If it fails, the surgical risk/benefit calculus for ICV dopamine delivery will be unfavorable, and the field will continue relying on iterative improvements to existing DATs like [[nd0612|ND0612]] and next-generation DBS systems. In either scenario, the pharmacological concept (direct dopamine replacement bypassing AADC) may find new life through less invasive delivery approaches — for example, AADC gene therapy ([[eladocagene]]) attempts to restore the conversion machinery rather than bypass it entirely.

## References

### Clinical Trials
- [DIVE-I Phase 1/2](https://clinicaltrials.gov/study/NCT04332276) — NCT04332276

### Key Publications
- [Intracerebroventricular anaerobic dopamine in Parkinson's disease with L-dopa-related complications: a phase 1/2 randomized-controlled trial | Nature Medicine (Jan 2025)](https://www.nature.com/articles/s41591-024-03428-2)

### Press Releases & Filings
- [InBrain Pharma Nature Medicine publication announcement (Jan 2025)](https://www.globenewswire.com/news-release/2025/01/27/3015736/0/en/With-significant-clinical-results-published-in-the-Nature-Medicine-Journal-InBrain-Pharma-is-about-to-durably-modify-the-advanced-Parkinson-s-disease-management.html)
- [InBrain Pharma DIVE-I positive results at MDS 2024 (Sep 2024)](https://www.globenewswire.com/news-release/2024/09/25/2952974/0/en/InBrain-Pharma-to-Present-Positive-Results-from-Its-DIVE-I-Phase-I-II-Clinical-Trial-for-Parkinson-s-Disease-at-the-Congress-of-Parkinson-s-Disease-and-Movement-Disorders-from-Sept.html)
- [InBrain Pharma long-term DIVE-I data at MDS 2025](https://www.biospace.com/press-releases/inbrain-pharma-to-present-long-term-follow-up-clinical-data-from-its-phase-i-ii-dive-i-trial-in-parkinsons-disease-at-the-mds-2025-conference)
- [InBrain Pharma PERCEPAR funding EUR 1.8M (May 2025)](https://www.globenewswire.com/news-release/2025/05/12/3079151/0/en/InBrain-Pharma-Secures-1-8-Million-in-Funding-for-the-PERCEPAR-Project-under-France-2030-s-First-Factory-Initiative-to-Industrialize-Anaerobic-Dopamine-Production-for-Parkinson-s-D.html)
- [France Parkinson equity stake in InBrain Pharma](https://www.inbrainpharma.com/blog/france-parkinson-takes-a-stake-in-inbrain-pharma-a-company-developing)
- [InBrain Pharma Phase III EMA positive opinion](https://manufacturingchemist.com/inbrain-pharma-phase-iii-ema-positive-opinion)

### Regulatory & Market
- [EMA positive scientific advice for DEEP-DIVE Phase 3 (Jul 2025)](https://manufacturingchemist.com/inbrain-pharma-phase-iii-ema-positive-opinion)
- [FDA Breakthrough Device Designation context — InBrain Neuroelectronics (separate company, graphene BCI)](https://parkinsonsnewstoday.com/news/inbrain-fda-breakthrough-device-status-parkinsons/) — Note: this is a different company (InBrain Neuroelectronics, Barcelona) from InBrain Pharma (Lille); they are unrelated despite similar names
