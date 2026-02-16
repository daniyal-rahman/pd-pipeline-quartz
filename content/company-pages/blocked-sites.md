# Blocked Sites - Manual Checking Required

#claude


**Research Date:** 2026-01-21

These company websites blocked automated access via Cloudflare, JavaScript rendering requirements, 403 errors, or connection issues.

---

## 403 Forbidden / Access Denied

| Company | URL Attempted | Error | Notes |
|---------|---------------|-------|-------|
| Passage Bio | https://www.passagebio.com/pipeline | 403 Forbidden | Also tried /programs - same result |
| Passage Bio | https://www.passagebio.com/programs | 403 Forbidden | Known PD gene therapy company |
| Neurocrine | https://www.neurocrine.com/pipeline | 403 Forbidden | Has approved PD treatments |
| AbbVie (Cerevel) | https://www.abbvie.com/cerevel.html | 403 Forbidden | Acquired Cerevel - has PD programs |
| AbbVie | https://www.abbvie.com/science/pipeline.html | 403 Forbidden | Major pharma with PD programs |
| GSK | https://www.gsk.com/en-gb/innovation/pipeline/ | JS-rendered | Only CSS/framework returned |

---

## SSL/Certificate Errors

| Company | URL Attempted | Error | Notes |
|---------|---------------|-------|-------|
| BlueRock Therapeutics | https://www.bluerocktx.com/pipeline | SSL certificate error | Known cell therapy company for PD |
| Neuropore Therapies | https://www.neuropore.com | ERR_TLS_CERT_ALTNAME_INVALID | Alpha-synuclein aggregation inhibitors |
| Annovis Bio IR | https://ir.annovisbio.com | Certificate expired | - |

---

## Connection Refused (ECONNREFUSED)

| Company | URL Attempted | Notes |
|---------|---------------|-------|
| Neuraly | https://www.neuraly.com | GLP-1 receptor agonist for PD (NLY01) |
| Enterin | https://www.enterin.com | ENT-01 for PD GI symptoms |
| Intec Pharma | https://www.intecpharma.com | Accordion Pill technology for PD |
| Nurotera | https://www.nurotera.com | - |
| IAMINTACT | https://www.iamintact.com | - |
| TreeWay Neuro | https://treewayneuro.com | - |
| NFLXBio | https://www.nflxbio.com | Alpha-synuclein research |
| Lysosomal Therapeutics | https://www.lysosomaltherapeutics.com | GCase activation |
| Neuracle Genetics | https://neuracle-genetics.com | - |
| Suneta Pharma | https://www.sunetapharma.com | - |
| Prilenia Therapeutics | https://www.prileniatherapeutics.com | Pridopidine (sigma-1 agonist) |
| Mitokinin Pharma | https://www.mitokininpharma.com | - |
| Cells N Biotech | https://www.cellsnbiotech.com | - |
| Ambrx | https://www.ambrx.com/pipeline | - |
| Sio Gene Therapies | https://www.sio-gene.com/pipeline | - |
| Tremontx | https://www.tremontx.com | - |
| Bind Therapeutics | https://www.bindtx.com | - |
| Spark Therapeutics | https://www.spark-therapeutics.com/en/pipeline | Gene therapy company |
| Sage Therapeutics | https://www.sage-therapeutics.com/pipeline | - |
| Intra-Cellular Therapies | https://www.intra-cellular.com/pipeline | Error 436 |
| BioNeutra | https://www.bioneutra.com | Error 436 |
| IPST Cell | https://www.ipstcell.co.jp/en/pipeline/ | iPSC cell therapy for PD |
| Sana Biotherapeutics | https://www.sanabiotherapeutics.com/pipeline | iPSC/hypoimmune cell therapy |

---

## JavaScript Redirects / Dynamic Content Only

| Company | URL Attempted | Issue | Notes |
|---------|---------------|-------|-------|
| Annovis Bio | https://annovis.com | JS redirect to /lander | **Successfully scraped via annovisbio.com** |
| Annovis Bio | https://www.annovis.bio | JS redirect to /lander | - |
| Gain Therapeutics | https://www.gaintherapeutics.com/pipeline | Only CSS/JS returned | GCase activator (GT-02287) for PD |
| Gain Therapeutics | https://www.gaintherapeutics.com/programs | 404 | - |
| Voyager Therapeutics | https://www.voyagertherapeutics.com/pipeline | Only CSS/JS returned | AAV gene therapy platform |
| Voyager Therapeutics | https://www.voyagertherapeutics.com/programs | 404 | - |
| Ionis | https://ionis.com/science-and-innovation/pipeline | Only framework returned | ASO platform - partners on PD programs |
| BIAL | https://www.bial.com/en/pipeline/ | Only CSS/JS returned | Opicapone (COMT inhibitor) approved |
| Ultragenyx | https://www.ultragenyx.com/pipeline/ | Only CSS returned | - |
| Novartis | https://www.novartis.com/research-development/novartis-pipeline | Paginated/filtered results | Need to filter by neuroscience |

---

## 404 Not Found

| Company | URL Attempted | Notes |
|---------|---------------|-------|
| Prevail Therapeutics | https://www.prevailtherapeutics.com/pipeline | **Successfully scraped homepage** |
| Ionis | https://www.ionispharma.com/pipeline | Redirected to ionis.com |
| Ionis | https://ionis.com/pipeline | 404 |
| Ionis | https://ionis.com/ionis-innovation/pipeline/ | 404 |
| Sumitomo Pharma | https://www.us.sumitomo-pharma.com/pipeline | 404 |
| Kyowa Kirin | https://www.kyowakirin.com/our_business/pipeline/ | 404 |
| Amgen | https://www.amgen.com/science/pipeline | 404 |
| Takeda | https://www.takeda.com/what-we-do/research-and-development/clinical-pipeline/ | 404 |
| Poxel Pharma | https://www.poxelpharma.com/pipeline/ | 404 (redirected from poxel.com) |
| Roche | https://www.roche.com/research-and-development/pipeline | 404 |
| MJFF Pipeline | https://www.michaeljfox.org/parkinsons-treatment-pipeline | 404 |
| Cure Parkinson's | https://www.cureparkinsons.org.uk/research-strategy/pipeline | 404 |
| Parkinson's Fund | https://www.parkinsonfund.org/research/pipeline | ECONNREFUSED |
| Clinuvel | https://www.clinuvel.com/pipeline/ | 404 |
| Cerecor | https://www.cerecor.com/pipeline | 404 |
| Pharmathen | https://www.pharmathen.com/pipeline | 404 |
| Therapeutics MD | https://www.therapeuticsmd.com/pipeline | 404 |

---

## Domain Issues / Company Changes

| Company | URL Attempted | Issue | Notes |
|---------|---------------|-------|-------|
| Annovis Bio | https://annovis.com/lander | Redirects to domain sale page (afternic.com) | **Use annovisbio.com instead** |
| Impel Biopharma | https://www.impelbiopharma.com/pipeline | ECONNREFUSED | May have been acquired |

---

## Priority Sites for Manual Checking

These are known PD-focused companies that require manual browser access:

1. **Passage Bio** - https://www.passagebio.com - GBA1 gene therapy (PBGN01)
2. **BlueRock Therapeutics** - https://www.bluerocktx.com - iPSC-derived DA neurons (bemdaneprocel)
3. **Neuraly** - https://www.neuraly.com - NLY01 (GLP-1 agonist for PD)
4. **Gain Therapeutics** - https://www.gaintherapeutics.com - GT-02287 (GCase activator)
5. **Voyager Therapeutics** - https://www.voyagertherapeutics.com - AAV gene therapy platform
6. **Enterin** - https://www.enterin.com - ENT-01 for PD GI dysfunction
7. **AbbVie/Cerevel** - https://www.abbvie.com/cerevel.html - Tavapadon (D1/D5 agonist)
8. **Novartis** - Filter pipeline by neuroscience
9. **Sana Bioterapeutics** - https://www.sanabiotherapeutics.com - Hypoimmune iPSC-DA cells
10. **Spark Therapeutics** - Gene therapy platform

---

*Documented 2026-01-21 - URLs should be checked manually via web browser*
