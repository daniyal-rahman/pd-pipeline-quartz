---
company_name: "Roche"
type: "big pharma"
publicly_traded: true
ticker: "SIX:ROG"
headquarters: "Basel, Switzerland"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.roche.com"
tags:
  - pd-pipeline
  - company
---

# Roche

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Roche" OR partner = "Roche"
SORT stage ASC
```
