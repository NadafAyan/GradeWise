import pandas as pd

# Load the cleaned data
file_path = "extracted_data\cleaned_marks.csv"
df = pd.read_csv(file_path)

# Select only the question columns
# Note: We are using a list of column names for this.
question_cols = ['Q1_a', 'Q1_b', 'Q2_a', 'Q2_b', 'Q3_a', 'Q3_b', 'Q4_a', 'Q4_b']

# Calculate the average (mean) for each question
average_marks_per_question = df[question_cols].mean()

# Sort the results to easily see the easiest and toughest questions
sorted_avg_marks = average_marks_per_question.sort_values(ascending=False)

# Print the results
print("Average Marks per Question (from easiest to toughest):")
print(sorted_avg_marks)