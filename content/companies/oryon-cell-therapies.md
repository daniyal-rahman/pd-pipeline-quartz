---
company_name: "Oryon Cell Therapies"
type: "startup"
publicly_traded: false
headquarters: "Barcelona, Spain"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Oryon Cell Therapies

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Oryon Cell Therapies" OR partner = "Oryon Cell Therapies"
SORT stage ASC
```
