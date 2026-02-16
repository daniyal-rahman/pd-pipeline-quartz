---
company_name: "Sumitomo Pharma"
type: "big pharma"
publicly_traded: true
ticker: "TSE:4506"
headquarters: "Osaka, Japan"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.sumitomo-pharma.com"
tags:
  - pd-pipeline
  - company
---

# Sumitomo Pharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Sumitomo Pharma / RACTHERA" OR partner = "Sumitomo Pharma / RACTHERA"
SORT stage ASC
```
