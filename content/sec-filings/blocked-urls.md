# Blocked URLs: SEC Filings That Could Not Be Accessed

#claude


*Research Date: January 21, 2026*

---

## Overview

During this research session, several SEC EDGAR URLs returned 403 (Forbidden) errors when accessed programmatically. These filings likely contain additional detail on Parkinson's disease pipeline programs.

---

## Blocked SEC EDGAR URLs

### Direct 10-K/20-F Filing Pages (403 Errors)

| Company | Filing | URL | Date |
|---------|--------|-----|------|
| Annovis Bio | 10-K FY2024 | https://www.sec.gov/Archives/edgar/data/1477845/000155837025003482/anvs-20241231x10k.htm | Dec 31, 2024 |
| Biogen | 10-K FY2024 | https://www.sec.gov/Archives/edgar/data/875045/000087504525000009/biib-20241231.htm | Dec 31, 2024 |
| AC Immune | 20-F FY2024 | https://www.sec.gov/Archives/edgar/data/1651625/000155837025002855/aciu-20241231x20f.htm | Dec 31, 2024 |

---

## Alternative Access Methods

### Method 1: SEC EDGAR Full-Text Search
- URL: https://efts.sec.gov/LATEST/search-index
- Search by company name + "Parkinson" keyword

### Method 2: Company Investor Relations Pages

| Company | Investor Relations URL |
|---------|----------------------|
| Annovis Bio | https://ir.annovisbio.com/sec-filings |
| Biogen | https://investors.biogen.com/sec-filings |
| AC Immune | https://ir.acimmune.com/sec-filings |
| Prothena | https://ir.prothena.com/investors/sec-filings |
| Denali | https://investors.denalitherapeutics.com/financials/sec-filings |
| Vaxxinity | https://ir.vaxxinity.com/sec-filings |
| Gain Therapeutics | https://ir.gaintherapeutics.com/sec-filings |
| Passage Bio | https://www.passagebio.com/investors-and-news/financials-and-filings/ |

### Method 3: Financial Data Providers
- Bloomberg Terminal
- FactSet
- S&P Capital IQ
- Refinitiv/LSEG

### Method 4: EDGAR Company Search
1. Go to https://www.sec.gov/cgi-bin/browse-edgar
2. Enter company name or CIK number
3. Filter by Form Type: 10-K, 20-F, or S-1
4. Access filing via direct download

---

## CIK Numbers for Key Companies

| Company | CIK Number |
|---------|------------|
| Annovis Bio | 1477845 |
| Biogen | 875045 |
| AC Immune | 1651625 |
| Prothena | 1559053 |
| Denali Therapeutics | 1714899 |
| Vaxxinity | 1851657 |
| Gain Therapeutics | 1819411 |
| Passage Bio | 1787297 |
| Prevail (historical) | 1714798 |
| Inhibikase | 1750149 |

---

## Why URLs May Be Blocked

1. **Rate limiting** - SEC servers may block automated/high-volume requests
2. **User-agent restrictions** - Non-browser access may be filtered
3. **Geographic/IP restrictions** - Certain access patterns flagged
4. **Direct file access blocked** - Some paths require navigation through search interface

---

## Workaround Used

For blocked URLs, pipeline information was extracted from:
- SEC press release exhibits (8-K filings)
- Company investor presentations filed as exhibits
- Web searches aggregating SEC filing content
- Third-party financial news services citing SEC filings

---

## Filings Successfully Accessed (Partial)

These filings returned content via web search results even if direct URL was blocked:

| Company | Filing Type | Key Content Extracted |
|---------|-------------|----------------------|
| Denali | 10-K exhibits, press releases | BIIB122/DNL151 clinical trial details |
| Prothena | 10-Q, press releases | Prasinezumab PADOVA results |
| Annovis | Press releases (8-K) | Buntanetap Phase 3 PD data |
| Gain Therapeutics | Press releases | GT-02287 Phase 1 results |

---

## Recommendations for Future Research

1. **Use SEC EDGAR search interface** rather than direct URL access
2. **Download filings as PDF** when available (often more accessible)
3. **Access during off-peak hours** (US evening/night)
4. **Use company IR pages** as primary access point
5. **Consider SEC API** for programmatic access (requires registration)

---

*Note: This limitation affects automated research tools but does not prevent manual access to SEC filings through standard browser navigation.*

---

*Last Updated: January 21, 2026*
