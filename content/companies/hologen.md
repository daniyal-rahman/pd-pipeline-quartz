---
company_name: "Hologen"
type: "biotech"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Hologen

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Hologen" OR partner = "Hologen"
SORT stage ASC
```
