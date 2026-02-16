---
company_name: "CiRA / Kyoto University"
type: "academic"
publicly_traded: false
headquarters: "Kyoto, Japan"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.cira.kyoto-u.ac.jp"
tags:
  - pd-pipeline
  - company
---

# CiRA / Kyoto University

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "CiRA (Kyoto University) / Sumitomo Pharma" OR partner = "CiRA (Kyoto University) / Sumitomo Pharma" OR developer = "CiRA Foundation / Kyoto University" OR partner = "CiRA Foundation / Kyoto University"
SORT stage ASC
```
