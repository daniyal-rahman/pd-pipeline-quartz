---
company_name: "LISCure Biosciences"
type: "biotech"
publicly_traded: false
headquarters: "Daejeon, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.liscure.com"
tags:
  - pd-pipeline
  - company
---

# LISCure Biosciences

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "LISCure Biosciences" OR partner = "LISCure Biosciences"
SORT stage ASC
```
