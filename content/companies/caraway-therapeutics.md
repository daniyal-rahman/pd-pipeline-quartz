---
company_name: "Caraway Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Boston, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Caraway Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Caraway Therapeutics (acquired by Merck)" OR partner = "Caraway Therapeutics (acquired by Merck)"
SORT stage ASC
```
