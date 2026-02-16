---
company_name: "Cedars-Sinai / Cure Parkinson's"
type: "academic"
publicly_traded: false
headquarters: "Los Angeles, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.cedars-sinai.org"
tags:
  - pd-pipeline
  - company
---

# Cedars-Sinai / Cure Parkinson's

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Academic (Cedars-Sinai / Cure Parkinson's)" OR partner = "Academic (Cedars-Sinai / Cure Parkinson's)"
SORT stage ASC
```
