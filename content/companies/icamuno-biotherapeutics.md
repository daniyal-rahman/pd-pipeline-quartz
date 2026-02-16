---
company_name: "iCamuno Biotherapeutics"
type: "biotech"
publicly_traded: false
headquarters: "Basel, Switzerland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.icamuno.com"
tags:
  - pd-pipeline
  - company
---

# iCamuno Biotherapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "iCamuno Biotherapeutics" OR partner = "iCamuno Biotherapeutics"
SORT stage ASC
```
