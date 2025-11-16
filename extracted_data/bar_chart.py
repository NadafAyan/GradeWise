import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
file_path = "extracted_data\cleaned_marks.csv"
df = pd.read_csv(file_path)

# Select only the question columns
question_cols = ['Q1_a', 'Q1_b', 'Q2_a', 'Q2_b', 'Q3_a', 'Q3_b', 'Q4_a', 'Q4_b']

# Calculate the average (mean) for each question
average_marks_per_question = df[question_cols].mean()

# Create a bar chart
plt.figure(figsize=(10, 6)) # Chart size set karna
average_marks_per_question.plot(kind='bar', color='skyblue')

# Add labels and title
plt.title('Average Marks per Question')
plt.xlabel('Question')
plt.ylabel('Average Marks')
plt.xticks(rotation=45) # Question labels ko rotate karna
plt.grid(axis='y', linestyle='--', alpha=0.7) # Grid lines add karna
plt.tight_layout() # Chart ko adjust karna

# Display the chart
plt.show()

print("Bar chart successfully generated!")