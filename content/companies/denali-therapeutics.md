---
company_name: "Denali Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:DNLI"
headquarters: "South San Francisco, CA, USA"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.denalitherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Denali Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Denali Therapeutics" OR partner = "Denali Therapeutics"
SORT stage ASC
```
