---
company_name: "Longevity Biotech"
type: "startup"
publicly_traded: false
headquarters: "Philadelphia, PA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.longevitybiotech.com"
tags:
  - pd-pipeline
  - company
---

# Longevity Biotech

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Longevity Biotech" OR partner = "Longevity Biotech"
SORT stage ASC
```
