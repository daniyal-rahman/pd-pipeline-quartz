---
company_name: "Stealth BioTherapeutics"
type: "biotech"
publicly_traded: true
ticker: "NASDAQ:MITO"
headquarters: "Newton, MA, USA"
pd_focus: "single-asset"
total_pd_assets: 1
website: "https://www.stealthbt.com"
tags:
  - pd-pipeline
  - company
---

# Stealth BioTherapeutics

## PD Pipeline

```dataview
TABLE drug_name AS "Asset", stage AS "Stage", status AS "Status", target AS "Target", confidence_rating AS "Conf."
FROM "pd-pipeline-research/assets"
WHERE developer = "Stealth BioTherapeutics" OR partner = "Stealth BioTherapeutics"
SORT stage ASC
```
