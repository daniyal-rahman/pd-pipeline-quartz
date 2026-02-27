---
drug_name: "BIIB122"
aliases: ["DNL151"]
target: "LRRK2 kinase"
mechanism: "Oral, brain-penetrant, selective LRRK2 kinase inhibitor that reduces pathogenic Rab GTPase phosphorylation to restore lysosomal function"
modality: "small molecule"
developer: "Denali Therapeutics"
company_type: "biotech"
publicly_traded: true
ticker: "DNLI"
partner: "Biogen"
partner_type: "big pharma"
stage: "Phase 2b"
status: "Active"
patient_population: "Early-stage idiopathic PD (sporadic) + LRRK2 mutation carriers"
route_of_administration: "oral (225 mg once daily)"
key_biomarkers: ["p-Rab10", "p-LRRK2 (pS935)", "urinary BMP"]
confidence_rating: "6/10"
next_catalyst: "LUMA Phase 2b readout"
catalyst_date: "March 2026"
thesis_cluster: "genetic-pd"
tags: [pd-pipeline, claude]
date: 2026-02-15
company_link: "[[companies/denali-therapeutics]]"
partner_link: "[[companies/biogen]]"
---

# BIIB122

## Summary

The most advanced LRRK2 inhibitor and the first to test whether LRRK2 kinase hyperactivity drives disease in sporadic PD, not just the 1-2% with LRRK2 coding mutations. Denali (biotech, DNLI) developed BIIB122 in a $2.15B partnership with Biogen (big pharma) -- the highest-conviction deal in the PD landscape by upfront-to-total ratio (47.7%). Phase 1b showed 80-87% p-Rab10 reduction, confirming robust target engagement. The LUMA Phase 2b readout (March 2026) is the single most consequential near-term catalyst in PD: if positive, it validates the [[pariceract|genetic PD]] thesis and opens a $5-10B market; if negative in the unselected population but BEACON (mutation carriers) succeeds, LRRK2 inhibition survives as a niche genetic therapy; if both fail, capital redirects to GBA1, mitophagy, and cell therapy, and [[neu-723|NEU-411]]'s precision-selection approach becomes the last test of the LRRK2 hypothesis.

## Deal Info

| Field | Value |
|-------|-------|
| Partner | Biogen |
| Deal Date | 2020 |
| Upfront | $1.025B ($560M cash + $465M equity) |
| Total (Biobucks) | $2.15B+ |
| Deal Type | Licensing/co-development |

## Notes

### Science
- Oral, brain-penetrant, selective LRRK2 kinase inhibitor dosed at 225 mg once daily; inhibits LRRK2-mediated phosphorylation of Rab GTPases (Rab10, Rab35), restoring vesicular trafficking and autophagy
- LRRK2 is the most common genetic cause of familial PD (4-5% of familial, 1-2% of sporadic); G2019S is the most prevalent pathogenic variant (1-6% sporadic, 3-19% familial, enriched in Ashkenazi Jewish populations); MDSGene database catalogs 211 potentially disease-causing variants across 3,387 PD patients
- Critical expanded hypothesis: sporadic PD patients show ~2x elevated p-Rab10 levels in blood vs. controls, and GWAS variant rs76904798 (LRRK2 promoter) is independently associated with increased LRRK2 protein expression and sporadic PD risk -- suggesting LRRK2 protein levels (not just mutations) drive pathology
- Convergence with GBA1 biology: LRRK2 phosphorylates Rab10, which reduces GCase activity; LRRK2 inhibition restores GCase function in both LRRK2-mutant AND GBA1-mutant neurons -- connecting this program mechanistically to [[pariceract|GBA1 targets]]
- Preclinical safety signal: reversible type II pneumocyte vacuolation in macaque lungs (class effect for all LRRK2 inhibitors); no functional respiratory impairment; resolves within 2 weeks of discontinuation; no kidney changes in primates at therapeutic doses; >100 healthy volunteers dosed in Phase 1/1b with zero pulmonary abnormalities
- ~40% of LRRK2 mutation carriers have NO Lewy bodies at autopsy (tau/TDP-43 instead) -- pathology heterogeneity means LRRK2 mutations feed into multiple downstream pathways, but the lysosomal dysfunction hypothesis positions LRRK2 upstream of protein aggregation regardless of substrate
- Key distinction vs. [[neu-723|NEU-411]]: BIIB122 tests the broad sporadic PD hypothesis in an unselected population (LUMA), while Neuron23 genetically enriches for LRRK2-driven disease via proprietary SNP panel claiming ~30% of idiopathic PD has elevated LRRK2 pathway activity
- Open question: peripheral target engagement (p-Rab10 in blood) has no validated CNS correlate -- whether 80-87% peripheral reduction translates to sufficient brain LRRK2 inhibition remains unproven

### Clinical

**Phase 1/1b** | NCT TBD | N=~100 | Healthy volunteers + PD patients
- **Primary endpoint:** Safety/tolerability --> Well-tolerated; no serious AEs
- **Key secondary:** 55-85% reduction in p-LRRK2 (pS935); 80-87% reduction in p-Rab10 at therapeutic doses; no pulmonary or renal functional changes for up to 28 days of dosing
- **Status:** Completed
- **Interpretation:** Established robust target engagement and clean safety profile; the 80-87% p-Rab10 reduction is the strongest demonstration of LRRK2 kinase inhibition in humans and enabled the Phase 2b hypothesis test

**LIGHTHOUSE (Phase 3)** | NCT TBD | N=TBD | LRRK2 mutation carriers
- **Primary endpoint:** Time to motor progression
- **Status:** Terminated (June 2023)
- **Interpretation:** NOT terminated for safety or efficacy concerns. Killed because 2031 estimated completion was unacceptable. The trial targeted only LRRK2 mutation carriers (~1-2% of PD), meaning both the timeline and addressable market were too constrained. Pivoted resources to LUMA to test the broader sporadic PD hypothesis with a 2026 readout -- 5 years faster. This was strategic redeployment, not retreat.

**LUMA (Phase 2b)** | NCT TBD | N=640-650 | Early-stage idiopathic PD + LRRK2 mutation carriers
- **Primary endpoint:** Time to confirmed worsening in MDS-UPDRS Parts II+III combined score
- **Key secondary:** Biomarker substudies (p-Rab10, urinary BMP, genetics) enabling post-hoc responder analysis; 98 centers across North America, Asia, Europe, Israel; 48-144 weeks treatment duration
- **Status:** Active; expected readout March 2026
- **Interpretation:** THE critical trial. Tests whether LRRK2 inhibition slows progression in broad early PD (not just mutation carriers). N=650 is large for Phase 2b, providing power for subgroup detection -- if 20-30% of sporadic PD patients are LRRK2-driven (as Neuron23 claims), that is 130-195 patients with potential signal. The unselected population is both the strength (if positive, validates broad applicability) and the risk (signal dilution if only a subset responds).

**BEACON (Phase 2a)** | NCT06602193 | N=~50 | Genetically confirmed LRRK2-PD
- **Primary endpoint:** Safety/tolerability
- **Key secondary:** Blood LRRK2 activity, urine BMP (biomarker validation); 12-week double-blind + 2-year open-label extension
- **Status:** Active; first patient dosed December 2024; estimated completion February 2028
- **Interpretation:** Serves as a positive control for the LRRK2 mechanism. If LUMA is equivocal but BEACON shows clear benefit in mutation carriers, the target survives with a narrower patient population. Running in parallel with LUMA hedges the sporadic PD bet.

### Financial
- **Deal structure:** 60/40 development cost share (Biogen/Denali); 50/50 US profit split; 60/40 China cost/profit (Biogen/Denali); tiered royalties to Denali for rest of world
- **Upfront conviction ratio:** 47.7% ($1.025B upfront on $2.15B total) -- among the highest in the PD deal landscape, reflecting genuine Biogen commitment at signing (2020)
- **Milestones remaining:** Up to $1.125B in development/regulatory/commercial milestones
- **Biogen PD portfolio post-2025 cuts:** Killed BIIB094 (LRRK2 ASO) and ION464 (alpha-synuclein ASO) in February 2025; BIIB122 retained as sole PD asset -- signals either concentrated LRRK2 conviction or broader retreat from neuro with one hedged position
- **Denali (DNLI):** Clinical-stage biotech; BIIB122 is their lead partnered PD program; stock directly tied to LUMA outcome (binary risk event)
- **Comparison:** [[neu-723|Neuron23]] raised $96.5M Series D (Nov 2024) for competing LRRK2 program -- VC validation of the target class, but at far smaller scale than the $2.15B Biogen deal

### Competitive

| File | stage | status | developer | modality |
| --- | --- | --- | --- | --- |
| [[biib094]] | Discontinued | Discontinued | Ionis Pharmaceuticals | ASO |
| [[montara-lrrk2]] | Preclinical | Active | Montara Therapeutics | small molecule |
| [[seal-rock-lrrk2]] | Preclinical | Active | Seal Rock Therapeutics | small molecule |
| [[snp614]] | IND-enabling | Active | SciNeuro Pharmaceuticals | ASO |
| [[arv-102]] | Phase 1 | Active | Arvinas | small molecule |
| [[neu-723]] | Phase 2 | Active | Neuron23 | small molecule |
| [[biib122]] | Phase 2b | Active | Denali Therapeutics | small molecule |

- [[neu-723|NEU-411]] (Neuron23) is the primary competitor: same target class but differentiated by precision patient selection (QIAGEN NGS companion diagnostic targeting 50+ SNPs), digital biomarker primary endpoint (Roche smartphone-based score), and genetically enriched trial design -- 18 months behind BIIB122 with 2027 readout
- The competitive dynamic is NOT a molecule race but an information race: Denali tests broad hypothesis first (LUMA, March 2026); Neuron23 tests enriched hypothesis second (NEULARK, 2027). If LUMA fails but NEULARK succeeds, it proves patient selection matters more than molecule. If both fail, LRRK2 inhibition is refuted.
- Earlier-stage competitors: Pfizer/Cerevel PFE-360 (rights transferred); next-generation Type II kinase inhibitors (Science paper, Jan 2025) and allosteric inhibitors could differentiate on safety if chronic lung toxicity emerges as an issue
- LRRK2 inhibition connects mechanistically to [[pariceract|GBA1 programs]] via lysosomal convergence -- success for either target validates the other, creating positive read-through across the [[pariceract|genetic PD]] cluster
- If LUMA succeeds: validates sporadic PD LRRK2 hypothesis, Denali dominates, combination therapy with GBA1 activators becomes the next frontier
- If LUMA fails: [[neu-723|NEU-411]]'s precision approach becomes the last test; if that also fails, capital redirects to [[pariceract|GBA1]], [[prasinezumab|alpha-synuclein]], and [[progenra-pink1|mitophagy]] targets

## Analysis

BIIB122 sits at the center of the most consequential binary event in PD drug development. The LUMA readout in March 2026 will determine not just the fate of one molecule but whether LRRK2 kinase hyperactivity -- the most genetically validated kinase target in PD -- translates into therapeutic benefit in sporadic disease. The target biology is strong: LRRK2 is the most common genetic cause of familial PD, GWAS signals implicate it in sporadic PD independently of coding mutations, p-Rab10 is elevated 2x in sporadic patients, and convergence with GBA1 (LRRK2 inhibition restores GCase activity) adds mechanistic depth that extends beyond the LRRK2 pathway alone.

**Analytical estimate -- Phase 2b success probability (positive primary endpoint in overall population): 25-35%.** This is our assessment, not from a published source. The reasoning:
- Base rate: Phase 2 success in neurodegeneration ~15-20%
- Adjustments upward: strongest genetic validation of any kinase target in PD (+10%), robust Phase 1b target engagement at 80-87% p-Rab10 reduction (+5%), convergent GBA1 biology adds mechanistic plausibility (+5%), Biogen's concentrated bet (killed everything else) signals internal conviction (+5%)
- Adjustments downward: unselected sporadic PD population creates signal dilution risk if only 20-30% are LRRK2-driven (-10%), no prior clinical efficacy data for LRRK2 inhibition in any human PD population (-5%), MDS-UPDRS is a noisy endpoint requiring large effects (-5%), pathology heterogeneity in LRRK2 carriers (40% non-Lewy body) (-5%)
- Net: ~25-35%

**Signal analysis:** Biogen's behavior tells a coherent story when read carefully. They signed the largest PD deal in history ($2.15B) in 2020, terminated Phase 3 LIGHTHOUSE in 2023 not because the science failed but because an 8-year timeline to readout was operationally unacceptable, killed both ASO programs (LRRK2 and alpha-synuclein) in 2025 to consolidate resources, and retained BIIB122 as their sole PD asset. The pattern is not retreat from the LRRK2 target -- it is modality selection (small molecule > ASO for chronic CNS disease) and timeline optimization (LUMA 2026 readout > LIGHTHOUSE 2031 readout). The 50/50 US profit split means Denali retains significant upside, while Biogen's 60% development cost share means they absorb majority risk. This structure -- signed when Biogen's neuro investment appetite was highest -- now functions as a concentrated bet: all PD eggs in one basket, with a near-term readout that provides a fast decision point.

The decision tree after LUMA is clear. Positive result: LRRK2 inhibition validated for sporadic PD, Phase 3 in biomarker-enriched population, $5-10B market potential, positive read-through to [[neu-723|NEU-411]] and the entire genetic PD cluster. Equivocal result (trends but misses significance): biomarker substudies become critical -- if p-Rab10-high or LRRK2-GWAS-positive subgroups show benefit, the thesis survives but requires precision enrichment (the [[neu-723|Neuron23]] model), and BEACON mutation-carrier data provides a fallback validation path. Negative result: LRRK2 inhibition hypothesis severely damaged, Biogen likely exits PD entirely, Denali stock faces binary downside, and the genetic PD field narrows to GBA1 targets ([[pariceract]]) and cell therapy approaches.

## References

### Clinical Trials
- [BEACON Phase 2a](https://clinicaltrials.ucsf.edu/trial/NCT06602193) -- NCT06602193
- [LUMA Phase 2b announcement | Biogen](https://investors.biogen.com/news-releases/news-release-details/denali-therapeutics-and-biogen-announce-initiation-phase-2b) -- NCT TBD
- [LIGHTHOUSE Phase 3 termination | NeurologyLive](https://www.neurologylive.com/view/biogen-denali-terminate-phase-3-lighthouse-study-biib122-lrrk2-parkinson-disease)

### Key Publications
- [Perspective on the current state of the LRRK2 field | npj Parkinson's Disease](https://www.nature.com/articles/s41531-023-00544-7)
- [Updated MDSGene review on clinical and genetic spectrum of LRRK2 variants | npj Parkinson's Disease](https://www.nature.com/articles/s41531-025-00881-9)
- [Recent advances in targeting LRRK2 for PD treatment | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12235878/)
- [LRRK2 and Parkinson's disease: from genetics to targeted therapy | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10270275/)
- [LRRK2 and idiopathic Parkinson's disease | Trends in Neurosciences](https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(21)00250-2)
- [LRRK2 Inhibition by BIIB122 in Healthy Participants and Patients with PD | Movement Disorders](https://movementdisorders.onlinelibrary.wiley.com/doi/10.1002/mds.29297)
- [Dysregulated phosphorylation of Rab GTPases by LRRK2 | Molecular Neurodegeneration](https://molecularneurodegeneration.biomedcentral.com/articles/10.1186/s13024-018-0240-1)
- [Phosphoproteomics reveals LRRK2 regulates Rab GTPases | eLife](https://elifesciences.org/articles/12813)
- [Current state of LRRK2-based biomarker assay development | Frontiers in Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.00865/full)
- [LRRK2 kinase activity regulates lysosomal glucocerebrosidase | Nature Communications](https://www.nature.com/articles/s41467-019-13413-w)
- [LRRK2, GBA and their interaction in autophagy regulation | Translational Neurodegeneration](https://translationalneurodegeneration.biomedcentral.com/articles/10.1186/s40035-022-00281-6)
- [GBA1- and LRRK2-directed treatments: the way forward | ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1353802024000518)
- [LRRK2 and alpha-synuclein: distinct or synergistic players in PD? | Frontiers in Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.00577/full)
- [LRRK2 is a component of granular alpha-synuclein pathology | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2833010/)
- [LRRK2 in Parkinson's disease: challenges of clinical trials | Nature Reviews Neurology](https://www.nature.com/articles/s41582-019-0301-2)
- [Coding and noncoding variation in LRRK2 and PD risk | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292230/)
- [Fine-mapping of non-coding variation driving the LRRK2 GWAS signal | ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1353802021000079)
- [LRRK2 in Parkinson's disease: upstream regulation and therapeutic targeting | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11466701/)
- [Type II kinase inhibitors that target PD-associated LRRK2 | Science Advances](https://www.science.org/doi/10.1126/sciadv.adt2050)

### Press Releases & Filings
- [Biogen and Denali to collaborate on LRRK2 program for PD | Biogen IR](https://investors.biogen.com/news-releases/news-release-details/biogen-and-denali-collaborate-lrrk2-program-parkinsons-disease)
- [Biogen provides update on PD clinical development program | Biogen IR](https://investors.biogen.com/news-releases/news-release-details/statement-biogen-provides-update-parkinsons-disease-clinical)
- [First patient treated in Phase 2a trial of BIIB122 in LRRK2-PD | NeurologyLive](https://www.neurologylive.com/view/first-patient-treated-phase-2a-trial-investigational-biib122-lrrk2-associated-pd)
- [Biogen axes Alzheimer's and Parkinson's prospects | FierceBiotech](https://www.fiercebiotech.com/biotech/biogen-axes-asset-73b-buyout-plus-alzehimers-and-parkinsons-prospects)
- [Anxious for actionable data sooner than 2031, Biogen trims Denali-partnered PD program | FierceBiotech](https://www.fiercebiotech.com/biotech/anxious-actionable-data-sooner-2031-biogen-trims-denali-partnered-parkinsons-program)
- [LRRK2 therapies speeding forward after $1B biotech deal | MJFF](https://www.michaeljfox.org/news/news-context-lrrk2-therapies-speeding-forward-after-1b-biotech-deal)
- [DNL151 | ALZFORUM](https://www.alzforum.org/therapeutics/dnl151)

### Regulatory & Market
- [Sigh of relief? Lung effects of LRRK2 inhibitors are mild | ALZFORUM](https://www.alzforum.org/news/research-news/sigh-relief-lung-effects-lrrk2-inhibitors-are-mild)
- [LRRK2 inhibitor hits target, appears safe for PD | ALZFORUM](https://www.alzforum.org/news/research-news/lrrk2-inhibitor-hits-target-appears-safe-parkinsons)
- [Genetic testing for PD in clinical practice | Journal of Neural Transmission](https://link.springer.com/article/10.1007/s00702-023-02612-x)
- [LRRK2-related Parkinson disease | GeneReviews NCBI](https://www.ncbi.nlm.nih.gov/sites/books/NBK1208/)
- [Development of inhibitors of LRRK2 as therapeutic strategy | British Journal of Pharmacology](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/bph.15575)
- [Selective LRRK2 kinase inhibition reduces phosphorylation of endogenous Rab10 and Rab12 | Scientific Reports](https://www.nature.com/articles/s41598-017-10501-z)
