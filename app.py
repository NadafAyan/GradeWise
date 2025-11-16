from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import tabula

# Flask app ka instance banate hain
app = Flask(__name__)

# Server ke liye 'uploads' aur 'extracted_data' folders ke paths define karte hain.
# yeh folders GradeWise folder ke andar banenge.
UPLOADS_FOLDER = os.path.join(app.root_path, 'uploads')
EXTRACTED_DATA_FOLDER = os.path.join(app.root_path, 'extracted_data')

# Ensure the folders exist. Agar nahi honge, toh code unhe bana dega.
if not os.path.exists(UPLOADS_FOLDER):
    os.makedirs(UPLOADS_FOLDER)
if not os.path.exists(EXTRACTED_DATA_FOLDER):
    os.makedirs(EXTRACTED_DATA_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOADS_FOLDER

# Home page route. Yahan index.html page dikhega.
@app.route('/')
def home():
    return render_template('index.html')

# Analysis route. Yahan file upload aur processing hoga.
@app.route('/analyze', methods=['POST'])
def analyze():
    # Check karte hain ki file upload hui hai ya nahi.
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # Agar user ne bina file select kiye submit kiya.
    if file.filename == '':
        return redirect(request.url)

    # Agar file mili toh...
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # --- Data Extraction (Part 1) ---
        try:
            tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

            if not tables:
                return "Error: PDF mein koi table nahi mila. Kripya sahi marksheet upload karein."

            df = pd.concat(tables, ignore_index=True)
            extracted_csv_path = os.path.join(EXTRACTED_DATA_FOLDER, "extracted_marks.csv")
            df.to_csv(extracted_csv_path, index=False)

        except Exception as e:
            return f"Error during data extraction: {e}"

        # --- Data Cleaning (Part 2) ---
        try:
            # Extracted CSV ko load karte hain aur clean karte hain.
            df_cleaned = pd.read_csv(extracted_csv_path, header=1)
            
            # Khali rows ko hatate hain aur 0 se fill karte hain.
            df_cleaned.dropna(subset=['Roll no', 'Name'], how='all', inplace=True)
            df_cleaned.fillna(0, inplace=True)

            # Columns ka naam badalte hain.
            df_cleaned = df_cleaned.rename(columns={'Que 1(a)': 'Q1_a', 'Que 1(b)': 'Q1_b', 'Que 2 (a)': 'Q2_a', 'Que 2 (b)': 'Q2_b', 'Que 3(a)': 'Q3_a', 'Que 3(b)': 'Q3_b', 'Que4(a)': 'Q4_a', 'Que4(b)': 'Q4_b'})

            # Marks columns ko integer mein convert karte hain.
            marks_columns = ['Q1_a', 'Q1_b', 'Q2_a', 'Q2_b', 'Q3_a', 'Q3_b', 'Q4_a', 'Q4_b', 'Total']
            for col in marks_columns:
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce').astype('Int64')

            # Cleaned data ko save karte hain.
            cleaned_csv_path = os.path.join(EXTRACTED_DATA_FOLDER, "cleaned_marks.csv")
            df_cleaned.to_csv(cleaned_csv_path, index=False)
            
            # Abhi ke liye success message dikhate hain.
            return f"File '{file.filename}' successfully uploaded, extracted, and cleaned! A cleaned CSV file has been saved in 'extracted_data' folder."
        
        except Exception as e:
            return f"Error during data cleaning: {e}"

    return redirect(url_for('home'))

# App ko chalao (debug mode ke saath).
if __name__ == '__main__':
    app.run(debug=True)