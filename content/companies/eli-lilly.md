---
company_name: "Eli Lilly"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:LLY"
headquarters: "Indianapolis, IN, USA"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.lilly.com"
tags:
  - pd-pipeline
  - company
---

# Eli Lilly

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Eli Lilly" OR partner = "Eli Lilly" OR developer = "Eli Lilly (parent company)" OR partner = "Eli Lilly (parent company)"
SORT stage ASC
```
