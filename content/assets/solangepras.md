---
drug_name: "Solengepras"
aliases: ["CVN424", "CVN-424"]
target: "GPR6 (G-protein coupled receptor 6, indirect striatopallidal pathway)"
mechanism: "First-in-class oral GPR6 inverse agonist that reduces constitutive cAMP signaling in D2-MSNs of the indirect pathway, bypassing dopamine receptors to restore motor function without inducing dyskinesia"
modality: "small molecule"
developer: "Cerevance"
company_type: "biotech"
publicly_traded: false
partner: ""
stage: "Phase 3"
status: "Active"
patient_population: "PD with motor fluctuations on stable levodopa (adjunctive); early untreated PD (monotherapy)"
route_of_administration: "oral"
key_biomarkers: ["daily OFF-time (Hauser diary)", "MDS-UPDRS Parts II+III"]
confidence_rating: "6/10"
next_catalyst: "ARISE Phase 3 topline readout"
catalyst_date: "H1 2026"
thesis_cluster: "symptomatic"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/cerevance]]"
---

# Solengepras

## Summary

Solengepras (CVN424) is a first-in-class oral GPR6 inverse agonist from Cerevance (biotech, private) that demonstrated a statistically significant 1.3-hour reduction in daily OFF-time (p=0.02) vs. placebo in a 28-day Phase 2 adjunctive trial (NCT04191577). Cerevance is now running the pivotal Phase 3 ARISE trial (NCT06553027, N=330) with topline data expected H1 2026 -- this is the nearest-term binary catalyst in the PD symptomatic pipeline. A separate Phase 2 ASCEND monotherapy trial in early PD showed non-significant motor improvement but trends favoring non-motor symptoms. If ARISE succeeds, solengepras becomes the first non-dopaminergic oral adjunctive therapy for PD motor fluctuations, opening a novel mechanism class. If it fails, the GPR6 target is unvalidated clinically and Cerevance faces existential risk as a private company with this as its lead asset.

## Notes

### Science
- GPR6 is an orphan GPCR with high constitutive Gs-coupled activity, expressed selectively on D2-type medium spiny neurons (MSNs) in the striatum -- the same neurons that form the indirect striatopallidal pathway
- In PD, dopamine depletion leads to hyperactivation of the indirect pathway (D2-MSNs are disinhibited), which produces bradykinesia and rigidity. Standard dopaminergic therapies (levodopa, D2 agonists) suppress this pathway by activating D2 receptors, but cause dyskinesia by simultaneously overstimulating the direct pathway
- GPR6 inverse agonism reduces constitutive cAMP in D2-MSNs, mimicking dopamine's inhibitory effect on the indirect pathway **without** engaging dopamine receptors -- theoretically allowing motor benefit without dyskinesia risk
- This is a genuinely novel, non-dopaminergic mechanism. GPR6 was identified through Cerevance's NETSseq (Nuclear Enriched Transcript Sort sequencing) platform, which profiles cell-type-specific gene expression in post-mortem human brain tissue
- CVN424 reversed haloperidol-induced catalepsy in rats and restored mobility in bilateral 6-OHDA-lesioned rat PD models, confirming in vivo normalization of basal ganglia circuitry
- Key scientific question: does a 28-day Phase 2 signal (1.3h OFF-time reduction) replicate and persist over 12 weeks in a larger, global Phase 3? The short treatment duration in Phase 2 leaves durability unproven
- The Phase 2 data showed increased ON-time without troublesome dyskinesia, without worsening of ON-time with troublesome dyskinesia -- consistent with the non-dopaminergic mechanism hypothesis

### Clinical

**Phase 1 (First-in-Human)** | NCT03657030 | N=multiple ascending dose cohorts | Healthy volunteers
- **Primary endpoint:** Safety/tolerability/PK --> Clean safety profile; no serious or severe adverse events
- **Key secondary:** Single doses 1-225 mg and repeated daily doses (25, 75, 150 mg for 7 days) well tolerated; no clinically significant vital sign or lab changes
- **Status:** Completed
- **Interpretation:** Established favorable PK/safety profile; enabled Phase 2 progression

**Phase 2 (Adjunctive)** | NCT04191577 | N=141 (randomized 1:1:1) | PD patients, Hoehn & Yahr 2-4, on stable levodopa, >=2h daily OFF-time
- **Primary endpoint:** Change from baseline in daily OFF-time at Day 27 --> CVN424 150 mg: -1.6h from baseline (-1.3h placebo-adjusted, p=0.02); CVN424 50 mg: -1.3h from baseline (not significant vs. placebo)
- **Key secondary:** Increase in ON-time without troublesome dyskinesia; no meaningful worsening of ON-time with troublesome dyskinesia
- **Safety:** Headache (9% at 150 mg vs. 2% placebo), nausea (6% at 150 mg vs. 2% placebo); no serious treatment-related AEs
- **Status:** Completed; published in eClinicalMedicine (Lancet Discovery Science, Oct 2024)
- **Interpretation:** Clinically meaningful OFF-time reduction at 150 mg despite short 28-day treatment period and small sample (47/arm). The dyskinesia-sparing profile supports non-dopaminergic mechanism. Short duration is the main limitation -- 12-week Phase 3 will test durability.

**ASCEND (Phase 2, Monotherapy)** | NCT06006247 | N=62 | Early PD, dopaminergic-therapy naive
- **Primary endpoint:** Change from baseline in MDS-UPDRS Parts II+III at 12 weeks --> Small, non-statistically significant improvement vs. placebo
- **Key secondary:** Trends favoring solengepras on MDS-UPDRS Part I (-1.38, p=0.12), Non-Motor Symptoms Scale (-1.7, p=0.59), Epworth Sleepiness Scale (-0.3, p=0.62)
- **Safety:** 100% treatment arm completion; no discontinuations due to drug-related AEs; no serious AEs; majority of AEs mild and transient
- **Status:** Completed; topline results presented at AD/PD 2025 (April 2025)
- **Interpretation:** Monotherapy miss is not fatal to the program -- the adjunctive setting (motor fluctuations on levodopa) is the registrational path. The non-motor trends are hypothesis-generating for GPR6's broader role in PD symptoms. Small sample (N=62) was underpowered.

**ARISE (Phase 3, Pivotal)** | NCT06553027 | N=330 | PD with motor fluctuations on stable levodopa
- **Primary endpoint:** Change from baseline in daily OFF-time at 12 weeks
- **Design:** Randomized, double-blind, placebo-controlled; 3 arms (solengepras 75 mg, 150 mg, placebo); ~20 US sites + 1 Philippines site
- **Status:** First patient dosed November 2024; topline data expected H1 2026
- **Interpretation:** Pivotal registrational trial. 12-week duration addresses the main Phase 2 limitation (28-day treatment). Testing two doses provides dose-response data for regulatory package. This readout is the next binary event.

### Financial
- **Private company:** Cerevance has raised ~$204-214M total across 6 rounds
- **Most recent round:** Series B-1 Extension ($47M, April 2024), bringing total Series B-1 to ~$98M; led by Agent Capital, Bioluminescence Ventures, and Double Point Ventures
- **Key investors:** Gates Frontier (Bill Gates), GV (Google Ventures), Foresite Capital, Casdin Capital, Lightstone Ventures, MQB Partners, LifeRock Ventures
- **No peak sales estimates publicly available** -- as a private company, analyst coverage is limited
- **Context:** A successful ARISE readout would likely trigger either a licensing deal with a large pharma partner or IPO. The adjunctive PD motor fluctuation market (OFF-time reduction) is established -- istradefylline (Nourianz, adenosine A2A antagonist) was the last novel mechanism approved in this space (2019), with modest commercial uptake (~$150M peak). Solengepras would need to demonstrate superiority to existing adjunctive therapies (MAO-B inhibitors, COMT inhibitors, istradefylline) to capture meaningful market share
- **Burn rate concern:** Running a 330-patient Phase 3 as a private company implies significant capital deployment; the Series B-1 extension was specifically flagged to fund the Phase 3 trial

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[eladocagene]] | Approved (AADC deficiency); Phase 1b completed (PD — terminated) | Active (AADC deficiency); Discontinued (PD) | PTC Therapeutics | AAV gene therapy |
| [[cavgene]] | Preclinical | Active | CavGene Therapeutics | AAV gene therapy |
| [[lario-cav23]] | Preclinical | Active | Lario Therapeutics | small molecule |
| [[otsuka-program]] | Preclinical | Active | Otsuka Pharmaceutical | Undisclosed |
| [[lu-af28996]] | Phase 1 | Active | Lundbeck | small molecule |
| [[ly03017]] | Phase 1 | Active | Luye Pharma Group | small molecule |
| [[irl757]] | Phase 1b | Active | IRLAB Therapeutics | small molecule |
| [[ser-252]] | Phase 1b | Active | Serina Therapeutics | small molecule |
| [[appello-mglu4]] | Phase 1/2 | Active | Appello Pharmaceuticals | small molecule |
| [[dive-inbrain]] | Phase 1/2 | Active | InBrain Pharma | device-aided therapy (drug/device combination) |
| [[vgn-r09b]] | Phase 1/2 | Active | Shanghai Vitalgen BioPharma | AAV gene therapy |
| [[aav-gad]] | Phase 2 | Active | MeiraGTx | AAV gene therapy |
| [[addex-program]] | Phase 2 | Deprioritized | Addex Therapeutics | small molecule |
| [[blarcamesine]] | Phase 2 | Active | Anavex Life Sciences | small molecule |
| [[glovadalen]] | Phase 2 | Active | UCB | small molecule |
| [[mesdopetam]] | Phase 3 | Active | IRLAB Therapeutics | small molecule |
| [[p2b001]] | Phase 3 | Active | Pharma Two B | small molecule |
| [[solangepras]] | Phase 3 | Active | Cerevance | small molecule |
| [[nd0612]] | NDA Filed | Active | NeuroDerm | small molecule |
| [[tavapadon]] | NDA Filed | Active | Cerevel Therapeutics | small molecule |
| [[ipx203]] | Approved | Active | Amneal Pharmaceuticals | small molecule |

- The primary competitive frame is **non-dopaminergic adjunctive PD therapies**. [[tavapadon|Tavapadon]] (AbbVie) is a D1/D5 partial agonist -- technically still dopaminergic but avoids D2/D3 side effects. [[mesdopetam|Mesdopetam]] (IRLAB/Ipsen) targets levodopa-induced dyskinesia specifically via D3 antagonism
- Istradefylline (Nourianz, Kyowa Kirin) is the closest approved comparator -- also a non-dopaminergic mechanism (adenosine A2A antagonist), also reduces OFF-time, but commercial performance has been modest, suggesting either market access barriers or limited physician adoption for non-dopaminergic mechanisms
- Solengepras' key differentiator is the dyskinesia-sparing profile: unlike levodopa dose escalation or dopamine agonists, GPR6 inverse agonism appears to increase ON-time without worsening dyskinesia. This matters most in advanced PD patients already experiencing levodopa-induced dyskinesia
- Cerevance appears to be the only company developing a GPR6 inverse agonist clinically -- no direct target competitors identified. This is both an advantage (first-in-class opportunity, clean IP) and a risk (no external validation of the target)

## Analysis

Solengepras occupies an unusual position in the PD pipeline: a symptomatic therapy with a genuinely novel non-dopaminergic mechanism, operating in a well-understood regulatory pathway (OFF-time reduction in motor fluctuations). The Phase 2 data (1.3h placebo-adjusted OFF-time reduction, p=0.02) is encouraging but carries the standard caveats of a small (N=141), short (28-day) trial. The ASCEND monotherapy miss, while not unexpected given the small sample and the indirect-pathway mechanism (which may require ongoing dopaminergic context to show benefit), adds a note of caution.

**Analytical estimate -- Phase 3 success probability: 40-50%.** This is our assessment, not from a published source. The reasoning:
- Base rate: ~60% of Phase 3 symptomatic PD trials succeed (higher than disease-modification trials) --> starting point ~60%
- Adjustments upward: statistically significant Phase 2 signal (+5%), novel mechanism with clean safety (+5%), well-established regulatory endpoint (OFF-time) with clear precedent (+5%)
- Adjustments downward: very short Phase 2 treatment (28 days vs. 12-week Phase 3) leaves durability unknown (-10%), small Phase 2 sample size (-5%), monotherapy ASCEND miss raises questions about effect robustness (-5%), private company running pivotal trial without large pharma partner resources (-5%)
- Net: ~40-50%

The company behavior signals are informative. Cerevance raised the Series B-1 extension specifically to fund ARISE, and the investor syndicate (Gates Frontier, GV, Foresite, Casdin) represents sophisticated life sciences capital. The decision to proceed directly to a pivotal Phase 3 rather than a confirmatory Phase 2b suggests internal conviction in the Phase 2 signal -- but also reflects the financial pressure of a private company needing to demonstrate value inflection. The absence of a pharma partner at this stage is notable; istradefylline had Kyowa Kirin's backing, and [[tavapadon]] had Cerevel/AbbVie. A positive ARISE readout would likely unlock partnering or IPO optionality, while a failure would be terminal for Cerevance's lead program.

The broader strategic question is whether the PD field values non-dopaminergic adjunctive therapies. Istradefylline's modest commercial trajectory suggests physicians are slow to adopt novel mechanisms when dopaminergic dose adjustments remain available. Solengepras' dyskinesia-sparing profile could be the differentiator that istradefylline lacked, but this needs to be demonstrated convincingly in ARISE.

## References

### Clinical Trials
- [Phase 1 First-in-Human](https://clinicaltrials.gov/study/NCT03657030) -- NCT03657030
- [Phase 2 Adjunctive Trial](https://clinicaltrials.gov/study/NCT04191577) -- NCT04191577
- [ASCEND Phase 2 Monotherapy](https://clinicaltrials.gov/study/NCT06006247) -- NCT06006247
- [ARISE Phase 3 Pivotal](https://clinicaltrials.gov/study/NCT06553027) -- NCT06553027

### Key Publications
- [CVN424, a GPR6 inverse agonist, for Parkinson's disease and motor fluctuations: a double-blind, randomized, phase 2 trial | eClinicalMedicine (Oct 2024)](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00461-9/fulltext)
- [Development of CVN424: A Selective and Novel GPR6 Inverse Agonist Effective in Models of Parkinson Disease | JPET (2021)](https://pubmed.ncbi.nlm.nih.gov/33795395/)
- [First-Time Disclosure of CVN424, a Potent and Selective GPR6 Inverse Agonist: Discovery, Pharmacological Validation, and Identification of a Clinical Candidate | J Med Chem (2021)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.0c02081)
- [Phase I, First-in-Human Study of CVN424 Safety, Tolerability, and PK | JPET (2022)](https://pubmed.ncbi.nlm.nih.gov/35110393/)
- [Structural insights into the high basal activity and inverse agonism of GPR6 | Science Signaling (2024)](https://www.science.org/doi/10.1126/scisignal.ado8741)
- [Solengepras (CVN424): A Novel GPR6 Inhibitor in Clinical Development for PD | Neurology (2024)](https://www.neurology.org/doi/10.1212/WNL.0000000000210649)

### Press Releases & Filings
- [Cerevance Doses First Patient in Pivotal Phase 3 ARISE Trial (Nov 2024)](https://www.globenewswire.com/news-release/2024/11/18/2982801/0/en/Cerevance-Doses-First-Patient-in-Pivotal-Phase-3-ARISE-Trial-of-Solengepras-for-Treatment-of-Parkinson-s-Disease.html)
- [Cerevance Presents ASCEND Phase 2 Monotherapy Topline Results at AD/PD 2025 (Apr 2025)](https://www.globenewswire.com/news-release/2025/04/01/3053340/0/en/Cerevance-Presents-Topline-Results-from-Phase-2-ASCEND-Trial-of-Solengepras-as-Monotherapy-Treatment-for-Early-Stage-Parkinson-s-Disease-at-AD-PD-2025.html)
- [Cerevance Showcases Positive Phase 2 Adjunctive Results (2024)](https://www.cerevance.com/media/cerevance-showcases-positive-phase-2-results-demonstrating-significant-reduction-in-off-time-with-solengepras-as-an-adjunctive-treatment-in-parkinsons-disease)
- [Cerevance Adds $47M in Series B-1 Extension (Apr 2024)](https://www.globenewswire.com/news-release/2024/04/25/2869554/0/en/Cerevance-Adds-47-Million-in-Series-B-1-Extension-to-Advance-Robust-Clinical-Pipeline.html)
- [Solengepras Profile | Alzforum](https://www.alzforum.org/therapeutics/solengepras)

### Regulatory & Market
- [Phase 3 ARISE Trial Begins Dosing | NeurologyLive (Nov 2024)](https://www.neurologylive.com/view/phase-3-arise-trial-parkinson-therapy-solengepras-begins-dosing)
- [APDA: New PD Treatments in the Clinical Trial Pipeline (2025)](https://www.apdaparkinson.org/article/new-pd-treatments-clinical-trial-pipeline/)
