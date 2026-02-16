---
company_name: "Pharma Two B"
type: "biotech"
publicly_traded: false
headquarters: "Rehovot, Israel"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.pharma2b.com"
tags:
  - pd-pipeline
  - company
---

# Pharma Two B

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Pharma Two B" OR partner = "Pharma Two B"
SORT stage ASC
```
