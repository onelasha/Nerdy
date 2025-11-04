"""
AI-Powered Student Risk Dashboard
Director of Engineering Case Study - Varsity Tutors
"""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import anthropic
import os

# Page configuration
st.set_page_config(
    page_title="Student Risk Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .risk-high { 
        background-color: #ffebee; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #f44336;
    }
    .risk-medium { 
        background-color: #fff3e0; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #ff9800;
    }
    .risk-low { 
        background-color: #e8f5e9; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #4caf50;
    }
    .metric-card {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Load and preprocess tutoring data"""
    try:
        df = pd.read_csv("tutoring_data.csv")
        df['session_date'] = pd.to_datetime(df['session_date'])
        return df
    except FileNotFoundError:
        st.warning("⚠️ tutoring_data.csv not found. Generating sample data...")
        with st.spinner("Generating 75 students with 12 weeks of data... This will take ~10 seconds."):
            try:
                from generate_data import generate_tutoring_data
                generate_tutoring_data()
                st.success("✅ Sample data generated successfully!")
                # Force a rerun to reload the page with the new data
                st.rerun()
            except Exception as e:
                st.error(f"❌ Failed to generate data: {str(e)}")
                st.info("Please run: `python generate_data.py` manually")
                st.code(str(e))
                st.stop()


def calculate_risk_metrics(df):
    """Calculate risk indicators for each student"""
    student_metrics = []
    
    for student_id in df['student_id'].unique():
        student_data = df[df['student_id'] == student_id].sort_values('session_date')
        
        # Calculate key metrics
        total_sessions = len(student_data)
        avg_engagement = student_data['engagement_score'].mean()
        completion_rate = student_data['completed'].mean()
        homework_rate = student_data['homework_completed'].mean()
        
        # Calculate engagement trend (last 4 weeks vs first 4 weeks)
        recent_data = student_data.tail(8)
        early_data = student_data.head(8)
        engagement_trend = recent_data['engagement_score'].mean() - early_data['engagement_score'].mean()
        
        # Calculate attendance consistency
        expected_sessions = 24  # 12 weeks * 2 sessions average
        attendance_rate = total_sessions / expected_sessions
        
        # Days since last session
        last_session = student_data['session_date'].max()
        days_since_last = (datetime.now() - last_session).days
        
        # Risk scoring
        risk_score = 0
        risk_factors = []
        
        if avg_engagement < 5:
            risk_score += 3
            risk_factors.append("Low engagement")
        elif avg_engagement < 7:
            risk_score += 1
            
        if engagement_trend < -2:
            risk_score += 3
            risk_factors.append("Declining engagement")
        elif engagement_trend < -1:
            risk_score += 2
            
        if completion_rate < 0.7:
            risk_score += 2
            risk_factors.append("Low session completion")
            
        if homework_rate < 0.5:
            risk_score += 2
            risk_factors.append("Low homework completion")
            
        if attendance_rate < 0.6:
            risk_score += 2
            risk_factors.append("Poor attendance")
            
        if days_since_last > 14:
            risk_score += 2
            risk_factors.append("Inactive student")
        
        # Determine risk level
        if risk_score >= 7:
            risk_level = "High"
        elif risk_score >= 4:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        student_metrics.append({
            'student_id': student_id,
            'student_name': student_data['student_name'].iloc[0],
            'grade_level': student_data['grade_level'].iloc[0],
            'risk_level': risk_level,
            'risk_score': risk_score,
            'avg_engagement': avg_engagement,
            'engagement_trend': engagement_trend,
            'completion_rate': completion_rate,
            'homework_rate': homework_rate,
            'attendance_rate': attendance_rate,
            'total_sessions': total_sessions,
            'days_since_last': days_since_last,
            'risk_factors': risk_factors,
            'last_session': last_session
        })
    
    return pd.DataFrame(student_metrics)


def generate_ai_explanation(student_metrics, student_data):
    """Generate AI explanation for why a student is at-risk using Claude"""
    try:
        # Try to get API key from Streamlit secrets first, then environment variable
        api_key = st.secrets.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return "⚠️ ANTHROPIC_API_KEY not set. Using rule-based explanation instead.\n\n" + generate_rule_based_explanation(student_metrics, student_data)
        
        client = anthropic.Anthropic(api_key=api_key)
        
        prompt = f"""Analyze this student's tutoring data and explain WHY they are at risk:

Student: {student_metrics['student_name']} (Grade {student_metrics['grade_level']})
Risk Level: {student_metrics['risk_level']}

Metrics:
- Average Engagement: {student_metrics['avg_engagement']:.1f}/10
- Engagement Trend: {student_metrics['engagement_trend']:.1f} (recent vs early)
- Session Completion Rate: {student_metrics['completion_rate']:.0%}
- Homework Completion Rate: {student_metrics['homework_rate']:.0%}
- Attendance Rate: {student_metrics['attendance_rate']:.0%}
- Total Sessions: {student_metrics['total_sessions']}
- Days Since Last Session: {student_metrics['days_since_last']}

Recent Session Data:
{student_data.tail(5)[['session_date', 'engagement_score', 'completed', 'homework_completed', 'subject']].to_string()}

Provide a concise 2-3 sentence explanation of the key risk factors and patterns you observe."""

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text
    
    except Exception as e:
        return f"⚠️ AI explanation unavailable: {str(e)}\n\n" + generate_rule_based_explanation(student_metrics, student_data)


def generate_rule_based_explanation(student_metrics, student_data):
    """Fallback rule-based explanation"""
    explanation = []
    
    if student_metrics['avg_engagement'] < 5:
        explanation.append(f"Low average engagement score of {student_metrics['avg_engagement']:.1f}/10 indicates the student is not actively participating.")
    
    if student_metrics['engagement_trend'] < -2:
        explanation.append(f"Engagement has declined significantly by {abs(student_metrics['engagement_trend']):.1f} points over the past weeks.")
    
    if student_metrics['completion_rate'] < 0.7:
        explanation.append(f"Only {student_metrics['completion_rate']:.0%} of sessions are being completed.")
    
    if student_metrics['homework_rate'] < 0.5:
        explanation.append(f"Homework completion rate is low at {student_metrics['homework_rate']:.0%}.")
    
    if student_metrics['attendance_rate'] < 0.6:
        explanation.append(f"Attendance is inconsistent at {student_metrics['attendance_rate']:.0%} of expected sessions.")
    
    if student_metrics['days_since_last'] > 14:
        explanation.append(f"Student has been inactive for {student_metrics['days_since_last']} days.")
    
    return " ".join(explanation) if explanation else "Student is performing well with no significant risk factors."


def generate_ai_recommendations(student_metrics, student_data):
    """Generate AI-powered intervention recommendations"""
    try:
        # Try to get API key from Streamlit secrets first, then environment variable
        api_key = st.secrets.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return generate_rule_based_recommendations(student_metrics)
        
        client = anthropic.Anthropic(api_key=api_key)
        
        prompt = f"""Based on this at-risk student's data, recommend 3 specific interventions:

Student: {student_metrics['student_name']} (Grade {student_metrics['grade_level']})
Risk Level: {student_metrics['risk_level']}
Risk Factors: {', '.join(student_metrics['risk_factors'])}

Key Metrics:
- Avg Engagement: {student_metrics['avg_engagement']:.1f}/10
- Engagement Trend: {student_metrics['engagement_trend']:.1f}
- Completion Rate: {student_metrics['completion_rate']:.0%}
- Homework Rate: {student_metrics['homework_rate']:.0%}
- Attendance: {student_metrics['attendance_rate']:.0%}

Provide 3 actionable recommendations as a numbered list. Be specific and practical."""

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text
    
    except Exception as e:
        return generate_rule_based_recommendations(student_metrics)


def generate_rule_based_recommendations(student_metrics):
    """Fallback rule-based recommendations"""
    recommendations = []
    
    if student_metrics['days_since_last'] > 14:
        recommendations.append("📞 **Immediate Outreach**: Contact student/parent to re-engage and understand barriers to attendance.")
    
    if student_metrics['avg_engagement'] < 5:
        recommendations.append("🎯 **Tutor Match Review**: Consider matching with a different tutor who specializes in engagement strategies.")
    
    if student_metrics['homework_rate'] < 0.5:
        recommendations.append("📚 **Homework Support Plan**: Implement a structured homework completion system with shorter, more manageable assignments.")
    
    if student_metrics['engagement_trend'] < -2:
        recommendations.append("🔍 **Root Cause Analysis**: Schedule a meeting with tutor, student, and parent to identify underlying issues causing declining engagement.")
    
    if student_metrics['attendance_rate'] < 0.6:
        recommendations.append("📅 **Schedule Optimization**: Work with family to find more convenient session times and reduce scheduling conflicts.")
    
    if student_metrics['completion_rate'] < 0.7:
        recommendations.append("⏰ **Session Structure Review**: Adjust session length or format to improve completion rates.")
    
    # Return top 3 recommendations
    return "\n\n".join(recommendations[:3]) if recommendations else "Continue monitoring student progress."


def create_engagement_trend_chart(df, student_id):
    """Create engagement trend visualization for a student"""
    student_data = df[df['student_id'] == student_id].sort_values('session_date')
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=student_data['session_date'],
        y=student_data['engagement_score'],
        mode='lines+markers',
        name='Engagement Score',
        line=dict(color='#2196F3', width=2),
        marker=dict(size=8)
    ))
    
    # Add trend line
    z = np.polyfit(range(len(student_data)), student_data['engagement_score'], 1)
    p = np.poly1d(z)
    fig.add_trace(go.Scatter(
        x=student_data['session_date'],
        y=p(range(len(student_data))),
        mode='lines',
        name='Trend',
        line=dict(color='#FF5722', width=2, dash='dash')
    ))
    
    fig.update_layout(
        title="Engagement Score Over Time",
        xaxis_title="Date",
        yaxis_title="Engagement Score",
        yaxis=dict(range=[0, 10]),
        hovermode='x unified',
        height=300
    )
    
    return fig


def create_overview_charts(df, student_metrics):
    """Create overview visualizations"""
    
    # Risk distribution
    risk_counts = student_metrics['risk_level'].value_counts()
    fig_risk = px.pie(
        values=risk_counts.values,
        names=risk_counts.index,
        title="Student Risk Distribution",
        color=risk_counts.index,
        color_discrete_map={'High': '#f44336', 'Medium': '#ff9800', 'Low': '#4caf50'}
    )
    
    # Engagement distribution by risk level
    fig_engagement = px.box(
        student_metrics,
        x='risk_level',
        y='avg_engagement',
        color='risk_level',
        title="Engagement Score by Risk Level",
        color_discrete_map={'High': '#f44336', 'Medium': '#ff9800', 'Low': '#4caf50'},
        category_orders={'risk_level': ['High', 'Medium', 'Low']}
    )
    
    # Weekly engagement trends
    df['week'] = df['session_date'].dt.isocalendar().week
    weekly_engagement = df.groupby('week')['engagement_score'].mean().reset_index()
    fig_weekly = px.line(
        weekly_engagement,
        x='week',
        y='engagement_score',
        title="Average Engagement Score by Week",
        markers=True
    )
    fig_weekly.update_layout(yaxis=dict(range=[0, 10]))
    
    return fig_risk, fig_engagement, fig_weekly


def main():
    """Main dashboard application"""
    
    # Header
    st.title("📊 AI-Powered Student Risk Dashboard")
    st.markdown("**Varsity Tutors - Director of Engineering Case Study**")
    st.markdown("---")
    
    # Load data
    df = load_data()
    student_metrics = calculate_risk_metrics(df)
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        options=['High', 'Medium', 'Low'],
        default=['High', 'Medium', 'Low']
    )
    
    grade_filter = st.sidebar.multiselect(
        "Grade Level",
        options=sorted(student_metrics['grade_level'].unique()),
        default=sorted(student_metrics['grade_level'].unique())
    )
    
    # Apply filters
    filtered_metrics = student_metrics[
        (student_metrics['risk_level'].isin(risk_filter)) &
        (student_metrics['grade_level'].isin(grade_filter))
    ].sort_values('risk_score', ascending=False)
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", len(student_metrics))
    with col2:
        high_risk = len(student_metrics[student_metrics['risk_level'] == 'High'])
        st.metric("High Risk", high_risk, delta=f"{high_risk/len(student_metrics)*100:.0f}%")
    with col3:
        medium_risk = len(student_metrics[student_metrics['risk_level'] == 'Medium'])
        st.metric("Medium Risk", medium_risk, delta=f"{medium_risk/len(student_metrics)*100:.0f}%")
    with col4:
        avg_engagement = student_metrics['avg_engagement'].mean()
        st.metric("Avg Engagement", f"{avg_engagement:.1f}/10")
    
    st.markdown("---")
    
    # Visualizations
    st.header("📈 Overview Analytics")
    
    fig_risk, fig_engagement, fig_weekly = create_overview_charts(df, student_metrics)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig_risk, use_container_width=True)
    with col2:
        st.plotly_chart(fig_engagement, use_container_width=True)
    with col3:
        st.plotly_chart(fig_weekly, use_container_width=True)
    
    st.markdown("---")
    
    # Student list
    st.header("👥 At-Risk Students")
    st.markdown(f"Showing **{len(filtered_metrics)}** students")
    
    # Display students
    for idx, row in filtered_metrics.iterrows():
        risk_class = f"risk-{row['risk_level'].lower()}"
        
        with st.expander(f"{'🔴' if row['risk_level']=='High' else '🟡' if row['risk_level']=='Medium' else '🟢'} {row['student_name']} - Grade {row['grade_level']} - **{row['risk_level']} Risk**"):
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Engagement", f"{row['avg_engagement']:.1f}/10")
            with col2:
                st.metric("Completion", f"{row['completion_rate']:.0%}")
            with col3:
                st.metric("Homework", f"{row['homework_rate']:.0%}")
            with col4:
                st.metric("Attendance", f"{row['attendance_rate']:.0%}")
            
            # Engagement trend chart
            student_data = df[df['student_id'] == row['student_id']]
            fig = create_engagement_trend_chart(df, row['student_id'])
            st.plotly_chart(fig, use_container_width=True)
            
            # AI Explanation
            st.subheader("🤖 AI Analysis: Why is this student at-risk?")
            with st.spinner("Generating AI explanation..."):
                explanation = generate_ai_explanation(row, student_data)
                st.info(explanation)
            
            # Risk Factors
            if row['risk_factors']:
                st.subheader("⚠️ Risk Factors")
                for factor in row['risk_factors']:
                    st.markdown(f"- {factor}")
            
            # AI Recommendations
            st.subheader("💡 Recommended Interventions")
            with st.spinner("Generating recommendations..."):
                recommendations = generate_ai_recommendations(row, student_data)
                st.success(recommendations)
            
            # Recent sessions
            st.subheader("📅 Recent Sessions")
            recent_sessions = student_data.sort_values('session_date', ascending=False).head(5)
            st.dataframe(
                recent_sessions[['session_date', 'subject', 'engagement_score', 'completed', 'homework_completed']],
                use_container_width=True,
                hide_index=True
            )


if __name__ == "__main__":
    main()
