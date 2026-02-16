---
company_name: "MUNA Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "Dublin, Ireland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.munatherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# MUNA Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "MUNA Therapeutics" OR partner = "MUNA Therapeutics"
SORT stage ASC
```
