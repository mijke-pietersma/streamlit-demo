# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 23:20:48 2025

@author: piete
"""
import streamlit as st
import pandas as pd

st.title("📊 Simple Data Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload your csv file:", type=["csv"])

if uploaded_file:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📥 Raw Data")
    st.write(df)

    # Simple analysis: describe numeric columns
    st.subheader("📈 Summary Statistics")
    summary = df.describe()
    st.write(summary)

    # Download button for summary table
    csv = summary.to_csv().encode('utf-8')
    st.download_button(
        label="⬇️ Download Summary CSV",
        data=csv,
        file_name='summary.csv',
        mime='text/csv'
    )
