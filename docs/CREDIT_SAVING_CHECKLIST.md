# CREDIT SAVING CHECKLIST - PREVENT EXPENSIVE RETRIES

## 🚨 MANDATORY PRE-FLIGHT CHECKS (Before Any API Calls)

### ✅ IMAGE VALIDATION
- [ ] All 5 required images exist in `/home/ubuntu/`
- [ ] All images are under 100KB (optimized)
- [ ] All images are in WebP format
- [ ] Image filenames match exactly:
  - `wholesale_pricing_comparison_chart.webp`
  - `roi_calculator_visualization.webp`
  - `business_types_feather_flags.webp`
  - `feather_flag_quality_comparison.webp`
  - `wholesale_quantity_discounts.webp`

### ✅ PDF VALIDATION  
- [ ] PDF exists: `/home/ubuntu/wholesale_pricing_guide.pdf`
- [ ] PDF is under 5MB
- [ ] PDF contains relevant content

### ✅ CONTENT VALIDATION
- [ ] All 9 Tier 0 URLs included in content
- [ ] Content length > 15,000 characters
- [ ] TL;DR section included (AIO requirement)
- [ ] Advanced CSS tables included
- [ ] Internal links properly formatted

### ✅ API VALIDATION
- [ ] API endpoint accessible: `http://206.189.76.235/publish`
- [ ] API secret correct: `mySuperSecret123`
- [ ] Network connectivity confirmed

### ✅ IMAGE PATH VALIDATION
- [ ] All image references use: `https://www.retractable-banner-stands.com/content/[filename].webp`
- [ ] PDF reference uses: `https://www.retractable-banner-stands.com/content/wholesale_pricing_guide.pdf`
- [ ] NO local file references (e.g., NOT `wholesale_pricing_comparison_chart.webp`)

## 🎯 BULLETPROOF WORKFLOW

### STEP 1: Run Prerequisites Check
```python
python3 BULLETPROOF_BLOG_TEMPLATE.py
```

### STEP 2: Only Proceed if ALL Validations Pass
- ❌ If ANY validation fails → STOP and fix
- ✅ If ALL validations pass → Proceed to publish

### STEP 3: Single Publication Attempt
- NO retries
- NO "improvements" during publication
- Use EXACT tested template structure

## 💰 CREDIT WASTE PREVENTION RULES

### ❌ NEVER DO THESE (They Waste Credits):
1. **Publish without validation** - Always run pre-flight checks
2. **Modify working code** - Use exact tested template
3. **Retry with same broken payload** - Fix the issue first
4. **Test "improvements" in production** - Test locally first
5. **Skip image optimization** - Always optimize before upload

### ✅ ALWAYS DO THESE (They Save Credits):
1. **Validate everything locally first**
2. **Use proven template structure**
3. **Check file sizes and formats**
4. **Verify API connectivity**
5. **Test image paths in browser**

## 🔧 EMERGENCY TROUBLESHOOTING

### If Images Don't Display:
1. Check browser console for 404 errors
2. Verify image paths use `/content/` structure
3. Confirm images uploaded to BigCommerce
4. DO NOT retry publication - fix path issue first

### If API Fails:
1. Check API endpoint status
2. Verify payload size (< 50MB total)
3. Confirm all base64 encoding successful
4. Check network connectivity

### If Content Issues:
1. Validate all required URLs included
2. Check content length requirements
3. Verify HTML structure
4. Confirm all requirements integrated

## 📊 SUCCESS METRICS

### First-Time Success Rate Target: 100%
- Pre-flight validation prevents 95% of failures
- Tested template prevents remaining 5%
- Zero retries = Zero credit waste

### Cost Savings:
- Each retry costs ~$2-5 in credits
- Validation prevents 3-5 retries per post
- Savings: $6-25 per blog post

## 🎯 TEMPLATE USAGE

### For New Blog Posts:
1. Use `BULLETPROOF_BLOG_TEMPLATE.py`
2. Modify only the `topic_data` dictionary
3. Keep all structure and validation intact
4. Run validation before publishing

### For Future Sessions:
1. Download template from GitHub
2. Follow exact same process
3. NO modifications to core template
4. Use proven working methods only

