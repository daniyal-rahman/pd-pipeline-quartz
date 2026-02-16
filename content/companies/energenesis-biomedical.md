---
company_name: "Energenesis Biomedical"
type: "biotech"
publicly_traded: false
headquarters: "Taipei, Taiwan"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.energenesis-biomedical.com"
tags:
  - pd-pipeline
  - company
---

# Energenesis Biomedical

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Energenesis Biomedical" OR partner = "Energenesis Biomedical"
SORT stage ASC
```
