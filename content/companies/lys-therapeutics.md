---
company_name: "Lys Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "France"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Lys Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Lys Therapeutics" OR partner = "Lys Therapeutics"
SORT stage ASC
```
