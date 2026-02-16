---
company_name: "Voyager Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:VYGR"
headquarters: "Lexington, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.voyagertherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Voyager Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Voyager Therapeutics" OR partner = "Voyager Therapeutics"
SORT stage ASC
```
