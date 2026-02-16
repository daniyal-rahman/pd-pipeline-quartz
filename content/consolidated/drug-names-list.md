# Parkinson's Disease Pipeline - Drug Names List

#claude

**Auto-generated from asset notes via Dataview.**

---

## All Pipeline Assets

```dataview
TABLE drug_name AS "Drug Name", developer AS "Developer", stage AS "Stage", status AS "Status", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null
SORT stage ASC, drug_name ASC
```

---

## Active Assets Only

```dataview
TABLE drug_name AS "Drug Name", developer AS "Developer", stage AS "Stage", target AS "Target"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null AND status = "Active"
SORT stage ASC, drug_name ASC
```

---

## By Thesis Cluster

```dataview
TABLE drug_name AS "Drug Name", developer AS "Developer", stage AS "Stage", status AS "Status"
FROM "pd-pipeline-research/assets"
WHERE drug_name != null AND status = "Active"
SORT thesis_cluster ASC, stage ASC
```

---

**Total asset notes:** `$= dv.pages('"pd-pipeline-research/assets"').where(p => p.drug_name).length` tracked
