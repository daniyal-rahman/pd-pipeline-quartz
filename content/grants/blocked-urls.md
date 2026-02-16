# Blocked URLs and Access Limitations

#claude


**Last Updated:** January 2026

This document tracks data sources that could not be accessed during the grant research.

---

## URLs That Returned Errors

### NIH Reporter Database
- **URL:** https://reporter.nih.gov/search/active-grants?query=parkinson&activityCodes=SBIR,STTR
- **Issue:** "We're sorry but RePORTER doesn't work properly without JavaScript enabled"
- **Alternative:** Used web searches to find publicly announced grants

### MJFF Funded Grants Page
- **URL:** https://www.michaeljfox.org/funded-grants
- **Error:** 404 Not Found
- **Alternative:** Used https://www.michaeljfox.org/funded-studies and press releases

### ASAP Funded Research Page
- **URL:** https://parkinsonsroadmap.org/funded-research
- **Error:** 404 Not Found
- **Alternative:** Used https://parkinsonsroadmap.org/research-network/ and press releases

### SBIR.gov Specific Award Page
- **URL:** https://www.sbir.gov/sbirsearch/detail/1325015/
- **Error:** 404 Not Found
- **Note:** Award database URLs may change or expire

---

## Data Sources With Limited Access

### NIH Reporter
- **Limitation:** Requires JavaScript rendering
- **Impact:** Could not directly query SBIR/STTR awards database
- **Workaround:** Relied on secondary sources and announced awards

### SBIR.gov Awards Database
- **Limitation:** Direct search not possible via web fetch
- **Note:** Award database files available for download (290MB with abstracts)
- **Recommendation:** Download data files for comprehensive analysis

### ASAP CRN Team Details
- **Limitation:** Research network page is a navigation hub, not a detailed roster
- **Missing:** Specific team rosters, PI names, institution affiliations, funding amounts
- **Recommendation:** Contact ASAP directly or visit full CRN subpages

---

## Recommended Direct Access Methods

### For NIH SBIR/STTR Data
1. **NIH Reporter:** https://reporter.nih.gov
   - Enable JavaScript
   - Filter by Activity Codes: R43, R44
   - Filter by Disease: Parkinson's disease
   - Filter by Fiscal Year: 2023, 2024

2. **SBIR.gov:** https://www.sbir.gov/awards
   - Download complete award data files
   - Data dictionary available on Data Resource Page

### For MJFF Data
1. **Funded Studies:** https://www.michaeljfox.org/funded-studies
2. **Press Releases:** Check MJFF news section for grant announcements

### For ASAP Data
1. **Research Network:** https://parkinsonsroadmap.org/research-network/
2. **Contact:** info@asap.science for detailed team information

---

## Program Status Notes

### SBIR/STTR Program Expiration
As of October 1, 2025, legislative authority for NIH SBIR/STTR programs expired. This affects:
- New application submissions (not accepted)
- Database updates (may be delayed or incomplete)
- Active award status queries

### FY24 Data Completeness
Per SBIR.gov: "Data for FY24 is not expected to be complete until March, 2025"
- Files refreshed monthly
- Recent awards may not appear in public databases

---

## Successful Data Sources

The following sources provided useful grant information:

| Source | Type | Information Obtained |
|--------|------|---------------------|
| MJFF Press Releases | News articles | Company grant awards, amounts, targets |
| GlobeNewswire | Press releases | SPARK NS cohort details |
| PRNewswire | Press releases | Individual company grants |
| BusinessWire | Press releases | Booster Therapeutics details |
| Parkinson's News Today | News | Summarized grant announcements |
| Philanthropy News Digest | News | ASAP funding totals |
| Company websites | Corporate | Research focus, funding history |
| Web search | Aggregated | Cross-referenced multiple sources |

---

## Recommendations for Future Research

1. **Set up alerts** for NIH Reporter, MJFF, and ASAP funding announcements
2. **Download SBIR.gov data files** for comprehensive historical analysis
3. **Monitor company press releases** for grant announcements
4. **Check ClinicalTrials.gov** for trials funded by these grants
5. **Track SEC filings** for public companies receiving grants (funding acknowledgments)
