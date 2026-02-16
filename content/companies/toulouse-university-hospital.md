---
company_name: "Toulouse University Hospital"
type: "academic"
publicly_traded: false
headquarters: "Toulouse, France"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Toulouse University Hospital

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Toulouse University Hospital (academic)" OR partner = "Toulouse University Hospital (academic)"
SORT stage ASC
```
