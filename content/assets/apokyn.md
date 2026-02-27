---
drug_name: "APOKYN"
aliases: ["apomorphine hydrochloride injection", "apomorphine SC injection", "APO-go"]
target: "dopamine receptors (D1-D5, non-selective full agonist)"
mechanism: "Subcutaneous apomorphine; potent non-ergot dopamine agonist with rapid onset (~10 min) for acute rescue of unpredictable PD OFF episodes when oral therapy is too slow or unreliable"
modality: "small molecule"
developer: "Supernus Pharmaceuticals"
company_type: "biotech"
publicly_traded: true
ticker: "SUPN"
stage: "Approved"
status: "Active"
patient_population: "Advanced PD patients with unpredictable OFF episodes inadequately controlled by oral rescue medications"
route_of_administration: "subcutaneous (injection)"
key_biomarkers: ["onset of ON response (target ≤10 min)", "OFF episode duration", "UPDRS motor score during OFF"]
next_catalyst: "ONAPGO (continuous SC apomorphine pump) ramp displacing episodic use"
catalyst_date: "2025-2027"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-26
company_link: "[[companies/supernus-pharmaceuticals]]"
---

# APOKYN (Apomorphine SC Injection)

## Summary

APOKYN is subcutaneous apomorphine for acute rescue of advanced PD OFF episodes, FDA-approved April 2004, generating $73.9M in FY2024 revenue for Supernus Pharmaceuticals (biotech, SUPN) [source](https://ir.supernus.com/news-releases/news-release-details/supernus-announces-fourth-quarter-and-full-year-2024-financial). It is the fastest-acting approved PD rescue therapy (~10 min to full ON), but the manual injection requirement and mandatory antiemetic co-administration (trimethobenzamide) create adherence friction. Supernus acquired APOKYN from US WorldMeds in 2020. The strategic successor is **ONAPGO** — a wearable continuous SC apomorphine infusion pump, FDA-approved Q1 2025, launched April 2025 — which converts episodic injection patients to a 24-hour automated infusion paradigm, mirroring AbbVie's [[duopa|Duopa]]-to-[[vyalev|VYALEV]] transition. APOKYN revenue will decline as ONAPGO ramps, but the episodic-rescue subpopulation (infrequent OFF episodes, preference for on-demand dosing) is not fully substituted by continuous infusion.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Supernus Pharmaceuticals (acquirer) |
| Deal Date | 2020 |
| Upfront | Not publicly disclosed |
| Total (Biobucks) | Not publicly disclosed |
| Deal Type | Acquisition (from US WorldMeds) |

## Notes

### Science
- **Mechanism:** Non-ergot dopamine agonist with nanomolar affinity for D1-D5 receptors. Full agonist; robust ON response within 4-12 minutes of SC injection. Half-life ~40 min; duration of effect 45-90 min. Short duration is by design — rescue use requires a predictable on/off kinetic profile
- **Non-ergot advantage:** Avoids the cardiac valvular fibrosis risk of ergot-derived DA agonists (bromocriptine, pergolide, cabergoline), which were withdrawn from market
- **Why SC is required:** Oral apomorphine bioavailability is ~0% due to extensive first-pass metabolism by the gut and liver. All viable apomorphine routes must bypass gut first-pass (SC injection, SC infusion, sublingual)
- **Antiemetic requirement:** Apomorphine stimulates the area postrema (outside BBB) via dopamine receptors, causing nausea/vomiting. Trimethobenzamide 300 mg TID is required starting 3 days pre-initiation; ondansetron is contraindicated (risk of profound hypotension; QT combination)
- **Key distinction vs. levodopa formulations:** Apomorphine bypasses the levodopa-to-dopamine conversion step (no AADC dependence, no BBB LAT1 transport needed). This makes it effective even in patients with very advanced PD and severe dopaminergic terminal degeneration who have poor or unreliable levodopa response
- **Distinction from [[vyalev|VYALEV]]/[[duopa|Duopa]]:** Those products deliver levodopa (endogenous precursor requiring enzymatic conversion); apomorphine is a direct receptor agonist. Some advanced patients benefit from both modalities simultaneously

### Clinical

**Registration Study (Phase 3)** | Multi-center | N=29 | Advanced PD with OFF episodes
- **Primary endpoint:** UPDRS motor score improvement during OFF episode → 97% responder rate at 20 min post-injection; mean UPDRS motor improvement ~23.9 points
- **Status:** Completed (basis for FDA approval April 20, 2004)
- **Interpretation:** Small trial, high responder rate. Approval based on a pharmacologically clear on/off effect evident to treating physicians and patients. EU apomorphine experience (APO-go, available in Europe since 1993) provided substantial pre-approval safety context

**Post-approval real-world data (10+ years US commercial use)**
- Multiple observational studies and registry analyses confirming 40-90% reduction in OFF duration in responders
- Key safety signals maintained in long-term data: injection site nodules (~5-10% with poor site rotation), nausea, dyskinesia, somnolence, hallucinations, orthostatic hypotension
- **Status:** Ongoing post-marketing surveillance per REMS program

### Financial
- **FY2024 net revenue:** $73.9M [source](https://ir.supernus.com/news-releases/news-release-details/supernus-announces-fourth-quarter-and-full-year-2024-financial)
- **Revenue trajectory:** APOKYN revenue will likely plateau and decline as ONAPGO (continuous SC apomorphine pump, launched April 2025) ramps. ONAPGO reported >750 enrollment forms in its first quarter of launch — indicating rapid uptake. Supernus has financial incentive to migrate continuous-use patients to ONAPGO (higher per-patient annual value, device platform harder to replicate than a generic SC injection)
- **Acquisition context:** Supernus acquired APOKYN and KYNMOBI (sublingual apomorphine film) from US WorldMeds in 2020. Deal terms not disclosed; the acquisition established Supernus as the dominant US commercial entity for apomorphine therapy in PD
- **Pricing:** APOKYN specialty pharmacy pricing ~$150-300 per cartridge at standard doses; annual cost varies significantly by OFF episode frequency (episodic patients: $5,000-20,000/yr est.; daily multiple-injection patients: $30,000+/yr est.). Reimbursement complexity: Medicare Part B (physician-administered first injection) vs. Part D (self-administered follow-on doses)
- **ONAPGO framing:** The continuous apomorphine pump changes the revenue model — ONAPGO is an annuity-like infusion product vs. APOKYN's episodic injection. Supernus's strategy of owning both acute rescue (APOKYN) and continuous delivery (ONAPGO) alongside dyskinesia therapy ([[gocovri|Gocovri]]) creates a multi-product PD symptomatic franchise

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

- **vs. KYNMOBI (Sunovion/Sumitomo Pharma):** Sublingual apomorphine film, approved May 2020. Needle-free advantage, but slower onset (15-30 min vs. 10 min SC) and lower bioavailability. Competes for needle-averse patients with infrequent OFF episodes
- **vs. Inbrija (inhaled levodopa, Acorda):** Rescue inhaler for OFF episodes; levodopa mechanism (not apomorphine). Onset ~10-15 min. Competes directly for the ON-demand rescue prescription. Does not require antiemetic co-administration — a convenience advantage
- **vs. ONAPGO (Supernus own product):** ONAPGO is a continuous 24-hour SC apomorphine pump rather than an episodic injection. Converts the daily-multiple-injection APOKYN patient to background infusion. Not a substitute for truly episodic rescue (1-2 OFF episodes/week); direct substitute for patients using APOKYN multiple times daily
- **vs. [[vyalev|VYALEV]] (AbbVie):** Advanced levodopa infusion for motor fluctuations. Different mechanism (levodopa vs. dopamine agonist), different patient profile. VYALEV is the dominant growing entrant in advanced PD infusion; APOKYN's differentiation is speed-of-action and the agonist mechanism for patients who have lost reliable levodopa response

## Analysis

APOKYN occupies a specific and durable niche: the fastest available rescue therapy for PD OFF episodes, with a clear pharmacological mechanism and 20+ years of US clinical use. The antiemetic burden and injection requirement are real friction points, but for the severe advanced PD patient experiencing abrupt, unpredictable OFFs, the 10-minute onset is a meaningful clinical advantage over all oral alternatives.

The strategic picture is managed transition. Supernus built a three-product PD apomorphine ecosystem (APOKYN acute rescue + KYNMOBI sublingual backup + ONAPGO continuous infusion). As ONAPGO ramps in 2025-2026, the segment of APOKYN users who take multiple injections daily will convert — these patients get equivalent or better coverage from continuous ONAPGO. The episodic-rescue segment (infrequent, unpredictable OFFs) is less substitutable and will sustain a base APOKYN revenue even at full ONAPGO adoption.

**Analytical estimate — APOKYN revenue trajectory: peak ~$80M (2024-2025), declining to ~$40-55M by 2028.** This is our assessment, not from a published source. The reasoning: ONAPGO converts the daily-injection subgroup (~30-40% of APOKYN users est.); episodic-rescue subgroup (~60-70%) less affected. Generic apomorphine SC is not approved in the US, providing pricing protection. Net decline of 30-40% from peak over 3-4 years is the central scenario, with the residual base stable thereafter unless KYNMOBI or another sublingual/inhaled option takes further share.

## References

### Clinical Trials
- [APOKYN registration NDA | FDA](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/21264_Apokyn.cfm)

### Key Publications
- [Subcutaneous apomorphine for Parkinson's disease: an evidence-based review | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293524/)
- [Apomorphine in Parkinson's Disease: Mechanisms, Clinical Uses, and Future Directions | Movement Disorders (2020)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.28131)
- [Dopamine Agonists in Early Parkinson's Disease | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6600280/)

### Press Releases & Filings
- [Supernus Q4 and Full Year 2024 Financial Results](https://ir.supernus.com/news-releases/news-release-details/supernus-announces-fourth-quarter-and-full-year-2024-financial)
- [ONAPGO (SC apomorphine pump) FDA Approval — Supernus (Q1 2025)](https://ir.supernus.com/news-releases/news-release-details/supernus-pharmaceuticals-announces-fda-approval-onapgo)
- [Supernus Q1 2025 Financial Results (ONAPGO launch)](https://ir.supernus.com/news-releases/news-release-details/supernus-pharmaceuticals-announces-first-quarter-2025-financial)

### Regulatory & Market
- [APOKYN Prescribing Information | FDA](https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/021264s021lbl.pdf)
- [APOKYN Product Page | Supernus](https://www.apokyn.com/)
- [FDA Approval Letter — Apokyn NDA 021264 (April 2004)](https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2004/21264ltr.pdf)
