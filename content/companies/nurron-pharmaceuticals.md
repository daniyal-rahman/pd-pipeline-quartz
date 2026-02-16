---
company_name: "NurrOn Pharmaceuticals"
type: "biotech"
publicly_traded: false
headquarters: "South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.nurron.com"
tags:
  - pd-pipeline
  - company
---

# NurrOn Pharmaceuticals

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "NurrOn Pharmaceuticals" OR partner = "NurrOn Pharmaceuticals"
SORT stage ASC
```
