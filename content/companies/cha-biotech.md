---
company_name: "CHA Biotech"
type: "biotech"
publicly_traded: false
headquarters: "Seongnam, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.chabio.com"
tags:
  - pd-pipeline
  - company
---

# CHA Biotech

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "CHA Biotech" OR partner = "CHA Biotech"
SORT stage ASC
```
