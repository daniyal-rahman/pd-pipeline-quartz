---
drug_name: "MK16 BLNP"
aliases: ["brain-targeted LNP", "BLNP"]
target: "BBB penetration (LNP-mediated mRNA delivery to neurons, astrocytes, and brain capillary endothelial cells)"
mechanism: "Lipid nanoparticle incorporating an MK-0752 (gamma-secretase inhibitor)-derived BBB-crossing module; crosses BBB via caveolae- and gamma-secretase-mediated transcytosis for whole-brain mRNA delivery via IV administration"
modality: "LNP"
developer: "Icahn School of Medicine at Mount Sinai"
company_type: "academic"
publicly_traded: false
stage: "Preclinical"
status: "Active"
patient_population: "N/A (platform technology; demonstrated in addiction, glioblastoma mouse models; potential across CNS diseases including PD)"
route_of_administration: "IV"
key_biomarkers: ["GFP+ cell transfection", "luciferase brain luminescence", "tdTomato expression (Cre recombinase)"]
confidence_rating: "N/A (platform, not PD-specific asset)"
next_catalyst: "NHP studies, IND-enabling toxicology"
catalyst_date: "Unknown"
thesis_cluster: "bbb-delivery"
tags: [bbb-delivery]
date: 2026-02-16
company_link: "[[companies/mount-sinai]]"
---

# MK16 BLNP

## Summary

MK16 BLNP is a blood-brain-barrier-crossing lipid nanoparticle platform developed at the Icahn School of Medicine at Mount Sinai by teams led by Yizhou Dong (nanomedicine/LNP) and Eric J. Nestler (neuroscience/addiction). Published in *Nature Materials* in February 2025, MK16 BLNP delivers mRNA across the BBB via intravenous injection by incorporating a novel BBB-crossing lipid module derived from MK-0752, a gamma-secretase inhibitor known to cross the BBB. In mice, a single IV injection at 1 mg/kg transfected 7.36% of neurons, 9.71% of astrocytes, and 9.18% of brain capillary endothelial cells throughout the brain -- 8.3-fold higher brain luminescence than the FDA-approved MC3 LNP (used in patisiran). The system was validated in isolated human brain tissue from neurosurgical patients, and demonstrated therapeutic efficacy in mouse models of cocaine addiction (DeltaFosB mRNA) and glioblastoma (PTEN mRNA, 70% survival >120 days). MK16 BLNP is not PD-specific, but as a generalizable IV-to-brain mRNA delivery platform, it represents potentially transformative enabling technology for any brain disorder requiring protein replacement, gene editing, or gene silencing -- including Parkinson's disease.

## Deal Info

| Field | Value |
|-------|-------|
| Developer | Icahn School of Medicine at Mount Sinai |
| PIs | Yizhou Dong, PhD; Eric J. Nestler, MD, PhD; Paul C. Peng (co-corresponding) |
| First Authors | Chang Wang, Yonger Xue, Tamara Markovic (equal contribution) |
| Funding | NIH R35GM144117 (NIGMS), P01DA047233 (NIDA), Biogen (industry support), Icahn School of Medicine funds |
| Industry Partner | Biogen (Jiayi Pan listed as Biogen employee on paper; funding acknowledged) |
| Commercialization | No spinout company or licensing deal announced as of February 2026; Mount Sinai Innovation Partners (MSIP) handles technology transfer |
| Patent Status | Unknown; MSIP evaluates, patents, and licenses Mount Sinai technologies |

## Notes

### Science

**Lipid Library Design**

The team designed and synthesized 72 BBB-crossing lipids (BLs) across six structural classes, each conjugating a known BBB-crossing molecular module to amino lipid tails ([Wang et al., *Nature Materials*, 2025](https://www.nature.com/articles/s41563-024-02114-5)):

| Class | BBB Module | Abbreviation |
|-------|-----------|-------------|
| L-DOPA derivatives | Dopamine precursor | LD |
| D-serine derivatives | NMDA receptor co-agonist | DS |
| Temozolomide derivatives | Alkylating agent (crosses BBB) | TM |
| Tryptamine derivatives | Serotonin precursor | TD |
| Cinnamic acid derivatives | Phenylpropanoid | CD |
| **MK-0752 derivatives** | **Gamma-secretase inhibitor** | **MK** |

The MK class won the screen. Synthesis involved condensing Boc-protected hexamethylenediamine with MK-0752, followed by Boc deprotection and reductive amination with lipid aldehydes to produce MK-series lipids. MK16 was selected as the lead compound ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)).

**MK16 BLNP Formulation**

| Parameter | Value |
|-----------|-------|
| Molar ratio | MK16 / DOPE / cholesterol / DMG-PEG2k = 60:30:40:0.75 |
| BL:mRNA weight ratio | 12.5:1 |
| Particle size | 137.0 +/- 4.1 nm |
| mRNA encapsulation efficiency | 84.8 +/- 1.5% |

([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))

**Mechanism of BBB Crossing**

MK16 BLNP crosses the BBB via transcytosis through two distinct pathways ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)):

1. **Caveolae-mediated transcytosis:** Pretreatment with methyl-beta-cyclodextrin (MbetaCD, caveolae inhibitor) reduced transcytosis by 43.3 +/- 1.7%
2. **Gamma-secretase-mediated transcytosis:** Pretreatment with nirogacestat (FDA-approved gamma-secretase inhibitor) reduced transcytosis by 63.8 +/- 3.1%

The MK-0752-derived lipid module appears to exploit transport machinery that normally recognizes MK-0752 (which is known to cross the BBB and reduce CNS Abeta in vivo). Critically, the MK16 BLNP does NOT activate MK-0752's pharmacological target: NOTCH pathway gene expression in MK16-treated mice was comparable to PBS controls, while free MK-0752 caused substantial NOTCH-related transcript alterations ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)). This is a key safety finding -- the BBB-crossing module is decoupled from the parent drug's biological activity.

**Why MK-0752?** MK-0752 is a Merck-developed gamma-secretase inhibitor originally investigated for Alzheimer's disease (dose-dependent CSF Abeta reduction) and oncology. It rapidly crosses the BBB after oral dosing, appearing in plasma and CSF within hours, with complete clearance by 36 hours ([MedChemExpress](https://www.medchemexpress.com/MK-0752.html); [DrugBank](https://go.drugbank.com/drugs/DB12852)). The Dong lab's insight was to use this BBB-crossing capability as a structural module for LNP design rather than as a therapeutic agent.

### Preclinical Efficacy

**Brain Cell Tropism (GFP mRNA, 1 mg/kg IV, mice)**

| Cell Type | GFP+ (%) | Notes |
|-----------|----------|-------|
| Neurons | 7.36 +/- 0.78% | Throughout brain including hippocampus, thalamus, cortex |
| Astrocytes | 9.71 +/- 0.70% | Highest transfection rate |
| Brain capillary endothelial cells | 9.18 +/- 0.80% | Expected given BBB transit |
| Microglia | 2.85 +/- 0.44% | Lower but present |
| Oligodendrocytes | Negligible | Not transfected |
| Neural stem cells | Negligible | Not transfected |

At the lower dose of 0.5 mg/kg: neurons 4.64 +/- 1.00%, astrocytes 6.63 +/- 0.62%, BCECs 5.62 +/- 0.78% ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)).

**Comparison to FDA-Approved LNPs (brain luminescence, mice)**

| LNP | Fold Improvement of MK16 |
|-----|--------------------------|
| MC3 (patisiran) | 8.3-fold |
| ALC-0315 (Comirnaty) | 7.4-fold |
| SM-102 (Spikevax) | 6.5-fold |

([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))

**Biodistribution (1 hour post-IV injection)**

| Organ | % Dose |
|-------|--------|
| Liver | 56.6 +/- 2.5% |
| **Brain** | **15.3 +/- 0.4%** |
| Lungs | 10.5 +/- 1.0% |
| Kidneys | 7.4 +/- 0.8% |
| Spleen | 6.5 +/- 1.1% |
| Heart | 3.7 +/- 1.4% |

15.3% brain accumulation is remarkable for an IV-administered nanoparticle. Most conventional LNPs deliver <1% of dose to the brain ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)).

**Functional Validation: Cre Recombinase mRNA in Ai14 Reporter Mice**

Single IV injection of Cre mRNA via MK16 BLNP induced tdTomato expression across brain regions ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)):

| Region | Neurons (%) | Astrocytes (%) |
|--------|-------------|----------------|
| Hippocampus | 5.98 +/- 1.52% | 8.36 +/- 1.85% |
| Thalamus | 5.86 +/- 0.42% | 8.49 +/- 1.53% |
| Cerebral cortex | 6.68 +/- 1.13% | 8.74 +/- 2.07% |

Triple injections approximately doubled expression to 17-19% in neurons/astrocytes and ~18% in endothelial cells. MC3 LNP comparison showed only ~1% positive cells in the same regions.

**Therapeutic Demonstrations**

1. **Cocaine Addiction Model (Conditioned Place Preference):** MK16-DeltaFosB mRNA delivered to nucleus accumbens enhanced cocaine preference in mice, recapitulating the known biology of DeltaFosB overexpression in reward circuitry. This validated functional mRNA expression in specific neuronal circuits after IV delivery ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)).

2. **Glioblastoma (Orthotopic U-118MG Model):** MK16-PTEN mRNA treatment resulted in 70% survival >120 days, with significantly reduced tumor growth vs. MC3-PTEN-treated controls. Nanoparticles preferentially accumulated within tumor rather than adjacent normal tissue ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)).

**Human Brain Tissue Validation (Ex Vivo)**

DeltaFosB mRNA delivered via MK16 BLNP to adult human cortical tissue obtained during deep brain stimulation surgery (n=2 patients) ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)):

| Cell Type | DeltaFosB Expression (%) |
|-----------|--------------------------|
| Neurons | 4.00 +/- 0.99% |
| Astrocytes | 6.49 +/- 2.33% |
| Microglia | 2.38 +/- 0.94% |

Untreated slices showed no detectable expression. This confirms the platform functions in human tissue, not just murine models.

### Safety / Tolerability

- **NOTCH pathway:** No activation; gene expression comparable to PBS controls, unlike free MK-0752 which caused substantial NOTCH transcript changes ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))
- **Inflammatory cytokines:** Proinflammatory profiles comparable to or milder than MC3 LNPs at 6h; reverted to baseline at 24-48h post-injection ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))
- **Hepatic/renal function:** AST, ALT, BUN remained within normal ranges across dosing regimens ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))
- **Histopathology:** No notable pathological alterations in brain, heart, liver, lungs, spleen, or kidneys after single or multiple injections ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))
- **In vitro cytotoxicity:** >= 80% cell viability in all treated groups at tested doses in N2a neuroblastoma cells ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))

### Competitive Landscape: Brain-Targeted LNP Approaches

MK16 BLNP enters a rapidly expanding field of brain-targeted LNP delivery. Key competing approaches as of early 2026:

| Approach | Group | Mechanism | Key Difference vs. MK16 |
|----------|-------|-----------|------------------------|
| **Peptide-functionalized LNPs** (RVG29, T7, AP2, mApoE) | Multiple groups (UPenn/Mitchell Lab, etc.) | Click chemistry-conjugated BBB-targeting peptides on LNP surface | External surface modification vs. MK16's intrinsic lipid-based crossing |
| **Transferrin receptor-targeted LNPs** | Dahlman Lab (Georgia Tech), others | TfR-binding ligands for receptor-mediated transcytosis | Single-pathway targeting vs. MK16's dual caveolae/gamma-secretase pathways |
| **Acetylcholine-conjugated LNPs** | Various | Small molecule BBB-crossing module (similar conceptual approach) | Less validated; different BBB module |
| **AI-validated brain-targeted LNPs** | Multiple | Machine learning-guided LNP design | Computational design vs. MK16's rational pharmacology-based approach |
| **Intrathecal LNPs** | Xue et al. (Dong Lab, *Advanced Materials* 2025) | Direct CSF injection, bypasses BBB entirely | Avoids BBB problem but requires intrathecal delivery; not systemic |

MK16's key advantages: (1) IV administration (non-invasive, scalable); (2) dual-pathway transcytosis (more robust than single-receptor targeting); (3) whole-brain distribution including deep structures; (4) decoupled BBB module (no parent drug pharmacology). Key disadvantage: 56.6% liver accumulation means significant off-target delivery, and 15.3% brain dose -- while high for the field -- still means most mRNA goes elsewhere.

### PD-Specific Implications

MK16 BLNP was not developed for or tested in PD models, but the platform has direct relevance to multiple PD therapeutic strategies:

**Potential PD Applications:**

1. **GBA1 enzyme replacement:** GCase deficiency is the strongest genetic risk factor for sporadic PD (5-10% of all PD patients carry GBA1 variants). IV delivery of GBA1 mRNA via MK16 BLNP could provide transient GCase protein replacement in neurons and astrocytes throughout the brain -- a non-viral alternative to AAV-GBA1 gene therapy ([[pariceract]] approach) that could be repeatedly dosed and titrated. The astrocyte tropism is particularly relevant since astrocytes are major producers of GCase for cross-cellular supply.

2. **GDNF/neurturin neurotrophic factor delivery:** Failed AAV-based GDNF/neurturin trials (CERE-120, etc.) were limited by focal delivery via stereotactic injection. MK16 BLNP could deliver neurotrophic factor mRNA to broad brain regions via simple IV infusion, potentially overcoming the distribution limitations that hampered earlier gene therapy approaches.

3. **SNCA silencing:** While MK16 BLNP has been demonstrated with mRNA, the LNP platform could potentially deliver siRNA or other oligonucleotides for alpha-synuclein knockdown -- an IV alternative to intrathecal delivery used by [[ion464|ION464]] (Biogen, discontinued) and [[ly3962681|LY3962681]] (Lilly). However, siRNA cargo compatibility with MK16 has not been demonstrated.

4. **CRISPR/base editing delivery:** The Cre recombinase mRNA results demonstrate that MK16 can deliver large, functional enzyme-encoding mRNA that achieves gene editing in vivo (Ai14 model). This opens the door to CRISPR-Cas9 or base editor mRNA delivery for PD-relevant targets (LRRK2 G2019S correction, GBA1 variant correction, SNCA silencing via CRISPRi).

5. **Neuroinflammation modulation:** Transfection of microglia (2.85%) and astrocytes (9.71%) enables delivery of anti-inflammatory mRNAs or immunomodulatory payloads targeting the neuroinflammatory component of PD.

**Critical Caveats for PD:**

- Neuron transfection is ~7-10%, not 50%+; for diseases requiring correction of the majority of dopaminergic neurons (substantia nigra), this efficiency may be insufficient
- Dopaminergic neuron-specific transfection was not measured; the reported neuronal numbers are pan-neuronal
- Substantia nigra pars compacta is a deep brain structure; while MK16 showed whole-brain distribution (hippocampus, thalamus, cortex), substantia nigra delivery was not specifically quantified
- Repeat dosing is required for mRNA therapy (transient expression); the chronic dosing safety profile in mice over months-to-years is unknown
- The 56.6% liver accumulation raises hepatotoxicity concerns with repeated IV dosing over years, as would be required for a chronic PD therapy

### Translation Potential

**Mouse to Human Gap:**

The human ex vivo validation is encouraging but limited (n=2, cortical tissue only, no in vivo human data). Key translational uncertainties:

- BBB structure and transporter expression differ between mice and humans; gamma-secretase-mediated transcytosis efficiency may not scale
- Mouse BBB is more permeable than human BBB; fold-improvements over MC3 may be smaller in primates
- No NHP data reported; NHP studies are the standard preclinical gate for CNS therapeutics
- The authors acknowledge: "For future investigational new drug applications, it is crucial to conduct a toxicology study following good laboratory practice based on FDA guidelines" and note the need for "dose escalation studies and repeat administrations" to determine maximum-tolerated dose ([Wang et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/))

**Estimated Timeline to Clinic (if pursued):**

| Stage | Estimated Timeline |
|-------|-------------------|
| NHP proof-of-concept | 2026-2027 |
| GLP toxicology | 2027-2028 |
| IND filing | 2028-2029 |
| Phase 1 (first-in-human) | 2029-2030 |

This assumes dedicated funding and a commercial partner. Without a spinout or licensing deal, the timeline extends significantly -- academic programs rarely achieve IND filing without industry involvement.

## Analysis

MK16 BLNP is the most compelling academic proof-of-concept for IV-to-brain mRNA delivery published to date, and the February 2025 *Nature Materials* paper represents a genuine advance in the BBB delivery field. Three features distinguish it from competing approaches:

**1. Mechanism novelty.** Rather than decorating LNPs with targeting peptides or antibodies (the dominant approach), the Dong lab embedded the BBB-crossing capability into the lipid structure itself by deriving it from a known BBB-crossing drug (MK-0752). This is conceptually elegant: the LNP does not need a surface ligand to be recognized by a receptor; the lipid component itself mediates transcytosis. The dual-pathway mechanism (caveolae + gamma-secretase) provides redundancy that single-receptor-targeted approaches lack, potentially making MK16 more robust across species and disease states.

**2. Quantitative performance.** 15.3% brain accumulation and 8.3-fold improvement over MC3 are the highest numbers reported for a systemically administered LNP. The ~7-10% neuron/astrocyte transfection efficiency after a single injection, doubling with triple injections, suggests that clinically meaningful brain protein levels could be achievable with repeat dosing.

**3. Safety separation.** The demonstration that MK16 BLNP does not activate NOTCH signaling (unlike the parent MK-0752 molecule) addresses the primary safety concern of incorporating a pharmacologically active module into a delivery vehicle. The BBB-crossing function is structurally preserved while the drug function is lost -- a design principle that could be generalized to other BBB-crossing drugs.

**For PD specifically, MK16 BLNP is not a near-term therapeutic candidate -- it is an enabling platform that could accelerate multiple PD drug development programs if successfully translated.** The most immediate PD application would be IV delivery of GBA1 mRNA to restore glucocerebrosidase activity across the brain, which would be relevant to the 5-10% of PD patients with GBA1 mutations and potentially to the broader sporadic PD population where lysosomal dysfunction is implicated. This would represent a non-viral, non-surgical, redosable alternative to AAV-GBA1 gene therapy (e.g., [[pariceract]], PR001).

**Key risks and open questions:**

- **No NHP data.** This is the critical gap. Mouse-to-human BBB translation is notoriously unreliable, and NHP studies are the gating experiment before any IND path becomes credible. Until NHP data exist, the 8.3-fold and 15.3% numbers should be treated as optimistic upper bounds.
- **Liver accumulation.** 56.6% liver deposition is the elephant in the room. For a one-time or short-course treatment (e.g., glioblastoma), this is acceptable. For chronic PD therapy requiring years of repeat IV dosing, cumulative hepatic exposure is a serious concern.
- **No commercial path announced.** The Biogen funding acknowledgment and Jiayi Pan's Biogen affiliation suggest industry awareness, but there is no disclosed license, option, or spinout as of February 2026. Academic platforms often languish without a commercial champion.
- **Cell-type specificity.** For PD, dopaminergic neurons in the substantia nigra are the critical target. MK16 transfects neurons broadly but has no demonstrated tropism for dopaminergic neurons or the substantia nigra specifically. A platform that delivers to "the brain" is valuable but not equivalent to one that targets the PD-relevant cell population.
- **mRNA transiency.** mRNA expression is inherently transient (days to weeks). Chronic PD therapy would require regular IV infusions -- possibly monthly or more -- creating both adherence and cumulative toxicity challenges. Gene editing payloads (CRISPR) could provide durable effects but add regulatory complexity.

**Signal to watch:** Whether Biogen (listed as funder and employer of a co-author) exercises any option on this technology. Biogen has a major CNS pipeline and recently discontinued ION464 (intrathecal alpha-synuclein ASO). If Biogen licenses MK16 BLNP, it would signal intent to pivot from intrathecal to IV delivery for CNS RNA therapeutics -- a strategically important move that would validate the platform and accelerate the clinical timeline. The absence of a deal one year after publication, however, may indicate either ongoing negotiation or skepticism about translatability.

## References

### Key Publications
- [Wang C, Xue Y, Markovic T, et al. Blood-brain-barrier-crossing lipid nanoparticles for mRNA delivery to the central nervous system. *Nature Materials* (2025). DOI: 10.1038/s41563-024-02114-5](https://www.nature.com/articles/s41563-024-02114-5)
- [Full text (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514551/)
- [Xue Y, et al. Lipid Nanoparticles Enhance mRNA Delivery to the Central Nervous System Upon Intrathecal Injection. *Advanced Materials* (2025)](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adma.202417097) -- complementary intrathecal work from same lab

### Press Releases & News
- [Mount Sinai Press Release: New Lipid Nanoparticle Platform Delivers mRNA to the Brain Through the Blood-Brain Barrier (Feb 17, 2025)](https://www.mountsinai.org/about/newsroom/2025/new-lipid-nanoparticle-platform-delivers-mrna-to-the-brain-through-the-blood-brain-barrier)
- [ScienceDaily Coverage (Feb 17, 2025)](https://www.sciencedaily.com/releases/2025/02/250217133446.htm)
- [EurekAlert Coverage (Feb 17, 2025)](https://www.eurekalert.org/news-releases/1073817)
- [GEN Coverage: Lipid Nanoparticle Platform Delivers mRNA to the Brain Through the Blood-Brain Barrier](https://www.genengnews.com/topics/translational-medicine/lipid-nanoparticle-platform-delivers-mrna-to-the-brain-through-the-blood-brain-barrier/)
- [Neuroscience News Coverage (Feb 2025)](https://neurosciencenews.com/mrna-nanoparticles-bbb-28423/)

### Background References
- [MK-0752 Pharmacology (MedChemExpress)](https://www.medchemexpress.com/MK-0752.html)
- [MK-0752 (DrugBank)](https://go.drugbank.com/drugs/DB12852)
- [Synapse Drug Profile: MK16 BLNP](https://synapse.patsnap.com/drug/af55b61962ae4223b715d2a4afd2a809)

### PI Profiles
- [Yizhou Dong, PhD -- Mount Sinai Profile](https://profiles.mountsinai.org/yizhou-dong)
- [Dong Research Group (Lab Website)](https://donglab.net/)
- [Eric J. Nestler, MD, PhD -- Mount Sinai Profile](https://profiles.mountsinai.org/eric-j-nestler)
- [Nestler Lab -- Friedman Brain Institute](https://labs.neuroscience.mssm.edu/project/nestler-lab/)
