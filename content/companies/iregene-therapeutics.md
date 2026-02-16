---
company_name: "iRegene Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Shenzhen, China"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.iregene.com"
tags:
  - pd-pipeline
  - company
---

# iRegene Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "iRegene Therapeutics" OR partner = "iRegene Therapeutics"
SORT stage ASC
```
