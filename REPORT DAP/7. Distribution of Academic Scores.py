import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_habits_performance.csv")
df['AcademicScore'].hist(bins=10)
plt.title("Distribution of Academic Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.show()
