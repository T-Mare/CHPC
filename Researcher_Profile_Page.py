import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit Title
st.title("Feature Distribution Analysis")

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("Selected", color)
bin  = st.slider("How many bins do you want?", 10, 50, 10, step=5)
st.write("I'm ", bin, "years old")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV dataset", type=["csv"])

if uploaded_file is not None:
    # Load DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display Data
    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    # Select numerical columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if num_cols:
        st.subheader("Feature Distributions")

        for col in num_cols:
            st.subheader(f"Distribution of {col}")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.histplot(df[col], kde=True, bins=bin, ax=ax, color=color )
            st.pyplot(fig)
    else:
        st.warning("No numerical columns found in the dataset.")
else:
    st.info("Please upload a CSV file to proceed.")

st.title("#FLAG#############")




