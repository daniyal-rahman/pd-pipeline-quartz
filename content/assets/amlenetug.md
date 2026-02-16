---
drug_name: "Amlenetug"
aliases: ["Lu AF82422"]
target: "alpha-synuclein (all extracellular forms, epitope aa 112-117)"
mechanism: "Fully human IgG1 mAb binding all major extracellular alpha-synuclein forms (monomeric, aggregated, truncated) to block neuronal uptake, inhibit prion-like seeding, and promote microglial clearance"
modality: "monoclonal antibody"
developer: "Lundbeck"
company_type: "big pharma"
publicly_traded: true
ticker: "HLUN-B (Copenhagen)"
partner: "Genmab"
partner_type: "biotech"
stage: "Phase 3"
status: "Active"
patient_population: "MSA (clinically probable/established, <5 yrs motor onset, age 40-75)"
route_of_administration: "IV (every 4 weeks)"
key_biomarkers: ["UMSARS", "brain MRI volumetrics", "free/total alpha-synuclein ratio (plasma and CSF)"]
confidence_rating: "4/10"
next_catalyst: "MASCOT Phase 3 topline readout"
catalyst_date: "2027 (estimated)"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/lundbeck]]"
partner_link: "[[companies/genmab]]"
---

# Amlenetug

## Summary

Amlenetug is Lundbeck's (big pharma, Copenhagen: HLUN-B) fully human anti-alpha-synuclein antibody in Phase 3 for Multiple System Atrophy (MSA) — a synucleinopathy closely related to PD. The Phase 2 AMULET trial missed its primary endpoint (UMSARS total score) but showed a consistent 19% slowing of clinical progression, with a more pronounced 37-42% effect in less-impaired patients. Lundbeck is advancing into the ~360-patient MASCOT Phase 3 trial (NCT06706622) with FDA Fast Track and Orphan Drug designations in hand. If MASCOT succeeds, amlenetug would become the first disease-modifying therapy approved in any synucleinopathy, validating the extracellular alpha-synuclein clearance hypothesis with direct read-through to PD — strengthening the case for [[prasinezumab]] and the broader anti-alpha-synuclein antibody modality. If it fails, it adds to the growing list of alpha-synuclein antibody misses and accelerates the field's pivot toward production inhibition via [[aro-snca|siRNA/ASO approaches]].

## Notes

### Science
- Fully human IgG1 monoclonal antibody that binds **all major extracellular forms** of alpha-synuclein: monomeric, aggregated, and C-terminal truncated species
- Epitope mapped to **amino acids 112-117** via crystallographic structure analysis — outside the central aggregating NAC domain, distinct from both C-terminal ([[prasinezumab]]) and N-terminal ([[cinpanemab]]) epitopes
- Proposed mechanism: binds extracellular pathological alpha-synuclein to (1) prevent neuronal uptake, (2) inhibit prion-like seeding and cell-to-cell spreading, and (3) facilitate microglial-mediated phagocytosis of aggregates
- Preclinically, amlenetug inhibits seeding induced by various alpha-synuclein fibrillar assemblies **and** by aggregates isolated directly from MSA brain homogenate — a key differentiator since MSA alpha-synuclein strains are structurally distinct from PD strains
- Phase 1 confirmed dose-proportional plasma/CSF penetration with mean plasma half-life of ~700 hours; high-dose PD cohort showed lowered free-to-total alpha-synuclein ratio in CSF, confirming central target engagement
- Open scientific question: MSA pathology is primarily oligodendroglial (glial cytoplasmic inclusions) vs. neuronal in PD — does clearing extracellular alpha-synuclein sufficiently address glial seeding? The MSA-first strategy is higher-risk but potentially higher-reward given faster disease progression and easier signal detection

### Clinical

**Phase 1 First-in-Human** | NCT03611569 | N=74 (59 healthy + 15 PD) | Healthy volunteers (18-55 yrs) and PD patients (40-80 yrs, H&Y ≤3)
- **Primary endpoint:** Safety/tolerability → Clean safety profile, no serious adverse events across single ascending doses (75-9000 mg IV)
- **Key secondary:** Dose-proportional PK in plasma and CSF; CSF concentrations ~0.1-0.5% of plasma levels; 37% reduction in free-to-total alpha-synuclein ratio in high-dose PD cohort, confirming central target engagement
- **Status:** Completed (July 2021)
- **Interpretation:** Established that clinically achievable doses provide CSF concentrations sufficient to target aggregated alpha-synuclein. PK profile supports monthly IV dosing.

**AMULET (Phase 2)** | NCT05104476 | N=61 | MSA patients (age 40-75), randomized 2:1 amlenetug (4.2g IV Q4W) : placebo, 48-72 weeks
- **Primary endpoint:** Longitudinal change from baseline in UMSARS Part I + Part II Total Score over 48-72 weeks → **19% slowing of progression vs. placebo — NOT statistically significant**
- **Key secondary:** Slope analysis of mUMSARS, UMSARS Part I, and UMSARS Part II showed consistent slowing of 27%, 22%, and 17% respectively. Trend toward smaller regional MRI volumetric reduction in amlenetug arm. Signals of efficacy across multiple clinical and biomarker endpoints.
- **Subgroup (less impaired patients, baseline UMSARS Part I <=16, n=42):** 37% slowing of clinical progression (post-hoc: up to 42% in some analyses)
- **Safety:** Generally well tolerated; 45/61 patients opted into 48-week open-label extension
- **Status:** Completed November 2023; results presented at AD/PD 2024 conference and MDS 2025
- **Interpretation:** Missed primary but pattern mirrors the broader alpha-synuclein antibody field. The less-impaired subgroup enrichment is the key design insight carried into Phase 3 — earlier-stage patients have less irreversible neuronal loss, giving the antibody more disease to modify. MASCOT eligibility criteria (<5 years motor onset) reflect this learning.

**MASCOT (Phase 3)** | NCT06706622 | N=~360 | MSA (probable/established, parkinsonian or cerebellar subtype, <5 yrs motor onset, age 40-75)
- **Primary endpoint:** Change from baseline in modified UMSARS score over 72 weeks, analyzed via Bayesian progression model
- **Design:** Randomized, double-blind, placebo-controlled, 3 arms (high-dose amlenetug, low-dose amlenetug, placebo), IV infusion every 4 weeks. Optional 72-week open-label extension.
- **Secondary endpoints:** UMSARS subscales, ADL scores, CGI/PGI, time to death, EuroQol, MSA-QoL, brain volume changes
- **Geographic scope:** North America, Europe, Asia, Australia
- **Status:** Initiated November 2024; enrollment ongoing globally
- **Interpretation:** One of the largest MSA trials ever conducted. Bayesian design is a sophisticated choice for a rare disease with high variability — allows adaptive inference. The two-dose design hedges on optimal exposure. Fast Track + Orphan Drug Designation + rolling review pathway could compress time to market if positive.

### Financial
- **Lundbeck financials:** ~24B DKK (~$3.5B) annual revenue (2025 LTM), ~$6B market cap. Brain-focused specialty pharma with CNS-only portfolio (depression, schizophrenia, epilepsy, PD, Alzheimer's)
- **Genmab collaboration:** Amlenetug was invented under a joint research and licensing agreement between Lundbeck and Genmab A/S. Detailed financial terms undisclosed
- **Longboard acquisition:** Lundbeck acquired Longboard Pharmaceuticals for $2.6B (2024) for bexicaserin (DEE/Dravet) — signals strategic commitment to neuro-rare disease franchise alongside amlenetug
- **Orphan Drug economics:** MSA has ~15,000-50,000 patients in the US. Orphan designation provides 7 years market exclusivity (US), 10 years (EU), plus tax credits and fee waivers. Orphan pricing for first-in-class disease-modifying MSA therapy could reach $100K-300K/year
- **Regulatory designations accumulated:** FDA Orphan Drug (April 2024), FDA Fast Track (2025), Japan Orphan Drug (March 2025), Japan SAKIGAKE (March 2023), EMA Orphan Drug (May 2021) — this regulatory strategy is comprehensive and signals serious commercial intent
- **Peak sales potential:** If approved in MSA alone, $500M-1B+ possible given orphan pricing and unmet need. PD indication expansion could dramatically increase TAM
- **Pipeline context:** Lundbeck targets 3-4 Phase 3 programs by 2026. Amlenetug and bexicaserin are the two lead late-stage assets; success of either transforms Lundbeck's growth profile

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "alpha-synuclein") AND file.name != "amlenetug"
SORT stage DESC
```

- Amlenetug's **MSA-first strategy** differentiates it from [[prasinezumab]] (PD-first) — MSA progresses faster (median survival 6-9 years), enabling shorter trials with clearer signal detection, and has no approved disease-modifying therapies (lower regulatory bar)
- Epitope at **aa 112-117** is distinct from [[prasinezumab]] (C-terminal) and [[cinpanemab]] (N-terminal aa 1-10), but the functional relevance of epitope differences among anti-alpha-synuclein antibodies remains unclear
- Key competitive read-through: if MASCOT succeeds in MSA, it validates extracellular alpha-synuclein clearance as a mechanism → directly strengthens [[prasinezumab]]'s thesis in PD and could motivate Lundbeck to pursue PD indication expansion for amlenetug
- If MASCOT fails alongside PARAISO ([[prasinezumab]]), the entire anti-alpha-synuclein antibody class is severely weakened → capital shifts to [[aro-snca|siRNA/gene silencing]], [[pariceract|GBA1]], and [[biib122|LRRK2]] approaches
- No direct MSA competitors at Phase 3 — amlenetug has a clear runway as potentially the first disease-modifying MSA therapy. Verve Therapeutics' BIIB101 (alpha-synuclein ASO, Biogen) was in MSA trials but had mixed results
- The broader alpha-synuclein antibody landscape (multiple Phase 2 failures) creates a headwind; MASCOT outcome will be interpreted in context of the class track record

## Analysis

Amlenetug occupies a strategically distinct position in the alpha-synuclein landscape: same target class as [[prasinezumab]], but pursued in MSA rather than PD. This is both a regulatory/commercial advantage (unmet need, orphan economics, faster progression = shorter trials) and a scientific risk (MSA alpha-synuclein pathology is glial-predominant, which may respond differently to extracellular antibody clearance than the neuronal pathology in PD). The AMULET Phase 2 miss on the primary endpoint follows the pattern seen across every alpha-synuclein antibody trial to date — none have met primary endpoints — but the consistent directional signal and subgroup enrichment provide enough rationale for a Phase 3 bet.

**Analytical estimate — Phase 3 success probability: 20-25%.** This is our assessment, not from a published source. The reasoning:
- Base rate: 0/6+ alpha-synuclein antibodies have met primary endpoints in any synucleinopathy → starting point ~10%
- Adjustments upward: MSA-specific enrichment for less-impaired patients (+8%), Bayesian adaptive design (+3%), two-dose arms increase chance of finding optimal exposure (+3%), Fast Track/rolling review reduces regulatory risk (+2%), no competing approved therapy lowers efficacy bar (+3%)
- Adjustments downward: AMULET primary miss (-5%), small Phase 2 (N=61) makes signal less reliable (-3%), MSA glial pathology may not respond to extracellular clearance (-3%), rare disease enrollment challenges could compromise power (-2%)
- Net: ~20-25% (lower than [[prasinezumab]] at 30-35% because the Phase 2 data package is thinner and the MSA biology is less well-validated for antibody intervention)

The most informative signal is Lundbeck's behavior. They are a mid-size pharma (~$6B market cap) betting significant resources on amlenetug — including the $2.6B Longboard acquisition that broadens their neuro-rare portfolio but also increases pressure on the MSA franchise to deliver. The comprehensive regulatory strategy (orphan + fast track in US, EU, and Japan) reflects genuine commercial preparation, not exploratory science. If MASCOT reads out positively, the orphan + first-in-class combination in MSA could produce a high-value small-population franchise ($500M-1B+ peak sales) even before any PD indication expansion. The PD landscape relevance is as a bellwether: a positive MASCOT result would be the first proof that any anti-alpha-synuclein antibody can modify disease in any synucleinopathy, materially de-risking [[prasinezumab]]'s PARAISO trial.

## References

### Clinical Trials
- [Phase 1 First-in-Human (NCT03611569)](https://clinicaltrials.gov/study/NCT03611569) — NCT03611569
- [AMULET Phase 2 (NCT05104476)](https://clinicaltrials.gov/study/NCT05104476) — NCT05104476
- [MASCOT Phase 3 (NCT06706622)](https://clinicaltrials.gov/study/NCT06706622) — NCT06706622

### Key Publications
- [Randomized Phase I Trial of the alpha-Synuclein Antibody Lu AF82422 | Movement Disorders (2024)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.29784)
- [Rational selection of the monoclonal alpha-synuclein antibody amlenetug (Lu AF82422) for the treatment of alpha-synucleinopathies | npj Parkinson's Disease (2025)](https://www.nature.com/articles/s41531-024-00849-1)
- [Nonclinical safety evaluation, PK, and target engagement of Lu AF82422 | mAbs (2021)](https://dx.doi.org/10.1080/19420862.2021.1994690)
- [An update on immune-based alpha-synuclein trials in Parkinson's disease | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638298/)
- [MASCOT Trial Design Abstract | MDS Abstracts](https://www.mdsabstracts.org/abstract/a-randomized-double-blind-phase-3-trial-of-amlenetug-versus-placebo-in-patients-with-msa-the-mascot-trial/)
- [AMULET Phase 2 results | MDS Abstracts](https://www.mdsabstracts.org/abstract/safety-and-efficacy-of-the-anti-alpha-synuclein-monoclonal-antibody-lu-af82422-for-the-treatment-of-patients-with-msa-results-from-the-phase-2-amulet-trial/)

### Press Releases & Filings
- [Lundbeck initiates Phase III trial with amlenetug for MSA (Nov 2024)](https://news.cision.com/h--lundbeck-a-s/r/lundbeck-initiates-a-phase-iii-trial-with-amlenetug-for-the-treatment-of-multiple-system-atrophy,c4071927)
- [Lundbeck announces supportive Phase II results from AMULET (Jan 2024)](https://news.cision.com/h--lundbeck-a-s/r/lundbeck-announces-supportive-phase-ii-results-with-lu-af82422-in-the-treatment-of-multiple-system-a,c3920120)
- [Lundbeck presents results at AD/PD 2024 conference (Mar 2024)](https://news.cision.com/h--lundbeck-a-s/r/lundbeck-presents-encouraging-results-from-the-lu-af82422-trial-for-multiple-system-atrophy-at-the-i,c3940069)
- [Lundbeck presents at MDS Congress 2025](https://news.cision.com/h--lundbeck-a-s/r/lundbeck-presents-results-from-two-studies-in-multiple-system-atrophy-at-international-congress-of-p,c4043552)
- [Lundbeck showcases MASCOT trial design at MDS 2025](https://www.prnewswire.com/news-releases/lundbeck-to-showcase-amlenetug-phase-3-mascot-trial-design-in-multiple-system-atrophy-at-the-international-congress-of-parkinsons-disease-and-movement-disorders-2025-302573439.html)
- [Amlenetug profile | Alzforum](https://www.alzforum.org/therapeutics/lu-af82422)

### Regulatory & Market
- [FDA Fast Track Designation for amlenetug in MSA (2025)](https://www.lundbeck.com/us/newsroom/2025/lundbecks-potential-treatment-amlenetug-for-multiple-system-atrophy-fast-track)
- [FDA Grants Fast Track Designation | NeurologyLive](https://www.neurologylive.com/view/fda-grants-fast-track-designation-promising-multiple-system-atrophy-agent-amlenetug)
- [Lundbeck pipeline overview](https://www.lundbeck.com/global/our-science/pipeline)
- [Japan Orphan Drug Designation for amlenetug (Mar 2025)](https://www.prnewswire.com/news-releases/lundbecks-potential-treatment-for-multiple-system-atrophy-granted-orphan-drug-designation-in-japan-302396851.html)
- [Lundbeck acquires Longboard Pharmaceuticals for $2.6B (2024)](https://www.lundbeck.com/us/newsroom/2024/lundbeck-to-acquire-longboard-pharmaceuticals-in-a-strategic-deal)
