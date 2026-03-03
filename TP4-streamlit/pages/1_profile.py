import streamlit as st

st.write("# 👤 Mon Profil")
st.text_input("Ton nom ?")
st.number_input("Ton âge ?", min_value=0)
st.selectbox("Ton pays ?", ["Tunisie", "France", "Maroc"])