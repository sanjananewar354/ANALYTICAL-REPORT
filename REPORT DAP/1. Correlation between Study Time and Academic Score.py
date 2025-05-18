import pandas as pd

df = pd.read_csv("student_habits_performance.csv")
correlation = df['study_hours_per_day'].corr(df['exam_score'])
print("Correlation between Study Time and Academic Score:", correlation)
