---
company_name: "Ionis Pharmaceuticals"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:IONS"
headquarters: "Carlsbad, CA, USA"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.ionispharma.com"
tags:
  - pd-pipeline
  - company
---

# Ionis Pharmaceuticals

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Ionis Pharmaceuticals" OR partner = "Ionis Pharmaceuticals"
SORT stage ASC
```
