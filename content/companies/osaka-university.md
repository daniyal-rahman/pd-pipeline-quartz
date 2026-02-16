---
company_name: "Osaka University"
type: "academic"
publicly_traded: false
headquarters: "Osaka, Japan"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.osaka-u.ac.jp"
tags:
  - pd-pipeline
  - company
---

# Osaka University

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Osaka University (academic collaboration)" OR partner = "Osaka University (academic collaboration)"
SORT stage ASC
```
