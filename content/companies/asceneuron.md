---
company_name: "Asceneuron"
type: "startup"
publicly_traded: false
headquarters: "Lausanne, Switzerland"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.asceneuron.com"
tags:
  - pd-pipeline
  - company
---

# Asceneuron

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Asceneuron" OR partner = "Asceneuron"
SORT stage ASC
```
