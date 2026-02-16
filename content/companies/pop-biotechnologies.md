---
company_name: "POP Biotechnologies"
type: "biotech"
publicly_traded: false
headquarters: "USA"
pd_focus: "single-asset"
total_pd_assets: 1
tags:
  - pd-pipeline
  - company
---

# POP Biotechnologies

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "POP Biotechnologies (via EuPOP Life Sciences JV)" OR partner = "POP Biotechnologies (via EuPOP Life Sciences JV)"
SORT stage ASC
```
