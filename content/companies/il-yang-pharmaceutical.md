---
company_name: "Il-Yang Pharmaceutical"
type: "biotech"
publicly_traded: true
ticker: "KRX:007570"
headquarters: "Seoul, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.ilyang.co.kr"
tags:
  - pd-pipeline
  - company
---

# Il-Yang Pharmaceutical

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Il-Yang Pharmaceutical" OR partner = "Il-Yang Pharmaceutical"
SORT stage ASC
```
