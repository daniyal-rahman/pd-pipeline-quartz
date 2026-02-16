---
company_name: "FAScinate Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# FAScinate Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "FAScinate Therapeutics" OR partner = "FAScinate Therapeutics"
SORT stage ASC
```
