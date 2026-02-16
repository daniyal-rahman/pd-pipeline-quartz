---
company_name: "Spark Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Philadelphia, PA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.sparktx.com"
tags:
  - pd-pipeline
  - company
---

# Spark Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Spark Therapeutics" OR partner = "Spark Therapeutics"
SORT stage ASC
```
