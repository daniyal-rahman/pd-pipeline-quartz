---
company_name: "IRLAB Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "STO:IRLAB-A"
headquarters: "Gothenburg, Sweden"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.irlab.se"
tags:
  - pd-pipeline
  - company
---

# IRLAB Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "IRLAB Therapeutics" OR partner = "IRLAB Therapeutics"
SORT stage ASC
```
