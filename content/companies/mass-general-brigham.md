---
company_name: "Mass General Brigham"
type: "academic"
publicly_traded: false
headquarters: "Boston, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.massgeneralbrigham.org"
tags:
  - pd-pipeline
  - company
---

# Mass General Brigham

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Mass General Brigham" OR partner = "Mass General Brigham"
SORT stage ASC
```
