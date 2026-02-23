---
drug_name: "Exablate Neuro"
aliases: ["MRgFUS", "ExAblate Neuro Type 2", "ExAblate Neuro 4000"]
target: "blood-brain barrier (transient opening via MRI-guided focused ultrasound)"
mechanism: "Non-invasive MRI-guided focused ultrasound system that transiently opens the BBB using low-intensity focused ultrasound with IV microbubbles, enabling localized drug delivery to targeted brain regions"
modality: "medical device"
developer: "InSightec"
company_type: "biotech"
publicly_traded: false
stage: "Phase 2"
status: "Active"
patient_population: "AD, GBM, potentially PD"
route_of_administration: "non-invasive transcranial device + IV microbubbles"
key_biomarkers: ["gadolinium contrast enhancement (BBB opening confirmation)", "amyloid PET (AD)", "MRI volumetrics"]
next_catalyst: "Lotus Neuro GBM pivotal trial data; PD GCase delivery Phase I/II readout"
catalyst_date: "2025-2026"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery]
date: 2026-02-16
company_link: "[[companies/insightec]]"
---

# Exablate Neuro

## Summary

Exablate Neuro is InSightec's MRI-guided focused ultrasound (MRgFUS) system that transiently opens the blood-brain barrier using low-intensity ultrasound and IV microbubbles -- the most clinically advanced non-invasive BBB-opening platform in existence. The NEJM 2024 aducanumab + FUS study showed ~50% amyloid reduction in targeted regions (vs. ~32% in untargeted contralateral regions), and the BT008NA Phase 1/2 GBM trial published in Lancet Oncology demonstrated a ~40% survival benefit (30 months vs. 19 months) when BBB opening was combined with temozolomide. The system holds FDA Breakthrough Device designation for neuro-oncology applications and is already FDA-approved for thermal ablation in essential tremor (2016) and tremor-dominant PD (2018). For PD specifically, Sunnybrook is running a Phase I/II trial using FUS-BBB opening to deliver glucocerebrosidase (Cerezyme) to the putamen in GBA-PD patients -- a direct test of whether FUS can enable CNS enzyme replacement therapy. InSightec spun out Lotus Neuro in December 2025 to advance therapeutic BBB-opening programs, signaling a strategic pivot from device-only to device-plus-drug development. If FUS-BBB opening proves clinically viable as a drug delivery platform, it could transform the treatment of every CNS disease limited by poor BBB penetration -- including PD, where most large-molecule therapeutics (antibodies, enzymes, gene therapies) face delivery barriers.

## Notes

### Science

- The ExAblate Neuro Type 2 system operates at 220-230 kHz using a hemispheric phased-array transducer with 1,024 ultrasound elements that converge on a focal point in the brain with real-time MRI guidance ([InSightec data sheet](https://insightec.com/files/PUB41006477-Neuro-System-Data-Sheet-Rev-2.pdf))
- Patient-specific phase corrections are computed from CT-derived skull maps to compensate for ultrasound distortion and attenuation by cranial bone, enabling precise transcranial targeting ([Karger technical review](https://karger.com/sfn/article/99/4/329/295165/Technical-Principles-and-Clinical-Workflow-of))
- Mechanism of BBB opening: low-intensity focused ultrasound interacts with IV-administered microbubbles (typically Definity/perflutren lipid microspheres) to produce **stable cavitation** -- rhythmic oscillation that generates mechanical shear forces on microvessel walls, transiently disrupting tight junctions, inducing sonoporation, and enhancing transcytosis ([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6134932/))
- BBB opening is **transient and reversible**: contrast extravasation resolves within 24 hours; no long-term neurological or physiological effects observed with repeated treatments in non-human primate studies over 20+ sessions ([PLOS ONE NHP safety study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0125911))
- The energy required for BBB opening is ~100-fold lower than for tissue ablation, meaning the same device platform (ExAblate Neuro) can perform both thermal ablation (thalamotomy for tremor) and non-thermal BBB opening (drug delivery) depending on power settings ([IEEE Pulse review](https://www.embs.org/pulse/articles/breaking-barriers-with-sound-focused-ultrasound-in-the-brain/))
- Treatment volume: the low-frequency system allows sonication within a ~4 cm diameter sphere without repositioning the helmet; each subspot has a focal depth of ~7 mm (full width at half maximum) ([ExAblate Neuro device profile, Expert Rev Med Devices 2021](https://www.tandfonline.com/doi/abs/10.1080/17434440.2021.1921572))
- Electronic steering range of +/-25 mm enables treatment volumes exceeding 30 cm^2, critical for covering tumor margins or neurodegenerative targets like the putamen ([PMC clinical review 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044032/))
- Key distinction from Carthera SonoCloud-9: Exablate is fully **non-invasive** (no implant, no surgery), but requires MRI suite access and longer procedure time; SonoCloud-9 is a surgically implanted 1 MHz device that can be activated in 4 minutes during routine infusion visits without MRI ([FUS Foundation comparison](https://www.fusfoundation.org/posts/therapeutic-ultrasound-for-recurrent-glioblastoma-a-qa-on-cartheras-comparative-clinical-trial/))
- Open scientific question: optimal microbubble parameters (size, concentration) significantly affect BBB opening duration -- standard clinical microbubbles yield 24-48 hour openings, but larger microbubbles (4-6 um) can extend opening to >5 days, raising questions about the ideal therapeutic window for different drug classes ([PMC microbubble review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6134932/))

### Clinical

**NEJM Aducanumab + FUS Study (Phase 1 proof-of-concept)** | N=3 | Mild-to-moderate AD
- **Design:** FUS-BBB opening applied to selected brain regions concurrent with six monthly aducanumab infusions; contralateral hemisphere served as within-patient control
- **Primary endpoint:** Safety/feasibility --> No serious adverse events; mild headache most common AE
- **Key result:** Amyloid-beta PET showed centiloid reductions of 48%, 49%, and 63% in FUS-targeted regions vs. untargeted contralateral regions (average ~32% reduction in SUVr overall, with centiloid reductions of 107.5, 87.6, and 158.1 points greater in FUS-targeted vs. non-targeted regions)
- **Authors:** Rezai AR, D'Haese PF, Finomore V, et al.
- **Published:** NEJM, January 4, 2024 (Vol 390, pp 55-62)
- **Status:** Completed
- **Interpretation:** First human demonstration that FUS-BBB opening meaningfully enhances anti-amyloid antibody efficacy in targeted brain regions. The ~50% additional amyloid clearance in FUS-targeted zones suggests that BBB limitation is a genuine bottleneck for antibody therapies, not just a theoretical concern. Limitation: N=3, no clinical outcome assessment. ([NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2308719))

**BT008NA GBM Trial (Phase 1/2)** | NCT TBD (ReFOCUSED Consortium) | N=34 | Newly diagnosed high-grade glioma (post-resection, post-chemoradiotherapy)
- **Design:** MB-FUS BBB opening at the beginning of each 28-day temozolomide cycle using ExAblate Neuro; multicentre, open-label, 5 sites in US and Canada
- **Primary endpoint:** Safety and feasibility --> No serious procedure- or device-related AEs
- **Key result:** Median progression-free survival ~14 months (vs. ~8 months historical control); median overall survival >30 months (vs. ~19 months control) -- a ~40% survival benefit
- **Lead investigators:** Graeme Woodworth (U Maryland), Nir Lipsman (Sunnybrook)
- **Published:** Lancet Oncology, 2025
- **Status:** Completed; pivotal trial planned via Lotus Neuro
- **Interpretation:** First demonstration of potential survival benefit from FUS-BBB opening in any indication. Temozolomide is a small molecule that already crosses the BBB to some extent -- the fact that enhanced delivery still improved outcomes suggests even partial BBB penetration is insufficient for optimal tumor drug levels. Validates the platform for larger trials. ([Lancet Oncology](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(25)00492-9/abstract))

**PD Dementia FUS-BBB Opening (Phase 1)** | N=5 | PD dementia
- **Design:** Two FUS-BBB opening sessions at 2-3 week intervals targeting parietal-occipital-temporal junction; no drug delivered (BBB opening alone)
- **Primary endpoint:** Safety/feasibility --> 8/10 treatments achieved successful BBB opening; no serious side effects
- **Key result:** Patients showed improvements on several cognitive tests, but no statistical testing, small N, no control group
- **Published:** Nature Communications, 2021
- **Status:** Completed
- **Interpretation:** Proof-of-concept that FUS-BBB opening is feasible and safe in PD patients. Cognitive improvements (if real) might reflect transient immunomodulatory effects of BBB opening itself -- preclinical data shows FUS-BBB opening can activate microglia and enhance waste clearance. Not definitive for PD but established safety profile for the Cerezyme delivery trial. ([Nature Communications](https://www.nature.com/articles/s41467-021-21022-9))

**Sunnybrook Cerezyme/GCase Delivery in PD (Phase I/II)** | NCT04370665 | N=4 (Phase I); N=15 planned (Phase I/II) | PD with GBA pathway dysfunction
- **Design:** MRgFUS-BBB opening in the putamen combined with IV imiglucerase (Cerezyme, recombinant glucocerebrosidase) every two weeks; Phase I: 4 patients, 3 doses each
- **Primary endpoint:** Safety/feasibility --> No significant adverse events in Phase I
- **Rationale:** GBA mutations are the most common genetic risk factor for PD; glucocerebrosidase deficiency leads to alpha-synuclein accumulation. Exogenous GCase cannot cross the BBB -- FUS enables targeted putaminal delivery
- **Phase I result:** Published September 2022 (Mov Disord) -- safe, feasible, first direct-to-brain therapeutic delivery in PD using FUS
- **Phase I/II:** Enrollment planned fall 2025, expected completion ~late 2025/2026
- **Status:** Active
- **Interpretation:** Directly relevant to PD thesis. If FUS can reliably deliver GCase to the putamen and reduce alpha-synuclein burden, this creates a non-genetic alternative to AAV-GBA1 gene therapy approaches like [[gba1-voyager|Voyager's VY-7523]]. The FUS approach is repeatable and dose-adjustable, unlike one-shot gene therapy. ([Sunnybrook](https://sunnybrook.ca/content/?page=focused-ultrasound-parkinsons-disease); [PubMed](https://pubmed.ncbi.nlm.nih.gov/36089809/))

**LIBERATE Liquid Biopsy Trial (Pivotal)** | N=TBD | GBM patients
- **Design:** FUS-BBB opening to release brain tumor biomarkers into blood for liquid biopsy detection
- **Status:** Enrolling at 15+ sites; Breakthrough Device designation granted
- **Interpretation:** A secondary but commercially important application -- if FUS can enable brain liquid biopsy, this creates a non-drug revenue stream for the platform and a diagnostic companion for brain cancers. ([InSightec press release](https://insightec.com/news/insightec-announces-milestone-of-first-patients-enrolled-in-the-pivotal-liberate-clinical-trial-liquid-biopsy-with-low-intensity-ultrasound-in-brain-tumors/))

**FDA-Approved Ablation Indications (not BBB opening -- thermal ablation)**
- Essential tremor thalamotomy: FDA-approved July 2016; bilateral approved subsequently (second side at 9+ months) ([FDA SSED](https://www.accessdata.fda.gov/cdrh_docs/pdf15/P150038B.pdf))
- Tremor-dominant PD thalamotomy: FDA-approved December 2018; staged bilateral approved more recently. On-medication tremor subscores improved 62% vs. 22% sham (p<0.001). Addresses ~10-20% of PD population with tremor-dominant phenotype ([NeurologyLive](https://www.neurologylive.com/view/fda-approves-exablate-neuro-treatment-tremor-dominant-parkinson-disease))
- Note: these ablation approvals use the ExAblate Neuro Type 1 (650 kHz, thermal); BBB opening uses the Type 2 (220-230 kHz, non-thermal). Same platform family, different clinical application.

### Financial

- **InSightec total funding:** ~$574M-$810M raised across 13-16 rounds (sources vary; most recent: $150M Series G in June 2024) ([Crunchbase](https://www.crunchbase.com/organization/insightec))
- **Key investors:** Koch Disruptive Technologies (led $150M Series E and subsequent rounds), Elbit Imaging (early investor, Israeli public company), York Capital Management, GE Healthcare, Exigent Capital Group ([InSightec press release](https://insightec.com/news/kdt-leads-series-e/))
- **Koch Disruptive Technologies Series E:** $150M round with KDT investing $75M for ~19.7% of outstanding shares (16.5% fully diluted), implying a post-money valuation of ~$760M at the time of that round ([PRNewswire](https://www.prnewswire.com/news-releases/insightec-investment-up-to-150-million-led-by-koch-disruptive-technologies-301019096.html))
- **Lotus Neuro spin-out (Dec 2025):** New clinical-stage biotech spun out of InSightec to advance BBB-opening therapeutic programs (GBM, diffuse midline gliomas, neurodegeneration). Funded by Nexus NeuroTech Ventures. CEO: Arjun (JJ) Desai, MD. InSightec retains device development; Lotus Neuro pursues device-plus-drug combinations ([InSightec press release](https://insightec.com/news/insightec-announces-spin-out-of-lotus-neuro-to-advance-focused-ultrasound-brain-therapies/))
- **Revenue base:** ExAblate Neuro is commercially installed at 100+ centers globally for thermal ablation (ET, PD tremor). BBB-opening applications are not yet commercialized
- **Market context:** If BBB opening becomes a standard-of-care adjunct for brain tumor chemotherapy, the addressable market expands from functional neurosurgery (~$500M) to neuro-oncology ($3-5B+) and potentially neurodegeneration ($10B+)
- **Comparison to Carthera:** SonoCloud-9 is also venture-backed (Carthera raised ~$50M), implantable design, Breakthrough Device designation for GBM. Both are pursuing GBM as lead indication. Carthera's SONOBIRD comparative trial (launched Feb 2024) is a head-to-head with standard of care in recurrent GBM ([FUS Foundation](https://www.fusfoundation.org/posts/therapeutic-ultrasound-for-recurrent-glioblastoma-a-qa-on-cartheras-comparative-clinical-trial/))

### Competitive

*No results*

- **Carthera SonoCloud-9:** Main direct competitor. Implantable (requires surgery), 1 MHz, no MRI needed during treatment, 4-minute sessions in infusion suite. Advantage: ease of repeated dosing, patient convenience. Disadvantage: requires craniotomy for implantation, fixed target location. ExAblate advantages: non-invasive, electronically steerable, can target any brain region per session. Clinical head-to-head: SonoCloud BBB opening resolves within ~1 hour vs. ~24 hours for ExAblate -- shorter window may limit drug exposure but reduces safety risk ([PMC systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11538134/))
- **NaviFUS (Taiwan):** Neuronavigation-guided portable FUS system without MRI; lower cost, mobile, but less precise targeting than MRgFUS. Being tested in GBM trials in Asia ([Ultrasound Med Biol](https://www.umbjournal.org/article/S0301-5629(19)31510-8/fulltext))
- For PD specifically, FUS-BBB opening competes with other delivery strategies: BBB-shuttled antibodies (e.g., Denali's TV platform [[dnl422|DNL422]]), intrathecal delivery ([[ly3962681|LY3962681]]), AAV gene therapy ([[gba1-voyager|VY-7523]]), and engineered AAV capsids ([[cap-003|CAP-003]])
- Key differentiator for PD: FUS is the only BBB-opening approach that is **non-invasive, repeatable, and drug-agnostic** -- it can enhance delivery of any circulating therapeutic (antibodies, enzymes, small molecules, nanoparticles) without requiring molecular engineering of the drug itself
- If the Sunnybrook GCase delivery trial succeeds, FUS-BBB opening could become a platform for delivering multiple PD therapeutics to specific brain regions, potentially enabling combination regimens (e.g., anti-synuclein antibody + GCase enzyme to putamen)

## Analysis

The Exablate Neuro platform occupies a unique strategic position in the BBB-delivery landscape because it is drug-agnostic: rather than engineering each therapeutic to cross the BBB (as with bispecific antibodies or engineered AAV capsids), FUS transiently opens the barrier to allow localized delivery of whatever drug is circulating in blood. The NEJM 2024 data showing ~50% additional amyloid clearance in FUS-targeted regions provides the clearest human evidence that BBB limitation is not just a theoretical concern for antibody therapeutics -- it is a quantifiable delivery bottleneck. The Lancet Oncology GBM survival data (30 vs. 19 months) demonstrates that even for small molecules with partial BBB penetration, enhanced delivery translates to meaningful clinical benefit.

For PD, the most directly relevant program is Sunnybrook's Cerezyme delivery trial (NCT04370665), which tests whether FUS can enable CNS enzyme replacement therapy in GBA-pathway PD. This is scientifically elegant: GBA mutations are the most common genetic risk factor for PD, glucocerebrosidase cannot cross the BBB, and recombinant GCase (Cerezyme) is already FDA-approved for Gaucher disease. If FUS can deliver therapeutic GCase levels to the putamen, it offers a repeatable, dose-adjustable alternative to one-shot AAV-GBA1 gene therapy (e.g., [[gba1-voyager|Voyager's VY-7523]]). The repeatable dosing advantage is significant: if the first dose is insufficient or needs adjustment, FUS allows re-dosing -- gene therapy does not. However, the procedure burden is substantial: each FUS-BBB session requires an MRI suite, stereotactic frame, IV microbubble infusion, and real-time monitoring. For a chronic disease like PD requiring repeated treatments, this creates practical scalability challenges that implantable systems like SonoCloud-9 may eventually address more efficiently.

**Analytical estimate -- Probability that FUS-BBB opening becomes standard of care for at least one CNS indication by 2030: 50-60%.** This is our assessment, not from a published source. The reasoning: the GBM survival data is compelling (base rate for device approval with Phase 1/2 survival benefit: ~40%), the Lotus Neuro spin-out signals commercial intent and investor confidence (+10%), FDA Breakthrough Device designation provides regulatory tailwind (+5%), and the drug-agnostic platform nature means success in one indication (GBM) immediately enables trials in others (AD, PD). Downside adjustments: single-arm Phase 1/2 data requires confirmation in randomized pivotal trial (-10%), logistical complexity of MRI-suite procedures limits adoption speed (-5%), competing approaches (implantable FUS, BBB-shuttle antibodies) could leapfrog if they prove more practical (-5%).

**Analytical estimate -- Probability that FUS-BBB opening is used therapeutically in PD by 2030: 15-20%.** This is our assessment, not from a published source. The reasoning: the Cerezyme delivery trial is Phase I/II with tiny N (15 patients), would need Phase 2/3 validation, and PD progression is slow enough that efficacy signals take years to emerge. The GBM and AD indications are 3-5 years ahead in clinical development. PD applications depend on either: (1) the GCase delivery approach working, which has multiple uncertainties (optimal dose, frequency, whether putaminal GCase replacement actually slows progression), or (2) FUS being paired with anti-synuclein antibodies like [[prasinezumab]], which would require new combination trials. The most realistic PD path is as a secondary indication after GBM or AD approval establishes the platform.

The Lotus Neuro spin-out is strategically significant: by separating device innovation (InSightec) from therapeutic development (Lotus Neuro), InSightec is creating a biotech entity that can pursue drug-device combination regulatory pathways, form pharma partnerships for specific indications, and raise dedicated therapeutic capital. This mirrors the Intuitive Surgical model of separating the robot platform from procedure development. Watch for Lotus Neuro partnerships with PD-focused companies (Roche, Prothena, Denali) as a signal that pharma sees FUS-BBB opening as a viable delivery enhancement for their existing PD pipelines.

## References

### Clinical Trials
- [Cerezyme BBB Disruption in PD](https://ctv.veeva.com/study/blood-brain-barrier-disruption-with-cerezyme-in-patients-with-parkinsons-disease) -- NCT04370665
- [BT008NA GBM Trial](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(25)00492-9/abstract) -- ReFOCUSED Consortium

### Key Publications
- [Ultrasound BBB Opening and Aducanumab in AD | NEJM (Jan 2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2308719) -- Rezai AR et al., Vol 390, pp 55-62
- [MB-FUS with Temozolomide for High-Grade Glioma (BT008NA) | Lancet Oncology (2025)](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(25)00492-9/abstract) -- Woodworth G, Lipsman N, et al.
- [BBB Opening with FUS in PD Dementia | Nature Communications (2021)](https://www.nature.com/articles/s41467-021-21022-9)
- [Putaminal GCase Delivery with MRgFUS in PD: Phase I | Mov Disord (2022)](https://pubmed.ncbi.nlm.nih.gov/36089809/)
- [Current Clinical Investigations of FUS-BBB Disruption: A Review | Neurotherapeutics (2024)](https://www.neurotherapeuticsjournal.org/article/S1878-7479(24)00038-2/fulltext)
- [FUS-BBB Enhancement for Brain Tumor Treatment: Systematic Review | J Neuro-Oncol (2024)](https://link.springer.com/article/10.1007/s11060-024-04795-z)
- [Long-Term Safety of Repeated BBB Opening via FUS in NHPs | PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0125911)
- [State-of-the-Art Microbubble-Assisted BBB Disruption | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6134932/)
- [Device Profile of ExAblate Neuro 4000 | Expert Rev Med Devices (2021)](https://www.tandfonline.com/doi/abs/10.1080/17434440.2021.1921572)

### Press Releases & Filings
- [InSightec Announces Spin-Out of Lotus Neuro (Dec 2025)](https://insightec.com/news/insightec-announces-spin-out-of-lotus-neuro-to-advance-focused-ultrasound-brain-therapies/)
- [InSightec FDA Breakthrough Designation for NSCLC Brain Mets (Mar 2022)](https://insightec.com/news/insightec-receives-fda-ide-approval-and-breakthrough-designation-for-nsclc-brain-mets-study-and-ide-approval-for-liquid-biopsy-study/)
- [Koch Disruptive Technologies $150M Investment](https://insightec.com/news/kdt-leads-series-e/)
- [InSightec $150M Series G Financing (Jun 2024)](https://insightec.com/news/insightec-announces-150m-financing-to-fund-continued-growth/)
- [FDA Approval of Exablate Neuro for PD Tremor (Dec 2018)](https://insightec.com/news/insightec-announces-fda-approval-of-staged-bilateral-focused-ultrasound-treatment-for-parkinsons-disease/)
- [LIBERATE Trial First Patients Enrolled](https://insightec.com/news/insightec-announces-milestone-of-first-patients-enrolled-in-the-pivotal-liberate-clinical-trial-liquid-biopsy-with-low-intensity-ultrasound-in-brain-tumors/)
- [Sunnybrook: First Direct-to-Brain Therapeutic Delivery in PD Using FUS](https://sunnybrook.ca/research/media/item.asp?c=2&i=2490&f=study-focused-ultrasound-technology)
- [FUS Foundation: Focused Ultrasound and PD](https://www.fusfoundation.org/posts/focused-ultrasound-and-parkinsons-disease/)

### Regulatory & Market
- [FDA SSED for Exablate Neuro (ET Approval)](https://www.accessdata.fda.gov/cdrh_docs/pdf15/P150038B.pdf)
- [InSightec Exablate Neuro Data Sheet](https://insightec.com/files/PUB41006477-Neuro-System-Data-Sheet-Rev-2.pdf)
- [Alzforum: Focused Ultrasound -- BBB Profile](https://www.alzforum.org/therapeutics/focused-ultrasound-blood-brain-barrier)
- [Carthera SONOBIRD Comparative Trial Q&A | FUS Foundation](https://www.fusfoundation.org/posts/therapeutic-ultrasound-for-recurrent-glioblastoma-a-qa-on-cartheras-comparative-clinical-trial/)
