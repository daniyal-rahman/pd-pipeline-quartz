---
company_name: "Bioasis Technologies"
type: "biotech"
publicly_traded: true
ticker: "TSXV:BTI"
headquarters: "Langley, BC, Canada"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.bioasis.ca"
tags:
  - pd-pipeline
  - company
---

# Bioasis Technologies

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Bioasis Technologies" OR partner = "Bioasis Technologies"
SORT stage ASC
```
