# Unmatched Clinical Trials

#claude

Cross-reference of all trials listed in `clinical-trials/` against asset notes in `assets/`. The following trials do **not** have a corresponding asset note.

---

## Methodology

Every trial entry in `trials-2024-2026.md` and `new-assets.md` was checked against the `assets/` folder by searching for:
- NCT number (exact match)
- Drug name and aliases
- Sponsor / company name
- Mechanism keywords

A trial is listed here only if none of these identifiers appear in any asset note.

---

## Unmatched Therapeutic Trials

### 1. NCT07232147 -- Unknown Stem Cell Therapy

| Field | Value |
|-------|-------|
| **NCT Number** | NCT07232147 |
| **Drug/Asset** | Stem cell therapy (name not specified) |
| **Sponsor** | Unknown |
| **Phase** | Phase 1 |
| **Mechanism** | Stem cell-based dopamine replacement |
| **Status** | Unknown |
| **Why unmatched** | No asset note exists. The trial entry in `trials-2024-2026.md` itself notes "Limited details available." No drug name, no sponsor name, and no additional identifiers were recoverable from the clinical-trials files. The NCT number does not appear anywhere in the `assets/` folder. This may be a newly posted or poorly characterized registration that needs manual lookup on ClinicalTrials.gov. |

**Recommended action:** Search ClinicalTrials.gov directly for NCT07232147 to retrieve sponsor, drug name, and mechanism details. If it turns out to be a duplicate of an existing asset (e.g., a second registration for ANPD001, Bemdaneprocel, RNDP-001, or another known cell therapy), link it; otherwise create a new asset note.

---

## Unmatched Diagnostic Studies (Non-Therapeutic)

These are diagnostic/biomarker studies, not drug candidates. They were listed in `trials-2024-2026.md` under "Diagnostic Studies (Not Therapeutics)" and have no corresponding asset note because the `assets/` folder tracks therapeutic pipeline assets.

### 2. NCT04700722 -- Synuclein-One (CND Life Sciences)

| Field | Value |
|-------|-------|
| **NCT Number** | NCT04700722 |
| **Study Name** | Synuclein-One |
| **Sponsor** | CND Life Sciences |
| **Purpose** | Skin biopsy detection of phosphorylated alpha-synuclein for PD diagnosis |
| **Why unmatched** | This is a diagnostic study, not a therapeutic asset. No dedicated asset note exists. CND Life Sciences is mentioned in passing in `assets/km-819.md` (as a reference link) but there is no asset file for this diagnostic platform. |

**Recommended action:** Consider whether diagnostic assets warrant their own notes. If so, create an asset note for CND Life Sciences / Synuclein-One skin biopsy test. Otherwise, this gap is expected and can be ignored.

### 3. NCT06621602 -- pSyn Quantification Study

| Field | Value |
|-------|-------|
| **NCT Number** | NCT06621602 |
| **Study Name** | pSyn quantification |
| **Sponsor** | Unknown |
| **Purpose** | CSF/skin alpha-synuclein measurement |
| **Why unmatched** | This is a biomarker quantification study, not a therapeutic asset. No asset note exists, and the NCT number does not appear anywhere in the `assets/` folder. Sponsor details were not captured in the clinical-trials data. |

**Recommended action:** Same as above -- decide whether diagnostic/biomarker studies belong in the asset tracker. If not, this gap is expected.

---

## Summary

| Category | Total Trials in clinical-trials/ | Matched to Asset Note | Unmatched |
|----------|---|----|---|
| **Therapeutic trials** | 19 | 18 | 1 |
| **Diagnostic studies** | 2 | 0 | 2 |
| **Total** | 21 | 18 | 3 |

### Matched Trials (for reference)

All of the following therapeutic trials have at least one corresponding asset note in `assets/`:

| NCT / ID | Drug | Asset File(s) |
|----------|------|---------------|
| NCT06344026 | ANPD001 | `anpd001.md` |
| NCT04802733 | Bemdaneprocel (MSK-DA01) | `bemdaneprocel.md` |
| NCT06687837 | Autologous mDAPs (MGH/Schweitzer) | `cellino-ipsc.md`, `autologous-mdaps.md` |
| NCT07106021 | RNDP-001 | `rndp-001.md` |
| NCT04127578 | PR001 / LY3884961 | `pr001.md` |
| NCT04167540 / NCT06285643 | AB-1005 (AAV2-GDNF) | `ab-1005.md` |
| NCT06602193 / NCT05348785 | BIIB122 (DNL151) | `biib122.md` |
| N/A | ARV-102 | `arv-102.md` |
| NCT06193421 | High-dose Ambroxol (Agyany) | `ambroxol.md` |
| NCT05287503 | Ambroxol (AMBITIOUS) | `ambroxol.md` |
| NCT03100149 | Prasinezumab | `prasinezumab.md` |
| N/A | UB-312 | `ub-312.md` |
| NCT05424276 | Risvodetinib (IkT-148009) | `risvodetinib.md` |
| NCT03439943 | Lixisenatide | `lixisenatide.md` |
| N/A | Exenatide | `exenatide.md` |
| N/A | Semaglutide | `semaglutide.md` |
| N/A | Dapansutrile (OLT1177) | `dapansutrile.md` |
| N/A | HER-096 | `her-096.md` |
| N/A | NRG5051 | `nrg5051.md` |
| N/A | NouvNeu001 | `nouvneu001.md` |

---

*Generated: 2026-02-16*
*Source files: `clinical-trials/trials-2024-2026.md`, `clinical-trials/new-assets.md`, all files in `assets/`*
