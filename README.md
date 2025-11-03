# 📊 AI-Powered Student Risk Dashboard

**Director of Engineering Case Study - Varsity Tutors**

An intelligent dashboard that identifies at-risk students and recommends AI-powered interventions to improve student outcomes.

## 🎯 Features

### ✅ Core Requirements Met

1. **Student Risk Indicators**
   - Automated risk classification (High/Medium/Low)
   - Multi-factor risk scoring algorithm
   - Real-time risk assessment based on 7+ key metrics

2. **AI-Generated Explanations**
   - Claude AI analyzes each student's data
   - Natural language explanations of risk factors
   - Pattern recognition across engagement, attendance, and performance

3. **AI-Powered Recommendations**
   - Personalized intervention strategies per student
   - Context-aware action items
   - Fallback to rule-based recommendations when API unavailable

4. **Data Visualizations**
   - Risk distribution pie chart
   - Engagement trends over time
   - Box plots by risk level
   - Weekly engagement patterns
   - Individual student trend analysis

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Sample Data

```bash
python generate_data.py
```

This creates `tutoring_data.csv` with 75 students and 12 weeks of session data.

### 3. Set Up AI (Optional but Recommended)

For AI-powered explanations and recommendations, set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**Note:** The dashboard works without an API key using rule-based analysis, but AI features provide richer insights.

### 4. Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 📊 How It Works

### Risk Assessment Algorithm

The system evaluates students across multiple dimensions:

1. **Engagement Score** (0-10 scale)
   - Average engagement across all sessions
   - Trend analysis (recent vs. early performance)

2. **Completion Metrics**
   - Session completion rate
   - Homework completion rate

3. **Attendance Patterns**
   - Total sessions vs. expected
   - Days since last session
   - Consistency over time

4. **Risk Scoring**
   - Weighted algorithm combining all factors
   - High Risk: Score ≥ 7
   - Medium Risk: Score 4-6
   - Low Risk: Score < 4

### AI Analysis

When an API key is provided, Claude AI:
- Analyzes student patterns and trends
- Generates natural language explanations
- Recommends targeted interventions
- Considers context and nuance in the data

### Interventions Recommended

The system suggests actions such as:
- Immediate outreach for inactive students
- Tutor matching optimization
- Schedule adjustments
- Homework support plans
- Parent/student meetings
- Session structure modifications

## 🏗️ Architecture

```
├── generate_data.py       # Sample data generator
├── dashboard.py           # Main Streamlit application
├── requirements.txt       # Python dependencies
└── tutoring_data.csv     # Generated student data
```

### Key Components

- **Data Layer**: Pandas for data manipulation and analysis
- **Risk Engine**: Custom algorithm with 7+ risk indicators
- **AI Layer**: Anthropic Claude for intelligent analysis
- **Visualization**: Plotly for interactive charts
- **UI**: Streamlit for rapid dashboard development

## 📈 Dashboard Features

### Overview Section
- Total student count
- Risk distribution metrics
- Average engagement score
- Visual analytics

### Filters
- Filter by risk level (High/Medium/Low)
- Filter by grade level (6-10)
- Dynamic updates

### Student Details
Each student card shows:
- Risk level indicator (🔴🟡🟢)
- Key metrics (engagement, completion, homework, attendance)
- Engagement trend chart with regression line
- AI-generated risk explanation
- Specific risk factors
- Actionable intervention recommendations
- Recent session history

## 🔧 Technical Decisions

### Why Streamlit?
- Rapid development (3-hour constraint)
- Built-in interactivity
- Easy deployment
- Python-native (matches data science stack)

### Why Claude AI?
- Strong analytical capabilities
- Natural language generation
- Context understanding
- Reliable API

### Risk Algorithm Design
- Multi-factor approach prevents single-metric bias
- Weighted scoring reflects relative importance
- Trend analysis catches declining students early
- Threshold-based classification for clear action items

## 📊 Sample Data

The generated dataset includes:
- **75 students** across 4 archetypes:
  - Thriving (high engagement, consistent)
  - Stable (moderate engagement)
  - Declining (engagement drops over time)
  - Struggling (low engagement throughout)
- **12 weeks** of session data
- **5 subjects**: Math (Algebra, Geometry), English, Science, History
- **Realistic patterns**: attendance variations, engagement fluctuations

## 🎓 Use Cases

1. **Academic Advisors**: Prioritize outreach to high-risk students
2. **Tutors**: Understand student challenges before sessions
3. **Parents**: Track student progress and engagement
4. **Operations**: Identify systemic issues (e.g., tutor matching)
5. **Leadership**: Monitor program health and intervention effectiveness

## 🚀 Future Enhancements

- **Predictive Modeling**: ML models to predict future risk
- **Automated Alerts**: Email/SMS notifications for high-risk students
- **Tutor Performance**: Correlate tutor effectiveness with student outcomes
- **A/B Testing**: Track intervention effectiveness
- **Mobile App**: On-the-go access for tutors and advisors
- **Integration**: Connect with existing student information systems

## 📝 Time Breakdown

- Data generation script: 15 minutes
- Risk assessment algorithm: 45 minutes
- AI integration: 30 minutes
- Dashboard UI: 60 minutes
- Visualizations: 30 minutes
- Testing & documentation: 30 minutes

**Total: ~3 hours**

## 🤝 About

Created for the Varsity Tutors Director of Engineering case study.

**Key Technologies:**
- Python 3.x
- Streamlit
- Pandas & NumPy
- Plotly
- Anthropic Claude AI

---

**Questions or feedback?** This dashboard demonstrates practical AI integration, data-driven decision making, and rapid prototyping skills essential for engineering leadership.
