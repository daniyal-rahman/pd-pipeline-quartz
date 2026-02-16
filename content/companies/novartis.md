---
company_name: "Novartis"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:NVS"
headquarters: "Basel, Switzerland"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.novartis.com"
tags:
  - pd-pipeline
  - company
---

# Novartis

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Novartis" OR partner = "Novartis"
SORT stage ASC
```
