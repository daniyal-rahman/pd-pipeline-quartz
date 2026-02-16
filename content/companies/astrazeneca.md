---
company_name: "AstraZeneca"
type: "big pharma"
publicly_traded: true
ticker: "NASDAQ:AZN"
headquarters: "Cambridge, UK"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.astrazeneca.com"
tags:
  - pd-pipeline
  - company
---

# AstraZeneca

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "AstraZeneca (originator of exenatide)" OR partner = "AstraZeneca (originator of exenatide)"
SORT stage ASC
```
