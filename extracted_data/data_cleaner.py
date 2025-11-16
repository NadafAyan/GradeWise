import pandas as pd
import numpy as np

# Load the CSV file again, this time with the correct header
file_path = r"C:\Users\Ayan Nadaf\Desktop\Projects\GradeWise\extracted_data\extracted_marks.csv"
df = pd.read_csv(file_path, header=1)

# Drop unnecessary rows which contain nulls for both Roll no and Name
df.dropna(subset=['Roll no', 'Name'], how='all', inplace=True)

# Rename the columns for better readability and to match the PDF.
df = df.rename(columns={'Que 1(a)': 'Q1_a', 'Que 1(b)': 'Q1_b', 'Que 2 (a)': 'Q2_a', 'Que 2 (b)': 'Q2_b', 'Que 3(a)': 'Q3_a', 'Que 3(b)': 'Q3_b', 'Que4(a)': 'Q4_a', 'Que4(b)': 'Q4_b'})

# Replace blank values with 0
df.fillna(0, inplace=True)

# Convert marks columns to integer type.
marks_columns = ['Q1_a', 'Q1_b', 'Q2_a', 'Q2_b', 'Q3_a', 'Q3_b', 'Q4_a', 'Q4_b', 'Total']
for col in marks_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].astype('Int64')

# Save the cleaned DataFrame to a new CSV file.
cleaned_file_path = "cleaned_marks.csv"
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete! The cleaned data is saved in 'cleaned_marks.csv'.")
print("\nFirst 5 rows of the cleaned DataFrame:")
print(df.head())

print("\nInformation of the cleaned DataFrame:")
print(df.info())