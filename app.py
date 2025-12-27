import pandas as pd
import numpy as np

np.random.seed(42)

n_students = 300

data = {
    "attendance": np.random.randint(40, 100, n_students),
    "avg_score": np.random.randint(8, 20, n_students),
    "homework_rate": np.random.randint(50, 100, n_students),
    "quiz_score": np.random.randint(5, 20, n_students),
    "lms_activity": np.random.randint(10, 100, n_students),
    "late_submission": np.random.randint(0, 10, n_students)
}

df = pd.DataFrame(data)

def assign_risk(row):
    if row["attendance"] < 60 or row["avg_score"] < 10:
        return "High"
    elif row["attendance"] < 75 or row["avg_score"] < 13:
        return "Medium"
    else:
        return "Low"

df["risk_level"] = df.apply(assign_risk, axis=1)

df.to_csv("student_data.csv", index=False)

print(df.head())
