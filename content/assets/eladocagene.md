---
drug_name: "Eladocagene exuparvovec"
aliases: ["PTC-AADC", "Upstaza", "Kebilidi", "VY-AADC01", "NBIb-1817", "AAV2-hAADC"]
target: "AADC (aromatic L-amino acid decarboxylase) enzyme restoration in putamen"
mechanism: "AAV2-delivered AADC gene therapy to putaminal neurons, restoring enzymatic conversion of levodopa to dopamine"
modality: "AAV gene therapy"
developer: "PTC Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "PTCT"
partner: ""
partner_type: ""
stage: "Approved (AADC deficiency); Phase 1b completed (PD — terminated)"
status: "Active (AADC deficiency); Discontinued (PD)"
patient_population: "AADC deficiency (approved); moderately advanced PD with motor fluctuations (historical PD trials)"
route_of_administration: "intracranial (bilateral MRI-guided stereotactic infusion to putamen)"
key_biomarkers: ["18F-DOPA PET (putaminal AADC activity)", "homovanillic acid (CSF dopamine metabolite)", "UPDRS Part 3"]
confidence_rating: "3/10"
next_catalyst: "Potential PD indication expansion decision by PTC Therapeutics"
catalyst_date: "Uncertain — no announced PD program"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Eladocagene exuparvovec

## Summary

Eladocagene exuparvovec is an AAV2 gene therapy delivering the human AADC gene directly to the putamen, approved for AADC deficiency (EU 2022 as Upstaza; US Nov 2024 as Kebilidi) but with a complicated PD development history. PTC Therapeutics (biotech, PTCT) acquired the AADC deficiency program from Agilis Biotherapeutics, while the PD-specific program (VY-AADC01/NBIb-1817) was developed separately by Voyager Therapeutics under a Neurocrine Biosciences partnership. The PD program completed Phase 1b (PD-1101) with encouraging 3-year safety data and 21-30% medication reduction, but the Phase 2 RESTORE-1 trial was placed on FDA clinical hold in December 2020 due to MRI abnormalities, and Neurocrine terminated the PD portion of the collaboration in August 2021. No company is currently advancing AAV2-AADC gene therapy for PD. If PTC Therapeutics were to leverage its Kebilidi manufacturing platform and AADC deficiency approval to pursue a PD indication expansion, it would re-enter a space now occupied by [[aav-gad|AAV-GAD]] (Phase 3) and [[ab-1005|AB-1005]] (Phase 2). If the PD indication remains dormant, the AADC gene therapy concept for PD becomes an academic footnote -- scientifically validated but commercially orphaned.

## Notes

### Science
- Delivers the human DDC gene (encoding aromatic L-amino acid decarboxylase) via AAV2 vector directly into the putamen bilaterally using MRI-guided stereotactic neurosurgery with convection-enhanced delivery (CED)
- AADC is the enzyme that converts L-DOPA (levodopa) to dopamine. In advanced PD, progressive loss of dopaminergic neurons depletes putaminal AADC, reducing the efficiency of oral levodopa therapy. Gene therapy restores local AADC expression, allowing transduced cells to convert exogenous levodopa to dopamine more efficiently
- Mechanism is fundamentally **symptomatic** -- it does not address underlying neurodegeneration but rather optimizes the dopaminergic response to levodopa in patients whose disease has progressed beyond adequate pharmacological control
- AAV2 serotype has natural tropism for neurons and limited spread from injection site, which provides targeted transduction of putaminal neurons but requires precise surgical delivery with adequate volume coverage
- 18F-DOPA PET imaging directly measures AADC enzymatic activity in the putamen, providing an objective pharmacodynamic biomarker: Phase 1b data showed 56-79% increases in AADC activity at higher doses, persisting over 4 years
- Key distinction vs. [[aav-gad|AAV-GAD]]: AADC gene therapy enhances levodopa response by restoring dopamine synthesis capacity, while AAV-GAD modulates basal ganglia circuitry independent of dopamine. AADC approach requires patients to remain on levodopa; AAV-GAD provides benefit regardless of dopaminergic medication
- Key distinction vs. [[ab-1005|AB-1005 (GDNF)]]: AADC is enzyme replacement (symptomatic improvement), while GDNF aims to rescue and regenerate dopaminergic neurons (disease modification). Different therapeutic goals despite both being intracranial AAV gene therapies
- The AADC deficiency and PD applications share the same vector, gene, and delivery target (putamen) but differ in patient biology: AADC deficiency is a monogenic disorder with complete enzyme absence, while PD involves progressive neuronal loss with residual but declining AADC levels
- Open questions: (1) Can putaminal AADC restoration provide clinically meaningful benefit when the downstream dopamine receptor apparatus is intact (PD) vs. absent enzyme (AADC deficiency)? (2) Does the MRI abnormality safety signal from RESTORE-1 represent a dose-dependent or procedure-dependent risk? (3) Would improved CED techniques and optimized dose selection overcome the issues that halted the PD program?

### Clinical

**PD-1101 (Phase 1b, Voyager)** | NCT01973543 | N=15 | Moderately advanced PD with motor fluctuations
- **Primary endpoint:** Safety/tolerability of bilateral MRI-guided putaminal VY-AADC01 infusion at three ascending doses (7.5x10^11, 1.5x10^12, 4.7x10^12 vg)
- **Key secondary:** 18F-DOPA PET: 13%/56%/79% increase in AADC activity across cohorts 1/2/3; UPDRS Part 3 OFF: stable or improved; medication requirements reduced 21-30% in cohorts 2-3 at 36 months; 14-32% increase in ON time without troublesome dyskinesia; 40-60% decrease in ON time with troublesome dyskinesia
- **Safety:** No serious adverse events attributed to VY-AADC01 over 3 years; well tolerated with acceptable surgical procedure risk
- **Status:** Completed (2013-2020)
- **Interpretation:** Proof-of-concept demonstrating that AAV2-AADC can durably increase putaminal enzyme activity and meaningfully improve motor fluctuations after a single administration. The dose-response relationship on PET and clinical measures supported dose selection for Phase 2. Published in Neurology (2021).

**PD-1102 (Phase 1b, Voyager)** | NCT03065192 | N=ongoing at termination | Moderately advanced PD
- **Primary endpoint:** Safety of higher-volume putaminal infusions
- **Status:** Terminated (2021, following Neurocrine partnership termination)
- **Interpretation:** Companion study to PD-1101 exploring whether larger infusion volumes could increase putaminal coverage beyond the 21-42% achieved in PD-1101

**RESTORE-1 (Phase 2, Neurocrine/Voyager)** | NCT03562494 | N=42 planned | Advanced PD with poor medication response
- **Primary endpoint:** Patient-reported motor fluctuations at 12 months; viral coverage of putamen; AADC enzyme activity change; safety
- **Safety event:** FDA clinical hold December 2020 after DSMB requested dosing pause due to MRI abnormalities in participants
- **Status:** Terminated (Neurocrine terminated PD collaboration August 2021)
- **Interpretation:** The MRI abnormality signal and subsequent clinical hold are the proximate cause of program termination. Whether the abnormalities were clinically significant, dose-related, or procedure-related has not been fully elucidated in public disclosures. Neurocrine cited "portfolio review and prioritization" rather than safety as the termination rationale, but the timing following the hold makes safety concerns the likely primary driver.

**AADC Deficiency Trials (PTC Therapeutics)** | NCT01395641 (Phase 1/2) and NCT02926066 (Phase 2b) | N=26+ | Children/adults with AADC deficiency
- **Primary endpoint:** Motor milestone achievement at 48 weeks → Significant improvements; 44% achieved head control and 20% sat unassisted at 12 months; 64%/50%/18% head control/sitting/standing at 24 months
- **Key secondary:** Sustained motor and cognitive improvements over 5+ years; 18F-DOPA PET confirmed dopamine production; first patient dosed 2010
- **Safety:** Most common AEs: dyskinesia (77%), pyrexia (38%), hypotension (31%), anemia (31%), procedural complications (15%)
- **Status:** Completed; supported EU (2022) and US (2024) approvals
- **Interpretation:** Demonstrates that AAV2-AADC gene therapy to the putamen produces durable, clinically meaningful benefit in a population with complete AADC absence. The AADC deficiency success validates the vector, gene, surgical delivery, and manufacturing platform -- but the extrapolation to PD (residual AADC, different pathology) is uncertain.

### Financial
- **PTC Therapeutics (PTCT):** Market cap ~$5.7-6.1B; 2025 revenue ~$823M (product + royalty); cash ~$1.94B as of December 2025
- **Kebilidi pricing:** Ultra-rare disease gene therapy pricing (estimated $1-3M per patient based on comparable CNS gene therapies); peak revenue estimate ~$266M by 2026 (AADC deficiency indication only)
- **Japan launch:** Pricing discussions concluded Q1 2026 with commercial launch shortly thereafter
- **VY-AADC PD program:** No ongoing commercial investment in PD indication. Neurocrine's $165M collaboration with Voyager terminated in 2021; rights situation for PD-specific development is unclear
- **PTC pipeline priorities:** Sephience (PKU), votoplam/PTC518 (Huntington's disease Phase 3 planned H1 2026), vatiquinone (Friedreich's ataxia). PD is not in PTC's stated pipeline
- **Market context:** If someone were to revive AAV2-AADC for PD, the addressable population is moderately advanced PD patients with motor fluctuations -- roughly 500K-1M patients in the US, but surgical delivery limits realistic penetration to <5% of that population
- **Historical deal:** Neurocrine-Voyager deal was $165M total ($115M upfront, $50M equity) in 2019 for VY-AADC + VY-FXN01. The PD portion was terminated ~2 years later, representing a significant write-off for Neurocrine

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(modality, "AAV gene therapy") AND file.name != "eladocagene"
SORT stage DESC
```

- **[[aav-gad|AAV-GAD]] (MeiraGTx)** is now the lead intracranial gene therapy for PD at Phase 3, with $430M Hologen partnership funding. AAV-GAD targets STN circuitry (dopamine-independent) while AADC gene therapy targets putaminal dopamine synthesis (dopamine-dependent). AAV-GAD's Phase 3 advancement with RMAT designation makes it the de facto standard-bearer for PD gene therapy
- **[[ab-1005|AB-1005]] (AskBio/Bayer)** is the other active PD gene therapy at Phase 2, delivering GDNF for neuroprotection rather than enzyme replacement. Different therapeutic goal (disease modification vs. symptomatic improvement)
- The VY-AADC termination casts a shadow over the AADC gene therapy approach in PD specifically -- the MRI abnormality safety signal is unresolved and any revival would need to address this directly with FDA
- **Cell therapy competitors** ([[bemdaneprocel]], [[ted-a9|TED-A9]]) also require neurosurgery but aim for dopaminergic neuron replacement rather than enzyme supplementation -- potentially more durable and disease-modifying
- The AADC deficiency approval validates the manufacturing platform and surgical delivery technique, which could lower the bar for a PD indication expansion if a sponsor were willing to bear the clinical risk
- Voyager Therapeutics has pivoted to BBB-crossing AAV capsids (anti-TfR technology) and GBA1 gene therapy partnerships -- they are unlikely to revisit VY-AADC for PD

## Analysis

Eladocagene exuparvovec occupies a paradoxical position: it is the most clinically validated AAV2 gene therapy ever delivered to the human putamen (26+ AADC deficiency patients treated since 2010, regulatory approvals in EU and US) and the Phase 1b PD data (PD-1101) showed genuinely encouraging 3-year safety and efficacy signals. Yet no company is advancing it for PD. The RESTORE-1 clinical hold and Neurocrine's termination in 2021 effectively killed the PD program, and PTC Therapeutics has shown no public interest in expanding Kebilidi's indication to PD.

**Analytical estimate -- Probability of PD indication revival within 5 years: 10-15%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Programs terminated after FDA clinical holds rarely return (~5-10% resurrection rate)
- Adjustments upward: Approved AADC deficiency product validates vector/manufacturing/delivery (+5%), PTC has $1.94B cash and established neurosurgical infrastructure (+3%), unmet medical need in advanced PD remains high (+3%), 3-year PD-1101 data was genuinely positive (+3%)
- Adjustments downward: MRI abnormality safety signal unresolved (-5%), PTC has other pipeline priorities (HD, FA, PKU) (-5%), competing gene therapies ([[aav-gad]], [[ab-1005]]) now more advanced (-5%), intracranial delivery faces increasing competition from IV-deliverable approaches (-3%)
- Net: ~10-15%

**Signal analysis:**
- PTC's silence on PD is itself a signal. With Kebilidi approved and manufacturing in place, a PD indication expansion would be a logical line extension if they believed the PD-1101 data warranted investment. Their choice not to pursue this suggests either: (a) the RESTORE-1 safety data was more concerning than publicly disclosed, (b) the PD market for intracranial gene therapy is too small to justify the clinical investment, or (c) PTC's strategic focus on rare genetic diseases (AADC deficiency, PKU, HD, FA) deliberately excludes common neurological diseases like PD.
- Neurocrine's termination framing ("portfolio review") rather than explicit safety concerns is standard pharma language for burying a program without admitting the data looked bad. The timing -- months after an FDA clinical hold for MRI abnormalities -- speaks louder than the press release.
- The broader PD gene therapy landscape has moved on: [[aav-gad]] has a Phase 3 trial (exPDite-2) with $430M in committed funding, and [[ab-1005]] is in Phase 2 with Bayer backing. Any revival of AADC gene therapy for PD would need to address the safety signal, design a new trial, and compete for patients and neurosurgical sites against these established programs.
- Decision tree: If PTC announces a PD indication study, this becomes immediately interesting -- the approved manufacturing platform and clinical infrastructure reduce execution risk significantly vs. a de novo program. If PTC continues to ignore PD, the AADC gene therapy concept for Parkinson's remains a validated but commercially orphaned approach, leaving [[aav-gad]] and [[ab-1005]] as the only active intracranial gene therapies for PD.

## References

### Clinical Trials
- [PD-1101 Phase 1b](https://clinicaltrials.gov/ct2/show/NCT01973543) -- NCT01973543
- [PD-1102 Phase 1b](https://clinicaltrials.gov/ct2/show/NCT03065192) -- NCT03065192
- [RESTORE-1 Phase 2](https://clinicaltrials.gov/ct2/show/NCT03562494) -- NCT03562494
- [AADC-010 Phase 1/2 (AADC deficiency)](https://clinicaltrials.gov/ct2/show/NCT01395641) -- NCT01395641
- [AADC-011 Phase 2b (AADC deficiency)](https://clinicaltrials.gov/ct2/show/NCT02926066) -- NCT02926066

### Key Publications
- [Safety of AADC Gene Therapy for Moderately Advanced PD: 3-Year PD-1101 Outcomes | Neurology (2021)](https://www.neurology.org/doi/10.1212/WNL.0000000000012952)
- [MRI-guided Phase 1 Trial of Putaminal AADC Gene Therapy for PD | Molecular Therapy (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6593762/)
- [Long-term Efficacy and Safety of Eladocagene Exuparvovec in AADC Deficiency | Molecular Therapy (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8822132/)
- [Gene Therapy in the Putamen for AADC Deficiency and PD | EMBO Mol Med (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8422070/)
- [Eladocagene Exuparvovec: First Approval | Drugs (2022)](https://pubmed.ncbi.nlm.nih.gov/36103022/)

### Press Releases & Filings
- [PTC Therapeutics FDA Approval of AADC Deficiency Gene Therapy (Nov 2024)](https://ir.ptcbio.com/news-releases/news-release-details/ptc-therapeutics-announces-fda-approval-aadc-deficiency-gene)
- [Voyager Update on NBIb-1817 (VY-AADC) Program (Feb 2021)](https://ir.voyagertherapeutics.com/news-releases/news-release-details/voyager-therapeutics-provides-update-nbib-1817-vy-aadc-gene-0/)
- [Neurocrine Exits $165M PD Pact with Voyager | Fierce Biotech (2021)](https://www.fiercebiotech.com/biotech/neurocrine-exits-165m-parkinson-s-pact-voyager-after-fda-hold)
- [VY-AADC PD Gene Therapy Program Terminated | NeurologyLive (2021)](https://www.neurologylive.com/view/vy-aadc-parkinson-disease-gene-therapy-program-terminated)
- [PTC Therapeutics J.P. Morgan 2025 Pipeline Update (Jan 2025)](https://ir.ptcbio.com/news-releases/news-release-details/ptc-therapeutics-provides-update-commercial-performance-and-rd)

### Regulatory & Market
- [Upstaza EU Marketing Authorization (July 2022)](https://www.neurologylive.com/view/european-commission-passes-eladocagene-exuparvovec-first-approved-treatment-for-aadc-deficiency)
- [Kebilidi FDA Approval -- First Brain-Delivered Gene Therapy | Pharmaphorum (Nov 2024)](https://pharmaphorum.com/news/ptc-gets-fda-okay-first-brain-delivered-gene-therapy)
- [VY-AADC Profile | Alzforum](https://www.alzforum.org/therapeutics/vy-aadc)
