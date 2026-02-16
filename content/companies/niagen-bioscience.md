---
company_name: "Niagen Bioscience"
type: "biotech"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Niagen Bioscience

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Niagen Bioscience" OR partner = "Niagen Bioscience"
SORT stage ASC
```
