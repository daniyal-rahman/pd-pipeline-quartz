---
drug_name: "Raguneprocel"
aliases: ["AMCHEPRY", "DSP-1083"]
target: "dopaminergic neuron replacement (iPSC-derived DA progenitors)"
mechanism: "Allogeneic iPSC-derived dopaminergic neural progenitor cells transplanted into the putamen to replace lost DA neurons and restore dopamine production"
modality: "cell therapy (iPSC allogeneic)"
developer: "Sumitomo Pharma / RACTHERA"
company_type: "big pharma"
publicly_traded: true
ticker: "4506.T"
partner: "CiRA Foundation / Kyoto University"
partner_type: "academic"
stage: "NDA Filed"
status: "Active"
patient_population: "Advanced PD with motor fluctuations (off-time)"
route_of_administration: "intracranial (bilateral stereotactic injection into putamen)"
key_biomarkers: ["18F-DOPA PET", "DaT-SPECT", "MDS-UPDRS"]
confidence_rating: "7/10"
next_catalyst: "PMDA approval decision (Japan)"
catalyst_date: "H2 2026"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Raguneprocel

## Summary

Raguneprocel (brand name AMCHEPRY) is poised to become the world's first iPSC-derived cell therapy approved for any indication. Sumitomo Pharma / RACTHERA (big pharma, 4506.T) filed an NDA with Japan's MHLW in August 2025 based on a Phase I/II investigator-initiated trial at Kyoto University Hospital (N=7) showing transplanted iPSC-derived DA progenitors survived, produced dopamine (confirmed by 18F-DOPA PET), and did not form tumors over 24 months of follow-up. The MHLW committee review is scheduled for February 19, 2026, with priority review designation granted. If approved, this validates the iPSC-to-neuron replacement paradigm, creates a regulatory pathway for cell therapies in neurodegeneration, and positions Japan as the global leader in regenerative medicine for PD. If rejected or delayed, [[bemdaneprocel]] (BlueRock/Bayer, ESC-derived, Phase 3) becomes the de facto front-runner in the cell therapy race.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | CiRA Foundation / Kyoto University |
| Deal Date | 2018 (investigator-initiated trial collaboration) |
| Upfront | N/A (academic collaboration) |
| Total (Biobucks) | N/A |
| Deal Type | Partnership |

## Notes

### Science
- Allogeneic iPSC-derived dopaminergic neural progenitor cells manufactured from HLA-matched iPS cell stock provided by CiRA Foundation (Kyoto University), differentiated using technology developed by Prof. Jun Takahashi's group at CiRA
- Cells are transplanted bilaterally into the putamen via stereotactic surgery, where they engraft, mature into dopaminergic neurons, and produce dopamine to replace neurons lost to PD pathology
- Key differentiation vs. [[bemdaneprocel]]: raguneprocel uses iPSCs (reprogrammed adult cells) while bemdaneprocel uses ESCs (embryonic stem cells) -- iPSCs avoid embryonic tissue sourcing concerns and enable HLA-matching from banked cell lines
- The CiRA iPS Cell Stock Project maintains a bank of clinical-grade iPSC lines from HLA-homozygous donors, enabling partial immunological matching and reduced immunosuppression requirements
- Preclinical data published in Nature Communications (2020) showed iPSC-derived DA progenitors survived in primate putamen, extended neurites, and produced dopamine without tumor formation
- Open scientific question: long-term durability of engraftment (>5 years) and whether a single transplant provides lasting benefit or repeat dosing is needed
- Manufacturing is handled by S-RACMO Co., Ltd. (Sumitomo regenerative medicine CDMO established 2020 in Osaka) -- scalability of iPSC manufacturing for commercial supply remains a key risk

### Clinical

**Kyoto University Phase I/II (Investigator-Initiated)** | UMIN000033564 / JMA-IIA00384 | N=7 | Advanced PD patients (ages 50-69)
- **Primary endpoint:** Safety (serious adverse events, tumor formation) → No serious adverse events related to cell product; 73 mild-to-moderate AEs over 24 months; no tumor formation
- **Key secondary:** 18F-DOPA PET showed increased uptake in bilateral putamen (color change from dark green to red), confirming dopamine synthesis by grafted cells; UPDRS motor scores showed trends toward improvement in off-time
- **Status:** Completed (enrolled 2018-2023; results published Nature, April 2025)
- **Interpretation:** The trial was powered for safety, not efficacy. The PET imaging data is the critical signal -- demonstrating that transplanted cells survive, engraft, and produce dopamine in human brain. The small N=7 and open-label design limit efficacy conclusions, but the safety/survival data was sufficient for Japan's PMDA to grant priority review and accept the NDA filing. This regulatory pathway leverages Japan's Regenerative Medicine framework, which allows conditional approval based on smaller datasets.

**UC San Diego Phase 1 (US Investigator-Initiated)** | NCT TBD | N=TBD | PD patients
- **Primary endpoint:** Safety of non-cryopreserved iPSC-derived DA progenitor cells
- **Status:** Initiated November 2023 at Sanford Stem Cell Institute CIRM Alpha Clinic, UCSD School of Medicine
- **Interpretation:** US trial uses non-cryopreserved formulation (vs. Japan trial). Critical for eventual US regulatory path but not the basis for the Japan NDA.

**Sumitomo Pharma Company-Sponsored US Study** | NCT TBD | N=TBD | PD patients
- **Status:** Initiated March 2024
- **Interpretation:** Company-sponsored study builds the dataset needed for potential US NDA; no results disclosed yet

### Financial
- **Sumitomo Pharma (4506.T):** Market cap ~$6B; trailing 12-month revenue $2.98B (as of Sep 2025); EPS $2.61
- **RACTHERA:** Joint venture between Sumitomo Chemical and Sumitomo Pharma, established December 2024, operational February 1, 2025 -- dedicated entity for regenerative medicine and cell therapy R&D; inherited all regenerative medicine IP from Sumitomo Pharma
- **S-RACMO:** CDMO subsidiary (est. 2020) manufacturing raguneprocel; new facility under construction in Osaka for commercial-scale production
- **Peak sales estimates:** Not publicly available from analysts. Market context: global PD therapeutics market projected at ~$7.9B by 2033 (CAGR 8.9%). Cell therapy for PD is a new category -- commercial pricing and patient volume are highly uncertain. Japan-only launch initially limits revenue but establishes first-mover regulatory precedent
- **Investment context:** Sumitomo has invested heavily in regenerative medicine infrastructure (RACTHERA JV, S-RACMO CDMO, multiple clinical programs). This is a platform bet, not a single-asset bet -- raguneprocel approval de-risks the entire iPSC manufacturing and regulatory pipeline
- **Competitive financing comparison:** BlueRock (Bayer subsidiary) has effectively unlimited big-pharma backing for [[bemdaneprocel]]; Aspen Neuroscience (autologous iPSC) raised $115M Series C in Nov 2025

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(thesis_cluster, "cell-therapy") AND file.name != "raguneprocel"
SORT stage DESC
```

- [[bemdaneprocel]] (BlueRock/Bayer) is the primary competitor -- ESC-derived (not iPSC), Phase 3 pivotal trial (exPDite-2) dosed first patient September 2025, readout expected ~2027. Received SAKIGAKE (Pioneering Regenerative Medical Product) designation in Japan in December 2025, signaling intent to compete in Japan market
- Raguneprocel has the regulatory lead (NDA filed vs. Phase 3 enrolling) but a smaller clinical dataset (N=7 vs. BlueRock's N=12 Phase 1). The Japan-first strategy via Regenerative Medicine framework allows conditional approval on smaller evidence packages
- Aspen Neuroscience (ANPD-001) is developing autologous iPSC-derived DA neurons -- individualized manufacturing per patient, entered Phase 1 in 2024, raised $115M Series C. Autologous avoids immunosuppression but is far more expensive and difficult to scale
- Oryon Cell Therapies and UniXell Biotechnology (UX-DA001, autologous iPSC, Phase 1 started 2025) are earlier-stage competitors
- Key modality distinction: cell replacement therapies aim to restore dopamine production directly, which is mechanistically orthogonal to disease modification approaches targeting alpha-synuclein ([[prasinezumab]], [[aro-snca|ARO-SNCA]]) or genetic pathways ([[biib122|LRRK2]], [[pariceract|GBA1]]). Cell therapy could complement rather than compete with those approaches
- If raguneprocel approved: establishes iPSC regulatory precedent globally, accelerates Sumitomo's broader regenerative medicine pipeline, puts pressure on BlueRock to differentiate on efficacy data in Phase 3
- If raguneprocel rejected: sets back the iPSC field broadly, strengthens ESC-derived [[bemdaneprocel]]'s positioning as the "safer" regulatory bet

## Analysis

Raguneprocel represents a watershed moment for regenerative medicine: the first iPSC-derived cell therapy to reach NDA filing for any indication worldwide. The February 19, 2026, MHLW committee review is the most important near-term catalyst in the entire cell therapy field. Japan's Regenerative Medicine framework allows conditional approval based on smaller datasets than FDA or EMA would require, which is both an advantage (faster path) and a limitation (conditional approval requires post-marketing confirmatory studies and may not be accepted by other regulators as sufficient evidence).

**Analytical estimate -- Probability of Japan conditional approval: 65-75%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Japan's Regenerative Medicine conditional approval pathway has a high acceptance rate for products that clear safety hurdles -- starting point ~60%
- Adjustments upward: clean safety profile in N=7 with no SAEs or tumors (+10%), PET imaging confirming dopamine production (+10%), priority review designation granted (+5%), strong institutional backing from CiRA/Kyoto University (+5%), national strategic interest in iPSC technology (+5%)
- Adjustments downward: very small N=7 open-label trial (-10%), no randomized controlled efficacy data (-10%), manufacturing scalability questions (-5%)
- Net: ~65-75%

**Signal analysis:**
- Sumitomo's corporate restructuring tells a clear story: establishing RACTHERA as a dedicated JV (Feb 2025), filing NDA (Aug 2025), and investing in S-RACMO manufacturing capacity are all consistent with a company preparing for commercial launch, not hedging its bets. This level of organizational commitment is a strong conviction signal.
- The Japan-first strategy is rational: Japan's regulatory framework for regenerative medicine is uniquely accommodating, and CiRA's iPSC Cell Stock Project is a Japanese national asset. First approval in Japan creates a reference point for subsequent US and EU filings, even if those require larger confirmatory trials.
- The transition from investigator-initiated trial (Kyoto University) to company-sponsored studies (UCSD, Sumitomo Phase 1) signals the classic academic-to-commercial handoff. The US program will be critical for global commercial potential but is years behind the Japan timeline.
- For the broader cell therapy field: raguneprocel approval would validate that iPSC-derived neurons can survive, function, and not form tumors in human brain -- the fundamental proof-of-concept question. This de-risks [[bemdaneprocel]] and every other cell therapy approach to PD, even though they use different source cells. Conversely, any safety signal (tumor, immune rejection) would damage the entire field.

## References

### Clinical Trials
- [Kyoto University Phase I/II (UMIN)](https://center6.umin.ac.jp/cgi-open-bin/ctr_e/ctr_view.cgi?recptno=R000038278) — UMIN000033564

### Key Publications
- [Phase I/II trial of iPS-cell-derived dopaminergic cells for Parkinson's disease | Nature (Apr 2025)](https://www.nature.com/articles/s41586-025-08700-0)
- [Pre-clinical study of iPSC-derived dopaminergic progenitor cells for PD | Nature Communications (2020)](https://www.nature.com/articles/s41467-020-17165-w)
- [iPS cell-based therapy for Parkinson's disease: A Kyoto trial | PubMed (2021)](https://pubmed.ncbi.nlm.nih.gov/33490319/)
- [Preparing for first human trial of iPSC-derived cells for PD: interview with Jun Takahashi | PubMed (2019)](https://pubmed.ncbi.nlm.nih.gov/30644333/)
- [Clinical trial highlights: Dopamine cell-replacement therapies | Journal of Parkinson's Disease (2026)](https://journals.sagepub.com/doi/10.1177/1877718X251397277)

### Press Releases & Filings
- [Sumitomo Pharma NDA submission announcement (Aug 5, 2025)](https://www.sumitomo-pharma.com/news/20250805-2.html)
- [Sumitomo Chemical NDA submission announcement (Aug 5, 2025)](https://www.sumitomo-chem.co.jp/english/news/files/docs/20250805_2e.pdf)
- [Sumitomo Chemical and Sumitomo Pharma establish RACTHERA JV (Dec 17, 2024)](https://www.sumitomo-pharma.com/news/20241217-2.html)
- [US investigator-initiated study initiation at UCSD (Dec 26, 2023)](https://www.sumitomo-pharma.com/news/20231226.html)
- [Company-sponsored US clinical study initiation (Mar 28, 2024)](https://www.sumitomo-pharma.com/news/20240328.html)
- [CiRA press release: iPSC therapy demonstrates safety and efficacy (Apr 17, 2025)](https://www.cira.kyoto-u.ac.jp/e/pressrelease/news/250417-000000.html)

### Regulatory & Market
- [Sumitomo Pharma MHLW committee review notification (Feb 13, 2026)](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260213/20260213562131.pdf)
- [Sumitomo Pharma iPSC therapy heads to Japan regulatory review | TipRanks](https://www.tipranks.com/news/company-announcements/sumitomo-pharmas-ips-cell-parkinsons-therapy-heads-to-key-japan-regulatory-review)
- [Sumitomo Parkinson's filing a pivotal moment for Japan's iPSC ambitions | Scrip/Citeline](https://insights.citeline.com/scrip/advanced-therapies/cell-therapies/sumitomo-parkinsons-filing-a-pivotal-moment-for-japans-ipsc-ambitions-I6FBZWYP4BGVLFKRMGL5V4DM4A/)
- [Japan Times: Drugmaker seeks approval for stem cell treatment for Parkinson's](https://www.japantimes.co.jp/news/2025/08/05/japan/science-health/parkinsons-ips-approval-application/)
