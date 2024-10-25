import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('data/final_workout_df_cleaned.csv')


st.title("🎈 Data Exploration")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# CCreate filter
columna_a_filtrar = st.selectbox('Selecciona una columna', df.columns)
valor_filtro = st.slider('Selecciona un valor', int(df[columna_a_filtrar].min()), int(df[columna_a_filtrar].max()))

