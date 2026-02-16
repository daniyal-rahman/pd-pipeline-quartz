---
company_name: "Parkinson's UK"
type: "nonprofit"
publicly_traded: false
headquarters: "London, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.parkinsons.org.uk"
tags:
  - pd-pipeline
  - company
---

# Parkinson's UK

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Parkinson's UK" OR partner = "Parkinson's UK"
SORT stage ASC
```
