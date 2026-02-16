---
company_name: "Teva Pharmaceutical"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:TEVA"
headquarters: "Tel Aviv, Israel"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.tevapharm.com"
tags:
  - pd-pipeline
  - company
---

# Teva Pharmaceutical

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Teva" OR partner = "Teva"
SORT stage ASC
```
