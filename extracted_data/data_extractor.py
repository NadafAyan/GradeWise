import tabula
import pandas as pd

# Define the PDF file path
pdf_path = r"C:\Users\Ayan Nadaf\Downloads\CAE 1 Marks - Sheet1.pdf"

# Read the tables from the PDF
# `multiple_tables=True` ensures all tables on a page are captured
# `pages='all'` tells tabula to process all pages in the PDF
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# The result is a list of DataFrames.
# Let's inspect each DataFrame to see which one contains our marks data.
# print(len(tables)) # You can uncomment this to check how many tables were found.

# We know from the PDF that there are a few tables,
# some of which contain the mark sheet.
# Let's assume the first and second relevant tables are at indices 0 and 1.
# This might change depending on the PDF's structure, so we'll need to check.
# From the provided PDF, we can see the data is split across two pages.
df1 = tables[0]
df2 = tables[1]

# Now, let's combine these two DataFrames into one single DataFrame.
main_df = pd.concat([df1, df2], ignore_index=True)

# Now, main_df contains all the data from both pages.
# Let's save this combined data into a CSV file for a quick check
main_df.to_csv("extracted_marks.csv", index=False)

print("PDF data successfully extracted and saved to 'extracted_marks.csv'!")
print("\nFirst 5 rows of the combined DataFrame:")
print(main_df.head())