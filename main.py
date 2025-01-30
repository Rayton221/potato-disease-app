import streamlit as st

st.title("Potato Disease Prediction App")

about_page = st.Page(
    page = "about_the_app.py",
    title="About the project",
    default=True
)

diseases_page = st.Page(
    page="diseases.py",
    title="Diseases"
)

make_prediction = st.Page(
    page="make_prediction.py",
    title= "Make prediction"
)

pg = st.navigation(
    pages=[about_page,diseases_page,make_prediction]
)
st.sidebar.markdown("[About me](https://rayton221.github.io/Portfolio/)")
pg.run()