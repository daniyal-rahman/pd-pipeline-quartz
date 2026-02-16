---
company_name: "SciNeuro Pharmaceuticals"
type: "biotech"
publicly_traded: false
headquarters: "South San Francisco, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.scineuropharma.com"
tags:
  - pd-pipeline
  - company
---

# SciNeuro Pharmaceuticals

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "SciNeuro Pharmaceuticals" OR partner = "SciNeuro Pharmaceuticals"
SORT stage ASC
```
