import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("merged_data.csv")

# Cleaning and standardizing column names
df.columns = df.columns.str.strip().str.upper()
df.rename(columns={
    "DISTNAME": "District",
    "CRIME_COUNT": "Crime Count",
    "TOTAL_SCHOOLS": "Schools",
    "TOTAL_HEALTHCARE": "Hospitals",
    "NEIGHBOUR_RATING": "Neighbourhood"
}, inplace=True)

# Streamlit UI
st.set_page_config(page_title="🏠 Smart Home Recommender", layout="centered")
st.title("🏠 Smart Home Location Recommender")
st.write("Choose what matters most to you:")

# User Preferences
low_crime = st.checkbox("Low Crime")
near_hospitals = st.checkbox("Near Hospitals")
near_schools = st.checkbox("Near Schools")
good_neighbourhood = st.checkbox("Good Neighbourhood")

# Scoring Logic
df['Score'] = 0

if low_crime:
    df['Score'] += (1 - (df['Crime Count'] / (df['Crime Count'].max() + 1))) * 40

if near_schools:
    df['Score'] += (df['Schools'] / (df['Schools'].max() + 1)) * 30

if near_hospitals:
    if "HOSPITALS" in df.columns:
        df['Score'] += (df['Hospitals'] / (df['Hospitals'].max() + 1)) * 30
    elif "TOTAL_HEALTHCARE" in df.columns:
        df['Score'] += (df['TOTAL_HEALTHCARE'] / (df['TOTAL_HEALTHCARE'].max() + 1)) * 30

if good_neighbourhood and "Neighbourhood" in df.columns:
    df['Score'] += (df['Neighbourhood'] / (df['Neighbourhood'].max() + 1)) * 30

# Sort and Select Top Recommendations
top_df = df[['District', 'Score']].sort_values(by="Score", ascending=False).reset_index(drop=True).head(3)

# Labeling
def label_rank(score):
    if score >= 90:
        return "✅ Best"
    elif score >= 80:
        return "👍 Good"
    elif score >= 70:
        return "😐 Average"
    else:
        return "⚠️ Below Average"

top_df['Recommendation'] = top_df['Score'].apply(label_rank)

# Display Output
if low_crime or near_hospitals or near_schools or good_neighbourhood:
    st.markdown("### 🎯 Your Preferences:")
    if low_crime:
        st.markdown("- Low Crime: ✅")
    if near_hospitals:
        st.markdown("- Near Hospitals: ✅")
    if near_schools:
        st.markdown("- Near Schools: ✅")
    if good_neighbourhood:
        st.markdown("- Good Neighborhood: ✅")

    st.markdown("### ✅ Based on your choices, the best places to stay are:")
    for idx, row in top_df.iterrows():
        st.markdown(f"**{idx+1}. {row['District']}** (Score: {row['Score']:.1f}) - {row['Recommendation']}")

    best_place = top_df.iloc[0]
    st.markdown(f"### 🏠 Recommendation: **{best_place['District']}** is an excellent place to live with a score of {best_place['Score']:.1f}.")
else:
    st.info("Please select at least one preference to get recommendations.")

