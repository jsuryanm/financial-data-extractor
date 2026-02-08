import streamlit as st 
import pandas as pd 
from data_extractor import extract_text

st.title("Financial Data Extractor")

paragraph = st.text_area("Enter financial paragraph:")

if st.button("Button"):
    if paragraph:
        extract_data = extract_text(paragraph)
        data = {
            "Measure":["Revenue","EPS"],
            "Estimated":[extract_data['revenue_expected'],extract_data['eps_expected']],
            "Actual":[extract_data['revenue_actual'],extract_data['eps_actual']]
        }

        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a paragraph to extract data from")