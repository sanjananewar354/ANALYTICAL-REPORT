import pandas as pd

df = pd.read_csv("student_habits_performance.csv")
top_students = df.sort_values(by="exam_score", ascending=False).head(10)
print(top_students[['student_id', 'exam_score']])
