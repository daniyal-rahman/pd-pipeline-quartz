---
company_name: "NRG Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "Edinburgh, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.nrgtherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# NRG Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "NRG Therapeutics" OR partner = "NRG Therapeutics"
SORT stage ASC
```
