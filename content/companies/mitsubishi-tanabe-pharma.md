---
company_name: "Mitsubishi Tanabe Pharma"
type: "big pharma"
publicly_traded: false
headquarters: "Osaka, Japan"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.mt-pharma.co.jp"
tags:
  - pd-pipeline
  - company
---

# Mitsubishi Tanabe Pharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Mitsubishi Tanabe Pharma" OR partner = "Mitsubishi Tanabe Pharma"
SORT stage ASC
```
