---
company_name: "NodThera"
type: "biotech"
publicly_traded: false
headquarters: "Cambridge, UK"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.nodthera.com"
tags:
  - pd-pipeline
  - company
---

# NodThera

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "NodThera" OR partner = "NodThera"
SORT stage ASC
```
