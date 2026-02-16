# Parkinson's Disease Pipeline - Master List

#claude

**Last Updated:** January 21, 2026 (narrative); asset data auto-refreshes via Dataview

---

## Pipeline Summary by Stage

```dataview
TABLE WITHOUT ID
  stage AS "Stage",
  length(rows) AS "Count"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null AND status = "Active"
GROUP BY stage
SORT stage ASC
```

---

## Approved

```dataview
TABLE drug_name AS "Drug", developer AS "Company", mechanism AS "Mechanism", route_of_administration AS "Route"
FROM "pd-pipeline-research/assets"
WHERE stage = "Approved" AND status = "Active"
SORT drug_name ASC
```

---

## NDA / MAA Filed

```dataview
TABLE drug_name AS "Drug", developer AS "Company", mechanism AS "Mechanism", next_catalyst AS "Next Catalyst", catalyst_date AS "Expected"
FROM "pd-pipeline-research/assets"
WHERE stage = "NDA Filed" AND status = "Active"
SORT drug_name ASC
```

### NDA-Stage Commentary

[[raguneprocel|Raguneprocel]] (Sumitomo/RACTHERA) filed the first iPSC-derived cell therapy NDA with Japan's MHLW in August 2025. If approved in H2 2026, this becomes the world's first iPSC therapy for any indication and validates the regulatory pathway for cell therapies in neurodegeneration. MHLW committee review is scheduled for February 19, 2026, with priority review designation granted.

[[tavapadon|Tavapadon]] (AbbVie, ex-Cerevel) is the first D1/D5 partial agonist to reach NDA, submitted September 2025. FDA decision expected 2026.

[[nd0612|ND0612]] (NeuroDerm/Mitsubishi Tanabe) is a subcutaneous levodopa/carbidopa pump with NDA resubmitted and MAA accepted. US launch expected 2026.

[[ipx203|IPX203]] (Zambon) is an extended-release levodopa/carbidopa with EMA submission June 2025.

---

## Phase 3 / Pivotal

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE (stage = "Phase 3" OR stage = "Phase 2/3") AND status = "Active"
SORT confidence_rating DESC
```

### Phase 3 Bottleneck Analysis

The Phase 3 PD pipeline faces a structural bottleneck: all four disease-modifying candidates rely on fundamentally different hypotheses, so there is no portfolio-level hedge within any single mechanism.

**Disease-modifying bets:**
- [[prasinezumab|Prasinezumab]] (Roche/Prothena) -- the only alpha-synuclein antibody to reach Phase 3 after [[cinpanemab|cinpanemab]] failed. PADOVA Phase 2b missed primary (p=0.0657) but a pre-specified levodopa subgroup showed 21% motor slowing. Roche advancing to Phase 3 (PARAISO) is a strong conviction signal, given they killed gantenerumab in AD after a similar miss.
- [[bemdaneprocel|Bemdaneprocel]] (Bayer/BlueRock) -- first large-scale cell therapy Phase 3 for any neurodegenerative disease. FDA RMAT + Fast Track, Japan Sakigake designation. Phase 1 showed graft survival by 18F-DOPA PET at 18 months.
- [[bhv-8000|BHV-8000]] (Biohaven) -- TYK2/JAK1 inhibitor, a neuroinflammation approach. First patient dosed June 2025. The only Phase 2/3 program testing a kinase inhibitor for neuroinflammation in PD at this scale.
- [[buntanetap|Buntanetap]] (Annovis Bio) -- neurotoxic protein reducer. Phase 3 completed (471 patients, positive results). NDA planned. The most controversial asset in the pipeline: positive topline results but thin peer-reviewed validation and significant market skepticism.

**Symptomatic programs:**
- [[p2b001|P2B001]] (Pharma Two B) -- ER pramipexole + rasagiline combo. Phase 3 completed, NDA planned H1 2026.
- [[mesdopetam|Mesdopetam]] (IRLAB, Sweden) -- D3 antagonist for dyskinesia. Phase 3 ready.
- [[amlenetug|Amlenetug]] (Lundbeck) -- anti-alpha-synuclein antibody for MSA (synucleinopathy).
- [[solangepras|Solangepras]] (Cerevance) -- GPR6 inverse agonist for motor fluctuations.

**Failed at Phase 3:**
- [[exenatide|Exenatide]] -- GLP-1R agonist, Phase 3 NEGATIVE (Lancet Feb 2025). No disease modification despite positive Phase 2. This is a cautionary tale for the entire GLP-1 class in PD.

---

## Phase 2b

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE stage = "Phase 2b" AND status = "Active"
SORT confidence_rating DESC
```

### Phase 2b Key Readouts

[[biib122|BIIB122/DNL151]] (Biogen/Denali) LUMA trial is the highest-impact upcoming readout in the field. 650-patient Phase 2b in idiopathic PD, readout expected March 2026. If positive, this validates LRRK2 kinase inhibition beyond mutation carriers and opens a massive sporadic PD market. BEACON trial in LRRK2 mutation carriers also active.

[[risvodetinib|Risvodetinib/IkT-148009]] (ABLi Therapeutics) -- c-Abl inhibitor. Phase 2 enrollment complete (120 pts, 32 sites). First program to claim alpha-synuclein pathology reduction via c-Abl inhibition. Phase 3 planning underway.

[[pariceract|Pariceract/BIA 28-6156]] (BIAL) -- GCase enzyme activator. ACTIVATE trial with 273 patients enrolled. One of the largest GBA-targeting trials.

---

## Phase 2

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE stage = "Phase 2" AND status = "Active"
SORT confidence_rating DESC
```

### Phase 2 Thesis-Level Observations

**Alpha-synuclein:** [[aci-7104|ACI-7104.056]] (AC Immune) reported 100% responder rate in Phase 2 interim (Dec 2025) -- the first efficacy signal for an active vaccine approach. [[exidavnemab|Lu AF82422]] (Lundbeck) may advance to Phase 3. The field is diversifying from antibodies toward vaccines ([[ub-312|UB-312]]), small molecules, and production inhibition.

**GBA/GCase:** The GCase space has become a multi-modality race. [[ambroxol|Ambroxol]] (high-dose, repurposed) in the AMBITIOUS trial represents the cheapest path to data. [[ab-1005|AB-1005/AAV2-GDNF]] (AskBio/Bayer) has RMAT designation and Sakigake (Japan) for GDNF gene therapy.

**GLP-1 agonists:** A field in disarray after [[exenatide|exenatide]] Phase 3 failure. [[lixisenatide|Lixisenatide]] showed a positive signal (NEJM 2024) but the mechanism remains unclear. [[semaglutide|Semaglutide]] (oral) in MOST-ABLE trial (Japan, 99 pts) and [[liraglutide|liraglutide]] still active. The class needs a biomarker-positive result to restore confidence.

**NLRP3 inflammasome:** Crowded and converging. [[nt-0796|NT-0796]] (NodThera) positive biomarker Aug 2025, [[vtx3232|VTX3232]] (Ventyx) positive at MDS 2025, [[dapansutrile|dapansutrile]] (Olatec) in DAPA-PD trial. Differentiation will come from CNS penetration and safety profiles. [[selnoflast|Selnoflast]] (Roche) Phase 1b active.

**Cell therapy at Phase 2:** [[cbt-npc|CBT-NPC]] (CHA Biotech, Korea) -- 40% UPDRS improvement with fetal midbrain cells. [[hb-admsc|HB-ADMSC]] active. The cell therapy landscape is fragmenting by cell source (ESC vs iPSC allogeneic vs iPSC autologous vs fetal).

**Gene therapy:** [[aav-gad|AAV-GAD]] (MeiraGTx/Hologen) in Phase 2 with $230M JV and AI partnership.

---

## Phase 1/2

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", modality AS "Modality", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE stage = "Phase 1/2" AND status = "Active"
SORT confidence_rating DESC
```

### Phase 1/2 Cell Therapy Race

This stage is dominated by cell therapy programs, each with distinct strategic positioning:
- [[anpd001|ANPD001]] (Aspen Neuroscience) -- autologous iPSC-DA. Fast Track, no immunosuppression required. ASPIRO trial active.
- [[ted-a9|TED-A9]] (S.BIOMEDICS, Korea) -- hESC-derived DA progenitors. Cell publication Oct 2025 showed 22-25% motor improvement with engraftment confirmed.
- [[nouvneu001|NouvNeu001]] (iRegene, China) -- first iPSC program with both FDA RMAT and Fast Track designations. Dual China/US IND.
- [[cap-003|CAP-003]] (Capsida) -- IV AAV GCase gene therapy with novel BBB-crossing capsid. IND cleared June 2025. This is the first IV-delivered gene therapy for PD, potentially avoiding intracranial surgery.
- [[pr001|PR001/LY3884961]] (Prevail/Lilly) -- AAV9-GBA1 gene therapy in PROPEL trial. 24 patients, completion 2029.

---

## Phase 1b

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE stage = "Phase 1b" AND status = "Active"
SORT confidence_rating DESC
```

### Phase 1b Highlights

[[gt-02287|GT-02287]] (Gain Therapeutics) -- first GCase modulator to show CSF substrate reduction in PD patients: 81% mean decrease in glucosylsphingosine. 21-patient open-label in Australia, 15 patients continuing into 9-month extension. Phase 2 (100-200 pts) planned for 2026.

[[vq-101|VQ-101]] (Vanqua Bio) -- another oral brain-penetrant GCase allosteric activator. Positive interim Oct 2025.

[[nt-0796|NT-0796]] (NodThera) -- NLRP3 inhibitor Phase 1b/2a completed with positive biomarker data Aug 2025.

[[her-096|HER-096]] (Herantis, Finland) -- CDNF mimetic peptide. Phase 1b completed, Phase 2 planned 2026. One of only two neurotrophic factor programs in the pipeline.

[[ub-312|UB-312]] (Vaxxinity) -- alpha-synuclein vaccine (C-terminal). Advancing from Phase 1b to Phase 2 with 20% toxic protein reduction.

---

## Phase 1

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", modality AS "Modality", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE stage = "Phase 1" AND status = "Active"
SORT confidence_rating DESC
```

### Phase 1 Signals

[[arv-102|ARV-102]] (Arvinas) -- the first LRRK2 PROTAC degrader in clinical development. >90% LRRK2 protein reduction achieved. Phase 1b in PSP planned for Q1 2026. This is the most novel modality in the LRRK2 space and represents a targeted protein degradation approach that could offer advantages over kinase inhibition.

[[nrg5051|NRG5051]] (NRG Therapeutics, UK) -- mPTP inhibitor for mitochondrial protection. Phase 1 started Jan 2026. One of only a handful of mitochondrial-targeted programs.

[[mtx325|MTX325]] (Mission Therapeutics, UK) -- USP30 inhibitor (mitophagy modulator). Expanded to 50 patients. DUB inhibitor approach.

[[nt-0150|NT-0150]] (NodThera) -- second-generation CNS-optimized NLRP3 inhibitor. SAD/MAD H2 2025.

[[rndp-001|RNDP-001]] (Kenai Therapeutics) -- allogeneic iPSC-DA off-the-shelf cell therapy. First patient dosed Dec 2025. Backed by $82M Series A.

[[ly03017|LY03017]] (Luye Pharma, China) -- 5-HT2AR inverse agonist for PD psychosis. Dual IND (China/US).

[[ser-252|SER-252]] (Serina Therapeutics) -- POZ-apomorphine for extended-release. Phase 1b starting Q4 2025.

---

## IND-Enabling / Clinical-Ready

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism", next_catalyst AS "Next Catalyst"
FROM "pd-pipeline-research/assets"
WHERE stage = "IND-enabling" AND status = "Active"
SORT drug_name ASC
```

### IND-Enabling Commentary

[[dnl111|DNL111]] and [[dnl422|DNL422]] (Denali) represent the next wave of Denali's transport vehicle platform. DNL111 (ETV:GCase) and DNL422 (OTV:alpha-synuclein silencing) could be the most technically differentiated programs at this stage if the delivery platforms perform as intended.

[[gba1-voyager|GBA1 Gene Therapy]] (Voyager/Neurocrine) -- IV AAV-GBA1 with VYGR holding 50% US rights option. Voyager's TRACER capsid technology for brain-penetrant IV delivery.

[[snp614|SNP614]] (SciNeuro) -- next-gen LRRK2 ASO with $5M MJFF grant. ARCH-backed.

[[vb-23|VB-23]] (Vincere Biosciences) -- USP30 inhibitor. Phase 1 planned 2026. Triple MJFF-validated ($5M x3 grants).

[[casma-trpml1|TRPML1 agonist]] (Casma Therapeutics) -- lysosomal calcium channel/autophagy. IND planned 2026.

---

## Preclinical (Named Programs)

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism"
FROM "pd-pipeline-research/assets"
WHERE stage = "Preclinical" AND status = "Active"
SORT drug_name ASC
```

---

## Discovery / Research

```dataview
TABLE drug_name AS "Drug", developer AS "Company", target AS "Target", mechanism AS "Mechanism"
FROM "pd-pipeline-research/assets"
WHERE (stage = "Discovery" OR stage = "Research") AND status = "Active"
SORT drug_name ASC
```

---

## Diagnostics / Imaging / Commercial

```dataview
TABLE drug_name AS "Drug", developer AS "Company", modality AS "Modality", mechanism AS "Mechanism"
FROM "pd-pipeline-research/assets"
WHERE (stage = "Commercial" OR thesis_cluster = "diagnostics") AND status = "Active"
SORT drug_name ASC
```

### Diagnostics Commentary

[[18f-fd4|18F-FD4]] (SynuSight/Mabwell, China) -- first selective alpha-synuclein PET tracer in clinical development. $3.84M MJFF grant. If validated, this transforms PD clinical trials by enabling target engagement measurement for alpha-synuclein therapies.

[[mk-7337|MK-7337]] (Merck) -- alpha-synuclein PET tracer. First signal in idiopathic PD.

[[saamplify-asyn|SAAmplify-aSYN]] (Amprion) -- CSF seed amplification assay (SAA) test. Already commercial with Mayo Clinic partnership. This is the current standard for biological diagnosis.

---

## Discontinued / Failed / Terminated

```dataview
TABLE drug_name AS "Drug", developer AS "Company", stage AS "Last Stage", status AS "Status", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE status = "Failed" OR status = "Terminated" OR status = "Discontinued"
SORT stage DESC
```

### Failure Pattern Analysis

The failure pattern in PD is instructive:
- **Alpha-synuclein antibodies:** [[cinpanemab|Cinpanemab]] (Biogen) failed Phase 2 (NEJM 2022). [[prasinezumab]] survived with a subgroup signal, but the antibody modality faces persistent questions about whether extracellular clearance is sufficient.
- **GLP-1 agonists:** [[exenatide|Exenatide]] Phase 3 NEGATIVE (Lancet 2025) despite positive Phase 2. The disconnect between Phase 2 and Phase 3 results is the single most important cautionary signal in PD drug development right now.
- **GCS inhibition:** Venglustat (Sanofi) MOVES-PD worsened vs placebo -- substrate reduction may be harmful in some contexts.
- **LRRK2 kinase inhibitors:** [[k0706|K0706]] (Sun Pharma) terminated, narrowing the field.

---

## Deprioritized / Inactive

```dataview
TABLE drug_name AS "Drug", developer AS "Company", stage AS "Stage", status AS "Status", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE status = "Deprioritized" OR status = "Inactive" OR status = "Unverified"
SORT stage DESC
```

---

## GEOGRAPHIC DISTRIBUTION

### By Region

| Region | Estimated Companies | Notable Programs |
|--------|---------------------|------------------|
| **USA** | 45+ | [[prasinezumab]], [[biib122]], [[anpd001]], [[arv-102]], [[cap-003]] |
| **China** | 10+ | [[ux-da001]], [[nouvneu001]], [[ly03017]], [[18f-fd4]] |
| **Japan** | 8+ | [[raguneprocel]] (NDA filed), [[nd0612]], [[ipx203]] |
| **Korea** | 8+ | [[ted-a9]], [[abl301]], [[hl192]], [[cbt-npc]] |
| **Europe** | 20+ | [[prasinezumab|Roche]], [[amlenetug|Lundbeck]], [[pariceract|BIAL]], [[emrusolmin|MODAG]], [[her-096|Herantis]], [[nrg5051|NRG]], [[endlyz|Endlyz]] |
| **Switzerland** | 5+ | [[aci-7104|AC Immune]], [[gt-02287|Gain]], [[asn51|Asceneuron]] |

### Asia Cell Therapy Leadership

```dataview
TABLE drug_name AS "Drug", developer AS "Company", modality AS "Modality", stage AS "Stage"
FROM "pd-pipeline-research/assets"
WHERE contains(modality, "cell therapy") AND status = "Active"
SORT stage ASC
```

Asia leads in clinical-stage cell therapy for PD. Japan's [[raguneprocel]] is at NDA stage. Korea has [[ted-a9]] (hESC-derived) and [[cbt-npc]] (fetal cells). China has three dual-IND programs ([[nouvneu001]], [[ux-da001]]) pursuing simultaneous NMPA and FDA paths -- a regulatory strategy that did not exist five years ago.

---

## MECHANISM LANDSCAPE

### Target Competition Analysis

```dataview
TABLE WITHOUT ID
  thesis_cluster AS "Thesis Cluster",
  length(rows) AS "Total Programs",
  length(filter(rows, (r) => r.status = "Active")) AS "Active"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null
GROUP BY thesis_cluster
SORT length(rows) DESC
```

### Novel/Emerging Targets (Low Competition)

| Target | Company | Rationale |
|--------|---------|-----------|
| ATP13A2/ATP10B | [[endlyz\|Endlyz]] (Belgium) | Lysosomal transport; PARK9 gene |
| USP30 | [[vb-23\|Vincere]], [[mtx325\|Mission]] | Mitophagy enhancement |
| mPTP | [[nrg5051\|NRG Therapeutics]] | Mitochondrial pore blockade |
| Parthanatos | [[nly03\|Neuraly (NLY03)]] | Cell death pathway |
| NOD2 | [[valo-merck\|Valo/Merck]] | Inflammation; AI-identified |
| Nurr1 | [[hl192\|HanAll]] | DA neuron master regulator |
| PINK1 | [[progenra-pink1\|Progenra]] | Mitochondrial kinase rescue |
| Kv1.3 | [[muna-kv13\|Muna]] | Microglial potassium channel |
| TRPML1 | [[casma-trpml1\|Casma]] | Lysosomal calcium channel |

---

## KEY 2026 MILESTONES

| Q1 2026 | Q2 2026 | H2 2026 |
|---------|---------|---------|
| [[biib122\|BIIB122]] LUMA readout (Mar) | [[prasinezumab]] Ph3 enrollment | [[raguneprocel\|Sumitomo approval (Japan)]] |
| [[tavapadon]] FDA decision | [[her-096\|HER-096]] Phase 2 start | [[cap-003\|CAP-003]] Phase 1/2 data |
| [[nd0612\|ND0612]] US launch | [[bemdaneprocel]] update | [[gt-02287]] full data |
| [[nrg5051\|NRG5051]] Phase 1 data | [[p2b001\|P2B001]] NDA decision | Multiple NLRP3 readouts |
| [[arv-102\|ARV-102]] Phase 1b PSP start | [[hl192]] patient trial start | Korea cell therapy advances |

---

## MAJOR DEALS (2024-2026)

| Deal | Value | Target | Date |
|------|-------|--------|------|
| Merck KGaA / [[valo-merck\|Valo Health]] | $3B+ | AI + NOD2 | Nov 2025 |
| Novartis / [[aro-snca\|Arrowhead]] | $2.2B | alpha-syn siRNA | 2024 |
| ABL Bio / Sanofi | $985M | alpha-syn bispecific ([[abl301]]) | 2022 |
| Biogen / Alectos | $722M | GBA2 inhibitor | 2024 |
| GSK / [[vesalius-gsk\|Vesalius]] | $650M | Undisclosed | Nov 2024 |
| MeiraGTx / Hologen | $430M JV | Gene therapy + AI ([[aav-gad]]) | Mar 2025 |
| AbbVie / [[cap-003\|Capsida]] | $160M | AAV platform | 2023 |

### Deal Commentary

The deal landscape signals a clear thesis shift: big pharma is buying **platforms and modalities**, not just individual molecules. The Valo/Merck ($3B), Arrowhead/Novartis ($2.2B), and MeiraGTx/Hologen ($430M) deals all involve platform technologies (AI discovery, siRNA, gene therapy + AI) rather than single-asset licenses. This suggests pharma views the PD target landscape as unresolved and wants optionality across multiple mechanisms.

---

## COMPANIES BY PIPELINE DEPTH

### Tier 1: Multiple Clinical Programs

| Company | Programs |
|---------|----------|
| Denali/Biogen | [[biib122\|BIIB122]] (Ph2b), [[dnl111]] (IND), [[dnl422]] (IND) |
| Neuraly | [[nly01\|NLY01]] (Ph2), [[nly02\|NLY02]] (IND), [[nly03\|NLY03]] (Preclin) |
| Alector | [[al050-abc\|AL050-ABC]] (Preclin), [[adp062-abc\|ADP062]] (Preclin), [[adp065-abc\|ADP065]] (Preclin) |
| Gain Therapeutics | [[gt-02287]] (Ph1b) for PD, Gaucher, DLB, AD + discovery |
| AC Immune | [[aci-7104\|ACI-7104.056]] (Ph2), Morphomer (Discovery) |
| Acadia | NUPLAZID (Approved), Remlifanserin (Ph2) |
| NodThera | [[nt-0796\|NT-0796]] (Ph1b), [[nt-0150\|NT-0150]] (Ph1) |

### Tier 2: Single Lead Program (Clinical Stage)

```dataview
TABLE drug_name AS "Lead Asset", stage AS "Stage", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE status = "Active" AND (stage = "Phase 3" OR stage = "Phase 2/3" OR stage = "Phase 2b" OR stage = "Phase 2" OR stage = "NDA Filed") AND company_type = "biotech"
SORT stage ASC, drug_name ASC
```

### Tier 3: Preclinical/Discovery

| Company | Focus |
|---------|-------|
| [[endlyz\|Endlyz]] | ATP13A2/ATP10B |
| [[vb-23\|Vincere]] | USP30 |
| [[snp614\|SciNeuro]] | LRRK2 ASO |
| [[nrg5051\|NRG Therapeutics]] | mPTP |
| [[stealth-bio\|Stealth Bio]] | Mitochondria |
| [[valo-merck\|Valo Health]] | AI + NOD2 |
| [[vesalius-gsk\|Vesalius/Flagship]] | Undisclosed |

---

## VC / EARLY-STAGE SOURCING SIGNALS

### Recently Funded (Seed/Series A)

| Company | Funding | Focus | Signal |
|---------|---------|-------|--------|
| [[endlyz\|Endlyz]] | EUR16M seed | ATP13A2 | DDF incubated 4yr |
| [[rndp-001\|Kenai]] | $82M Series A | Allogeneic iPSC | Cure Ventures led |
| [[nrg5051\|NRG Therapeutics]] | GBP50M Series B | mPTP | Ph1 started |
| [[anpd001\|Aspen Neuroscience]] | $115M Series C | Autologous iPSC | Kite invested |
| [[snp614\|SciNeuro]] | $53M + $5M MJFF | LRRK2 ASO | ARCH-backed |
| [[vb-23\|Vincere]] | $5M MJFF x3 | USP30 | Multi-grant validation |

### Stealth/Emerging Signals

- **DDF pattern:** Incubates 3-4 years before launch ([[endlyz\|Endlyz]] example)
- **MJFF grants:** Often precede company formation by 1-2 years
- **Unnamed YC company:** AI-neuro targeting PD
- **Flagship portfolio:** Multiple undisclosed neuro programs

---

## NOT PD-FOCUSED (Clarifications)

| Company | Notes |
|---------|-------|
| **Passage Bio** | NO PD programs. Pipeline: FTD-GRN (Ph1/2), FTD-C9orf72 (preclinical), ALS (preclinical), AD (discovery), HD (preclinical) |
| Regeneron | No PD programs (HD focus) |
| Sarepta | No PD programs (SCA, HD focus) |

---

## DATA QUALITY & GAPS

### Confidence Levels

| Source | Confidence | Coverage |
|--------|------------|----------|
| ClinicalTrials.gov | High | Phase 1+ only |
| Company websites (accessible) | High | ~60% access rate |
| SEC filings | Medium | Public companies only |
| Press releases | Medium | Announced programs only |
| Overseas registries | Medium | Language barriers |
| Patents | Low | Does not equal active development |
| Grants | Low | Very early stage |

### Known Gaps (Manual Verification Needed)

**Company websites blocked:**
- AbbVie/Cerevel detailed pipeline
- Novartis neuroscience filter
- Sana Bioterapeutics
- Spark Therapeutics

**Paywalled sources:**
- BioCentury deal terms
- Endpoints premium articles
- Citeline/Cortellis full data

**Geographic gaps:**
- Taiwan, Singapore, Australia programs
- India PD biotechs
- Eastern European programs

### Manual Verification Completed
- Passage Bio (NO PD programs -- confirmed)
- BlueRock ([[bemdaneprocel]] Ph3 -- confirmed)
- Neuraly ([[nly01]]/[[nly02]]/[[nly03]] -- confirmed)
- Gain Therapeutics ([[gt-02287]] Ph1b -- confirmed)
- Voyager ([[gba1-voyager\|GBA1 GT]] partnership -- confirmed)

### Still Needs Manual Verification
- AbbVie/Cerevel detailed pipeline
- Novartis neuroscience pipeline
- Sana Bioterapeutics iPSC programs
- Spark Therapeutics gene therapy

---

*Generated from multi-source parallel agent research*
*Includes: Baseline, Clinical Trials, SEC, Press, Company Pages, Funding, Patents, Grants, Tech Transfer, Incubators, Conferences, China, Japan, Korea, Europe*
*Asset data auto-refreshes via Dataview queries from `pd-pipeline-research/assets/`*
