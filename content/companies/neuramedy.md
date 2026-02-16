---
company_name: "Neuramedy"
type: "biotech"
publicly_traded: false
headquarters: "Daejeon, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.neuramedy.com"
tags:
  - pd-pipeline
  - company
---

# Neuramedy

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neuramedy" OR partner = "Neuramedy"
SORT stage ASC
```
