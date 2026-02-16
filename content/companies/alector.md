---
company_name: "Alector"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:ALEC"
headquarters: "South San Francisco, CA, USA"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.alector.com"
tags:
  - pd-pipeline
  - company
---

# Alector

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Alector" OR partner = "Alector"
SORT stage ASC
```
