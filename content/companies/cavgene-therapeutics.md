---
company_name: "CavGene Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# CavGene Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "CavGene Therapeutics" OR partner = "CavGene Therapeutics"
SORT stage ASC
```
