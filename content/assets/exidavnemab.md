---
drug_name: "Exidavnemab"
aliases: ["BAN0805", "ABBV-0805", "mAb47"]
target: "alpha-synuclein (aggregated, oligomeric/protofibrillar)"
mechanism: "Humanized IgG4 mAb with 100,000-fold selectivity for aggregated vs. monomeric alpha-synuclein, clearing soluble oligomeric/protofibrillar species to block prion-like cell-to-cell spread"
modality: "monoclonal antibody"
developer: "BioArctic"
company_type: "biotech"
publicly_traded: true
ticker: "BIOA-B (Stockholm)"
partner: ""
stage: "Phase 2"
status: "Active"
patient_population: "Mild to moderate PD on stable symptomatic therapy; expanded to include MSA"
route_of_administration: "IV (monthly infusion)"
key_biomarkers: ["plasma alpha-synuclein", "CSF alpha-synuclein", "digital biomarkers"]
confidence_rating: "4/10"
next_catalyst: "EXIST Phase 2a topline results"
catalyst_date: "H2 2026"
thesis_cluster: "alpha-synuclein"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/bioarctic]]"
---

# Exidavnemab

## Summary

BioArctic (biotech, BIOA-B Stockholm) is advancing exidavnemab in the Phase 2a EXIST trial (NCT06671938) in mild-to-moderate PD and MSA, with first patient dosed December 2024 and topline results expected after summer 2026. The antibody has >100,000-fold selectivity for aggregated vs. monomeric alpha-synuclein (KD = 18 pM) and compelling preclinical data (prolonged lifespan in three transgenic mouse models), but carries the baggage of AbbVie's 2022 termination of a $755M deal on the cusp of Phase 2 -- a decision that reads as a strategic retreat from alpha-synuclein antibodies rather than a data-driven kill. If EXIST shows clean safety and biomarker engagement, BioArctic will likely seek a new pharma partner for Phase 2b; if it fails, the aggregate-selective antibody thesis narrows to [[prasinezumab]] alone. The broader read-through depends on whether [[prasinezumab]]'s PARAISO Phase 3 validates extracellular alpha-synuclein clearance -- a positive PARAISO would dramatically increase exidavnemab's partnering value, while a negative PARAISO could make exidavnemab a stranded asset.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | AbbVie (terminated) |
| Deal Date | 2016 (option); 2018 (license) |
| Upfront | $80M (collaboration) + $50M (option exercise) |
| Total (Biobucks) | ~$755M + royalties |
| Deal Type | Licensing/co-development |

AbbVie terminated the collaboration in April 2022 after completing Phase 1 but before initiating Phase 2 -- all rights reverted to BioArctic. BioArctic subsequently self-funded INN designation (exidavnemab), new Phase 1 PK studies, and the Phase 2a EXIST trial.

## Notes

### Science
- Humanized **IgG4** mAb (notable: IgG4 rather than IgG1 subclass, reducing Fc-mediated effector function -- a deliberate choice to minimize potential neuroinflammation from microglial activation upon target engagement)
- **KD = 18 pM** binding affinity with **>100,000-fold selectivity** for pathological aggregated forms (oligomers, protofibrils, fibrils) over physiological monomeric alpha-synuclein -- the highest reported selectivity ratio among anti-alpha-synuclein antibodies
- Binds a broad spectrum of soluble aggregated alpha-synuclein, including small and large aggregates of different conformations
- Key distinction vs. [[prasinezumab]]: prasinezumab is IgG1 (pro-phagocytic) with 800-fold aggregate selectivity; exidavnemab is IgG4 (anti-inflammatory) with 100,000-fold selectivity -- different design philosophies on whether you want microglial engagement
- Key distinction vs. [[cinpanemab]]: cinpanemab targeted N-terminal epitope (aa 1-10) and failed Phase 2 (SPARK); exidavnemab targets aggregated conformations regardless of epitope, selecting for pathological species
- Key distinction vs. [[amlenetug]]: amlenetug (Lundbeck) is IgG1 binding all extracellular forms including monomers; exidavnemab spares monomers entirely, preserving physiological alpha-synuclein function
- Preclinical: murine version of ABBV-0805 tested in three transgenic alpha-synuclein mouse models -- dose-dependent reduction in brain alpha-synuclein aggregates, prevention of spreading, delayed motor symptom onset, and **significantly prolonged lifespan** (published in Neurobiology of Disease, 2021)
- Exidavnemab demonstrated binding to Lewy body-positive post-mortem brain tissue from PD patients, confirming target engagement on human pathological alpha-synuclein (published 2025)
- Elimination half-life of ~30 days supports once-monthly dosing
- Open question: does the IgG4 backbone sacrifice clearance efficacy for safety? IgG1 antibodies like [[prasinezumab]] recruit microglia for phagocytosis; IgG4 relies primarily on sequestration and peripheral sink mechanisms
- Standard mAb CNS penetration (~0.1-0.2% of blood levels) applies; whether the ultra-high affinity compensates for low brain exposure is unproven

### Clinical

**Phase 1 SAD (AbbVie-era)** | NCT04127695 | N=~40 | Healthy volunteers
- **Primary endpoint:** Safety/tolerability --> Well-tolerated, no concerning safety signals
- **Key secondary:** Pharmacokinetics supported once-monthly dosing; dose-linear PK
- **Status:** Withdrawn July 2020 for "strategic considerations" (AbbVie); results presented at MDS September 2021
- **Interpretation:** Clean Phase 1 data; the withdrawal was administrative (AbbVie restructuring) not safety-related

**Phase 1 SAD (BioArctic-era)** | NCT TBD | N=98 | Healthy Western Caucasian, Japanese, and Han Chinese volunteers
- **Primary endpoint:** Safety/tolerability + PK of IV and SC formulations --> Well-tolerated across all ethnic populations
- **Key secondary:** Dose-linear PK, elimination half-life ~30 days, low anti-drug antibody incidence
- **Status:** Completed; published in Journal of Clinical Pharmacology (2024)
- **Interpretation:** Bridging study establishing global PK consistency; SC formulation evaluated (potential future advantage over IV-only competitors)

**EXIST Phase 2a (EXIdavnemab Synucleinopathy Trial)** | NCT06671938 | N=24 PD + 12 MSA | Mild-to-moderate PD on stable symptomatic therapy; MSA patients
- **Primary endpoint:** Safety and tolerability
- **Key secondary:** PK, broad biomarker panel (plasma, CSF, digital measurements)
- **Design:** Randomized, double-blind, placebo-controlled, multiple ascending dose (MAD); 2 dose cohorts in PD (lower vs. higher dose), 1 cohort in MSA; IV infusions over 6 months
- **Geography:** Europe (Poland, Spain)
- **Status:** First patient dosed December 2024; positive interim safety review June 2025 (Cohort 1); Cohort 2 (higher dose) now initiated; MSA expansion approved May 2025
- **Regulatory:** FDA Orphan Drug Designation for MSA (March 2025); EMA Orphan Medicinal Product positive opinion for MSA (2025)
- **Expected readout:** After summer 2026; BioArctic preparing for Phase 2b
- **Interpretation:** Small safety/PK study -- not powered for efficacy. The MSA expansion is strategically smart: MSA is a more aggressive alpha-synucleinopathy with faster progression and orphan drug economics, providing an alternative development path if the PD indication stalls

### Financial
- **AbbVie deal (terminated):** BioArctic received ~$130M total (upfront + option exercise + milestones) before AbbVie walked away in 2022; $625M+ in milestones were never triggered
- **Self-funded Phase 2:** BioArctic is funding exidavnemab development from its own balance sheet, supported by lecanemab (Leqembi) royalties from Eisai (~SEK 117M/quarter in Q3 2025) and BrainTransporter platform deals
- **BrainTransporter platform revenue:** BMS deal ($100M upfront, $1.25B milestones); Novartis deal ($30M upfront, $772M milestones); Eisai deal -- collectively >$2B in deal value, providing substantial non-dilutive funding
- **BioArctic profitability:** Company expects to achieve profitability in 2025, reducing financial risk for the exidavnemab program
- **Market cap:** BIOA-B trades on Nasdaq Stockholm Large Cap (Swedish krona-denominated)
- **Orphan drug strategy:** MSA orphan designation provides 7 years US market exclusivity + 10 years EU exclusivity, accelerated regulatory pathway, and potentially lower bar for approval in a disease with zero approved therapies
- **Partnering potential:** If EXIST data are positive, the asset becomes highly partnerable -- BioArctic has demonstrated platform partnering capability (6 pharma deals on BrainTransporter), and a positive PARAISO readout for [[prasinezumab]] would create a tailwind for all aggregate-selective alpha-syn antibodies

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[cinpanemab]] | Terminated | Failed | Biogen | monoclonal antibody |
| [[ion464]] | Discontinued | Discontinued | Ionis Pharmaceuticals | ASO |
| [[minzasolmin]] | Terminated | Terminated | UCB | small molecule |
| [[saamplify-asyn]] | Commercial | Active | Amprion | diagnostic assay |
| [[trimtech-trim21]] | Discovery | Active | TRIMTECH Therapeutics | small molecule |
| [[adp062-abc]] | Preclinical | Active | Alector | siRNA |
| [[aro-snca]] | Preclinical | Active | Arrowhead Pharmaceuticals | siRNA |
| [[booster-therapeutics]] | Preclinical | Active | Booster Therapeutics | small molecule |
| [[eubiologics-vaccine]] | Preclinical | Active | EuBiologics | active vaccine |
| [[lbp-pd01]] | Preclinical | Active | LISCure Biosciences | live biotherapeutic product |
| [[mor-a-syn]] | Preclinical | Active | AC Immune | small molecule |
| [[act-02]] | IND-enabling | Active | Accure Therapeutics | small molecule |
| [[dnl422]] | IND-enabling | Active | Denali Therapeutics | ASO |
| [[18f-fd4]] | Phase 1 | Active | SynuSight Biotech | PET tracer |
| [[abl301]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |
| [[energi-f705pd]] | Phase 1 | Active | Energenesis Biomedical | small molecule |
| [[ly3962681]] | Phase 1 | Active | Prevail Therapeutics (Eli Lilly subsidiary) | siRNA |
| [[mk-7337]] | Phase 1 | Discontinued | Merck | PET tracer |
| [[nm-101]] | Phase 1 | Active | Neuramedy | monoclonal antibody |
| [[sar446159]] | Phase 1 | Deprioritized | ABL Bio | bispecific antibody |
| [[ucb7853]] | Phase 1 | Active | UCB | monoclonal antibody |
| [[vt-5006]] | Phase 1 | Active | Vertero Therapeutics | small molecule |
| [[emrusolmin]] | Phase 1b | Active | MODAG GmbH | small molecule |
| [[her-096]] | Phase 1b | Active | Herantis Pharma | peptide |
| [[ub-312]] | Phase 1b | Active | Vaxxinity | active vaccine |
| [[aci-7104]] | Phase 2 | Active | AC Immune | active vaccine |
| [[ath-434]] | Phase 2 | Active | Alterity Therapeutics | small molecule |
| [[exidavnemab]] | Phase 2 | Active | BioArctic | monoclonal antibody |
| [[lu-af67643]] | Phase 2 | Unverified | Lundbeck | monoclonal antibody |
| [[amlenetug]] | Phase 3 | Active | Lundbeck | monoclonal antibody |
| [[buntanetap]] | Phase 3 | Active | Annovis Bio | small molecule |
| [[prasinezumab]] | Phase 3 | Active | Prothena | Monoclonal antibody |

- [[prasinezumab]] (Prothena/Roche) is the clear category leader at Phase 3, with the most clinical data (PASADENA, PADOVA, PARAISO). Exidavnemab's fate is partially correlated: a PARAISO success would validate extracellular alpha-synuclein clearance and boost partnering prospects; a PARAISO failure would undermine the entire antibody modality
- Within aggregate-selective antibodies, exidavnemab's **100,000-fold selectivity** vs. prasinezumab's **800-fold selectivity** is a potential differentiator -- though higher selectivity has not been shown to translate into better clinical outcomes
- The IgG4 vs. IgG1 distinction matters: [[amlenetug]] (IgG1, Lundbeck) showed clean safety in Phase 1 for MSA, suggesting IgG1-mediated microglial activation is tolerable. If IgG1 antibodies prove safe AND more efficacious (via phagocytic clearance), exidavnemab's IgG4 design becomes a disadvantage
- [[aro-snca|ARO-SNCA]] (Alnylam/Novartis) represents the production-inhibition alternative -- targets alpha-synuclein at the mRNA level rather than clearing extracellular aggregates. If antibodies fail as a class, siRNA becomes the dominant modality
- [[aci-7104|ACI-7104.056]] (AC Immune) and [[ub-312|UB-312]] (Vaxxinity) are active vaccine approaches generating endogenous anti-alpha-synuclein antibodies -- lower COGS, easier dosing, but less control over antibody specificity and titer. If exidavnemab shows efficacy, vaccines targeting similar conformational epitopes become more attractive
- MSA indication creates a distinct competitive lane: [[amlenetug]] is also in Phase 2 for MSA, making it the direct MSA competitor. The orphan drug path means exidavnemab and [[amlenetug]] may race for first MSA approval, which carries significant market exclusivity advantages

## Analysis

Exidavnemab occupies an unusual position in the alpha-synuclein landscape: the strongest preclinical selectivity data among anti-alpha-synuclein antibodies, paired with the stigma of AbbVie's high-profile termination. The termination narrative requires careful parsing. AbbVie walked away from the entire alpha-synuclein antibody portfolio in April 2022 -- a period when the field was broadly derisked following [[cinpanemab]]'s SPARK failure (March 2022) and before [[prasinezumab]]'s OLE data revived the thesis (2024). This was a strategic portfolio decision, not a data-driven safety or efficacy kill. The Phase 1 data were clean, and BioArctic retained all rights, suggesting AbbVie saw no scientific red flags but chose to reallocate capital.

**Analytical estimate -- Phase 2a success probability (safety/biomarker): 70-75%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Phase 1-to-Phase 2 transition for mAbs in neurodegeneration is ~60-65%
- Adjustments upward: clean Phase 1 data across two studies (+10%), well-characterized mechanism with no safety signals in >100 subjects (+5%), IgG4 backbone reduces neuroinflammation risk (+5%)
- Adjustments downward: small trial (N=24 PD) limits statistical power for rare AEs (-5%)
- Net: ~70-75% probability of a "positive" Phase 2a (defined as safe + biomarker signal)

**Analytical estimate -- probability of eventually reaching market (PD): 8-12%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Phase 2 to approval in PD disease modification is ~5%
- Adjustments upward: strong preclinical data including lifespan extension (+3%), ultra-high selectivity theoretically reduces off-target engagement (+2%), MSA orphan pathway provides alternative (+3%)
- Adjustments downward: no pharma partner for Phase 2b+ (-3%), 0/6 alpha-syn antibodies have met primary endpoints in PD (-5%), BioArctic's small clinical development infrastructure limits execution speed (-2%)
- Net: ~8-12%

**Signal analysis:**
- BioArctic's decision to self-fund exidavnemab through Phase 2a while earning $100M+ annually from lecanemab royalties shows this is a company that can afford patience. They are not desperate for a partner -- they can wait for EXIST data and PARAISO readout to maximize partnering leverage.
- The MSA expansion is a sophisticated regulatory play. MSA is a devastating alpha-synucleinopathy with no approved therapies, faster clinical progression (easier to show signal), smaller trial sizes required, and orphan drug incentives. If exidavnemab works in MSA, it provides a proof-of-concept for the antibody mechanism that de-risks the larger PD program.
- The IgG4 vs. IgG1 design choice will become increasingly important as more alpha-syn antibodies enter trials. If [[prasinezumab]] (IgG1) succeeds, the question becomes whether IgG4's reduced effector function is a feature or a bug. BioArctic may need to demonstrate that sequestration alone is sufficient without phagocytic clearance.
- If EXIST Phase 2a succeeds: BioArctic will seek a pharma partner for Phase 2b in PD and potentially accelerate MSA development independently. Expect deal terms materially below the original AbbVie $755M ceiling given the asset is now Phase 2 with a terminated partner.
- If EXIST Phase 2a fails (safety signal or no biomarker engagement): exidavnemab is likely shelved, and BioArctic's alpha-synuclein thesis collapses back to the BrainTransporter platform for delivering other companies' antibodies across the BBB.

## References

### Clinical Trials
- [EXIST Phase 2a](https://clinicaltrials.gov/ct2/show/NCT06671938) -- NCT06671938
- [ABBV-0805 Phase 1 (AbbVie-era, withdrawn)](https://clinicaltrials.gov/ct2/show/NCT04127695) -- NCT04127695

### Key Publications
- [ABBV-0805, a novel antibody selective for soluble aggregated alpha-synuclein, prolongs lifespan and prevents buildup of alpha-synuclein pathology in mouse models of PD | Neurobiology of Disease (2021)](https://pubmed.ncbi.nlm.nih.gov/34737044/)
- [Safety, Tolerability, and Pharmacokinetics of Single Doses of Exidavnemab (BAN0805) in Healthy Adults | J Clin Pharmacol (2024)](https://pubmed.ncbi.nlm.nih.gov/39105497/)
- [Exidavnemab binds to aggregated alpha-synuclein in human brains affected by alpha-synucleinopathies | PubMed (2025)](https://pubmed.ncbi.nlm.nih.gov/41198458/)

### Press Releases & Filings
- [First patient dosed in EXIST Phase 2a study in PD (Dec 2024)](https://www.bioarctic.com/en/first-patient-dosed-in-exist-phase-2a-study-in-parkinsons-disease/)
- [Exidavnemab Phase 2a study expanded to include MSA patients (May 2025)](https://www.bioarctic.com/en/exidavnemab-phase-2a-study-expanded-to-include-msa-patients/)
- [BioArctic to initiate next cohorts after positive safety review (Jun 2025)](https://www.prnewswire.com/news-releases/bioarctic-to-initiate-next-cohorts-in-exidavnemab-phase-2a-study-after-positive-safety-review-302480954.html)
- [AbbVie terminates collaboration with BioArctic on alpha-synuclein portfolio (Apr 2022)](https://www.bioarctic.com/en/abbvie-terminates-collaboration-with-bioarctic-on-alpha-synuclein-portfolio/)
- [BioArctic outlicenses alpha-synuclein antibody portfolio to AbbVie (Dec 2018)](https://www.bioarctic.com/en/bioarctic-outlicenses-its-alpha-synuclein-antibody-portfolio-for-parkinsons-disease-to-abbvie-after-receiving-clearance/)
- [BioArctic receives Orphan Drug Designation for exidavnemab in MSA (Mar 2025)](https://www.pharmacytimes.com/view/fda-grants-orphan-drug-designation-to-exidavnemab-for-multiple-system-atrophy)
- [BioArctic receives EMA orphan designation positive opinion for MSA (2025)](https://www.bioarctic.com/en/bioarctic-receives-positive-opinion-for-orphan-medicinal-product-designation-in-the-eu-for-exidavnemab-in-multiple-system-atrophy/)
- [Exidavnemab profile | Alzforum](https://www.alzforum.org/therapeutics/exidavnemab)

### Regulatory & Market
- [AbbVie shreds alpha-synuclein pact on cusp of Phase 2 | Fierce Biotech (Apr 2022)](https://www.fiercebiotech.com/biotech/abbvie-shreds-alpha-synuclein-parkinsons-pact-cusp-phase-2-thinning-field-led-roche)
- [BioArctic Interim Report July-September 2025](https://www.bioarctic.com/en/interim-report-for-the-period-july-september-2025/)
- [BioArctic Capital Markets Day 2025](https://www.marketscreener.com/quote/stock/BARRICK-MINING-CORPORATIO-56593706/news/BioArctic-s-Capital-Markets-Day-2025-entering-a-new-era-of-growth-50127983/)
