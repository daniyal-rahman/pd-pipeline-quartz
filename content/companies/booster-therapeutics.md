---
company_name: "Booster Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "Hangzhou, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Booster Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Booster Therapeutics" OR partner = "Booster Therapeutics"
SORT stage ASC
```
