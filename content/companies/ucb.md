---
company_name: "UCB"
type: "big pharma"
publicly_traded: true
ticker: "EURONEXT:UCB"
headquarters: "Brussels, Belgium"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.ucb.com"
tags:
  - pd-pipeline
  - company
---

# UCB

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "UCB" OR partner = "UCB"
SORT stage ASC
```
