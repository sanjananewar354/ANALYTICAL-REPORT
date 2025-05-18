import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_habits_performance.csv")

avg_scores_activities = df.groupby('extracurricular')['AcademicScore'].mean()

print(avg_scores_activities)

plt.figure(figsize=(8, 6))
avg_scores_activities.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Academic Score by Extracurricular Participation')
plt.xlabel('Extracurricular Activities')
plt.ylabel('Average Academic Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
