---
company_name: "Serina Therapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Huntsville, AL, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.serinatherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Serina Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Serina Therapeutics" OR partner = "Serina Therapeutics"
SORT stage ASC
```
