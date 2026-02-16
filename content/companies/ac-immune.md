---
company_name: "AC Immune"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:ACIU"
headquarters: "Lausanne, Switzerland"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.acimmune.com"
tags:
  - pd-pipeline
  - company
---

# AC Immune

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "AC Immune" OR partner = "AC Immune"
SORT stage ASC
```
