---
company_name: "Shanghai Vitalgen BioPharma"
type: "biotech"
publicly_traded: false
headquarters: "Shanghai, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Shanghai Vitalgen BioPharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Shanghai Vitalgen BioPharma" OR partner = "Shanghai Vitalgen BioPharma"
SORT stage ASC
```
