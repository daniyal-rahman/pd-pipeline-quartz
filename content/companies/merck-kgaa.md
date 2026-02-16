---
company_name: "Merck KGaA"
type: "big pharma"
publicly_traded: true
ticker: "XETRA:MRK"
headquarters: "Darmstadt, Germany"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.emdgroup.com"
tags:
  - pd-pipeline
  - company
---

# Merck KGaA

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Merck KGaA (EMD Serono)" OR partner = "Merck KGaA (EMD Serono)"
SORT stage ASC
```
