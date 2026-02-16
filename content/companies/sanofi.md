---
company_name: "Sanofi"
type: "big pharma"
publicly_traded: true
ticker: "NASDAQ:SNY"
headquarters: "Paris, France"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.sanofi.com"
tags:
  - pd-pipeline
  - company
---

# Sanofi

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Sanofi" OR partner = "Sanofi" OR developer = "Sanofi (drug supply)" OR partner = "Sanofi (drug supply)"
SORT stage ASC
```
