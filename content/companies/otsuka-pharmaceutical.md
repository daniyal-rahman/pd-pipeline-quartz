---
company_name: "Otsuka Pharmaceutical"
type: "big pharma"
publicly_traded: true
ticker: "TSE:4578"
headquarters: "Tokyo, Japan"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.otsuka.co.jp"
tags:
  - pd-pipeline
  - company
---

# Otsuka Pharmaceutical

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "MSRD (Otsuka)" OR partner = "MSRD (Otsuka)" OR developer = "Otsuka Pharmaceutical" OR partner = "Otsuka Pharmaceutical"
SORT stage ASC
```
