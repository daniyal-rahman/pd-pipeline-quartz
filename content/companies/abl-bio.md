---
company_name: "ABL Bio"
type: "biotech"
publicly_traded: true
ticker: "KOSDAQ:298380"
headquarters: "Daejeon, South Korea"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.ablbio.com"
tags:
  - pd-pipeline
  - company
---

# ABL Bio

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "ABL Bio" OR partner = "ABL Bio"
SORT stage ASC
```
