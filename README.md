# 🏠 Smart Home Location Recommender

This project is a simple Streamlit web application that recommends the best home locations based on user preferences like crime rate, school proximity, hospital availability, and neighborhood rating.

## 📌 Features

- ✅ Choose what's most important to you:
  - Low crime areas
  - Proximity to schools
  - Proximity to hospitals
  - Good neighborhood ratings
- ✅ Get scored and ranked recommendations
- ✅ User-friendly web interface built using Streamlit

## 📂 Files

- `app.py` – Main Python application that runs the Streamlit app.
- `merged_data.csv` – Dataset containing information about various districts (crime stats, schools, hospitals, neighborhood scores, etc.).

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install streamlit pandas
2. Run the app
bash
Copy
Edit
streamlit run app.py
The app will open in your default web browser.

📊 Dataset Columns (Expected)
The merged_data.csv file should contain the following (case-insensitive) columns:

DISTNAME – Name of the district

CRIME_COUNT – Number of crimes reported

TOTAL_SCHOOLS – Total number of schools

TOTAL_HEALTHCARE – Number of nearby hospitals/clinics

NEIGHBOUR_RATING – Neighborhood quality score

These are renamed internally for consistency.

⚙️ Scoring Logic
The score for each district is calculated based on:

Crime rate (lower is better)

Number of schools (higher is better)

Number of hospitals (higher is better)

Neighborhood rating (higher is better)

Each factor is normalized and weighted:

Crime: 40%

Schools: 30%

Hospitals: 30%

Neighborhood: 30%

Weights are applied only if the user selects the respective checkbox.

🧠 Author
Developed by [Your Name] – A simple tool to help people make smarter location decisions based on real data.


License

Eluru Poojith Kumar Reddy
