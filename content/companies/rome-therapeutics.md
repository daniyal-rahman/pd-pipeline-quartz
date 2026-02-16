---
company_name: "ROME Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Boston, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.rometx.com"
tags:
  - pd-pipeline
  - company
---

# ROME Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "ROME Therapeutics" OR partner = "ROME Therapeutics"
SORT stage ASC
```
