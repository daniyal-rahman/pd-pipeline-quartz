---
company_name: "XellSmart / Shize Bio"
type: "biotech"
publicly_traded: false
headquarters: "Shanghai, China"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# XellSmart / Shize Bio

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "XellSmart / Shize Bio (士泽生物)" OR partner = "XellSmart / Shize Bio (士泽生物)"
SORT stage ASC
```
