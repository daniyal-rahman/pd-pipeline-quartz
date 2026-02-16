---
company_name: "AbbVie"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:ABBV"
headquarters: "North Chicago, IL, USA"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.abbvie.com"
tags:
  - pd-pipeline
  - company
---

# AbbVie

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "AbbVie" OR partner = "AbbVie" OR developer = "AbbVie (pre-acquisition collaboration)" OR partner = "AbbVie (pre-acquisition collaboration)"
SORT stage ASC
```
