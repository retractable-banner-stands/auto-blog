# 🕷️ MONTHLY CRAWL INSTRUCTIONS
## For Future Manus Sessions - Step-by-Step Process

---

## 🚨 WHEN USER REQUESTS MONTHLY RECRAWL

**USER WILL SAY SOMETHING LIKE:**
- "Time for monthly crawl update"
- "Please recrawl the site and update GitHub"
- "Monthly site crawl needed"
- "Update the Tier 4 page list"

---

## 📋 IMMEDIATE ACTIONS (CRITICAL!)

### **STEP 1: READ DOCUMENTATION**
**BEFORE doing anything else, read these files:**
1. `MASTER_SESSION_CONTINUITY_GUIDE.md` - Complete system overview
2. `comprehensive_site_pages_tier4.md` - Current page inventory
3. `workflow_updates_log.md` - All requirements details

### **STEP 2: CONFIRM UNDERSTANDING**
**Message user to confirm:**
- "I've read the continuity documentation and understand the monthly crawl process"
- "Current focus is [MONTH X]: [FOCUS AREA]"
- "I'll now perform comprehensive site crawl and update the Tier 4 system"

---

## 🕷️ COMPREHENSIVE CRAWL PROCESS

### **STEP 3: SYSTEMATIC SITE CRAWL**

**A. Start with Homepage:**
```javascript
// Use this browser console command to extract all links
const links = Array.from(document.querySelectorAll('a[href]'))
  .map(link => ({
    href: link.href,
    text: link.textContent.trim(),
    isInternal: link.href.includes('retractable-banner-stands.com')
  }))
  .filter(link => link.isInternal && link.href !== window.location.href)
  .reduce((unique, link) => {
    if (!unique.find(u => u.href === link.href)) {
      unique.push(link);
    }
    return unique;
  }, [])
  .sort((a, b) => a.href.localeCompare(b.href));

console.log(`Found ${links.length} unique internal links`);
links.forEach((link, index) => {
  console.log(`${index + 1}. ${link.href} - "${link.text}"`);
});
```

**B. Explore Main Navigation Sections:**
- Custom Feather Banners
- Feather Banners  
- Feather Flags
- Retractable Banner Stands
- All dropdown menus and subcategories

**C. Check for New Categories:**
- Look for any new product lines
- Identify seasonal or promotional pages
- Note any structural changes

### **STEP 4: COMPARE WITH EXISTING INVENTORY**
- Cross-reference with comprehensive_site_pages_tier4.md
- Identify NEW pages not in current list
- Identify REMOVED pages no longer available
- Note any URL changes or redirects

---

## 📊 DOCUMENTATION UPDATE PROCESS

### **STEP 5: UPDATE MASTER FILE**
**Update comprehensive_site_pages_tier4.md:**
- Add new pages to appropriate categories (A-M)
- Remove dead/redirected pages
- Update page counts
- Adjust monthly rotation if needed

### **STEP 6: CREATE MONTHLY REPORT**
**Create new file: YYYY-MM-crawl-results.md**

**Template:**
```markdown
# Monthly Crawl Results - [MONTH YEAR]
## Site: retractable-banner-stands.com
### Crawl Date: [DATE]

## 📊 CRAWL SUMMARY
- **Total Pages Found:** [NUMBER]
- **New Pages:** [NUMBER]
- **Removed Pages:** [NUMBER]
- **Changed URLs:** [NUMBER]

## 🆕 NEW PAGES DISCOVERED
[List new pages with categories]

## ❌ REMOVED PAGES
[List removed/dead pages]

## 🔄 CHANGED URLS
[List any redirects or URL changes]

## 📅 NEXT MONTH FOCUS
**Month [X+1]:** [Next focus area from rotation]

## 🎯 RECOMMENDATIONS
[Any strategic recommendations based on findings]
```

### **STEP 7: UPDATE ROTATION SCHEDULE**
- Advance to next month's focus area
- Update the monthly rotation in master file
- Note any special considerations

---

## 📤 GITHUB UPDATE PROCESS

### **STEP 8: PREPARE FILES FOR UPLOAD**
**Files to update/create:**
1. Updated `comprehensive_site_pages_tier4.md`
2. New `YYYY-MM-crawl-results.md`
3. Updated `MASTER_SESSION_CONTINUITY_GUIDE.md` (if needed)

### **STEP 9: REQUEST GITHUB ACCESS**
**Message user:**
- "Crawl complete! Found [X] new pages and [Y] changes"
- "Ready to update GitHub with monthly crawl results"
- "Please set repository to PUBLIC temporarily for update"
- "Files ready: [list files to upload]"

### **STEP 10: UPLOAD TO GITHUB**
**When repository is PUBLIC:**
1. Clone repository: `git clone https://github.com/retractable-banner-stands/auto-blog.git`
2. Update existing files in /docs/ folder
3. Add new monthly report to /docs/monthly_crawl_updates/ folder
4. Commit with descriptive message
5. Push changes
6. Confirm successful upload

### **STEP 11: CONFIRM COMPLETION**
**Message user:**
- "✅ Monthly crawl update completed successfully"
- "📊 Summary: [brief findings]"
- "📅 Next month focus: [next area]"
- "🔒 You can set repository back to PRIVATE now"

---

## 🎯 QUALITY CONTROL CHECKLIST

### **BEFORE REPORTING COMPLETION:**
- [ ] All documentation files read and understood
- [ ] Comprehensive crawl performed (100+ pages expected)
- [ ] New pages properly categorized
- [ ] Removed pages documented
- [ ] Monthly rotation advanced
- [ ] Files properly formatted and complete
- [ ] GitHub upload successful
- [ ] User notified of completion

### **RED FLAGS TO WATCH FOR:**
- ❌ Finding significantly fewer pages (possible crawl error)
- ❌ Major site structure changes (needs special attention)
- ❌ Many broken links (site issues)
- ❌ New product categories (may need strategy adjustment)

---

## 📅 MONTHLY FOCUS AREAS (REFERENCE)

**ROTATION SCHEDULE:**
1. **September 2025:** Custom Feather Flags variations
2. **October 2025:** Feather Flags categories
3. **November 2025:** Specialized Feather Flags
4. **December 2025:** Real Estate & Open House
5. **January 2026:** Retractable Banner Stands
6. **February 2026:** Banner Sizes
7. **March 2026:** Teardrop Products
8. **April 2026:** Trade Show Displays
9. **May 2026:** Accessories & Info Pages
10. **June 2026:** Trust & Policy Pages
11. **July 2026:** Special Promotions
12. **August 2026:** Comprehensive Review & Restart

---

## 🚨 EMERGENCY PROCEDURES

### **IF MAJOR SITE CHANGES FOUND:**
1. Document all changes thoroughly
2. Alert user immediately
3. Recommend strategy review
4. Don't proceed with standard rotation

### **IF CRAWL FAILS OR ERRORS:**
1. Try alternative crawl methods
2. Document the issue
3. Provide partial results
4. Recommend manual review

### **IF GITHUB ACCESS ISSUES:**
1. Create ZIP file with updates
2. Provide for manual upload
3. Document the process
4. Ensure continuity maintained

---

**🎯 SUCCESS CRITERIA:**
- Monthly crawl completed on schedule
- All new pages documented and categorized
- GitHub repository updated with latest findings
- Next month's focus area confirmed
- User informed of completion and next steps

**This process ensures consistent, thorough monthly updates regardless of which Manus session performs the crawl!**

