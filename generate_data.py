# generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_tutoring_data(output_file="tutoring_data.csv"):
    """Generate sample tutoring data for 75 students over 12 weeks"""
    np.random.seed(42)
    random.seed(42)

    data = []
    start_date = datetime(2025, 1, 6)
    subjects = ["Math - Algebra", "Math - Geometry", "English - Writing",
                "Science - Biology", "History - US History"]
    names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery",
             "Quinn", "Parker", "Reese"] * 8

    for i in range(75):
        archetype = random.choice(["thriving", "stable", "declining", "struggling"])
        base_engagement = {"thriving": 9, "stable": 7, "declining": 8, "struggling": 4}[archetype]
        sessions_per_week = {"thriving": 3, "stable": 2, "declining": 2, "struggling": 1}[archetype]
        
        for week in range(12):
            engagement = base_engagement
            if archetype == "declining":
                engagement = max(2, base_engagement - week * 0.6)
            
            for _ in range(sessions_per_week if random.random() > 0.2 else sessions_per_week - 1):
                data.append({
                    "student_id": f"STU-{i+1:03d}",
                    "student_name": names[i],
                    "grade_level": random.randint(6, 10),
                    "session_date": (start_date + timedelta(weeks=week, days=random.randint(0, 6))).strftime("%Y-%m-%d"),
                    "session_duration_minutes": random.choice([30, 45, 60]),
                    "subject": random.choice(subjects),
                    "tutor_id": f"TUT-{random.randint(101, 125)}",
                    "completed": random.random() > 0.1,
                    "engagement_score": int(engagement) + random.randint(-1, 1),
                    "tutor_notes": f"Session notes here. Student engagement: {int(engagement)}/10",
                    "homework_completed": random.random() > 0.3,
                    "sessions_this_week": sessions_per_week,
                    "total_sessions": week * sessions_per_week + 1
                })

    pd.DataFrame(data).to_csv(output_file, index=False)
    print(f"✅ Generated {output_file} with {len(data)} sessions for 75 students")
    return output_file


if __name__ == "__main__":
    generate_tutoring_data()
