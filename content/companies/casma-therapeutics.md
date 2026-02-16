---
company_name: "Casma Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Cambridge, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.casmatx.com"
tags:
  - pd-pipeline
  - company
---

# Casma Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Casma Therapeutics" OR partner = "Casma Therapeutics"
SORT stage ASC
```
