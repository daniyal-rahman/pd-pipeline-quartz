---
company_name: "Progenra"
type: "startup"
publicly_traded: false
headquarters: "Malvern, PA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.progenra.com"
tags:
  - pd-pipeline
  - company
---

# Progenra

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Progenra" OR partner = "Progenra"
SORT stage ASC
```
