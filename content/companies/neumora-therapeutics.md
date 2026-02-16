---
company_name: "Neumora Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:NMRA"
headquarters: "Boston, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.neumoratx.com"
tags:
  - pd-pipeline
  - company
---

# Neumora Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neumora Therapeutics" OR partner = "Neumora Therapeutics"
SORT stage ASC
```
