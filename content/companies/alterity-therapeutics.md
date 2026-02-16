---
company_name: "Alterity Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:ATHE"
headquarters: "Melbourne, Australia"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.alteritytherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Alterity Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Alterity Therapeutics" OR partner = "Alterity Therapeutics"
SORT stage ASC
```
