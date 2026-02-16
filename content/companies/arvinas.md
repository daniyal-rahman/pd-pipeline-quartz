---
company_name: "Arvinas"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:ARVN"
headquarters: "New Haven, CT, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.arvinas.com"
tags:
  - pd-pipeline
  - company
---

# Arvinas

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Arvinas" OR partner = "Arvinas"
SORT stage ASC
```
