---
company_name: "Kainos Medicine"
type: "biotech"
publicly_traded: true
ticker: "KOSDAQ:371950"
headquarters: "Seoul, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.kainosmedicine.com"
tags:
  - pd-pipeline
  - company
---

# Kainos Medicine

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Kainos Medicine" OR partner = "Kainos Medicine"
SORT stage ASC
```
