---
company_name: "Capsida Biotherapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Thousand Oaks, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.capsida.com"
tags:
  - pd-pipeline
  - company
---

# Capsida Biotherapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Capsida Biotherapeutics" OR partner = "Capsida Biotherapeutics"
SORT stage ASC
```
