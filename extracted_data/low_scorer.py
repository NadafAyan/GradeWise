import pandas as pd

# Load the cleaned data
file_path = "extracted_data\cleaned_marks.csv"
df = pd.read_csv(file_path)

# Filter the DataFrame for students with 0 total marks
low_scorers_df = df[df['Total'] == 0]

# Print the names and total marks of these students
print("Students with 0 total marks:")
print(low_scorers_df[['Name', 'Total']])