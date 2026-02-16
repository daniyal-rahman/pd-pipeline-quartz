---
company_name: "Neuron23"
type: "biotech"
publicly_traded: false
headquarters: "South San Francisco, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.neuron23.com"
tags:
  - pd-pipeline
  - company
---

# Neuron23

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neuron23" OR partner = "Neuron23"
SORT stage ASC
```
