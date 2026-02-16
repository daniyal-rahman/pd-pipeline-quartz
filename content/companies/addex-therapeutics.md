---
company_name: "Addex Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "SIX:ADXN"
headquarters: "Geneva, Switzerland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.addextherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Addex Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Addex Therapeutics" OR partner = "Addex Therapeutics"
SORT stage ASC
```
