---
company_name: "Neurocrine Biosciences"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:NBIX"
headquarters: "San Diego, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.neurocrine.com"
tags:
  - pd-pipeline
  - company
---

# Neurocrine Biosciences

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Neurocrine Biosciences" OR partner = "Neurocrine Biosciences"
SORT stage ASC
```
