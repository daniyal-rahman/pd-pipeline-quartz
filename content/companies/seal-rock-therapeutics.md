---
company_name: "Seal Rock Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "Seattle, WA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.sealrocktx.com"
tags:
  - pd-pipeline
  - company
---

# Seal Rock Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Seal Rock Therapeutics" OR partner = "Seal Rock Therapeutics"
SORT stage ASC
```
