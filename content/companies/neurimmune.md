---
company_name: "Neurimmune"
type: "biotech"
publicly_traded: false
headquarters: "Zurich, Switzerland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.neurimmune.com"
tags:
  - pd-pipeline
  - company
---

# Neurimmune

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neurimmune" OR partner = "Neurimmune"
SORT stage ASC
```
