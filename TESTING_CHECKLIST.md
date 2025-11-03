# 🧪 Testing Checklist

Use this checklist to verify the dashboard before submission.

## ✅ Setup Tests

- [ ] Dependencies install successfully: `pip install -r requirements.txt`
- [ ] Data generation works: `python generate_data.py`
- [ ] CSV file created with correct structure
- [ ] Dashboard launches: `streamlit run dashboard.py`

## ✅ Dashboard Functionality

### Overview Section
- [ ] Total student count displays (should be 75)
- [ ] Risk metrics show correct counts
- [ ] Average engagement score displays
- [ ] All three overview charts render

### Visualizations
- [ ] Risk distribution pie chart shows 3 categories
- [ ] Engagement box plot displays by risk level
- [ ] Weekly trend line chart shows 12 weeks
- [ ] Charts are interactive (hover, zoom)

### Filters
- [ ] Risk level filter works (High/Medium/Low)
- [ ] Grade level filter works (6-10)
- [ ] Student list updates when filters change
- [ ] Filter combinations work correctly

### Student Cards
- [ ] Cards expand/collapse properly
- [ ] Risk indicator emoji displays (🔴🟡🟢)
- [ ] Four metrics display correctly
- [ ] Engagement trend chart renders
- [ ] Trend line shows on chart
- [ ] Risk factors list appears
- [ ] Recent sessions table displays

## ✅ AI Features

### Without API Key
- [ ] Explanations show rule-based fallback
- [ ] Recommendations show rule-based fallback
- [ ] Warning message displays about API key
- [ ] Dashboard remains functional

### With API Key (if available)
- [ ] Set: `export ANTHROPIC_API_KEY='your-key'`
- [ ] AI explanations generate successfully
- [ ] Explanations are relevant to student data
- [ ] AI recommendations generate successfully
- [ ] Recommendations are actionable
- [ ] No error messages appear

## ✅ Data Quality

### Risk Classification
- [ ] High-risk students have low engagement (<5)
- [ ] High-risk students show declining trends
- [ ] Medium-risk students have moderate issues
- [ ] Low-risk students have good metrics

### Metrics Accuracy
- [ ] Engagement scores range 0-10
- [ ] Completion rates are percentages
- [ ] Attendance calculations make sense
- [ ] Days since last session is accurate

## ✅ User Experience

- [ ] Page loads quickly (<3 seconds)
- [ ] No console errors in browser
- [ ] Layout is responsive
- [ ] Colors are consistent with risk levels
- [ ] Text is readable
- [ ] Navigation is intuitive

## ✅ Edge Cases

- [ ] Empty filters show "no students"
- [ ] All students filtered works
- [ ] Single student filtered works
- [ ] Long student names display properly
- [ ] Large numbers format correctly

## ✅ Documentation

- [ ] README.md is comprehensive
- [ ] QUICKSTART.md has correct commands
- [ ] SUBMISSION.md is complete
- [ ] Code has helpful comments
- [ ] Requirements.txt is accurate

## 🐛 Known Issues

Document any issues found:

1. _None identified - dashboard working as expected_

## 📊 Test Results Summary

**Date Tested:** _______________  
**Tester:** _______________  
**Overall Status:** ⬜ Pass / ⬜ Fail  

**Notes:**
_____________________________________
_____________________________________
_____________________________________

## 🚀 Pre-Submission Checklist

- [ ] All tests pass
- [ ] Code is clean and commented
- [ ] Documentation is complete
- [ ] Example data generates correctly
- [ ] Dashboard runs without errors
- [ ] AI features work (or gracefully degrade)
- [ ] Ready for submission

---

**Recommendation:** Test both with and without ANTHROPIC_API_KEY to demonstrate graceful degradation.
