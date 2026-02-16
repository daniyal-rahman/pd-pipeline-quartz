---
company_name: "Hangzhou Highlightll Pharma"
type: "biotech"
publicly_traded: false
headquarters: "Hangzhou, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Hangzhou Highlightll Pharma

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Hangzhou Highlightll Pharma" OR partner = "Hangzhou Highlightll Pharma"
SORT stage ASC
```
