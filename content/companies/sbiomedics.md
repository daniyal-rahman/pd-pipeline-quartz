---
company_name: "S.BIOMEDICS"
type: "biotech"
publicly_traded: false
headquarters: "Seoul, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# S.BIOMEDICS

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "S.BIOMEDICS" OR partner = "S.BIOMEDICS"
SORT stage ASC
```
