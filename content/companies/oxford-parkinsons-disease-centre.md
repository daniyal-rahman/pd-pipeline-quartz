---
company_name: "Oxford Parkinson's Disease Centre"
type: "academic"
publicly_traded: false
headquarters: "Oxford, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.opdc.ox.ac.uk"
tags:
  - pd-pipeline
  - company
---

# Oxford Parkinson's Disease Centre

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Oxford Parkinson's Disease Centre (OPDC)" OR partner = "Oxford Parkinson's Disease Centre (OPDC)"
SORT stage ASC
```
