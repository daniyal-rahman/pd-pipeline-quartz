---
drug_name: "Duopa"
aliases: ["Duodopa", "LCIG", "carbidopa/levodopa enteral suspension", "ABT-SLV187", "levodopa-carbidopa intestinal gel"]
target: "dopamine replacement (continuous intestinal levodopa delivery)"
mechanism: "Continuous intrajejunal infusion of carbidopa/levodopa gel bypasses erratic gastric emptying to maintain steady-state plasma levodopa levels, reducing motor fluctuations in advanced PD"
modality: "drug-device combination"
developer: "AbbVie"
company_type: "big pharma"
publicly_traded: true
ticker: "ABBV"
stage: "Approved"
status: "Active"
patient_population: "Advanced PD with severe motor fluctuations not adequately controlled by oral levodopa"
route_of_administration: "intrajejunal (PEG-J)"
key_biomarkers: ["OFF time (patient diary)", "ON time without troublesome dyskinesia"]
next_catalyst: "Progressive displacement by VYALEV (subcutaneous foslevodopa/foscarbidopa)"
catalyst_date: "2025-2027 (transition period)"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-20
company_link: "[[companies/abbvie]]"
---

# Duopa (Carbidopa/Levodopa Enteral Suspension)

## Summary

Duopa is the incumbent continuous levodopa delivery system for advanced PD, FDA-approved January 2015, generating ~$447M globally in 2024 (as Duodopa ex-US). It proved that continuous dopaminergic stimulation reduces OFF time by ~2 hours vs. oral IR levodopa, but surgical PEG-J placement, tube complications (~50% J-tube issues, ~36% PEG issues), and the CADD-Legacy pump's bulk limit uptake to ~10,000 patients globally. AbbVie's own [[vyalev|VYALEV]] (subcutaneous foslevodopa/foscarbidopa, FDA-approved October 2024) is designed to replace it -- same continuous delivery thesis, no surgery, 24-hour infusion vs. 16-hour. Duopa's commercial trajectory is now in managed decline; the strategic question is how fast VYALEV cannibalization occurs and whether [[nd0612|ND0612]] (NeuroDerm/Mitsubishi Tanabe) captures share during the transition.

## Notes

### Science
- **Core pharmacology:** Carbidopa (4.63 mg/mL) + levodopa (20 mg/mL) suspended in a carboxymethylcellulose gel. The gel formulation prevents the solubility issues that limit aqueous levodopa concentrations.
- **Delivery rationale:** Oral levodopa has 30-60 min half-life and erratic gastric emptying in PD patients (gastroparesis is common). This creates pulsatile dopamine receptor stimulation that drives motor fluctuations and dyskinesia. Continuous jejunal delivery bypasses the stomach entirely and maintains plasma levodopa within a narrow therapeutic window.
- **Device system:** PEG-J tube (percutaneous endoscopic gastrostomy with jejunal extension) connected to a portable CADD-Legacy 1400 infusion pump. The pump delivers a morning bolus plus continuous infusion over ~16 hours (typically stopped overnight). The cassette holds one day's supply (~100 mL).
- **Distinction from oral extended-release formulations:** [[ipx203|IPX-203]] and [[rytary|Rytary]] attempt to smooth oral levodopa delivery but still rely on gastric emptying, which is the fundamental bottleneck in advanced PD. Duopa eliminates this variable entirely.
- **Key limitation:** The PEG-J tube is a surgical intervention requiring endoscopic placement, and the jejunal extension frequently migrates or kinks. This is the fundamental design flaw that VYALEV and [[nd0612|ND0612]] solve by moving to subcutaneous delivery.

### Clinical

**S187.3.002 (Phase 3 Pivotal)** | NCT00660387 | N=71 | Advanced PD with motor fluctuations
- **Primary endpoint:** Change in mean daily OFF time at 12 weeks → **-1.91 hours vs. oral LC-IR (p=0.0015)**
- **Key secondary:** ON time without troublesome dyskinesia → **+1.86 hours vs. oral LC-IR (p=0.006)**
- **Safety:** Most common AEs were device/procedure-related: complication of device insertion (57%), nausea (30%), incision site erythema (19%). Depression (11% vs. 3%), peripheral edema (8% vs. 0%).
- **Status:** Completed (basis for FDA approval January 12, 2015)
- **Interpretation:** Small trial (N=71) with large effect size. The ~2-hour OFF time reduction vs. optimized oral therapy was clinically meaningful and exceeded what oral extended-release formulations achieve. However, the 12-week duration was short for a surgical intervention meant to be permanent, and the double-dummy design (all patients received PEG-J) complicates real-world generalizability.

**S187.3.001 (Phase 3 Supportive)** | NCT00357994 | N=354 (open-label) | Advanced PD
- **Primary endpoint:** Safety and tolerability over 12 months
- **Key findings:** Mean OFF time reduction maintained at -4.4 hours from baseline at 12 months. Discontinuation rate ~18%, primarily due to device complications and AEs.
- **Status:** Completed
- **Interpretation:** Confirmed durability of benefit but highlighted the ongoing device burden -- nearly 1 in 5 patients stopped within a year.

**DYSCOVER (Phase 3b)** | NCT02799381 | Advanced PD with dyskinesia
- **Primary endpoint:** Unified Dyskinesia Rating Scale → LCIG significantly improved dyskinesia vs. optimized medical treatment
- **Status:** Completed
- **Interpretation:** Extended the clinical story beyond OFF time to show dyskinesia improvement, broadening the label narrative.

**DUOGLOBE (Observational)** | NCT02611713 | N=195 (15 countries) | Real-world advanced PD
- **Primary endpoint:** OFF time change at 12 months → **-3.1 hours from baseline** (p<0.001)
- **3-year results:** Sustained OFF time reduction; ~30% of patients experienced device-related serious AEs over 3 years
- **Status:** Completed (3-year final results published 2023)
- **Interpretation:** Real-world data confirmed pivotal trial efficacy but also confirmed the device complication burden at scale. The 30% serious device-AE rate over 3 years is the data point that makes the case for subcutaneous alternatives.

### Financial
- **2024 global revenue:** $447M total ($96M US Duopa + $351M ex-US Duodopa; down 4.7% from $468M in 2023) [source](https://news.abbvie.com/2025-01-31-AbbVie-Reports-Full-Year-2024-Financial-Results)
- **Revenue trajectory:** Declining. Peaked in the ~$500M range. VYALEV launch (October 2024 US, EU approval pending) will accelerate decline.
- **VYALEV peak sales estimate:** >$2B (Evercore ISI), which implies AbbVie expects VYALEV to capture the Duopa installed base plus expand the market by removing the surgical barrier.
- **Global footprint:** Approved in 41 countries. Branded as Duopa (US), Duodopa (EU, Japan, rest of world).
- **Pricing context:** Duopa costs ~$80,000-$100,000/year in the US (drug + device + procedure), making it one of the most expensive PD therapies. This price point is sustainable because the patient population is small (~10,000 globally) and the alternative is frequent hospitalizations for uncontrolled motor fluctuations.
- **Competitive pricing pressure:** [[nd0612|ND0612]] subcutaneous levodopa/carbidopa (if approved) and VYALEV will compete on convenience; pricing is expected to be in a similar range.

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[sana-program]] | Preclinical | Deprioritized | Sana Biotechnology | cell therapy (iPSC allogeneic) |
| [[alc01]] | Phase 1 | Active | iCamuno Biotherapeutics | cell therapy (iPSC allogeneic) |
| [[autologous-mdaps]] | Phase 1 | Active | McLean Hospital / Neuroregeneration Research Institute (NRI) | cell therapy (iPSC autologous) |
| [[cellino-ipsc]] | Phase 1 | Active | Cellino Biotech | platform |
| [[lu-af28996]] | Phase 1 | Active | Lundbeck | small molecule |
| [[rndp-001]] | Phase 1 | Active | Kenai Therapeutics | cell therapy (iPSC allogeneic) |
| [[ux-da001]] | Phase 1 | Active | UniXell Biotechnology | cell therapy (iPSC autologous) |
| [[ser-252]] | Phase 1b | Active | Serina Therapeutics | small molecule |
| [[anpd001]] | Phase 1/2 | Active | Aspen Neuroscience | cell therapy (iPSC autologous) |
| [[dive-inbrain]] | Phase 1/2 | Active | InBrain Pharma | device-aided therapy (drug/device combination) |
| [[kyoto-ipsc]] | Phase 1/2 | Active | CiRA (Kyoto University) / Sumitomo Pharma | cell therapy (iPSC allogeneic) |
| [[nouvneu001]] | Phase 1/2 | Active | iRegene Therapeutics | cell therapy (iPSC allogeneic) |
| [[sizhe-biopharma]] | Phase 1/2 | Active | XellSmart / Shize Bio (士泽生物) | cell therapy (iPSC allogeneic) |
| [[stem-pd]] | Phase 1/2 | Active | Lund University / University of Cambridge | cell therapy (ESC) |
| [[ted-a9]] | Phase 1/2 | Active | S.BIOMEDICS | cell therapy (ESC) |
| [[vgn-r09b]] | Phase 1/2 | Active | Shanghai Vitalgen BioPharma | AAV gene therapy |
| [[cbt-npc]] | Phase 2 | Active | CHA Biotech | cell therapy (ESC) |
| [[glovadalen]] | Phase 2 | Active | UCB | small molecule |
| [[bemdaneprocel]] | Phase 3 | Active | BlueRock Therapeutics | cell therapy (ESC) |
| [[mesdopetam]] | Phase 3 | Active | IRLAB Therapeutics | small molecule |
| [[p2b001]] | Phase 3 | Active | Pharma Two B | small molecule |
| [[raguneprocel]] | NDA Filed | Active | Sumitomo Pharma / RACTHERA | cell therapy (iPSC allogeneic) |
| [[tavapadon]] | NDA Filed | Active | Cerevel Therapeutics | small molecule |
| [[apokyn]] | Approved | Active | Supernus Pharmaceuticals | small molecule |
| [[carbidopa-levodopa]] | Approved | Active | Multiple (generic) | small molecule |
| [[crexont]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[duopa]] | Approved | Active | AbbVie | drug-device combination |
| [[gocovri]] | Approved | Active | Supernus Pharmaceuticals | small molecule |
| [[ipx203]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[neupro]] | Approved | Active | UCB | small molecule |
| [[rytary]] | Approved | Active | Amneal Pharmaceuticals | small molecule |
| [[vyalev]] | Approved | Active | AbbVie | drug-device combination |

- **[[vyalev|VYALEV]] (AbbVie):** The direct successor. Subcutaneous foslevodopa/foscarbidopa via wearable pump, FDA-approved October 2024. 24-hour continuous infusion (vs. Duopa's 16-hour), no surgery, reduces morning akinesia. AbbVie will manage the transition to protect the combined franchise revenue. Phase 3 showed +2.72 hours ON time vs. +0.9 hours for oral control.
- **[[nd0612|ND0612]] (NeuroDerm/Mitsubishi Tanabe):** Subcutaneous levodopa/carbidopa infusion pump. FDA rejected June 2024 (CMC/device issues); resubmitted May 2025. If approved, competes directly with VYALEV for the same post-Duopa market. ND0612 uses levodopa itself (not a prodrug), which creates formulation challenges at the injection site.
- **[[ipx203|IPX-203]] (Amneal/Impel):** Extended-release oral carbidopa/levodopa. Addresses the mild-to-moderate fluctuation segment that Duopa doesn't reach. Not a direct competitor for advanced PD patients who have failed oral optimization.
- **[[rytary|Rytary]] (Amneal):** Extended-release oral carbidopa/levodopa capsules (IPX066). Similar positioning to IPX-203 -- oral extended-release, used before patients progress to device-based therapy. Duopa patients are typically Rytary failures.
- **Apomorphine pumps (Britannia):** Subcutaneous apomorphine continuous infusion, available in EU but not US. Competes in the same advanced PD space but uses a dopamine agonist rather than levodopa, with a different side-effect profile (nausea, nodules, neuropsychiatric).

## Analysis

Duopa validated the continuous dopaminergic stimulation hypothesis in a rigorous double-blind trial -- an achievement that underpins the entire therapeutic class including VYALEV and [[nd0612|ND0612]]. The ~2-hour OFF time reduction vs. optimized oral therapy set the efficacy benchmark. But the PEG-J delivery system is the product's fatal flaw: tube complications in ~50% of patients, surgical barrier to adoption, and 16-hour-only infusion that leaves overnight gaps. These limitations capped the addressable market at ~10,000 patients globally despite an estimated 1-2 million advanced PD patients who could benefit from continuous levodopa delivery.

**Analytical estimate -- Duopa revenue trajectory: decline to <$200M by 2028.** This is our assessment, not from a published source. The reasoning: VYALEV offers the same continuous levodopa thesis without surgery, with 24-hour coverage, and is marketed by the same company (AbbVie) that controls Duopa prescriber relationships. AbbVie has every incentive to migrate patients to VYALEV, which has higher peak sales potential ($2B+) by expanding the market beyond surgery-eligible patients. The transition will be gradual -- existing Duopa patients on stable therapy may not switch immediately, and VYALEV's infusion site reaction profile needs real-world validation. But new starts will overwhelmingly go to VYALEV or (if approved) [[nd0612|ND0612]].

The strategic significance of Duopa in 2026 is as a proof-of-concept for continuous levodopa delivery, not as a growth asset. Every subcutaneous levodopa program in development -- VYALEV, [[nd0612|ND0612]], and others -- builds on the clinical evidence base that Duopa established. AbbVie's ability to execute a franchise transition from Duopa to VYALEV without revenue disruption is the key commercial question. The parallels to AbbVie's Humira-to-Skyrizi/Rinvoq transition in immunology are instructive: AbbVie is experienced at managing product succession within a therapeutic class.

## References

### Clinical Trials
- [S187.3.002 Phase 3 Pivotal](https://clinicaltrials.gov/ct2/show/NCT00660387) -- NCT00660387
- [S187.3.001 Phase 3 Open-Label](https://clinicaltrials.gov/ct2/show/NCT00357994) -- NCT00357994 / NCT00335153
- [DYSCOVER Phase 3b](https://clinicaltrials.gov/ct2/show/NCT02799381) -- NCT02799381
- [DUOGLOBE Observational](https://clinicaltrials.gov/ct2/show/NCT02611713) -- NCT02611713

### Key Publications
- [Olanow et al. Continuous intrajejunal infusion of levodopa-carbidopa intestinal gel for patients with advanced PD | Lancet Neurology (2014)](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(13)70293-X/abstract)
- [DUOGLOBE 3-Year Final Results | J Parkinsons Dis (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10473130/)
- [Long-Term PEG-J Tube Safety in Patients With Advanced PD | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4822096/)
- [The Long-Term Impact of LCIG on OFF-time: Systematic Review | Advances in Therapy (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8189983/)
- [24-Hour LCIG Clinical Experience and Practical Recommendations | CNS Drugs (2020)](https://link.springer.com/article/10.1007/s40263-020-00782-w)
- [Impact of tube replacement timing on PEG-J AEs | BMC Neurology (2021)](https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-021-02269-7)

### Press Releases & Filings
- [AbbVie FDA Approval Announcement (Jan 2015)](https://news.abbvie.com/2015-01-12-AbbVie-Announces-U-S-FDA-Approval-of-DUOPA-TM-carbidopa-and-levodopa-Enteral-Suspension-for-the-Treatment-of-Motor-Fluctuations-in-Patients-with-Advanced-Parkinsons-Disease)
- [AbbVie VYALEV FDA Approval (Oct 2024)](https://news.abbvie.com/2024-10-17-U-S-FDA-Approves-VYALEV-TM-foscarbidopa-and-foslevodopa-for-Adults-Living-with-Advanced-Parkinsons-Disease)
- [Duodopa Sales History and Forecasts | DrugAnalyst](https://www.druganalyst.com/AbbVie/Duodopa)

### Regulatory & Market
- [FDA Prescribing Information -- Duopa](https://www.rxabbvie.com/pdf/duopa_pi.pdf)
- [FDA Approves Duopa | MJFF](https://www.michaeljfox.org/news/fda-approves-duopa-carbidopalevodopa-enteral-suspension-method-new-us-market)
- [EU Orphan Designation EU/3/01/035 | EMA](https://www.ema.europa.eu/en/medicines/human/orphan-designations/eu-3-01-035)
- [Vyalev vs. Duopa comparison | Oreate AI](https://www.oreateai.com/blog/vyalev-vs-duopa-a-new-era-in-parkinsons-disease-treatment/d06a8cdbb6af8c7b2eae51d5b2031892)
- [Foslevodopa/Foscarbidopa subcutaneous review | Mov Disord Clin Pract (2024)](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mdc3.14161)
