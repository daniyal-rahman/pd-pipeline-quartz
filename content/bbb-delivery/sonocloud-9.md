---
drug_name: "SonoCloud-9"
aliases: ["SC9", "SonoCloud"]
target: "blood-brain barrier (transient opening via focused ultrasound)"
mechanism: "Implantable 9-emitter, 1-MHz focused ultrasound device that transiently opens the BBB using low-intensity pulsed ultrasound (LIPU) with IV microbubbles (DEFINITY), increasing brain drug concentrations 4-6x"
modality: "medical device"
developer: "Carthera"
company_type: "startup"
publicly_traded: false
stage: "Phase 3"
status: "Active"
patient_population: "Recurrent glioblastoma (primary); potential PD/AD applications"
route_of_administration: "implanted device + IV microbubbles"
key_biomarkers: ["gadolinium-enhanced MRI (BBB opening confirmation)", "brain-to-plasma drug ratio"]
confidence_rating: "7/10"
next_catalyst: "SONOBIRD Phase 3 readout"
catalyst_date: "2027-2028"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery, claude]
date: 2026-02-16
company_link: "[[companies/carthera]]"
---

# SonoCloud-9

## Summary

SonoCloud-9 is Carthera's (startup, Lyon, France) implantable ultrasound device that transiently opens the blood-brain barrier to increase brain drug concentrations 4-6x. The Phase 1/2 trial (NCT03744026) in recurrent glioblastoma demonstrated 90% BBB disruption across nine emitters with a clean safety profile (33 patients, 90 sonications, no DLTs), and the Phase 1 nab-paclitaxel trial at Northwestern confirmed the 4-6x drug concentration increase. Carthera is now running SONOBIRD (NCT05902169), a 560-patient Phase 3 pivotal comparing SonoCloud-9 + carboplatin vs. standard-of-care in recurrent GBM, with 130 patients enrolled as of April 2025 and FDA Breakthrough Device designation. If SONOBIRD succeeds, it validates implantable ultrasound BBB opening as a platform technology with direct implications for PD drug delivery -- any systemically administered therapeutic (antibodies, enzyme replacement, gene therapy vectors) could achieve dramatically higher brain concentrations. If it fails, the implantable approach loses momentum, but the broader focused ultrasound BBB-opening field continues via non-invasive alternatives like InSightec's Exablate Neuro.

## Notes

### Science

- **Core mechanism:** Low-Intensity Pulsed Ultrasound (LIPU) at 1 MHz is emitted by nine 10-mm diameter transducers implanted epidurally in the skull. Simultaneously, IV microbubbles (DEFINITY, perflutren lipid microspheres at 10 ul/kg) circulate through brain microvasculature. The ultrasound causes the microbubbles to oscillate (stable cavitation), mechanically loosening tight junctions between endothelial cells and transiently opening the BBB ([Carthera, Our Solutions](https://carthera.eu/our-solutions/); [Nature Communications 2024](https://www.nature.com/articles/s41467-024-45818-7))
- **BBB opening is reversible:** The opening closes within hours of the procedure. SonoCloud-9 BBB opening resolved within approximately 1 hour on contrast-enhanced MRI, compared to up to 24 hours for MRI-guided focused ultrasound systems ([IEEE Pulse review](https://www.embs.org/pulse/articles/breaking-barriers-with-sound-focused-ultrasound-in-the-brain/))
- **Coverage:** The 9-emitter grid covers a ~58 mm x 58 mm skull area, producing BBB disruption in a volume 9x larger than the original single-emitter SonoCloud-1 device. This is critical for covering the infiltrative margin around brain tumors ([FUS Foundation](https://www.fusfoundation.org/posts/cartheras-sonocloud-9-device-facilitates-delivery-of-chemotherapy-to-glioblastomas/))
- **Sonication duration:** 270 seconds (~4.5 minutes) per treatment session; emitters fire sequentially to avoid acoustic interference between adjacent elements ([Nature Communications 2024](https://www.nature.com/articles/s41467-024-45818-7))
- **Drug agnostic platform:** The BBB opening is independent of the drug being delivered -- demonstrated with carboplatin (small molecule), nab-paclitaxel (albumin-bound nanoparticle), and the Alzheimer's pilot implies applicability to biologics. This makes SonoCloud-9 a potential platform for enhancing brain delivery of any circulating therapeutic ([FUS Foundation](https://www.fusfoundation.org/posts/recurrent-glioblastoma-clinical-trial-results-of-sonocloud-9-plus-chemotherapy/))
- **Implantation trade-off:** Requires neurosurgical craniotomy for device placement (the device replaces a bone flap), which is acceptable in GBM patients already undergoing tumor resection but is a significant barrier for chronic neurodegenerative disease indications like PD where patients do not routinely undergo craniotomy ([FUS Foundation Q&A](https://www.fusfoundation.org/posts/therapeutic-ultrasound-for-recurrent-glioblastoma-a-qa-on-cartheras-comparative-clinical-trial/))
- **Activation method:** The device is activated via a transdermal needle connection to an external control unit -- does not require MRI guidance or general anesthesia, enabling outpatient treatment ([Carthera, Our Solutions](https://carthera.eu/our-solutions/))

### Clinical

**Phase 1/2 Carboplatin Trial (NCT03744026)** | N=33 | 6 sites (4 France, 2 US) | Recurrent GBM
- **Design:** Single-arm dose-escalation (Phase 1: 1-9 emitters) then expansion (Phase 2: all 9 emitters)
- **Primary endpoint:** Safety/BBB opening efficacy -> No DLTs across 90 sonications
- **BBB opening rate:** 90% of activated emitters produced BBB disruption in gray and/or white matter with good repeatability
- **Drug concentration:** 7.58-fold increase in brain/plasma carboplatin ratio in 3 patients with intraoperative measurement
- **Survival (carboplatin before sonication, n=12):** Median OS 14.0 months, 1-year OS 58%
- **Survival (carboplatin after sonication, n=15):** Median OS 11.8 months, 1-year OS 47%
- **Safety:** Two transient grade 3 wound infections and one grade 1 meningocele considered procedure-related. Treatment-related AEs included scalp pain, nausea, dizziness, headache, aphasia, and blurred vision -- all but one case resolved within 15 minutes
- **Status:** Completed
- **Publication:** [Nature Communications (Feb 2024)](https://www.nature.com/articles/s41467-024-45818-7)
- **Interpretation:** Established proof-of-concept that repeated BBB opening with an implantable device is safe and achieves clinically meaningful drug concentration increases. The timing difference (drug before vs. after sonication) informed the Phase 3 design

**Phase 1 Nab-Paclitaxel Trial (NCT04528680)** | N=17 | Northwestern University | Recurrent GBM
- **Design:** Bayesian adaptive dose-escalation; nab-paclitaxel delivered every 3 weeks with BBB opening
- **Primary endpoint:** Safety/tolerability -> Well tolerated, some patients received up to 6 cycles
- **Drug concentration:** 4-6x increase in paclitaxel brain concentrations, confirming the platform works across different drug classes
- **Status:** Completed
- **Publication:** Results presented at ASCO 2022 ([JCO 2022](https://ascopubs.org/doi/abs/10.1200/JCO.2022.40.16_suppl.2016)); published in Lancet Oncology
- **Interpretation:** Replicated the BBB opening effect with a second drug (albumin-bound nanoparticle), strengthening the platform thesis

**SONOBIRD Phase 3 Pivotal (NCT05902169)** | N=560 (target) | ~40 sites across US and Europe | Recurrent GBM (first recurrence)
- **Design:** Randomized (1:1), open-label, two-arm comparative trial. All patients undergo craniotomy; randomization determines whether SonoCloud-9 is implanted. Treatment arm receives SonoCloud-9 + IV carboplatin every 3 weeks (up to 7 cycles / ~6 months). Control arm receives physician-choice lomustine (CCNU) or temozolomide (TMZ)
- **Primary endpoint:** Overall survival
- **Secondary endpoint:** Progression-free survival
- **Sites:** Belgium, France, Germany, Italy, Netherlands, Spain, Switzerland (plus Denmark, Sweden planned) in Europe; 12+ US states including NY, CA, IL, TX, FL, PA, MD, MN, CO, NC, UT, IN
- **Enrollment status:** First patient enrolled February 2024; 100 patients reached April 2025; 130/560 enrolled as of May 2025 ([BusinessWire, April 2025](https://www.businesswire.com/news/home/20250422399922/en/Carthera-Reaches-Recruitment-Milestone-in-SONOBIRD-Pivotal-Trial-for-Recurrent-Glioblastoma))
- **Target completion:** ~2 years from initiation (enrollment target ~early 2026)
- **Status:** Active, enrolling
- **Interpretation:** This is the pivotal trial for potential FDA approval. The 560-patient size and overall survival primary endpoint are robust. FDA Breakthrough Device designation (granted 2022) provides priority review and intensive FDA interaction ([FUS Foundation](https://www.fusfoundation.org/posts/cartheras-sonocloud-9-system-designated-as-a-breakthrough-device/))

**BOREAL Alzheimer's Pilot (NCT03119961)** | N=10 | France | Mild Alzheimer's disease
- **Design:** Single-arm pilot using SonoCloud-1 (single emitter); 7 BBB opening sessions over 3.5 months targeting left supra-marginal gyrus
- **Primary endpoint:** Safety -> Confirmed safe in older (median age 71), cognitively impaired population
- **Amyloid change:** Non-significant decrease of -6.6% (SD=7.2%) in amyloid accumulation on 18F-Florbetapir PET in sonicated gray matter in 6/10 participants
- **Status:** Completed
- **Publication:** [Alzheimer's Research & Therapy (2022)](https://alzres.biomedcentral.com/articles/10.1186/s13195-022-00981-1)
- **Interpretation:** Proof-of-concept that ultrasound BBB opening alone (without a therapeutic) may reduce amyloid load, possibly by enhancing clearance. Demonstrates safety in a neurodegenerative disease population -- important precedent for any future PD application

### Financial

- **Total funding raised:** EUR 42M (~$45M) in Series B financing as of December 2023 ([ALA Associates](https://ala.associates/funding/carthera-brings-series-b-round-to-e42m-with-additional-e4-5m-funding/))
- **Key investors:** Panakes Partners, Supernova Invest, Sham Innovation Sante (Turenne Capital), Groupe Arnault, European Innovation Council (EIC), Relyens, Unorthodox Ventures, Bouscas Med ([Crunchbase](https://www.crunchbase.com/organization/carthera); [PharmiWeb](https://www.pharmiweb.com/press-release/2020-09-14/carthera-to-receive-2m-grant-and-105m-equity-from-the-european-innovation-council-for-development))
- **EIC funding:** EUR 2M grant + EUR 10.5M equity from European Innovation Council Accelerator (2020) ([PharmiWeb](https://www.pharmiweb.com/press-release/2020-09-14/carthera-to-receive-2m-grant-and-105m-equity-from-the-european-innovation-council-for-development))
- **French government support:** EUR 5.7M from Bpifrance "Investments for the Future Program" for the DOME project ([BioPharma Dive](https://www.biopharmadive.com/press-release/20161012-carthera-secures-57-million-in-funding-for-its-dome-project-from-frances/)); French High Authority for Health (HAS) positive opinion on Innovation Funding scheme for recurrent GBM treatment (July 2024) ([PharmiWeb](https://www.pharmiweb.com/press-release/2024-07-01/carthera-receives-positive-opinion-from-french-high-authority-for-health-on-innovation-funding-schem))
- **For a private startup**, EUR 42M is a modest raise -- adequate for a single pivotal trial with regulatory support but would likely need additional financing or a partnership to support commercialization and expansion into neurodegenerative indications
- **No disclosed pharma partnerships** as of early 2026; Carthera has stated it is "actively pursuing pharmaceutical partnerships" ([FUS Foundation Company Profile](https://www.fusfoundation.org/posts/company-profile-carthera/))

### Competitive

The competitive landscape for focused ultrasound BBB opening includes both device competitors and alternative BBB-crossing technologies:

**Focused Ultrasound BBB Opening Devices:**
- **InSightec Exablate Neuro (MRgFUS):** Non-invasive, helmet-style 1,024-element phased array at ~650 kHz. FDA-approved for essential tremor/PD tremor (ablation). In clinical trials for BBB opening in GBM and Alzheimer's. Key advantages: no surgery required, precise MRI-guided targeting to any brain region, adjustable focal zone. Key disadvantages: requires MRI suite for each treatment, ~60 min procedure under MRI, cannot easily repeat treatments at outpatient frequency. The contrast extravasation (BBB opening) takes up to 24 hours to resolve vs. ~1 hour for SonoCloud-9 ([IEEE Pulse](https://www.embs.org/pulse/articles/breaking-barriers-with-sound-focused-ultrasound-in-the-brain/))
- **Sunnybrook/UHN (academic, Exablate-based):** First-in-human delivery of a therapeutic (Cerezyme/imiglucerase) across the BBB in PD patients using MRI-guided FUS. Phase I study (4 patients, 3 doses each) published in Movement Disorders (2022) showed safety and "early suggestions of biologic efficacy." Phase I/II trial launched 2025 ([Sunnybrook Research](https://sunnybrook.ca/research/media/item.asp?c=2&i=2204&f=world-first-focused-ultrasound-parkinsons-disease); [FUS Foundation](https://www.fusfoundation.org/posts/focused-ultrasound-for-parkinsons-disease-results-of-first-clinical-trial-to-deliver-therapeutics/))

**Alternative BBB-Crossing Approaches (Non-FUS):**
- Transferrin receptor bispecific antibodies (Denali TV platform, Roche BBB shuttle) -- engineered molecules rather than devices
- Receptor-mediated transcytosis platforms (various)
- AAV capsid engineering for BBB crossing (Capsida, Voyager)
- Intrathecal/intracerebroventricular delivery (bypasses BBB entirely)

**SonoCloud-9 competitive positioning:**
- Unique as the only **implantable** FUS BBB-opening device in pivotal trials
- The implant enables repeated outpatient treatments without MRI, which is a major practical advantage for chronic regimens
- However, the surgical implantation requirement is the core limitation for expansion beyond oncology into PD/AD
- Carthera would need either a less-invasive next-generation device or a clinical rationale strong enough to justify craniotomy in PD patients (e.g., combined with DBS implantation)

## Analysis

SonoCloud-9 is primarily an oncology asset, but its relevance to PD lies in the platform thesis: if transient BBB opening can safely and repeatedly increase brain drug concentrations 4-6x, it fundamentally changes the pharmacokinetics of every PD drug that currently struggles with brain penetration. Anti-alpha-synuclein antibodies like [[prasinezumab]] achieve only ~0.1-0.2% of blood levels in CSF -- a 4-6x increase would push this to 0.4-1.2%, potentially crossing the threshold for meaningful target engagement. GBA1 enzyme replacement (the approach being piloted at Sunnybrook using Exablate + Cerezyme) is directly analogous to what SonoCloud-9 could enable. Growth factors, gene therapy vectors, and even cell therapies could all benefit from enhanced BBB permeability.

The critical barrier for PD application is the surgical implantation. GBM patients already undergo craniotomy, making SonoCloud-9 implantation a trivial addition. PD patients do not routinely undergo craniotomy unless receiving DBS. One scenario where SonoCloud-9 becomes relevant for PD is combination with DBS implantation -- if a patient is already undergoing stereotactic neurosurgery, adding a SonoCloud device to enable enhanced drug delivery becomes surgically feasible. This would create a hybrid DBS + BBB-opening platform for advanced PD. However, Carthera has not publicly disclosed any PD-specific development plans.

**Analytical estimate -- SONOBIRD Phase 3 success probability: 45-55%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Phase 3 oncology device trials with Breakthrough Designation have higher-than-average success rates (~50-60%)
- Adjustments upward: compelling Phase 1/2 data (4-6x drug concentration, 90% BBB opening rate) (+10%), mechanism is physically validated rather than biologically uncertain (+5%), FDA Breakthrough Device designation enabling intensive interaction (+5%)
- Adjustments downward: recurrent GBM is notoriously difficult (standard OS ~8-10 months) (-5%), open-label design introduces potential bias (-5%), relatively small company running a 560-patient international trial (-5%)
- Net: ~45-55%

**Signal analysis:**
- FDA Breakthrough Device designation (2022) is a meaningful regulatory signal -- it indicates the FDA agrees the device "may provide more effective treatment for a life-threatening condition"
- The French HAS positive opinion on Innovation Funding demonstrates European regulatory alignment
- Enrollment pace (130/560 in ~14 months) suggests roughly 2.5-3 years for full enrollment, potentially pushing readout to 2027-2028
- The EUR 42M raised is thin for a 560-patient Phase 3 across 40 international sites -- Carthera likely needs a pharma partner or additional financing before trial completion. A partnership announcement would be a positive signal for both the oncology program and future neurology expansion

**PD-specific decision tree:**
- If SONOBIRD succeeds: validates the device platform, likely attracts pharma partnership, enables a funded PD pilot study (probably SonoCloud-9 combined with an anti-alpha-synuclein antibody or GCase enzyme replacement). Timeline for PD application: 2029+ at earliest
- If SONOBIRD fails: SonoCloud-9 specifically loses momentum, but the broader FUS BBB-opening field continues via InSightec Exablate (non-invasive, no surgery). The Sunnybrook PD program with Exablate is already independent of Carthera's outcome
- Regardless of outcome: the non-invasive Exablate Neuro platform is likely more relevant for PD long-term because it does not require surgical implantation

## References

### Clinical Trials
- [Phase 1/2 Carboplatin + SonoCloud-9](https://clinicaltrials.gov/study/NCT03744026) -- NCT03744026
- [Phase 1 Nab-paclitaxel + SonoCloud-9](https://clinicaltrials.gov/study/NCT04528680) -- NCT04528680
- [SONOBIRD Phase 3 Pivotal](https://clinicaltrials.gov/study/NCT05902169) -- NCT05902169
- [BOREAL Alzheimer's Pilot](https://clinicaltrials.gov/study/NCT03119961) -- NCT03119961
- [Sunnybrook FUS + Cerezyme in PD](https://clinicaltrials.gov/study/NCT07179328) -- NCT07179328

### Key Publications
- [Repeated BBB opening with SonoCloud-9 + carboplatin in rGBM: Phase I/II | Nature Communications (Feb 2024)](https://www.nature.com/articles/s41467-024-45818-7)
- [Repeated BBB opening with SonoCloud-9 + nab-paclitaxel: Phase 1 | JCO (2022)](https://ascopubs.org/doi/abs/10.1200/JCO.2022.40.16_suppl.2016)
- [BOREAL: Repeated BBB disruption in mild AD with SonoCloud-1 | Alzheimer's Research & Therapy (2022)](https://alzres.biomedcentral.com/articles/10.1186/s13195-022-00981-1)
- [BBB opening with FUS in PD dementia | Nature Communications (2021)](https://www.nature.com/articles/s41467-021-21022-9)
- [Putaminal GCase delivery with MRgFUS in PD: Phase I | Movement Disorders (2022)](https://pubmed.ncbi.nlm.nih.gov/36089809/)
- [FUS-mediated BBB opening for neurodegenerative diseases | Frontiers in Neurology (2021)](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.749047/full)
- [FUS-enhanced anti-alpha-synuclein antibody delivery for PD | bioRxiv (2024)](https://www.biorxiv.org/content/10.1101/2024.09.13.611071v1.full)
- [FUS-mediated BBB opening for delivering drugs to gliomas: systematic review | PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11538134/)

### Press Releases & Filings
- [Carthera Reaches Recruitment Milestone in SONOBIRD (April 2025)](https://www.businesswire.com/news/home/20250422399922/en/Carthera-Reaches-Recruitment-Milestone-in-SONOBIRD-Pivotal-Trial-for-Recurrent-Glioblastoma)
- [Carthera receives FDA Breakthrough Device designation (2022)](https://www.fusfoundation.org/posts/cartheras-sonocloud-9-system-designated-as-a-breakthrough-device/)
- [Carthera brings Series B round to EUR 42M (Dec 2023)](https://ala.associates/funding/carthera-brings-series-b-round-to-e42m-with-additional-e4-5m-funding/)
- [Carthera receives EUR 2M grant + EUR 10.5M equity from EIC (2020)](https://www.pharmiweb.com/press-release/2020-09-14/carthera-to-receive-2m-grant-and-105m-equity-from-the-european-innovation-council-for-development)
- [Carthera secures EUR 5.7M from Bpifrance (2016)](https://www.biopharmadive.com/press-release/20161012-carthera-secures-57-million-in-funding-for-its-dome-project-from-frances/)
- [French HAS positive opinion on Innovation Funding for SonoCloud-9 (July 2024)](https://www.pharmiweb.com/press-release/2024-07-01/carthera-receives-positive-opinion-from-french-high-authority-for-health-on-innovation-funding-schem)
- [FUS for PD: Results of first clinical trial to deliver therapeutics (2025)](https://www.fusfoundation.org/posts/focused-ultrasound-for-parkinsons-disease-results-of-first-clinical-trial-to-deliver-therapeutics/)

### Regulatory & Market
- [FDA Breakthrough Device Program overview](https://www.fda.gov/medical-devices/how-study-and-market-your-device/breakthrough-devices-program)
- [SONOBIRD trial site page](https://sonobird.eu/sonobird-trial/)
- [Carthera company website](https://carthera.eu/)
- [FUS Foundation: Company Profile -- CarThera](https://www.fusfoundation.org/posts/company-profile-carthera/)
- [FUS Foundation: Parkinson's Disease page](https://www.fusfoundation.org/diseases-and-conditions/parkinsons-disease/)
