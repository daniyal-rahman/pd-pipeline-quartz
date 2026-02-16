---
company_name: "UniXell Biotechnology"
type: "startup"
publicly_traded: false
headquarters: "Shanghai, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# UniXell Biotechnology

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "UniXell Biotechnology" OR partner = "UniXell Biotechnology"
SORT stage ASC
```
