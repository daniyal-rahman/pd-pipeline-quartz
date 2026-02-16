---
company_name: "BIAL"
type: "biotech"
publicly_traded: false
headquarters: "Porto, Portugal"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.bial.com"
tags:
  - pd-pipeline
  - company
---

# BIAL

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "BIAL" OR partner = "BIAL"
SORT stage ASC
```
