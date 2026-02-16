---
drug_name: "Cinpanemab"
aliases: ["BIIB054"]
target: "alpha-synuclein (aggregated, N-terminal aa 1-10)"
mechanism: "Human-derived IgG1 mAb binding N-terminal epitope (aa 1-10) of alpha-synuclein to clear extracellular aggregates"
modality: "monoclonal antibody"
developer: "Biogen"
company_type: "big pharma"
publicly_traded: true
ticker: "BIIB"
partner: "Neurimmune"
partner_type: "biotech"
stage: "Terminated"
status: "Failed"
patient_population: "Early PD (diagnosed within 3 years, Hoehn & Yahr ≤2.5)"
route_of_administration: "IV (every 4 weeks)"
key_biomarkers: ["DaT-SPECT", "MDS-UPDRS", "CSF alpha-synuclein seeding", "NfL"]
confidence_rating: "N/A"
next_catalyst: "N/A"
catalyst_date: "N/A"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline, claude, failure-case]
date: 2026-02-15
company_link: "[[companies/biogen]]"
partner_link: "[[companies/neurimmune]]"
---

# Cinpanemab

## Summary

Cinpanemab failed. The SPARK Phase 2 trial (N=357) showed no difference from placebo on any clinical, imaging, or biomarker endpoint at 52 weeks, and Biogen (big pharma, BIIB) terminated the program in February 2021 with a $75M impairment charge. The most important lesson from this failure is epitope-specific: cinpanemab targeted the **N-terminus** (aa 1-10) of alpha-synuclein, while [[prasinezumab]] targets the **C-terminus** — and among five Phase 2 antibodies in the alpha-synuclein space, cinpanemab was the only N-terminal binder and the only one to show zero signal. This epitope distinction is now a central organizing principle in the field. Biogen has since exited alpha-synuclein entirely (also discontinuing [[ion464|ION464]], their alpha-synuclein ASO), retaining only [[biib122|BIIB122]] (LRRK2 inhibitor) as their sole PD program.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Neurimmune |
| Deal Date | 2010 |
| Upfront | Undisclosed |
| Total (Biobucks) | Undisclosed |
| Deal Type | Licensing/co-development |

## Notes

### Science
- Human-derived IgG1 monoclonal antibody with **800-fold selectivity** for aggregated vs. monomeric alpha-synuclein, binding the **N-terminal epitope (amino acids 1-10)**
- Mechanism: designed to bind and clear extracellular alpha-synuclein aggregates, blocking prion-like cell-to-cell propagation — same general strategy as [[prasinezumab]] but targeting a different region of the protein
- **Critical epitope distinction:** cinpanemab binds the N-terminus; [[prasinezumab]] binds the C-terminus. Among five alpha-synuclein antibodies that entered Phase 2, cinpanemab was the **only N-terminal binder** — and the only one with a completely null result. The four C-terminal binders (including [[prasinezumab]]) showed at least some biological signal ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638298/))
- The N-terminal region (aa 1-10) is exposed in both monomeric and aggregated forms of alpha-synuclein, meaning cinpanemab may have been sequestered by abundant monomeric protein in the periphery, reducing the effective dose reaching aggregates in the CNS
- CSF-to-serum ratio was 0.13-0.56% in Phase 1 — within the expected range for standard mAbs (~0.1-0.2%), but whether this was sufficient for target engagement at the N-terminal epitope is unknown
- Phase 1 confirmed BIIB054/alpha-synuclein complex formation in plasma and near-complete saturation in PD participants, but peripheral target engagement did not translate to CNS efficacy
- Alpha-synuclein SAA confirmed 93% of enrolled CSF subgroup participants were seeding-positive at baseline, verifying the trial enrolled a true synucleinopathy population — the failure was not due to misdiagnosis

### Clinical

**BIIB054 Phase 1 (SAD)** | NCT02459886 | N=66 (48 healthy volunteers + 18 PD) | Healthy volunteers (age 40-65) + early PD (age 47-75, H&Y ≤2.5)
- **Primary endpoint:** Safety/tolerability → Clean profile; most AEs mild and unrelated to drug. One participant in 135 mg/kg cohort developed asymptomatic ischemia (right parietal lobe)
- **Key secondary:** Dose-proportional PK (1-135 mg/kg); serum half-life 28-35 days; CSF-to-serum ratio 0.13-0.56%; confirmed alpha-synuclein complex formation in plasma
- **Status:** Completed
- **Interpretation:** Favorable PK/PD and safety supported Phase 2 progression. CSF penetration confirmed but quantitatively low, consistent with standard mAb limitations

**SPARK (Phase 2)** | NCT03318523 | N=357 | Early PD (diagnosed ≤3 years, H&Y ≤2.5, dopaminergic deficit on DaT-SPECT)
- **Primary endpoint:** Change from baseline in MDS-UPDRS total score at weeks 52 and 72 → **No difference from placebo at any dose** (placebo: +10.8 points; 250mg: +10.5; 1,250mg: +11.3; 3,500mg: +10.9)
- **Key secondary:** DaT-SPECT striatal binding ratio change → **No difference from placebo**. CSF NfL, total alpha-synuclein, alpha-synuclein seeding → **No treatment effect on any biomarker**
- **Design:** 2:1:2:2 randomization (placebo : 250mg : 1,250mg : 3,500mg), IV every 4 weeks, 52-week double-blind + dose-blinded extension up to 112 weeks
- **Interim analysis:** Terminated after week 72 interim due to lack of efficacy
- **Safety:** Favorable; AE rates comparable to placebo across all doses
- **Status:** Terminated (February 2021)
- **Interpretation:** A clean, unambiguous failure. No signal on clinical endpoints, no signal on imaging, no signal on fluid biomarkers, at any dose. The absence of ANY dose-response trend across a 14-fold dose range (250mg to 3,500mg) strongly suggests the drug did not engage its target in a therapeutically meaningful way in the CNS. This is not a "borderline miss" — it is a null result

### Financial
- **Licensing:** Biogen licensed cinpanemab from Neurimmune in 2010; financial terms undisclosed
- **Impairment:** Biogen took a **$75.4M GAAP impairment charge** (Q4 2020) to write IPR&D intangible asset to zero, partially offset by $51M gain from adjustment of contingent consideration obligation
- **Strategic impact:** The SPARK failure, combined with the later discontinuation of [[ion464|ION464]] (alpha-synuclein ASO, February 2025), represents Biogen's complete exit from the alpha-synuclein target class. Their sole remaining PD program is [[biib122|BIIB122]] (LRRK2 kinase inhibitor)
- **Context:** Biogen's $75M write-off is modest relative to the cumulative $5B+ industry investment in alpha-synuclein therapeutics. The real cost was the 3+ years of clinical development time in a competitive field

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "alpha-synuclein") AND file.name != "cinpanemab"
SORT stage DESC
```

- Cinpanemab's failure is the **critical negative control** for the alpha-synuclein antibody field: same selectivity (800-fold for aggregates), same route (IV), same population (early PD) — but different epitope (N-terminus vs. C-terminus). The fact that [[prasinezumab]] (C-terminal) showed a borderline motor signal (HR=0.84, p=0.0657 in PADOVA) while cinpanemab showed zero signal at any dose is the strongest evidence that epitope selection matters
- The complete absence of DaT-SPECT changes in SPARK — unlike minzasolmin (which showed imaging changes without clinical benefit in ORCHESTRA) — suggests cinpanemab may not have achieved sufficient target engagement to produce any measurable CNS effect
- Cinpanemab's failure did NOT kill the alpha-synuclein target hypothesis. The field interpreted it as an epitope/modality failure, which enabled [[prasinezumab]] to advance to Phase 3, Novartis to invest $2.2B in [[aro-snca|ARO-SNCA]], and Lilly to enter with [[ly3962681|LY3962681]]. Whether this interpretation is correct or is motivated reasoning remains an open question

## Analysis

Cinpanemab's SPARK trial is the cleanest negative result in the alpha-synuclein therapeutic space. Unlike [[prasinezumab]]'s PADOVA (which missed primary but showed subgroup signals) or minzasolmin's ORCHESTRA (which showed imaging changes without clinical benefit), SPARK produced a perfectly flat null across all endpoints, all doses, all biomarkers. There is no subgroup, no secondary endpoint, and no post-hoc analysis that salvages any signal from this trial. This cleanness is scientifically valuable because it allows the field to attribute the failure to something specific rather than chalking it up to noise.

The leading explanation is **epitope-specific failure**. The N-terminal region of alpha-synuclein is accessible in both monomeric and aggregated forms, meaning cinpanemab likely saturated peripheral monomeric alpha-synuclein (confirmed by Phase 1 plasma complex data) while achieving insufficient binding to pathological aggregates in the CNS. The C-terminal region may be preferentially exposed on aggregated species or more relevant to the toxic conformation that drives prion-like spreading. This explanation is supported by the observation that all four C-terminal-targeting antibodies in Phase 2 showed at least some biological activity, while the sole N-terminal binder showed none. However, this explanation is post-hoc and untested — no head-to-head study has compared N-terminal vs. C-terminal targeting.

**Analytical estimate — probability that N-terminal epitope was the primary cause of failure: 55-65%.** This is our assessment, not from a published source. The reasoning: the epitope hypothesis is consistent with the cross-program comparison (4 C-terminal binders with signals, 1 N-terminal binder without), but alternative explanations remain viable. The 52-week duration may have been too short (prasinezumab's strongest data is from the 4-year OLE). The unselected population (no levodopa enrichment, no SAA stratification at enrollment despite 93% SAA positivity confirmed retrospectively) may have introduced heterogeneity. And the fundamental challenge of antibody CNS penetration applies equally to all alpha-synuclein mAbs regardless of epitope. The truth is likely multi-factorial: wrong epitope AND insufficient duration AND insufficient CNS exposure.

The most consequential downstream effect of cinpanemab's failure is what it enabled. Biogen's exit from alpha-synuclein created strategic space for competitors. Roche/Prothena interpreted SPARK as evidence that [[prasinezumab]]'s C-terminal approach was differentiated, which supported their Phase 3 advancement decision. Novartis interpreted the broader antibody record (including SPARK) as evidence that the modality — not the target — was wrong, justifying the $2.2B investment in production inhibition via [[aro-snca|ARO-SNCA]]. Whether these interpretations prove correct depends on the PARAISO Phase 3 readout (2027-2028) and ARO-SNCA clinical data (2027-2029).

## References

### Clinical Trials
- [SPARK Phase 2](https://clinicaltrials.gov/study/NCT03318523) — NCT03318523
- [BIIB054 Phase 1 SAD](https://clinicaltrials.gov/study/NCT02459886) — NCT02459886

### Key Publications
- [Trial of Cinpanemab in Early Parkinson's Disease | NEJM (Aug 2022)](https://www.nejm.org/doi/full/10.1056/NEJMoa2203395)
- [Cinpanemab in Early Parkinson Disease: Evaluation of Biomarker Results From the Phase 2 SPARK Clinical Trial | Neurology (Feb 2024)](https://www.neurology.org/doi/abs/10.1212/WNL.0000000000209137)
- [Randomized Phase I Clinical Trial of Anti-Alpha-Synuclein Antibody BIIB054 | Mov Disord (2019)](https://pubmed.ncbi.nlm.nih.gov/31211448/)
- [Phase II Dose Selection for Cinpanemab Based on Target Protein Binding Levels in the Brain | CPT (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7499191/)
- [Update on Immune-Based Alpha-Synuclein Trials in Parkinson's Disease | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638298/)
- [Trial of Prasinezumab in Early-Stage Parkinson's Disease (PASADENA) | NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2202867) — companion C-terminal antibody trial for comparison

### Press Releases & Filings
- [Biogen Discontinues Development of Cinpanemab for Parkinson's (Feb 2021)](https://parkinsonsnewstoday.com/2021/02/04/biogen-announcement-discontinue-cinpanemab-parkinsons/)
- [Biogen Tosses Out Cinpanemab, Pays $75M Impairment | Fierce Biotech (Feb 2021)](https://www.fiercebiotech.com/biotech/biogen-tosses-out-parkinson-s-hopeful-cinpanemab-pays-75m-for-its-syn)
- [Cinpanemab Profile | Alzforum](https://www.alzforum.org/therapeutics/cinpanemab)
