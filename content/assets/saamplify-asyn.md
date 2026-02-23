---
drug_name: "SAAmplify-aSYN"
aliases: ["SYNTap", "synSAA", "ASYNC"]
target: "alpha-synuclein (misfolded aggregates)"
mechanism: "Seed amplification assay that detects trace amounts of misfolded alpha-synuclein in CSF by exploiting prion-like templated amplification — pathological seeds recruit normal alpha-synuclein monomers into detectable aggregates"
modality: "diagnostic assay"
developer: "Amprion"
company_type: "startup"
publicly_traded: false
partner: "Mayo Clinic Laboratories"
partner_type: "academic"
stage: "Commercial"
status: "Active"
patient_population: "Suspected synucleinopathies (PD, LBD/DLB, MSA, AD with Lewy body co-pathology)"
route_of_administration: "CSF (lumbar puncture)"
key_biomarkers: ["alpha-synuclein SAA positivity", "SAA amplification kinetics"]
next_catalyst: "FDA clearance/approval (beyond current LDT status)"
catalyst_date: "TBD"
thesis_cluster: "diagnostics"
tags: [pd-pipeline]
date: 2026-02-15
company_link: "[[companies/amprion]]"
partner_link: "[[companies/mayo-clinic]]"
---

# SAAmplify-aSYN

## Summary

SAAmplify-aSYN (Amprion, startup) is the first and only commercially available seed amplification assay for misfolded alpha-synuclein, delivering 96% sensitivity and 92% specificity with autopsy-confirmed accuracy. The test received FDA Breakthrough Device Designation in 2019 and an FDA Letter of Support in September 2024 endorsing its use for clinical trial patient selection. The March 2025 Mayo Clinic Laboratories collaboration massively expands US distribution. This is a "picks and shovels" asset -- it wins regardless of which alpha-synuclein therapeutic modality succeeds, because every future PD disease-modifying trial requires SAA-based patient stratification (the [[minzasolmin]] failure demonstrated what happens without it). If alpha-synuclein therapies like [[prasinezumab]] or [[aro-snca|ARO-SNCA]] reach approval, SAAmplify becomes a mandatory companion diagnostic for commercial patient identification; if they all fail, SAA remains essential for trial design and differential diagnosis.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Mayo Clinic Laboratories |
| Deal Date | March 2025 |
| Upfront | Undisclosed |
| Total (Biobucks) | Undisclosed |
| Deal Type | Partnership |

## Notes

### Science
- Exploits the **prion-like seeding** property of misfolded alpha-synuclein: a CSF sample containing even trace pathological alpha-synuclein seeds is incubated with recombinant alpha-synuclein monomers. If seeds are present, they template the conversion of normal monomers into aggregates, amplifying signal to a detectable threshold via fluorescence (thioflavin T binding)
- Originally based on Protein Misfolding Cyclic Amplification (PMCA) technology developed by co-founder Claudio Soto at UT McGovern Medical School; sometimes referred to as RT-QuIC (Real-Time Quaking-Induced Conversion) in the broader field, though Amprion's proprietary implementation differs in protocol details
- **96% sensitivity, 92% specificity** against autopsy-confirmed pathology -- the gold standard validation in neurodegeneration diagnostics
- Detects pathological alpha-synuclein years before overt clinical symptoms, enabling prodromal identification. A 2025 Neurology publication showed that SAA-positive prodromal PD patients had greater likelihood of phenoconversion to PD or DLB
- The assay can differentiate synucleinopathies (PD, DLB, MSA) from non-synucleinopathies, though PD vs. MSA subtype differentiation remains an area of active development (different alpha-synuclein strains produce different amplification kinetics)
- Key limitation: requires lumbar puncture for CSF collection, which is a barrier in routine clinical practice. Amprion's patent US20240085435A1 covers SAA for **peripheral matrices** (blood, skin), which would be transformative if validated
- The ~8% false-negative rate means SAA-negative patients are not definitively excluded from synucleinopathy -- clinical context remains essential

### Clinical
- SAAmplify-aSYN is a diagnostic, not a therapeutic -- there are no interventional clinical trials of the test itself
- **Pivotal validation** was performed against autopsy-confirmed cases from multiple brain bank cohorts, achieving the 96%/92% sensitivity/specificity benchmark
- The test is embedded in numerous ongoing PD therapeutic trials as a stratification biomarker, including trials for [[prasinezumab]], [[aro-snca|ARO-SNCA]], and other alpha-synuclein-targeting programs
- The PPMI (Parkinson's Progression Markers Initiative) study by the Michael J. Fox Foundation uses alpha-synuclein SAA as a core biological definition of PD, establishing the assay as a field-wide standard
- The [[minzasolmin]] Phase 2 failure is the cautionary case: the trial enrolled patients before SAA was available, likely including ~12% alpha-synuclein-negative patients and LRRK2 carriers with only 34.7% SAA positivity, massively diluting the treatment signal

### Financial
- **Series B:** $15M target, with $6M initial close in October 2024. Led by Formation Venture Engineering (FVE) with participation from **Eli Lilly** and Series A investors
- **Total raised:** Approximately $17M in investor capital plus >$8M in grant funding
- **Revenue model:** Laboratory Developed Test (LDT) — Amprion performs the assay in its own CLIA/CAP-accredited lab in San Diego and bills per test. Not yet FDA-cleared/approved as an IVD, which limits reimbursement pathways
- **Reimbursement:** Currently billed as an LDT; FDA clearance/approval would unlock broader insurance coverage and higher reimbursement rates
- **Mayo Clinic Laboratories partnership** (March 2025) is the key commercial inflection point — MCL distributes to thousands of hospital and clinic clients across the US, dramatically expanding test ordering access (Mayo ID: ASYNC)
- **2024 BioTech Breakthrough Award:** "Clinical Diagnostics Solution of the Year" — validates commercial positioning
- **Lilly's participation** in the Series B is notable: Lilly has no PD alpha-synuclein therapeutic but is investing in the diagnostic layer, suggesting they view SAA as infrastructure regardless of therapeutic outcomes
- **Valuation:** Undisclosed. For a pre-FDA-clearance diagnostics company with $17M raised, commercial product, and Mayo partnership, comparable diagnostics companies suggest a $50-100M range, but this is speculative

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[saamplify-asyn]] | Commercial | Active | Amprion | diagnostic assay |
| [[ai-blood-test]] | Research | Active | UCL / Guilford Street Laboratories | diagnostic assay |
| [[18f-fd4]] | Phase 1 | Active | SynuSight Biotech | PET tracer |
| [[mk-7337]] | Phase 1 | Discontinued | Merck | PET tracer |

- SAAmplify-aSYN is currently the **only commercially available** alpha-synuclein SAA test, giving Amprion first-mover advantage in a market that is becoming mandatory for PD drug development
- **Academic SAA labs** (e.g., Indiana University RT-QuIC, MJFF-funded academic sites) perform similar assays for research, but none have Amprion's commercial infrastructure, CLIA certification, or Mayo distribution
- The FDA Letter of Support (September 2024) specifically endorsed the SAA technology class, not Amprion exclusively -- this opens the door for competitors to develop their own commercial assays
- **Alpha-synuclein PET tracers** (SynuSight's 18F-FD4, AC Immune's ACI-12589) are a complementary/competitive threat: PET imaging could eventually provide spatial resolution of alpha-synuclein pathology that CSF SAA cannot, though PET tracers are years behind in development
- **Blood-based alpha-synuclein detection** (multiple academic groups) would eliminate the lumbar puncture barrier. Amprion's own peripheral matrix patent positions them for this transition, but validation lags CSF SAA by years
- **QIAGEN/Neuron23** focus on LRRK2 genetic testing -- a different diagnostic axis (genetic vs. proteopathic), not directly competitive but part of the broader PD precision medicine ecosystem
- The competitive moat is narrow: the underlying SAA/RT-QuIC technology is published and accessible. Amprion's advantages are regulatory (Breakthrough Device Designation), commercial (CLIA lab, Mayo partnership), and operational (assay optimization, turnaround time). A well-funded competitor with diagnostic infrastructure could replicate within 2-3 years

## Analysis

SAAmplify-aSYN occupies a unique position in the PD landscape: it is a commercial-stage diagnostic that functions as critical infrastructure for the entire alpha-synuclein therapeutic ecosystem. The [[minzasolmin]] failure crystallized the field consensus that SAA stratification is non-negotiable for future trials. Every alpha-synuclein program -- whether antibody ([[prasinezumab]]), siRNA ([[aro-snca|ARO-SNCA]]), ASO ([[ly3962681|LY3962681]]), or vaccine ([[ub-312|UB-312]], [[aci-7104|ACI-7104]]) -- now depends on SAA to enrich trial populations for biologically confirmed synucleinopathy patients.

**Analytical estimate -- SAAmplify commercial value depends on two scenarios.** This is our assessment, not from a published source. The reasoning:
- **Scenario A (any alpha-syn therapy approved):** SAA becomes a mandatory companion diagnostic. With ~1 million PD patients diagnosed annually in the US/EU and a diagnostic test priced at $1,000-2,000, the addressable market for initial diagnosis alone is $1-2B. Amprion captures a fraction as competitors emerge, but first-mover advantage and Mayo distribution provide a durable share. Estimated Amprion-specific revenue: $100-300M/year at maturity.
- **Scenario B (all alpha-syn therapies fail):** SAA remains valuable for clinical trial patient selection (pharma services revenue), differential diagnosis (distinguishing synucleinopathies from tauopathies), and prodromal identification (research use). Market is smaller -- estimated $20-50M/year for Amprion. But the company survives because diagnostic utility persists independent of therapeutic success.

**Signal analysis:** Eli Lilly's participation in the Series B is the most informative data point. Lilly has deep PD therapeutic investments but no alpha-synuclein program -- their interest in Amprion is purely about diagnostic infrastructure. This suggests Lilly views SAA as becoming standard-of-care regardless of which therapeutic wins. The Mayo Clinic Laboratories partnership is the commercial validation: Mayo's distribution network transforms SAAmplify from a niche research tool into a broadly accessible clinical test. The company's small size ($17M raised, undisclosed valuation) relative to its strategic importance creates an asymmetry -- Amprion is underpriced relative to its role as an enabling platform for a multi-billion-dollar therapeutic category.

The key risk is technological displacement. If blood-based alpha-synuclein detection achieves comparable sensitivity/specificity to CSF SAA, the lumbar puncture requirement becomes an existential liability. Amprion's peripheral matrix patent provides some hedge, but execution risk is high. The other risk is that a large diagnostics company (Roche Diagnostics, Abbott, Siemens Healthineers) builds a competing SAA or develops an immunoassay that is "good enough" for clinical use, leveraging their existing lab infrastructure to commoditize the test.

## References

### Key Publications
- [Alpha-Synuclein SAA Amplification Parameters and Risk of Progression in Prodromal PD | Neurology (2025)](https://www.neurology.org/doi/10.1212/WNL.0000000000210279)
- [High diagnostic performance of independent alpha-synuclein SAAs for detection of early PD | PMC (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8572469/)
- [Alpha-synuclein SAA: Data sharing, standardization needed for clinical use | Science Advances (2025)](https://www.science.org/doi/10.1126/sciadv.adt7195)

### Press Releases & Filings
- [FDA Issues Letter of Support for Alpha-Synuclein SAA (Sep 2024)](https://www.businesswire.com/news/home/20240905546394/en/FDA-Issues-Letter-of-Support-for-%CE%B1-Synuclein-Seed-Amplification-Assay-%E2%80%93-The-Core-Technology-Used-in-Amprion%E2%80%99s-First-Commercial-Test)
- [Amprion Initial Close of $15M Series B Financing (Oct 2024)](https://www.businesswire.com/news/home/20241009892605/en/Amprion-Announces-Initial-Close-of-a-%2415M-Financing-to-Commercialize-Groundbreaking-Neurologic-Diagnostics)
- [Amprion Wins 2024 BioTech Breakthrough Award (Nov 2024)](https://www.businesswire.com/news/home/20241119785149/en/Amprion-Honored-to-Win-the-2024-BioTech-Breakthrough-Award-%E2%80%98Clinical-Diagnostics-Solution-of-the-Year%E2%80%99)
- [Mayo Clinic Laboratories and Amprion Collaboration (Mar 2025)](https://news.mayocliniclabs.com/2025/03/26/mayo-clinic-laboratories-and-amprion-announce-collaboration-to-advance-neurodegenerative-disease-diagnostics/)

### Regulatory & Market
- [FDA Breakthrough Device Designation | Amprion](https://ampriondx.com/misfolded-proteins/fda-breakthrough/)
- [SAAmplify-aSYN Biomarker Test FAQ | Amprion](https://ampriondx.com/ordering-instructions/faq/)
- [Alpha-Synuclein Biomarker Testing | Mayo Clinic Laboratories](https://news.mayocliniclabs.com/alpha-synuclein-biomarker-testing/)

### Patents
- US20240085435A1 — Alpha-Synuclein Seed Amplification Assay for Peripheral Matrices (Amprion Inc, 2024)
