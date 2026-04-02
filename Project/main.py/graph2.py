import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\mugesh\studentdetails.csv")

df.columns = df.columns.str.strip()

df['Score'] = df['Duration'] * df['Focus']

top_students = df.groupby('name')['Score'].sum().sort_values()

low_performance_students = df.groupby('name')['Score'].sum().sort_values()

print("Top 5 students:")
print(top_students.head(5))

print("\nLow 5 students:")
print(low_performance_students.head(5))

data = df.groupby('subject')["Duration"].sum()

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(df['session_date'], df['Duration'], marker='o')
plt.xticks(rotation=45)
plt.title("Study Duration Over Time")

plt.subplot(2,2,2)
plt.bar(data.index, data.values)
plt.xticks(rotation=45)
plt.title("Subject-wise Study Time")

top_subjects = data.sort_values(ascending=False).head(5)

plt.subplot(2,2,3)
plt.pie(top_subjects.values, labels=top_subjects.index, autopct='%1.1f%%')
plt.title("Top 5 Subjects")

plt.subplot(2,2,4)
plt.hist(df['Duration'], bins=10)
plt.title("Duration Distribution")

plt.tight_layout()
plt.show()
