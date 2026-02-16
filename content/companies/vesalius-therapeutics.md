---
company_name: "Vesalius Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.vesaliustx.com"
tags:
  - pd-pipeline
  - company
---

# Vesalius Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Vesalius Therapeutics" OR partner = "Vesalius Therapeutics"
SORT stage ASC
```
