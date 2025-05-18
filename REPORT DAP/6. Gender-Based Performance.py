import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_habits_performance.csv")

gender_perf = df.groupby('gender')['AcademicScore'].mean()

print("Average Academic Score by gender:")
print(gender_perf)

plt.figure(figsize=(6, 5))
gender_perf.plot(kind='bar', color=['lightcoral', 'lightseagreen'], edgecolor='black')
plt.title('Average Academic Score by gender')
plt.xlabel('Gender')
plt.ylabel('Average Academic Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
