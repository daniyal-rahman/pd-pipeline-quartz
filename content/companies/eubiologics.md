---
company_name: "EuBiologics"
type: "biotech"
publicly_traded: true
ticker: "KOSDAQ:206650"
headquarters: "Chuncheon, South Korea"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.eubiologics.com"
tags:
  - pd-pipeline
  - company
---

# EuBiologics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "EuBiologics" OR partner = "EuBiologics"
SORT stage ASC
```
