---
company_name: "Cure Parkinson's"
type: "nonprofit"
publicly_traded: false
headquarters: "London, UK"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.cureparkinsons.org.uk"
tags:
  - pd-pipeline
  - company
---

# Cure Parkinson's

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Cure Parkinson's / MRC / NIHR" OR partner = "Cure Parkinson's / MRC / NIHR" OR developer = "Cure Parkinson's / Parkinson's UK / MJFF / Van Andel Institute" OR partner = "Cure Parkinson's / Parkinson's UK / MJFF / Van Andel Institute"
SORT stage ASC
```
