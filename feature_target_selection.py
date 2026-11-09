
import pandas as pd

# Create Student Performance Dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 2, 5, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 55, 78, 95],
    "Previous_Marks": [45, 50, 55, 60, 65, 70, 75, 40, 62, 88],
    "Assignment_Score": [50, 55, 60, 65, 70, 75, 80, 45, 68, 90],
    "Final_Marks": [48, 53, 58, 65, 72, 78, 85, 42, 70, 95]
}

df = pd.DataFrame(data)

print("STUDENT PERFORMANCE DATASET")
print(df)

# Feature Selection
X = df[["Study_Hours", "Attendance",
        "Previous_Marks", "Assignment_Score"]]

# Target Selection
y = df["Final_Marks"]

print("\nSELECTED FEATURES")
print(X)

print("\nSELECTED TARGET")
print(y)

print("\nFEATURE SHAPE:", X.shape)
print("TARGET SHAPE:", y.shape)

print("\nEXPLANATION")
print("Study Hours: Study time")
print("Attendance: Attendance percentage")
print("Previous Marks: Past performance")
print("Assignment Score: Assignment performance")
print("Final Marks: Target variable")

print("\nTASK COMPLETED SUCCESSFULLY!")
