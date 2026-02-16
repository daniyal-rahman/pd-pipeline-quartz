---
company_name: "PTC Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:PTCT"
headquarters: "South Plainfield, NJ, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.ptcbio.com"
tags:
  - pd-pipeline
  - company
---

# PTC Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "PTC Therapeutics" OR partner = "PTC Therapeutics"
SORT stage ASC
```
