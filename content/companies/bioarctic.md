---
company_name: "BioArctic"
type: "biotech"
publicly_traded: true
ticker: "STO:BIOA-B"
headquarters: "Stockholm, Sweden"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.bioarctic.se"
tags:
  - pd-pipeline
  - company
---

# BioArctic

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "BioArctic" OR partner = "BioArctic"
SORT stage ASC
```
