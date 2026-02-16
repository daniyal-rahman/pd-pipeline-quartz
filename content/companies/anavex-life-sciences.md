---
company_name: "Anavex Life Sciences"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:AVXL"
headquarters: "New York, NY, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.anavex.com"
tags:
  - pd-pipeline
  - company
---

# Anavex Life Sciences

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Anavex Life Sciences" OR partner = "Anavex Life Sciences"
SORT stage ASC
```
