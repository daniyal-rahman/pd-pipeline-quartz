---
company_name: "Partner Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Lexington, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.partnertx.com"
tags:
  - pd-pipeline
  - company
---

# Partner Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Partner Therapeutics" OR partner = "Partner Therapeutics"
SORT stage ASC
```
