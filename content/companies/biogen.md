---
company_name: "Biogen"
type: "big pharma"
publicly_traded: true
ticker: "NASDAQ:BIIB"
headquarters: "Cambridge, MA, USA"
pd_focus: "primary"
total_pd_assets: 5
website: "https://www.biogen.com"
tags:
  - pd-pipeline
  - company
---

# Biogen

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Biogen" OR partner = "Biogen"
SORT stage ASC
```
