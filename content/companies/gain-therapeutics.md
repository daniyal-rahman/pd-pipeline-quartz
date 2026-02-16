---
company_name: "Gain Therapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:GANX"
headquarters: "Bethesda, MD, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.gaintherapeutics.com"
tags:
  - pd-pipeline
  - company
---

# Gain Therapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Gain Therapeutics" OR partner = "Gain Therapeutics"
SORT stage ASC
```
