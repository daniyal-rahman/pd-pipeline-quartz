---
company_name: "Lario Therapeutics"
type: "startup"
publicly_traded: false
headquarters: "Cambridge, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.lariotherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Lario Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Lario Therapeutics" OR partner = "Lario Therapeutics"
SORT stage ASC
```
