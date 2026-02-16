---
company_name: "Amneal Pharmaceuticals"
type: "biotech"
publicly_traded: true
ticker: "NYSE:AMRX"
headquarters: "Bridgewater, NJ, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.amneal.com"
tags:
  - pd-pipeline
  - company
---

# Amneal Pharmaceuticals

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Amneal Pharmaceuticals" OR partner = "Amneal Pharmaceuticals"
SORT stage ASC
```
