---
company_name: "GSK"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:GSK"
headquarters: "London, UK"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.gsk.com"
tags:
  - pd-pipeline
  - company
---

# GSK

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "GSK" OR partner = "GSK"
SORT stage ASC
```
