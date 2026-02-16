---
company_name: "Celltrion"
type: "biotech"
publicly_traded: true
ticker: "KRX:068270"
headquarters: "Incheon, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.celltrion.com"
tags:
  - pd-pipeline
  - company
---

# Celltrion

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Celltrion" OR partner = "Celltrion"
SORT stage ASC
```
