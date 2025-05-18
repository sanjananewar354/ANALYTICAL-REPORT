import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_habits_performance.csv")
sns.boxplot(x='sleep_hours', y='AcademicScore', data=df)
plt.title("Academic Score by Sleep Hours")
plt.show()
