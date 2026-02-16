---
company_name: "Tricumed / Flowonix"
type: "biotech"
publicly_traded: false
headquarters: "Germany / USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Tricumed / Flowonix

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Tricumed / Flowonix (pump manufacturers)" OR partner = "Tricumed / Flowonix (pump manufacturers)"
SORT stage ASC
```
