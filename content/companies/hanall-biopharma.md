---
company_name: "HanAll BioPharma"
type: "biotech"
publicly_traded: true
ticker: "KOSDAQ:009420"
headquarters: "Seoul, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.hanall.co.kr"
tags:
  - pd-pipeline
  - company
---

# HanAll BioPharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "HanAll BioPharma / Daewoong Pharmaceutical" OR partner = "HanAll BioPharma / Daewoong Pharmaceutical"
SORT stage ASC
```
