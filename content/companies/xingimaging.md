---
company_name: "XingImaging"
type: "startup"
publicly_traded: false
headquarters: "China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# XingImaging

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "XingImaging" OR partner = "XingImaging"
SORT stage ASC
```
