---
company_name: "Genmab"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:GMAB"
headquarters: "Copenhagen, Denmark"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.genmab.com"
tags:
  - pd-pipeline
  - company
---

# Genmab

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Genmab" OR partner = "Genmab"
SORT stage ASC
```
