---
company_name: "Cognition Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:CGTX"
headquarters: "Pittsburgh, PA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.cogrx.com"
tags:
  - pd-pipeline
  - company
---

# Cognition Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Cognition Therapeutics" OR partner = "Cognition Therapeutics"
SORT stage ASC
```
