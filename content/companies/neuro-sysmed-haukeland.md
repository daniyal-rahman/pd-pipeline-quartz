---
company_name: "Neuro-SysMed / Haukeland University Hospital"
type: "academic"
publicly_traded: false
headquarters: "Bergen, Norway"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.uib.no/en/neuro-sysmed"
tags:
  - pd-pipeline
  - company
---

# Neuro-SysMed / Haukeland University Hospital

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neuro-SysMed / Haukeland University Hospital" OR partner = "Neuro-SysMed / Haukeland University Hospital"
SORT stage ASC
```
