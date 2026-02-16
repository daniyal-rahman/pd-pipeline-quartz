---
drug_name: "Sana PD Program"
aliases: ["Sana HIP-DA", "Sana hypoimmune dopaminergic neurons"]
target: "dopaminergic neuron replacement (cell therapy)"
mechanism: "Allogeneic iPSC-derived dopaminergic neurons engineered with hypoimmune (HIP) modifications (B2M-/-CIITA-/-CD47+) to evade immune rejection without immunosuppression"
modality: "cell therapy (iPSC allogeneic)"
developer: "Sana Biotechnology"
company_type: "biotech"
publicly_traded: true
ticker: "SANA"
stage: "Preclinical"
status: "Deprioritized"
patient_population: "PD (not yet defined; program never reached IND)"
route_of_administration: "intracranial (presumed; stereotactic putaminal injection)"
key_biomarkers: ["18F-DOPA PET (graft survival)", "DaT-SPECT"]
confidence_rating: "2/10"
next_catalyst: "Partnership or spinout announcement for CNS programs"
catalyst_date: "TBD"
thesis_cluster: "cell-therapy"
tags: [pd-pipeline, claude]
date: 2026-02-15
---

# Sana PD Program

## Summary

Sana Biotechnology (biotech, SANA) developed a hypoimmune (HIP) iPSC platform that could theoretically generate off-the-shelf allogeneic dopaminergic neurons for PD without requiring immunosuppression -- a major differentiator vs. [[bemdaneprocel]] (allogeneic ESC, requires immunosuppression) and a potential scalability advantage over autologous approaches like [[anpd001]]. However, in November 2024 Sana deprioritized all CNS programs, including SC379 (glial progenitor cells for neurodegenerative diseases), to focus resources on type 1 diabetes (SC451) and autoimmune/oncology CAR-T (SG293). No PD-specific dopaminergic neuron candidate was ever publicly designated with a program code or advanced to IND-enabling studies. The HIP platform technology remains scientifically validated in NHP models, and Sana is actively seeking partners or a spinout for its CNS portfolio -- meaning this program could resurface under different ownership. For now, it is functionally inactive as an internal Sana program.

## Notes

### Science
- Sana's hypoimmune (HIP) platform engineers iPSCs with three genetic modifications: knockout of B2M (eliminates HLA class I), knockout of CIITA (eliminates HLA class II), and overexpression of CD47 ("don't eat me" signal) -- making cells invisible to both T cells and NK cells
- In fully immunocompetent allogeneic rhesus macaques, HIP-modified iPSCs survived for >40 weeks without immunosuppression, differentiated into cells from all three germ layers, and maintained functional engraftment (published in Nature Biotechnology, 2023)
- Wild-type (non-HIP) iPSCs were vigorously rejected in the same model, confirming the immune evasion is specifically attributable to the HIP modifications
- The platform is modality-agnostic: the same HIP engineering could be applied to dopaminergic neuron progenitors, cardiomyocytes, or pancreatic islet cells -- Sana has demonstrated clinical proof-of-concept in islet cells for type 1 diabetes (UP421)
- Key scientific distinction vs. [[bemdaneprocel]]: BlueRock uses ESC-derived neurons requiring chronic immunosuppression; Sana's HIP approach would eliminate immunosuppression entirely, removing a major long-term safety burden (infection risk, malignancy risk) for a therapy intended for decades-long engraftment
- Key scientific distinction vs. [[anpd001]]: Aspen's autologous iPSC approach also avoids immunosuppression but requires patient-specific manufacturing (~$100K+ per batch, months-long lead time); Sana's allogeneic HIP approach could enable off-the-shelf manufacturing at scale
- Open question: HIP-modified iPSC differentiation into high-purity, functional A9 dopaminergic neurons has not been publicly demonstrated by Sana -- the NHP survival data used undifferentiated iPSCs, not committed neuronal progenitors
- Safety concern specific to HIP: cells that evade immune surveillance could theoretically be harder to eliminate if tumorigenic -- CD47 overexpression prevents macrophage-mediated clearance, raising the question of whether a safety switch mechanism is needed

### Clinical
No clinical trials initiated. No IND filed for a PD indication. The program never progressed beyond early preclinical/platform validation stage.

Sana's SC379 program (glial progenitor cells for CNS diseases including Huntington's) was the closest neuroscience program to clinical development, with preclinical data published in Nature Biotechnology. SC379 was deprioritized in November 2024, and Sana is seeking a partner or spinout opportunity.

No PD-specific dopaminergic neuron candidate was ever publicly assigned a program code (e.g., "SC-XXX") or disclosed with IND-enabling study data.

### Financial
- **IPO:** February 2021, raised $587.5M at $25/share -- the largest gene/cell therapy IPO at the time
- **Total raised:** >$1B in equity capital since founding (2018)
- **Current market cap:** ~$1.1B (as of early 2026); stock price ~$4, down ~84% from IPO price
- **Cash position:** $153.1M as of September 30, 2025; pro forma ~$170.5M including ATM activity
- **Cash runway:** Into late 2026, per company guidance
- **November 2024 restructuring:** Deprioritized oncology CAR-T (SC291 in cancer), CNS (SC379), and other programs; layoffs across all functions; reduced operating burn to focus on SC451 (T1D) and SG293 (in vivo CAR-T for autoimmune)
- **Relevance to PD program:** The CNS deprioritization means zero internal capital is being allocated to dopaminergic neuron development; any PD program resurrection depends on finding an external partner or spinout
- **Key investors:** ARCH Venture Partners, Flagship Pioneering, F-Prime Capital, GV (Google Ventures)
- **Comparison:** BlueRock Therapeutics ([[bemdaneprocel]]) was acquired by Bayer for ~$1B in 2019 specifically for its PD cell therapy -- Sana's HIP platform IP for neuroscience could be attractive to a pharma acquirer at a fraction of that cost given the deprioritized status

### Competitive

```dataview
TABLE stage, status, developer, modality
FROM "pd-pipeline-research/assets"
WHERE contains(target, "dopaminergic neuron replacement") AND file.name != "sana-program"
SORT stage DESC
```

- [[bemdaneprocel]] (BlueRock/Bayer) is the clear leader in allogeneic cell therapy for PD: Phase 3 (exPDite-2), ESC-derived, RMAT + Fast Track -- but requires chronic immunosuppression, which Sana's HIP platform was designed to eliminate
- [[anpd001]] (Aspen Neuroscience) is the autologous iPSC leader: Phase 1/2 (ASPIRO), no immunosuppression required, early efficacy signals at 6 months -- but faces manufacturing scalability challenges that an allogeneic approach like Sana's could avoid
- [[rndp-001]] (Renew Biopharma/I Peace) represents the allogeneic iPSC competitor landscape; similarly preclinical
- [[raguneprocel]] (Novo Nordisk/CiRA) and [[kyoto-ipsc|Kyoto iPSC program]] represent the Japanese iPSC-derived DA neuron lineage with Phase 1/2 data published in Nature (2025)
- If [[bemdaneprocel]] succeeds in Phase 3 but immunosuppression burden limits adoption, the value of Sana's HIP platform for PD increases dramatically -- an HIP-modified allogeneic neuron that matches BlueRock's efficacy without immunosuppression would be a clear next-generation product
- If autologous approaches like [[anpd001]] demonstrate strong efficacy and solve manufacturing, the allogeneic HIP value proposition weakens
- The competitive window for Sana's PD program is narrowing: [[bemdaneprocel]] Phase 3 readout expected 2027-2028, and multiple other cell therapy programs are advancing while Sana's PD effort remains dormant

## Analysis

Sana's HIP platform is the most scientifically compelling approach to the immunosuppression problem in allogeneic cell therapy -- the NHP data showing >40-week survival of HIP-modified iPSCs without immunosuppression is a genuine platform breakthrough. The tragedy for PD is that this technology is now stranded without internal development resources. Sana's November 2024 strategic pivot was driven by cash constraints and the need to demonstrate clinical proof-of-concept in its most advanced programs (T1D, oncology), not by any scientific failure of the HIP-neuron concept.

**Analytical estimate -- Probability of Sana's PD program reaching clinical testing (under any ownership): 30-40%.** This is our assessment, not from a published source. The reasoning:
- Base rate for deprioritized preclinical programs being partnered or spun out: ~20-30%
- Adjustments upward: validated platform with NHP data (+10%), clear unmet need for immunosuppression-free allogeneic cells (+5%), multiple pharma companies actively investing in PD cell therapy (+5%)
- Adjustments downward: no PD-specific preclinical data package to license (-10%), competing HIP/immune evasion approaches emerging (-5%), Sana's weakened negotiating position as a cash-constrained company (-5%)
- Net: ~30-40%

**Signal analysis:**
- Sana's deprioritization of CNS is a resource allocation decision, not a scientific verdict on HIP-modified neurons for PD. The company chose to concentrate on programs closer to clinical proof-of-concept (T1D islets, CAR-T) where HIP validation data could be generated faster.
- The most important near-term signal for this program is whether a pharma partner (Bayer, Novo Nordisk, or another cell therapy investor) acquires or licenses the HIP-neuroscience IP. If [[bemdaneprocel]]'s Phase 3 data show efficacy limited by immunosuppression complications, demand for HIP technology surges.
- For the cell therapy field broadly, Sana's HIP platform is a technology to track regardless of Sana's corporate trajectory -- the IP could end up in a BlueRock competitor, an academic consortium, or a new startup specifically focused on immunosuppression-free neural grafts.
- The company's stock (SANA) is not a PD investment at current positioning -- it is a T1D/autoimmune play. Any PD value in SANA shares is deeply out-of-the-money optionality.

## References

### Key Publications
- [Hypoimmune iPSCs survive long term in fully immunocompetent allogeneic rhesus macaques | Nature Biotechnology (2023)](https://pubmed.ncbi.nlm.nih.gov/37156915/)
- [Sana preclinical data: HIP-engineered cells escape immune detection | Nature Biotechnology](https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-announces-preclinical-data-published-nature-0)
- [SC379 glial progenitor cell transplantation for neurodegenerative conditions | Nature Biotechnology](https://sana.gcs-web.com/news-releases/news-release-details/sana-biotechnology-highlights-publication-nature-biotechnology/)

### Press Releases & Filings
- [Sana Biotechnology increased focus on T1D and autoimmune diseases; CNS deprioritized (Nov 2024)](https://sana.gcs-web.com/news-releases/news-release-details/sana-biotechnology-announces-increased-focus-type-1-diabetes-and)
- [Sana strips back cancer, CNS programs; further layoffs (Nov 2024)](https://www.fiercebiotech.com/biotech/sana-strips-back-cancer-cns-programs-cell-therapy-biotech-warns-further-layoffs)
- [Sana Q3 2025 financial results and business updates](https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-reports-third-quarter-2025-financial-results)
- [Sana IPO raises $587.5M (Feb 2021)](https://www.fiercebiotech.com/biotech/sana-snags-587-5m-ipo-to-catapult-cell-therapies-into-clinic)

### Regulatory & Market
- [Sana Biotechnology pipeline page](https://sana.com/our-pipeline/)
- [Sana Biotechnology investor relations](https://ir.sana.com/)
- Limited source material — requires primary research. Company website was blocked during initial pipeline research (Jan 2026). No PD-specific program code, IND filing, or clinical trial registration exists in public records.
