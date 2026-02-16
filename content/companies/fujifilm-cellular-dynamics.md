---
company_name: "FUJIFILM Cellular Dynamics"
type: "biotech"
publicly_traded: false
headquarters: "Madison, WI, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.fujifilmcdi.com"
tags:
  - pd-pipeline
  - company
---

# FUJIFILM Cellular Dynamics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "FUJIFILM Cellular Dynamics" OR partner = "FUJIFILM Cellular Dynamics"
SORT stage ASC
```
