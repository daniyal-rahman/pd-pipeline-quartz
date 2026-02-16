---
company_name: "Sun Pharma Advanced Research"
type: "biotech"
publicly_traded: true
ticker: "NSE:SPARC"
headquarters: "Mumbai, India"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.sparc.life"
tags:
  - pd-pipeline
  - company
---

# Sun Pharma Advanced Research

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Sun Pharma Advanced Research (SPARC)" OR partner = "Sun Pharma Advanced Research (SPARC)"
SORT stage ASC
```
