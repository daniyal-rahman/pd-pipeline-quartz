---
company_name: "Prothena"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:PRTA"
headquarters: "Dublin, Ireland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.prothena.com"
tags:
  - pd-pipeline
  - company
---

# Prothena

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Prothena" OR partner = "Prothena"
SORT stage ASC
```
