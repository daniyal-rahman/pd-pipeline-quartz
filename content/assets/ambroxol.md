---
drug_name: "Ambroxol"
aliases: ["Mucosolvan", "SidSyn"]
target: "GBA1 / GCase (glucocerebrosidase)"
mechanism: "Pharmacological chaperone that binds misfolded GCase in the ER, facilitates proper folding and trafficking to lysosomes, restoring enzymatic activity and downstream alpha-synuclein clearance"
modality: "small molecule"
developer: "Multiple investigators / Agyany Pharma"
company_type: "academic"
publicly_traded: false
partner: ""
partner_type: ""
stage: "Phase 2"
status: "Active"
patient_population: "GBA-PD and idiopathic PD (early to moderate)"
route_of_administration: "oral"
key_biomarkers: ["GCase activity (blood/CSF)", "alpha-synuclein (CSF)", "GFAP (plasma)", "MDS-UPDRS"]
confidence_rating: "4/10"
next_catalyst: "AMBITIOUS Phase 2 readout; ASPro-PD Phase 3 interim data"
catalyst_date: "2026-2027"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Ambroxol (High-Dose)

## Summary

Ambroxol is a repurposed over-the-counter mucolytic being developed as a GCase pharmacological chaperone for Parkinson's disease, with multiple independent trials running globally. The open-label AIM-PD trial (2020) demonstrated CNS penetration and GCase target engagement; the randomized PDD trial (JAMA Neurology, 2025) confirmed safety and target engagement but failed to show cognitive benefit in Parkinson's disease dementia. The AMBITIOUS Phase 2 trial (NCT05287503) is testing ambroxol specifically in GBA-PD, and the ASPro-PD Phase 3 trial (NCT05778617) began recruiting in the UK in early 2025 with 330 participants including both GBA-PD and idiopathic PD. If AMBITIOUS or ASPro-PD demonstrate disease modification, ambroxol becomes a uniquely accessible generic therapy competing directly with [[pariceract|purpose-built GCase activators]] for GBA-PD; if both fail, the pharmacological chaperone approach to GCase loses credibility relative to allosteric activators and the field recalibrates around [[pariceract]] and substrate reduction strategies.

## Notes

### Science
- Ambroxol acts as a **pharmacological chaperone**: it binds misfolded GCase protein in the endoplasmic reticulum, assists proper folding, and facilitates trafficking to lysosomes where GCase activity is needed
- Distinct from [[pariceract|allosteric activators like pariceract]]: ambroxol rescues mutant enzyme trafficking rather than boosting activity at the catalytic site. Ambroxol also functions as a concurrent inhibitor at low pH (lysosomal conditions) while acting as a chaperone at neutral pH (ER conditions)
- GBA1 mutations are the most common genetic risk factor for PD, present in ~7-10% of PD patients. Heterozygous GBA1 carriers have 5-20x increased PD risk, with faster motor and cognitive decline
- Preclinical validation: ambroxol increases GCase activity 3.3-3.5 fold in macrophages from Gaucher disease and GBA-PD patients; crosses BBB and increases brain GCase activity in non-human primates
- Key biological rationale extends beyond GBA-PD: even in idiopathic PD, GCase activity is reduced in the substantia nigra, and restoring GCase activity reduces alpha-synuclein levels through enhanced lysosomal degradation
- Major advantage is extensive safety data from decades of OTC mucolytic use at standard doses (30-120 mg/day). PD trials use substantially higher doses (1,200-1,800 mg/day), where the safety profile is less established but has been acceptable so far
- Open scientific question: is pharmacological chaperoning sufficient to meaningfully restore GCase activity in the brain at tolerable doses, or does the concurrent inhibitor activity at lysosomal pH partially offset the benefit?

### Clinical

**AIM-PD (Phase 2, open-label)** | NCT02941822 | N=17 | PD patients with and without GBA1 mutations
- **Primary endpoint:** Safety, tolerability, CSF penetration → Safe and well tolerated; CSF ambroxol concentration confirmed BBB penetration
- **Key secondary:** GCase protein levels increased in blood; CSF alpha-synuclein levels increased (consistent with enhanced lysosomal recycling); 6.8-point MDS-UPDRS improvement
- **Status:** Completed (results published JAMA Neurology, Jan 2020)
- **Interpretation:** Proof-of-concept for CNS penetration and target engagement. Open-label, small N, and uncontrolled — clinical improvement signal cannot be causally attributed. But it provided the rationale for all subsequent controlled trials.

**PDD Trial (Phase 2, RCT)** | NCT02914366 | N=55 | Parkinson's disease dementia (mild-moderate)
- **Primary endpoint:** ADAS-Cog13 and CGIC at 52 weeks → **No significant difference** between ambroxol and placebo on cognition
- **Key secondary:** GCase activity significantly higher in ambroxol group vs. placebo at week 26 (12.45 vs. 8.50 nmol/h/mg; p=0.05), confirming target engagement
- **Exploratory:** Neuropsychiatric Inventory (NPI) scores worsened in placebo, remained stable in ambroxol group. GFAP (neurodegeneration marker) increased in placebo but remained stable in high-dose ambroxol. GBA1 variant carriers showed trends toward cognitive and neuropsychiatric improvement (N too small for significance)
- **Status:** Completed (results published JAMA Neurology, 2025)
- **Interpretation:** Target engagement confirmed but clinical efficacy unproven. The PDD population may have been too advanced for disease modification — neurodegeneration already extensive. GFAP stabilization is intriguing but exploratory. Underpowered (N=55) with high dropout.

**AMBITIOUS (Phase 2, RCT)** | NCT05287503 | N=~315 | GBA-associated PD (multiple GBA1 mutation severities)
- **Primary endpoint:** Change in MoCA score and frequency of MCI/dementia at 52 weeks
- **Key secondary:** Motor progression (MDS-UPDRS), biomarkers, quality of life
- **Status:** Active, recruiting. 315 patients enrolled including 186 idiopathic PD, 39 severe GBA-PD, 24 mild GBA-PD, 56 risk GBA-PD
- **Interpretation:** Largest ambroxol trial to date. Includes both GBA-PD and idiopathic PD comparator arm. Cognitive endpoint is rational given accelerated cognitive decline in GBA-PD. Readout expected 2026-2027.

**ASPro-PD (Phase 3)** | NCT05778617 | N=330 | Early PD (diagnosed <7 years), half GBA1 carriers
- **Primary endpoint:** Slowing of disease progression (composite including motor and quality of life measures) over 2 years, followed by 6-month open-label extension
- **Status:** Active; first site opened February 2025; 15 UK sites planned; recruitment through ~2027
- **Interpretation:** The definitive trial. Charity-funded (Cure Parkinson's, Parkinson's UK, Van Andel Institute), led by Prof. Anthony Schapira at UCL. Including both GBA1+ and GBA1- patients tests the broader hypothesis that GCase enhancement benefits all PD. Two-year treatment duration is appropriate for disease modification. Readout not expected before 2028-2029.

**GREAT Trial (Phase 2, RCT)** | NCT TBD | N=80 | Early PD with GBA mutations (Groningen, Netherlands)
- **Primary endpoint:** Change in MDS-UPDRS Part III (off-state) at 60 weeks (48-week treatment + 12-week washout)
- **Dose:** Ambroxol 1,800 mg/day (higher than AMBITIOUS 1,200 mg/day)
- **Status:** Active; single-center at University Medical Center Groningen; expected completion 2025
- **Interpretation:** Washout design specifically tests whether any motor benefit persists after drug withdrawal — critical for distinguishing symptomatic vs. disease-modifying effects. Higher dose may be informative if AMBITIOUS shows dose-response.

**Agyany Pharma Trial** | NCT06193421 | N=TBD | GBA1-related PD (newly diagnosed)
- **Primary endpoint:** TBD — high-dose ambroxol in early GBA1-PD
- **Status:** Active
- **Interpretation:** Agyany positions ambroxol as "SidSyn" for GBA1-associated PD (Sidransky Syndrome), drawing on Gaucher disease experience. May pursue regulatory pathway as repurposed generic.

### Financial
- **No traditional pharma deal structure** — ambroxol is an off-patent generic mucolytic, which makes it unpatentable in its current form. This is both the asset's greatest advantage (cheap, accessible, proven safety) and greatest commercial limitation (no proprietary protection)
- **ASPro-PD trial cost: GBP 5.5M** (~$7M), funded by Cure Parkinson's (GBP 2.2M), Parkinson's UK, Van Andel Institute, and John Black Charitable Foundation
- **Agyany Pharma** appears to be pursuing a proprietary strategy around high-dose ambroxol formulations and the "SidSyn" brand for GBA1-PD, potentially creating IP around formulation/indication rather than the molecule itself
- **Commercial paradox:** if ambroxol works, it could be prescribed off-label for pennies — but regulatory approval as a PD therapy would require someone to fund Phase 3 and submit an NDA. The charity-funded model (ASPro-PD) solves this but limits commercial upside
- **Cost comparison:** ASPro-PD's GBP 5.5M total trial cost is orders of magnitude cheaper than industry-run Phase 3 trials ($200-400M+), reflecting the repurposed drug advantage
- **If successful:** creates a pricing paradox — an approved PD therapy costing a fraction of biologics ([[prasinezumab]], [[aro-snca|ARO-SNCA]]) or gene therapies. Disrupts high-COGS modalities but may not attract pharma investment precisely because margins are thin

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "GCase") AND file.name != "ambroxol"
SORT stage DESC
```

- [[pariceract]] (BIAL) is the primary competitor — a purpose-built allosteric GCase activator rather than a repurposed chaperone. Pariceract binds a distinct allosteric site and does not have the concurrent inhibitor liability at lysosomal pH. If pariceract succeeds in Phase 2, it likely supersedes ambroxol for pharma investment regardless of ambroxol's own data
- Venglustat (Sanofi) pursued substrate reduction inhibition (blocking glucosylceramide synthesis) rather than enzyme enhancement — **Phase 3 terminated** due to lack of efficacy (MOVES-PD), which removes one competitive approach but also raises questions about the GBA pathway broadly
- Ambroxol's key competitive advantage is **accessibility**: off-patent, oral, decades of safety data, and negligible COGS. If disease modification is modest, this becomes the advantage — a cheap daily pill beats an expensive biologic for health systems
- If AMBITIOUS and ASPro-PD both fail, the pharmacological chaperone approach to GCase is likely dead, and capital shifts to [[pariceract|allosteric activators]] or away from GCase entirely toward other genetic PD targets ([[biib122|LRRK2 inhibitors]])
- The inclusion of idiopathic PD patients in ASPro-PD is strategically important: if GCase enhancement benefits non-GBA-PD, the addressable market expands from ~7-10% of PD to all PD — a transformative finding

## Analysis

Ambroxol occupies a unique position in the PD pipeline: a generic, off-patent molecule with demonstrated CNS penetration and GCase target engagement, being advanced primarily by academic investigators and charitable organizations rather than pharma. The clinical evidence so far is mixed — target engagement is consistent across trials, but clinical efficacy remains unproven. The PDD trial's cognitive failure is concerning but may reflect patient selection (too advanced) rather than mechanism failure. The GFAP stabilization signal and neuropsychiatric trends are encouraging but exploratory.

**Analytical estimate — Probability of at least one trial showing disease modification: 20-25%.** This is our assessment, not from a published source. The reasoning:
- Base rate: GCase-targeting therapies in PD have 0/1 Phase 3 completions (venglustat failed, but via substrate reduction, a different mechanism) — limited base rate data, starting at ~15%
- Adjustments upward: confirmed CNS penetration and target engagement across multiple trials (+10%), strong genetic validation for GBA1 pathway (+10%), extensive safety record enabling longer trials (+5%), multiple parallel trials increasing chance of at least one success (+5%)
- Adjustments downward: PDD trial showed no clinical efficacy (-10%), pharmacological chaperone has concurrent inhibitor liability at lysosomal pH (-5%), generic molecule means less rigorous dose optimization than purpose-built drugs (-5%), charity-funded trials may have less rigorous site management (-5%)
- Net: ~20-25%

**Signal analysis:**
- The charity-funding model tells us something important: no pharma company has licensed ambroxol for PD despite 6+ years of clinical data. This could reflect the commercial unattractiveness of a generic molecule, or it could reflect pharma's assessment that the data is insufficiently compelling. Probably both.
- Agyany Pharma's entry suggests at least one commercial entity sees an opportunity, likely through formulation IP and the "SidSyn" branding for GBA1-PD as a defined genetic indication.
- Professor Schapira's sustained commitment (AIM-PD through ASPro-PD, spanning nearly a decade) reflects genuine academic conviction in the mechanism. The Cure Parkinson's community has invested heavily in this program — there is significant patient advocacy momentum.
- The key decision tree: if AMBITIOUS shows cognitive protection in GBA-PD (2026-2027), ASPro-PD becomes the pivotal confirmation trial and ambroxol enters a regulatory pathway. If AMBITIOUS fails but ASPro-PD's 2-year motor endpoint shows benefit (2028-2029), the cognitive hypothesis is wrong but motor disease modification may still hold. If both fail, the chaperone approach is likely abandoned and the GCase field consolidates around [[pariceract]] or pivots to [[biib122|LRRK2]] and other genetic targets.

## References

### Clinical Trials
- [AIM-PD Phase 2](https://clinicaltrials.gov/ct2/show/NCT02941822) — NCT02941822
- [PDD Trial Phase 2](https://clinicaltrials.gov/ct2/show/NCT02914366) — NCT02914366
- [AMBITIOUS Phase 2](https://clinicaltrials.gov/ct2/show/NCT05287503) — NCT05287503
- [ASPro-PD Phase 3](https://clinicaltrials.gov/ct2/show/NCT05778617) — NCT05778617
- [Agyany High-Dose Ambroxol](https://clinicaltrials.gov/ct2/show/NCT06193421) — NCT06193421

### Key Publications
- [Ambroxol for the Treatment of Patients With PD With and Without GBA Mutations | JAMA Neurology (Jan 2020)](https://jamanetwork.com/journals/jamaneurology/fullarticle/2758317)
- [Ambroxol as a Treatment for Parkinson Disease Dementia: A Randomized Clinical Trial | JAMA Neurology (2025)](https://pubmed.ncbi.nlm.nih.gov/40587145/)
- [AMBITIOUS study protocol | BMJ Open (Nov 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10679992/)
- [GREAT trial protocol | BMC Neurology (2024)](https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-024-03629-9)
- [Ambroxol as a pharmacological chaperone for mutant glucocerebrosidase | Human Molecular Genetics (2012)](https://pubmed.ncbi.nlm.nih.gov/23158495/)
- [Ambroxol effects in GCase and alpha-synuclein transgenic mice | Annals of Neurology (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5132106/)
- [Oral ambroxol increases brain GCase activity in a nonhuman primate | Synapse (2017)](https://pubmed.ncbi.nlm.nih.gov/28295625/)

### Press Releases & Filings
- [ASPro-PD trial is now underway | Cure Parkinson's (Apr 2025)](https://cureparkinsons.org.uk/2025/04/the-aspro-pd-trial-is-now-underway/)
- [Phase 3 trial of ambroxol is underway | Parkinson's UK (2025)](https://www.parkinsons.org.uk/news/2025/phase-3-trial-ambroxol-underway)
- [Phase 3 clinical trial of ambroxol confirmed | Cure Parkinson's (Jan 2023)](https://cureparkinsons.org.uk/2023/01/phase-3-trial-ambroxol-in-parkinsons/)
- [Parkinson's UK to co-fund Phase 3 with Cure Parkinson's | Parkinson's UK](https://www.parkinsons.org.uk/news/parkinsons-uk-co-fund-phase-3-stage-clinical-trial-cure-parkinsons)
- [Ambroxol shows target engagement but no cognitive benefit in PDD | Practical Neurology (2025)](https://practicalneurology.com/news/ambroxol-shows-target-engagement-but-no-cognitive-benefit-in-individuals-with-parkinson-disease-dementia/2475884/)
- [Agyany Pharma](https://www.agyanypharma.com/)

### Regulatory & Market
- [Ambroxol: A potential therapeutics against neurodegeneration | ScienceDirect (2023)](https://www.sciencedirect.com/science/article/pii/S2772632023000223)
- [Could ambroxol help slow cognitive change in PD? | Cure Parkinson's (Jul 2025)](https://cureparkinsons.org.uk/2025/07/could-ambroxol-help-to-slow-cognitive-change-in-people-with-parkinsons/)
- [2026: reflecting on the last year's research progress | Cure Parkinson's (Jan 2026)](https://cureparkinsons.org.uk/2026/01/2026-research-progress/)
