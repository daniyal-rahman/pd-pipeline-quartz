---
company_name: "Zambon"
type: "big pharma"
publicly_traded: false
headquarters: "Milan, Italy"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.zambon.com"
tags:
  - pd-pipeline
  - company
---

# Zambon

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Zambon" OR partner = "Zambon"
SORT stage ASC
```
