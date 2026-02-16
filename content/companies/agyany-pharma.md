---
company_name: "Agyany Pharma"
type: "startup"
publicly_traded: false
headquarters: "India"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Agyany Pharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Multiple investigators / Agyany Pharma" OR partner = "Multiple investigators / Agyany Pharma"
SORT stage ASC
```
