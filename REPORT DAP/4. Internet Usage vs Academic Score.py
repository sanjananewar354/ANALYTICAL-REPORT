import pandas as pd

df = pd.read_csv("student_habits_performance.csv")
avg_scores = df.groupby('InternetUsage')['AcademicScore'].mean()
print(avg_scores)
