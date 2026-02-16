---
company_name: "MODAG"
type: "biotech"
publicly_traded: false
headquarters: "Wendelsheim, Germany"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.modag.net"
tags:
  - pd-pipeline
  - company
---

# MODAG

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "MODAG GmbH" OR partner = "MODAG GmbH"
SORT stage ASC
```
