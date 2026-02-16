---
company_name: "Lundbeck"
type: "big pharma"
publicly_traded: true
ticker: "CPH:HLUN-B"
headquarters: "Copenhagen, Denmark"
pd_focus: "primary"
total_pd_assets: 4
website: "https://www.lundbeck.com"
tags:
  - pd-pipeline
  - company
---

# Lundbeck

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Lundbeck" OR partner = "Lundbeck"
SORT stage ASC
```
