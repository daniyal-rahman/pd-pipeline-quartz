---
company_name: "Bayer"
type: "big pharma"
publicly_traded: true
ticker: "XETRA:BAYN"
headquarters: "Leverkusen, Germany"
pd_focus: "secondary"
total_pd_assets: 2
website: "https://www.bayer.com"
tags:
  - pd-pipeline
  - company
---

# Bayer

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Bayer" OR partner = "Bayer"
SORT stage ASC
```
