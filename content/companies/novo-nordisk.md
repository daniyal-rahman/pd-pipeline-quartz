---
company_name: "Novo Nordisk"
type: "big pharma"
publicly_traded: true
ticker: "NYSE:NVO"
headquarters: "Bagsvaerd, Denmark"
pd_focus: "primary"
total_pd_assets: 3
website: "https://www.novonordisk.com"
tags:
  - pd-pipeline
  - company
---

# Novo Nordisk

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Novo Nordisk" OR partner = "Novo Nordisk" OR developer = "Novo Nordisk (originator)" OR partner = "Novo Nordisk (originator)" OR developer = "Novo Nordisk / Osaka University" OR partner = "Novo Nordisk / Osaka University"
SORT stage ASC
```
