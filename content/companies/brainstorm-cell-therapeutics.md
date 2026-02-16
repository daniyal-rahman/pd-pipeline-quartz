---
company_name: "BrainStorm Cell Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:BCLI"
headquarters: "New York, NY, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.brainstorm-cell.com"
tags:
  - pd-pipeline
  - company
---

# BrainStorm Cell Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "BrainStorm Cell Therapeutics" OR partner = "BrainStorm Cell Therapeutics"
SORT stage ASC
```
