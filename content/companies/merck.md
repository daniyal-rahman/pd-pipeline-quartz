---
company_name: "Merck"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:MRK"
headquarters: "Rahway, NJ, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.merck.com"
tags:
  - pd-pipeline
  - company
---

# Merck

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Merck" OR partner = "Merck"
SORT stage ASC
```
