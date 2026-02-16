---
company_name: "Sana Biotechnology"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:SANA"
headquarters: "Seattle, WA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.sana.com"
tags:
  - pd-pipeline
  - company
---

# Sana Biotechnology

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Sana Biotechnology" OR partner = "Sana Biotechnology"
SORT stage ASC
```
