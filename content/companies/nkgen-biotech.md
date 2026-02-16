---
company_name: "NKGen Biotech"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:NKGN"
headquarters: "Santa Ana, CA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.nkgenbiotech.com"
tags:
  - pd-pipeline
  - company
---

# NKGen Biotech

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "NKGen Biotech" OR partner = "NKGen Biotech"
SORT stage ASC
```
