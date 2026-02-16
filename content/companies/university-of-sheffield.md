---
company_name: "University of Sheffield"
type: "academic"
publicly_traded: false
headquarters: "Sheffield, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.sheffield.ac.uk"
tags:
  - pd-pipeline
  - company
---

# University of Sheffield

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "University of Sheffield / UCL" OR partner = "University of Sheffield / UCL"
SORT stage ASC
```
