---
company_name: "Montara Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Montara Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Montara Therapeutics" OR partner = "Montara Therapeutics"
SORT stage ASC
```
