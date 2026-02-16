---
company_name: "Insilico Medicine"
type: "biotech"
publicly_traded: false
headquarters: "Hong Kong, China"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.insilico.com"
tags:
  - pd-pipeline
  - company
---

# Insilico Medicine

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Insilico Medicine" OR partner = "Insilico Medicine"
SORT stage ASC
```
