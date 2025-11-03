# 🚀 Quick Start Guide

## Installation & Setup (2 minutes)

### Option 1: Automated Setup

```bash
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python generate_data.py

# Run dashboard
streamlit run dashboard.py
```

## Running the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open at: **http://localhost:8501**

## Optional: Enable AI Features

For AI-powered explanations and recommendations:

```bash
export ANTHROPIC_API_KEY='your-anthropic-api-key'
streamlit run dashboard.py
```

**Note:** Dashboard works without API key using rule-based analysis.

## What You'll See

### 📊 Overview Section
- Total students: 75
- Risk distribution (High/Medium/Low)
- Average engagement metrics
- Visual analytics

### 👥 Student List
- Expandable cards for each at-risk student
- Risk indicators (🔴 High, 🟡 Medium, 🟢 Low)
- Engagement trends
- AI explanations (if API key set)
- Intervention recommendations

### 🔍 Filters
- Filter by risk level
- Filter by grade (6-10)

## Key Features Demonstrated

✅ **Risk Classification** - Automated high/medium/low risk scoring  
✅ **AI Explanations** - Why each student is at-risk  
✅ **AI Recommendations** - Specific intervention actions  
✅ **Data Visualizations** - Engagement trends, distributions, patterns  

## Sample Students to Check

Look for these patterns in the data:
- **High Risk**: Low engagement + declining trends
- **Medium Risk**: Inconsistent attendance or homework
- **Low Risk**: Consistent high engagement

## Troubleshooting

### "tutoring_data.csv not found"
Run: `python generate_data.py`

### "Module not found" errors
Run: `pip install -r requirements.txt`

### AI features not working
Set your API key: `export ANTHROPIC_API_KEY='your-key'`

---

**Time to complete:** ~2 minutes setup + exploration
