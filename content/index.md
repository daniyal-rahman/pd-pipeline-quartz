# Parkinson's Disease Therapeutic Pipeline

135+ asset notes tracking the PD therapeutic landscape across disease-modifying, symptomatic, diagnostic, and platform programs from approved through discovery stage.

---

## Pipeline Snapshot

```dataview
TABLE WITHOUT ID
  stage AS "Stage",
  length(rows) AS "Programs",
  length(filter(rows, (r) => r.status = "Active")) AS "Active"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null
GROUP BY stage
SORT choice(stage, "Approved", 0, "NDA Filed", 1, "Phase 3", 2, "Phase 2/3", 3, "Phase 2b", 4, "Phase 2", 5, "Phase 1/2", 6, "Phase 1b", 7, "Phase 1", 8, "IND-enabling", 9, "Preclinical", 10, "Discovery", 11, 99) ASC
```

---

## Key Assets to Watch

| Asset | Company | Stage | Why |
|-------|---------|-------|-----|
| [[prasinezumab]] | Roche/Prothena | Phase 3 | Only α-syn antibody to reach Phase 3; PARAISO pivotal |
| [[biib122]] | Biogen/Denali | Phase 2b | LUMA readout Mar 2026 — validates LRRK2 in sporadic PD |
| [[bemdaneprocel]] | Bayer/BlueRock | Phase 3 | First large-scale cell therapy Phase 3 in neurodegeneration |
| [[gt-02287]] | Gain Therapeutics | Phase 1b | 81% CSF substrate reduction — strongest GCase biomarker signal |
| [[arv-102]] | Arvinas | Phase 1 | First LRRK2 PROTAC degrader, >90% protein knockdown |
| [[aci-7104]] | AC Immune | Phase 2 | 100% responder rate in interim — first vaccine efficacy signal |
| [[raguneprocel]] | Sumitomo | NDA Filed | World's first iPSC therapy NDA (Japan) |

---

## Market & Deal Highlights

**$15B+ in PD deals (2022-2026)** — pharma buying platforms, not just molecules.

| Deal | Value | Thesis |
|------|-------|--------|
| [[deals/Merck-Valo-Deal-Analysis\|Merck/Valo]] | $3B+ | AI discovery + NOD2 |
| [[deals/deal-analysis-novartis-arrowhead-aro-snca\|Novartis/Arrowhead]] | $2.2B | α-syn siRNA |
| [[deals/Sanofi-ABL-Bio-Deal-Analysis\|Sanofi/ABL Bio]] | $985M | α-syn bispecific |
| [[deals/Biogen-Alectos-GBA2-Deal-Analysis\|Biogen/Alectos]] | $722M | GBA2 inhibitor |
| [[deals/GSK-Vesalius-Deal-Analysis\|GSK/Vesalius]] | $650M | Undisclosed (AI) |
| [[deals/MeiraGTx-Hologen-Deal-Analysis\|MeiraGTx/Hologen]] | $430M | Gene therapy + AI |

Full deal analyses: [[deals/FINAL-PD-Deal-Landscape-Report|Deal Landscape Report]]

---

## Thesis Clusters

```dataview
TABLE WITHOUT ID
  thesis_cluster AS "Cluster",
  length(rows) AS "Total",
  length(filter(rows, (r) => r.status = "Active")) AS "Active"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null
GROUP BY thesis_cluster
SORT length(rows) DESC
```

---

## Browse

| Section | Description |
|---------|-------------|
| [[consolidated/master-pd-pipeline\|Master Pipeline]] | Full pipeline with strategic narrative and Dataview tables |
| [[consolidated/drug-names-list\|Drug Names List]] | Sortable asset index |
| [[coverage-gaps\|Coverage Gaps]] | Unmatched patents, trials, and overseas programs |
| **Synthesis** | |
| [[synthesis/synthesis-1-alpha-synuclein\|Alpha-Synuclein]] | Antibodies, vaccines, siRNA, small molecules |
| [[synthesis/synthesis-2-genetic-pd\|Genetic PD]] | GBA1/LRRK2/GCase programs |
| [[synthesis/synthesis-3-bbb-platforms\|BBB Platforms]] | Blood-brain barrier delivery + gene therapy |
| [[synthesis/synthesis-4-neuroinflammation\|Neuroinflammation]] | NLRP3, TLR2, microglia |
| [[synthesis/synthesis-5-celltherapy-symptomatic\|Cell Therapy & Symptomatic]] | iPSC, dopamine formulations, non-motor |
| **Research** | |
| [[overseas/\|Overseas Pipelines]] | China, Japan, Korea, Europe |
| [[sec-filings/\|SEC Filings]] | Public company disclosures |
| [[vc-sourcing/\|VC Sourcing]] | Early-stage signals and investor patterns |
| [[baseline/\|Baseline]] | Original company/asset reference lists |
| [[deals/\|Deal Analyses]] | 27 individual deal deep-dives |

---

## Data Export

```dataview
TABLE drug_name AS "Drug", developer AS "Company", stage AS "Stage", status AS "Status", confidence_rating AS "Conf.", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null AND status = "Active"
SORT choice(stage, "Approved", 0, "NDA Filed", 1, "Phase 3", 2, "Phase 2/3", 3, "Phase 2b", 4, "Phase 2", 5, "Phase 1/2", 6, "Phase 1b", 7, "Phase 1", 8, "IND-enabling", 9, "Preclinical", 10, "Discovery", 11, 99) ASC
```

Excel version with full metadata: `PD_Pipeline_Atomic_Notes.xlsx` (in Downloads)
