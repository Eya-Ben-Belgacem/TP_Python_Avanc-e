import streamlit as st
import pandas as pd
import numpy as np
st.write('Hello World')

# --- Text Input ---
x = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {x}")

# --- Bouton ---
is_clicked = st.button("Click Me")
if is_clicked:
    st.write("You clicked the button!")

# --- Markdown & Titres ---
st.write("## This is a H2 Title!")

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
# --- Données fictives à la place du CSV ---
st.write("## 🎬 Movies Dataset")
data = pd.DataFrame({
    "Title": ["Inception", "Interstellar", "The Matrix", "Avatar"],
    "Genre": ["Sci-Fi", "Sci-Fi", "Action", "Sci-Fi"],
    "Year": [2010, 2014, 1999, 2009],
    "Rating": [8.8, 8.6, 8.7, 7.8]
})
st.write(data)

# --- Graphiques ---
st.write("## 📊 Random Charts")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.write("### Bar Chart")
st.bar_chart(chart_data)

st.write("### Line Chart")
st.line_chart(chart_data)
st.write("# Page Principale")
st.write("Bienvenue sur mon app multi-pages !")