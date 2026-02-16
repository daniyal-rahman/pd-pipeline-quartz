---
company_name: "UCLH NHS Foundation Trust"
type: "academic"
publicly_traded: false
headquarters: "London, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.uclh.nhs.uk"
tags:
  - pd-pipeline
  - company
---

# UCLH NHS Foundation Trust

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "UCLH NHS Foundation Trust" OR partner = "UCLH NHS Foundation Trust"
SORT stage ASC
```
