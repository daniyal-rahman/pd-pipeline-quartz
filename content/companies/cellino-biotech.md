---
company_name: "Cellino Biotech"
type: "startup"
publicly_traded: false
headquarters: "Cambridge, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.cellinobio.com"
tags:
  - pd-pipeline
  - company
---

# Cellino Biotech

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Cellino Biotech" OR partner = "Cellino Biotech"
SORT stage ASC
```
