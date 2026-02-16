---
company_name: "University of Nebraska Medical Center"
type: "academic"
publicly_traded: false
headquarters: "Omaha, NE, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.unmc.edu"
tags:
  - pd-pipeline
  - company
---

# University of Nebraska Medical Center

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "University of Nebraska Medical Center (Howard Gendelman)" OR partner = "University of Nebraska Medical Center (Howard Gendelman)"
SORT stage ASC
```
