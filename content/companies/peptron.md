---
company_name: "Peptron"
type: "biotech"
publicly_traded: true
ticker: "KOSDAQ:087010"
headquarters: "Daejeon, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.peptron.com"
tags:
  - pd-pipeline
  - company
---

# Peptron

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Peptron" OR partner = "Peptron"
SORT stage ASC
```
