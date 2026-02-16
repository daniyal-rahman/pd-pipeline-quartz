---
drug_name: "Selnoflast"
aliases: ["RO7486967", "RG-6418", "IZD-334", "Somalix"]
target: "NLRP3 inflammasome"
mechanism: "Orally available, peripherally-restricted small molecule that blocks NLRP3 inflammasome assembly, preventing caspase-1 activation and downstream IL-1beta/IL-18 release"
modality: "small molecule"
developer: "Roche"
company_type: "big pharma"
publicly_traded: true
ticker: "ROG"
stage: "Phase 1b"
status: "Active"
patient_population: "Early-stage Parkinson's disease"
route_of_administration: "oral"
key_biomarkers: ["TSPO PET ([18F]-DPA-714)", "IL-1beta", "IL-18"]
confidence_rating: "3/10"
next_catalyst: "Phase 1b PD results disclosure"
catalyst_date: "2025-2026"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/roche]]"
---

# Selnoflast

## Summary

Selnoflast is Roche's (big pharma, ROG) peripherally-restricted NLRP3 inflammasome inhibitor, acquired through the Inflazome purchase in 2020 for ~EUR 380M. The Phase 1b PD trial (NCT05924243) enrolled 60 of 72 planned patients and completed in July 2024, but results remain undisclosed as of early 2026 -- an unusually long silence that may signal underwhelming data. The critical open question is whether a peripheral NLRP3 inhibitor that does not cross the blood-brain barrier can meaningfully reduce neuroinflammation in PD, especially when brain-penetrant competitors like NT-0796 (NodThera) and VTX3232 (Ventyx) have already reported positive CSF biomarker data. If Phase 1b shows TSPO PET signal reduction, Roche likely advances to a larger efficacy trial; if it does not, the peripheral-only NLRP3 approach for neurodegeneration is likely abandoned in favor of CNS-penetrant alternatives.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Inflazome (acquired) |
| Deal Date | September 2020 |
| Upfront | EUR 380M |
| Total (Biobucks) | EUR 380M + undisclosed milestones |
| Deal Type | Acquisition |

## Notes

### Science
- NLRP3 inflammasome is a cytoplasmic multiprotein complex (NLRP3 sensor + ASC adaptor + caspase-1) that, when activated, cleaves pro-IL-1beta and pro-IL-18 into their active inflammatory forms and can trigger pyroptotic cell death
- In PD, aggregated alpha-synuclein activates microglial NLRP3, driving a chronic neuroinflammatory cycle: alpha-synuclein aggregates activate microglia, which release IL-1beta and IL-18, which in turn promote further alpha-synuclein aggregation and neuronal death
- Selnoflast is a sulfonylurea-based compound that bears a negative charge at physiological pH, which **limits BBB penetration** -- it acts peripherally rather than centrally. Roche's rationale is that peripheral immune activation (circulating monocytes, systemic cytokines) contributes to PD neuroinflammation and can be targeted without CNS entry
- Key scientific concern: a 2024 publication (Tate et al., npj Parkinson's Disease) found **no genetic evidence** supporting NLRP3 inflammasome involvement in PD pathogenesis -- no GWAS associations, no rare variant signals, no pathway polygenic risk score association. The target rationale rests entirely on functional/pathological data rather than Mendelian or GWAS validation
- Roche also acquired inzomelid (emlenoflast) from Inflazome, which is brain-penetrant, but has not advanced it into PD trials -- suggesting Roche may have deprioritized central NLRP3 inhibition or encountered development challenges
- The NLRP3 inflammasome thesis overlaps with but is distinct from broader neuroinflammation approaches ([[prasinezumab]] targets extracellular alpha-synuclein; NLRP3 inhibition targets the downstream inflammatory cascade triggered by alpha-synuclein)

### Clinical

**Phase 1 (Healthy Volunteers / CAPS)** | NCT not disclosed | N=64 | Healthy adults + CAPS patients
- **Primary endpoint:** Safety/tolerability, PK --> Clean safety profile
- **Key secondary:** Single and multiple ascending dose PK characterization
- **Status:** Completed (September 2019 - February 2020, pre-acquisition)
- **Interpretation:** Established basic human safety and PK; conducted by Inflazome prior to Roche acquisition

**Phase 1b (Ulcerative Colitis)** | NCT not disclosed | N=19 | Moderate-to-severe active UC
- **Primary endpoint:** Safety/tolerability --> Well tolerated at 450 mg QD x 7 days
- **Key secondary:** Plasma and tissue NLRP3 inhibition confirmed; however, no meaningful changes in colon histology or inflammation markers
- **Status:** Completed (November 2021)
- **Interpretation:** Target engagement confirmed but no efficacy signal in UC. Published: Klughammer et al., 2023. Demonstrated that peripheral NLRP3 inhibition alone may be insufficient for tissue-level inflammation

**Phase 1b (Parkinson's Disease)** | NCT05924243 | N=60 (of 72 planned) | Early-stage PD
- **Primary endpoint:** Safety (adverse events, suicidality assessment)
- **Key secondary:** PK in plasma; neuroinflammation via [18F]-DPA-714 TSPO PET imaging pre/post treatment
- **Design:** Randomized, double-blind, placebo-controlled; 200 mg BID x 28 days; 2:1 randomization; 20 centers across Europe and U.S.
- **Status:** Completed July 2024; results unpublished as of February 2026
- **Interpretation:** The TSPO PET endpoint is the critical readout -- it will show whether peripheral NLRP3 inhibition can reduce brain microglial activation. The 18-month silence post-completion is concerning. The study enrolled 60 of 72 planned participants, a modest shortfall

**Phase 1b (Coronary Artery Disease)** | NCT TBD | Active
- Additional indication being explored by Roche

**Phase 1b (Asthma)** | NCT TBD | Active
- Additional indication being explored by Roche

### Financial
- **Inflazome acquisition:** EUR 380M upfront in September 2020, plus undisclosed milestone payments. Roche obtained full rights to selnoflast, inzomelid, and the preclinical NLRP3 portfolio
- **Prior Inflazome fundraising:** EUR 55M from Forbion, Longitude Capital, Fountain Healthcare Partners, and Novartis Venture Fund
- **Roche NLRP3 investment:** This was Roche's second NLRP3 acquisition after Jecure Therapeutics (2018), demonstrating sustained strategic interest in the inflammasome space
- **No peak sales estimates** publicly available for selnoflast in PD specifically; Roche has not disclosed revenue projections for this program
- **Context:** The EUR 380M acquisition was for the entire Inflazome portfolio, not selnoflast alone. The portfolio spans PD, UC, COPD, asthma, and coronary artery disease -- diversifying risk across multiple indications

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "NLRP3") AND file.name != "selnoflast"
SORT stage DESC
```

- **NT-0796 (NodThera):** Brain-penetrant NLRP3 inhibitor with Phase 1b/2a data in PD (published August 2025, Movement Disorders). Demonstrated dose-dependent reductions in CSF IL-1beta, IL-6, CCL2, CXCL1, CXCL8 over 28 days, plus reductions in sTREM2 and NfL. This is the most advanced competitor and the first to demonstrate central NLRP3 target engagement in PD patients. Brain penetrance is the key differentiator vs. selnoflast
- **VTX3232 (Ventyx Biosciences):** CNS-penetrant NLRP3 inhibitor with positive Phase 2a data (June 2025). Open-label study in 10 early PD patients showed no drug-related TEAEs, significant reductions in NLRP3-related CSF and plasma biomarkers, and clinically significant improvements on MDS-UPDRS Parts II and III (with caveat of small, open-label design). Ventyx is advancing to larger trials
- **Inzomelid / Emlenoflast (Roche, from Inflazome):** Brain-penetrant NLRP3 inhibitor from the same acquisition, completed Phase 1 in healthy volunteers. Roche has not advanced it into PD trials despite its CNS penetrance -- unclear why
- The NLRP3 PD space is crowded with at least 4 clinical-stage programs. Selnoflast's peripheral-only mechanism is a potential disadvantage vs. brain-penetrant competitors that have already shown CSF biomarker effects
- If brain-penetrant NLRP3 inhibitors (NT-0796, VTX3232) succeed in efficacy trials, selnoflast's peripheral approach may be validated as a complementary strategy or may be rendered irrelevant. If NLRP3 inhibition broadly fails in PD, the entire neuroinflammation thesis shifts toward other targets (TREM2, CD33, complement)

## Analysis

The fundamental question for selnoflast is whether peripheral NLRP3 inhibition can meaningfully impact a central neurodegenerative disease. Roche's rationale -- that circulating monocytes and systemic cytokines contribute to PD neuroinflammation -- has biological plausibility but faces a steep burden of proof. The Phase 1b PD trial's TSPO PET endpoint was well designed to test this hypothesis directly: if peripheral-only selnoflast reduces brain microglial activation on PET, it would validate the peripheral-to-central inflammatory axis. But the 18-month gap between trial completion (July 2024) and results disclosure (still pending as of February 2026) is a negative signal by industry standards.

**Analytical estimate -- Probability of advancing to Phase 2 in PD: 25-30%.** This is our assessment, not from a published source. The reasoning:
- Base rate: NLRP3 inhibitors in neurodegeneration are a novel class with no validated precedent --> starting point ~20%
- Adjustments upward: Roche committed EUR 380M+ to the inflammasome space across two acquisitions (+5%), preclinical evidence for NLRP3 in alpha-synuclein-driven neuroinflammation is robust (+5%), PET-based pharmacodynamic endpoint enables clear go/no-go decision (+5%)
- Adjustments downward: no genetic validation from GWAS/Mendelian randomization (-5%), peripheral-only mechanism when competitors are brain-penetrant (-10%), delayed results disclosure (-5%), UC Phase 1b showed target engagement but no efficacy (-5%), 12 of 72 patients not enrolled (-2%)
- Net: ~25-30%

**Signal analysis:**
- Roche's silence on the Phase 1b PD data, while continuing selnoflast development in asthma and coronary artery disease, may indicate that the PD indication specifically underperformed. Companies typically disclose positive PD data promptly given the unmet need and investor interest
- The competitive dynamics are unfavorable: NodThera (NT-0796) and Ventyx (VTX3232) have both published positive PD biomarker data from brain-penetrant NLRP3 inhibitors while selnoflast results remain withheld. If Roche's PET data showed comparable signal, there would be strong incentive to publish
- Roche's broader PD strategy centers on [[prasinezumab]] (Phase 3) as the anchor program. Selnoflast appears to be a lower-priority exploratory bet in their neuroscience portfolio. If forced to choose, Roche will allocate resources to prasinezumab
- The lack of genetic validation (no GWAS signal for NLRP3 in PD) is a concern for the entire class, not just selnoflast. However, many successful anti-inflammatory drugs target pathways without direct genetic links to disease -- the functional and pathological evidence may be sufficient if clinical biomarker data confirms the hypothesis

## References

### Clinical Trials
- [Phase 1b in Parkinson's Disease](https://clinicaltrials.gov/study/NCT05924243) -- NCT05924243

### Key Publications
- [Phase 1b Study Design in Early-Stage PD (AAN 2024 poster) | Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000203618)
- [Phase 1b selnoflast in ulcerative colitis | Klughammer et al., 2023](https://pubmed.ncbi.nlm.nih.gov/37962000/)
- [Lack of genetic evidence for NLRP3 inflammasome involvement in PD pathogenesis | npj Parkinson's Disease (2024)](https://www.nature.com/articles/s41531-024-00744-9)
- [NLRP3 Inflammasome-Mediated Neuroinflammation and Mitochondrial Impairment in PD | Neuroscience Bulletin (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10169990/)
- [Anti-Neuroinflammatory Effects of NT-0796 in PD (competitor data) | Movement Disorders (2025)](https://movementdisorders.onlinelibrary.wiley.com/doi/full/10.1002/mds.30307)
- [NLRP3 Inhibitors Update | Alzheimer's Drug Discovery Foundation (2024)](https://www.alzdiscovery.org/uploads/cognitive_vitality_media/NLRP3_Inhibitors_UPDATE_(drug_in_development).pdf)

### Press Releases & Filings
- [Inflazome Announces Acquisition by Roche (September 2020)](https://www.businesswire.com/news/home/20200920005066/en/Inflazome-Announces-Acquisition-by-Roche)
- [Roche buys Inflazome as pharma interest in targeting inflammation grows | BioPharma Dive](https://www.biopharmadive.com/news/roche-inflazome-nlrp3-inflammasome-drug-deal/585566/)
- [Roche pays EUR 380M for NLRP3 biotech Inflazome | Fierce Biotech](https://www.fiercebiotech.com/biotech/roche-pays-eu380m-for-nlrp3-biotech-inflazome-claiming-a-leading-position-hot-field)
- [Ventyx VTX3232 Phase 2a positive topline data in early PD (June 2025)](https://ir.ventyxbio.com/news-releases/news-release-details/ventyx-biosciences-announces-positive-top-line-data-its-phase-2a)
- [Selnoflast profile | Alzforum](https://www.alzforum.org/therapeutics/selnoflast)
- [Selnoflast overview | Science of Parkinson's](https://scienceofparkinsons.com/2022/12/15/selnoflast/)

### Regulatory & Market
- [Roche Pharma Day 2025 (neuroscience strategy)](https://assets.roche.com/f/176343/x/059c686d27/20250922_pharma-day-2025_vf_online.pdf)
- [PD Drug Therapies in Clinical Trial Pipeline: 2024 Update | JPD](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307066/)
