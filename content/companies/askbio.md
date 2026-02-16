---
company_name: "AskBio"
type: "biotech"
publicly_traded: false
headquarters: "Research Triangle Park, NC, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.askbio.com"
tags:
  - pd-pipeline
  - company
---

# AskBio

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "AskBio" OR partner = "AskBio"
SORT stage ASC
```
