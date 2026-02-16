---
company_name: "Shanghai East Hospital / Tongji University"
type: "academic"
publicly_traded: false
headquarters: "Shanghai, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Shanghai East Hospital / Tongji University

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Shanghai East Hospital (Tongji University)" OR partner = "Shanghai East Hospital (Tongji University)"
SORT stage ASC
```
