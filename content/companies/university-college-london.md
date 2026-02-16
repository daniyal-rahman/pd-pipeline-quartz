---
company_name: "University College London"
type: "academic"
publicly_traded: false
headquarters: "London, UK"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.ucl.ac.uk"
tags:
  - pd-pipeline
  - company
---

# University College London

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "UCL (Tom Foltynie)" OR partner = "UCL (Tom Foltynie)" OR developer = "UCL / Guilford Street Laboratories" OR partner = "UCL / Guilford Street Laboratories" OR developer = "UCL / MRC Clinical Trials Unit" OR partner = "UCL / MRC Clinical Trials Unit"
SORT stage ASC
```
