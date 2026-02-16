---
company_name: "QIAGEN"
type: "biotech"
publicly_traded: true
ticker: "NYSE:QGEN"
headquarters: "Venlo, Netherlands"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.qiagen.com"
tags:
  - pd-pipeline
  - company
---

# QIAGEN

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "QIAGEN" OR partner = "QIAGEN"
SORT stage ASC
```
