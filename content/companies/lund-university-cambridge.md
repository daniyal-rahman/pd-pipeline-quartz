---
company_name: "Lund University / University of Cambridge"
type: "academic"
publicly_traded: false
headquarters: "Lund, Sweden / Cambridge, UK"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# Lund University / University of Cambridge

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Lund University / University of Cambridge" OR partner = "Lund University / University of Cambridge"
SORT stage ASC
```
