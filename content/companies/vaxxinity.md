---
company_name: "Vaxxinity"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:VAXX"
headquarters: "Dallas, TX, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.vaxxinity.com"
tags:
  - pd-pipeline
  - company
---

# Vaxxinity

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Vaxxinity" OR partner = "Vaxxinity"
SORT stage ASC
```
