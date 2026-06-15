import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Student_Marks.csv")
data = data.astype({
    "number_courses":int,
    "time_study":int,
    "Marks":float
})

data["Student_ID"] = [int(idx) for idx in range(len(data))] 

#Index(['number_courses', 'time_study', 'Marks', 'ID'], dtype='str')

top_students = pd.DataFrame(columns=data.columns)
poor_students = pd.DataFrame(columns=data.columns)

top_10 = data["Marks"].quantile(0.90)
least_10 = data["Marks"].quantile(0.10)

top_students = data[data["Marks"]>=top_10]
poor_students = data[data["Marks"]<least_10]

print("\n Top performing students:")
print(top_students)

print("\nStudents at the risk of failing!:")
print(poor_students)

#overall class performance statistics:
print(f"\nHighest Mark :{max(data['Marks'])}\nLowest Mark :{min(data['Marks'])}\nAverage Mark :{(data['Marks'].mean()):.2f}\n")

#plotting
plt.title("Bar chart for Study time Vs. Performance")
plt.bar(data["time_study"],data["Marks"],color='lightblue')
plt.xlabel("Study time(hrs)")
plt.ylabel("Marks obtained(out of 60)")
plt.show()

plt.title(f"Marks with respect to average mark({(data["Marks"].mean()):.2f}%)")
above = (data["Marks"]>=data["Marks"].mean()).sum()
below = (data["Marks"]<data["Marks"].mean()).sum()
plt.pie([above,below],labels=["Above Average","Below Average"],autopct='%1.1f%%')
plt.show()
