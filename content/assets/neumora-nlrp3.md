---
drug_name: "NMRA-NLRP3"
aliases: ["NMRA-215"]
target: "NLRP3 inflammasome"
mechanism: "Oral, brain-penetrant small molecule NLRP3 inflammasome inhibitor blocking neuroinflammatory cytokine release (IL-1beta/IL-18) to reduce microglial-driven neurodegeneration"
modality: "small molecule"
developer: "Neumora Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "NMRA"
partner: "Parkinson's UK"
partner_type: "academic"
stage: "Preclinical"
status: "Active"
patient_population: "Parkinson's disease (planned)"
route_of_administration: "oral"
key_biomarkers: ["IL-1beta", "IL-18", "hsCRP"]
confidence_rating: "2/10"
next_catalyst: "Completion of IND-enabling studies (Parkinson's UK-funded)"
catalyst_date: "2026-2027"
thesis_cluster: "neuroinflammation"
tags: [pd-pipeline, claude]
date: 2026-02-16
company_link: "[[companies/neumora-therapeutics]]"
partner_link: "[[companies/parkinsons-uk]]"
---

# NMRA-NLRP3

## Summary

NMRA-NLRP3 is Neumora Therapeutics' (biotech, NMRA) oral, brain-penetrant NLRP3 inflammasome inhibitor with Parkinson's disease listed as a secondary indication behind obesity. Parkinson's UK invested GBP 2.1M through its Virtual Biotech programme in March 2024 to fund IND-enabling preclinical studies -- two-species safety, PK, drug interactions, and formulation work needed for a clinical filing. Neumora's pipeline page now lists this compound as "NMRA-215" with dual obesity/PD indications, but the PD program has no disclosed timeline, no published preclinical PD efficacy data, and no IND filing target date. Obesity is the clear lead indication, with Phase 1 expected in H1 2026 and weight loss data by year-end 2026. The key differentiator claimed is "best-in-class brain penetration," which would matter for PD but has not been quantified publicly (no CSF:plasma ratio, no IC50, no head-to-head vs. [[vtx3232|VTX3232]] or [[nt-0796|NT-0796]]). If the obesity Phase 1 confirms CNS penetration and clean safety, the PD program could accelerate on the back of that data package; if the obesity program fails or Neumora deprioritizes CNS indications, the PD program likely dies as a grant-funded side project without internal champion.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Parkinson's UK (Virtual Biotech) |
| Deal Date | March 2024 |
| Upfront | GBP 2.1M (grant) |
| Total (Biobucks) | GBP 2.1M |
| Deal Type | Partnership |

## Notes

### Science
- NLRP3 inflammasome is an intracellular multi-protein complex in microglia and peripheral immune cells; when activated by damage-associated molecular patterns (DAMPs) including alpha-synuclein aggregates, it triggers caspase-1 activation, IL-1beta/IL-18 release, and pyroptotic cell death
- Claimed to be "highly brain-penetrant" -- critical for PD where neuroinflammation is a central process, but no quantitative BBB data disclosed (CSF:plasma ratio, brain Cmax, IC50 for NLRP3 assembly)
- NLRP3 genetic validation for PD is weak: a 2024 large-scale Mendelian randomization study found no association between NLRP3 variants and PD risk, creating a disconnect between strong preclinical inflammatory cascades and absent genetic causation
- The same compound is being developed for obesity (hypothalamic neuroinflammation → appetite dysregulation), which means the molecule was likely optimized for hypothalamic penetration, not necessarily substantia nigra or basal ganglia exposure
- Key scientific question: is brain penetration sufficient in PD-relevant regions (midbrain, substantia nigra), or was the compound optimized for hypothalamic exposure relevant to obesity?
- Competes in a crowded NLRP3 space where [[vtx3232|VTX3232]] (Lilly) already has Phase 2a PD motor data and [[nt-0796|NT-0796]] (NodThera) has Phase 1b/2a CSF biomarker proof in PD patients

### Clinical
No clinical trials initiated for PD.

- **IND-enabling studies (Parkinson's UK-funded):** GBP 2.1M grant supports two-species toxicology, safety pharmacology, drug-drug interaction studies, and ADME characterization required for IND filing. Timeline: 2-year project from March 2024 grant date (completion expected ~2026)
- **Obesity Phase 1 (NMRA-215):** Expected H1 2026 initiation; weight loss data by end-2026. This trial will generate human PK/safety data relevant to PD development but is not a PD trial
- No NCT numbers registered for PD indication
- No published PD-specific preclinical efficacy data (alpha-synuclein models, dopaminergic neuroprotection, microglial activation endpoints)

### Financial
- **Neumora total funding:** ~$612M raised across Series A ($500M, including $100M Amgen), Series B ($112M), and September 2023 IPO
- **Cash position:** $171.5M as of Q3 2025; runway into Q3 2027
- **Market cap:** ~$515M (February 2026)
- **PD investment:** Entirely grant-funded (GBP 2.1M from Parkinson's UK). No disclosed internal R&D spend on PD NLRP3 program
- **Context:** Neumora's capital allocation is focused on navacaprant (Phase 3 depression, lead asset), NMRA-511 (Phase 1b Alzheimer's agitation), and NMRA-215 obesity. PD is not a stated capital priority
- **Comparison:** GBP 2.1M grant-funded IND-enabling work vs. Lilly's $1.2B acquisition of Ventyx for [[vtx3232|VTX3232]], or NodThera's venture-funded Phase 1b/2a of [[nt-0796|NT-0796]]. The investment differential is ~500x, signaling PD is exploratory for Neumora, not a strategic commitment

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "NLRP3") AND file.name != "neumora-nlrp3"
SORT stage DESC
```

- Enters one of the most crowded PD target classes: at least 6 NLRP3 programs with PD data or active PD trials
- [[vtx3232|VTX3232]] (Lilly/Ventyx) is the clinical leader with Phase 2a open-label PD data showing motor improvement and CSF biomarker engagement; acquired for $1.2B in January 2026
- [[nt-0796|NT-0796]] (NodThera) completed Phase 1b/2a in PD patients with CSF IL-1beta, sTREM2, and NfL reductions -- the first placebo-controlled biomarker proof for brain NLRP3 inhibition in PD
- [[dapansutrile]] (Olatec) is in a Phase 2 PD trial at Cambridge, also brain-penetrant and oral
- [[ism8969|ISM8969]] (Insilico/Hygtia) received FDA IND clearance January 2026 for PD, entering Phase 1
- [[selnoflast]] (Roche) is peripherally restricted and Phase 1b PD results remain undisclosed -- if the peripheral approach fails, it strengthens the case for brain-penetrant compounds like NMRA-NLRP3
- [[vent-02|VENT-02]] (Ventus) was terminated mid-Phase 2a in PD (October 2025) -- a negative signal for the NLRP3/PD thesis overall
- NMRA-NLRP3's only stated differentiator is "best-in-class brain penetration," which remains unquantified and unverified against [[vtx3232|VTX3232]] or [[nt-0796|NT-0796]] benchmarks

## Analysis

NMRA-NLRP3 is best understood as a grant-funded exploratory program within a company whose strategic priorities lie elsewhere. Neumora's capital, management attention, and pipeline milestones are concentrated on depression (navacaprant Phase 3), Alzheimer's agitation (NMRA-511), schizophrenia (M4 PAM franchise), and obesity (NMRA-215). PD does not appear in the company's January 2026 pipeline strategy press release. The GBP 2.1M Parkinson's UK grant funds IND-enabling work, but there is no evidence of matching internal investment, no disclosed PD-specific preclinical data, and no IND filing timeline.

**Analytical estimate -- Probability of reaching Phase 1 for PD: 15-20%.** This is our assessment, not from a published source. The reasoning: the IND-enabling studies are funded and the compound appears to be brain-penetrant, which provides a floor (~25% base for funded preclinical programs to reach IND). However, PD is a secondary indication behind obesity, the company has no stated PD commitment beyond the grant, the NLRP3/PD field is increasingly crowded with more advanced competitors, and Neumora's cash runway into Q3 2027 creates pressure to focus on value-driving programs (navacaprant readout, obesity data). Downward adjustments for deprioritization risk (-10%) and competitive crowding (-5%) bring the estimate to 15-20%.

The most informative near-term signal will be the NMRA-215 obesity Phase 1 data (expected late 2026). If that study confirms robust brain penetration and clean human safety, the PD IND becomes a low-marginal-cost filing using the same toxicology package. If the obesity program stumbles -- safety signal, poor PK, company restructuring -- the PD program has no independent survival path. The Parkinson's UK grant provides external accountability (deliverables, timelines) that an internal exploratory program would lack, which modestly increases the probability of completion.

For the broader NLRP3/PD thesis, NMRA-NLRP3 adds one more data point to the "brain-penetrant" camp alongside [[vtx3232|VTX3232]], [[nt-0796|NT-0796]], [[dapansutrile]], and [[ism8969|ISM8969]], but it is the least advanced and least committed of the group. The program's primary value is as an option: if [[vtx3232|VTX3232]] Phase 2b validates NLRP3 inhibition in PD, a differentiated brain-penetrant molecule from Neumora could attract partnership interest. Without that external validation, NMRA-NLRP3 is unlikely to advance on its own.

## References

### Key Publications
- [NLRP3 inflammasome and neuroinflammation in PD | MJFF Grant (2015)](https://www.michaeljfox.org/foundation/grant-detail.php?grant_id=1430) -- Early academic validation of NLRP3 targeting in PD models

### Press Releases & Filings
- [Parkinson's UK invests GBP 2.1M in Neumora for NLRP3 PD program | Parkinson's UK (Apr 2024)](https://www.parkinsons.org.uk/news/parkinsons-uk-invests-potential-new-drug-targeting-brain-inflammation)
- [Parkinson's UK invests GBP 2.1M in Neumora Therapeutics | News-Medical (Apr 2024)](https://www.news-medical.net/news/20240427/Parkinsone28099s-UK-invests-c2a321-million-in-Neumora-Therapeutics-for-preclinical-testing-of-new-Parkinsone28099s-drug.aspx)
- [Neumora Therapeutics Highlights 2026 Pipeline Strategy | GlobeNewsWire (Jan 2026)](https://www.globenewswire.com/news-release/2026/01/05/3212570/0/en/Neumora-Therapeutics-Highlights-2026-Pipeline-Strategy-and-Anticipated-Upcoming-Milestones.html)
- [NMRA-215 Class-Leading Weight Loss in DIO Model | Neumora IR (Oct 2025)](https://ir.neumoratx.com/news-releases/news-release-details/neumora-therapeutics-announces-class-leading-weight-loss)
- [Neumora Q3 2025 Financial Results | Neumora IR (Nov 2025)](https://ir.neumoratx.com/news-releases/news-release-details/neumora-therapeutics-reports-third-quarter-2025-financial)
- [Neumora Pipeline Page](https://neumoratx.com/pipeline/)
