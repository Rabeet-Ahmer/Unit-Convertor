import os
import streamlit as st
import wolframalpha
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WOLFRAM_API_KEY")
client = wolframalpha.Client(API_KEY)

st.set_page_config(
    page_title="Unit Convertor",
    page_icon="https://img.icons8.com/?size=96&id=4Ck-DjQC5PyG&format=png",
    layout="centered",
)

def solution(number:int, unit_from:str, unit_to:str) -> str:
    try:
        res = client.query(f"Convert {number} {unit_from} to {unit_to}")
        answer = next(res.results).text
        return answer
    except Exception as e:
        return f"Could not convert: {str(e)}"

def main():
    st.title("Unit Convertor")
    st.write("""Welcome to the "Unit Converter!". This app converts units of length.""")
    select = st.selectbox("Select the unit",["Length","Temperature","Weight","Volume"])
    
    col1, col2, col3= st.columns([1, 1, 1])

    if select == "Length":
        with col1:
            units_from = st.selectbox("From",["m","cm","mm","km","in","ft","yd","mi"])
            numbers = st.number_input(value=1, min_value=1, label_visibility="collapsed", label="Number")

        with col2:
            st.markdown("<br>" * 2, unsafe_allow_html=True)
            convert = st.button("Convert", key="convert", use_container_width=True)

        with col3:
            units_to = st.selectbox("To",["m","cm","mm","km","in","ft","yd","mi"])

            if convert:
                answer = solution(numbers, units_from, units_to)
                st.info(answer)

    elif select == "Temperature":
        with col1:
            units_from = st.selectbox("From",["Celsius","Fahrenheit","Kelvin"])
            numbers = st.number_input(value=1, label_visibility="collapsed", label="Number")

        with col2:
            st.markdown("<br>" * 2, unsafe_allow_html=True)
            convert = st.button("Convert", key="convert", use_container_width=True)

        with col3:
            units_to = st.selectbox("To",["Celsius","Fahrenheit","Kelvin"])

            if convert:
                answer = solution(numbers, units_from, units_to)
                st.info(answer)

    elif select == "Weight":
        with col1:
            units_from = st.selectbox("From",["g","kg","mg","t","oz","lb"])
            numbers = st.number_input(value=1, label_visibility="collapsed", label="Number")

        with col2:
            st.markdown("<br>" * 2, unsafe_allow_html=True)
            convert = st.button("Convert", key="convert", use_container_width=True)

        with col3:
            units_to = st.selectbox("To",["g","kg","mg","t","oz","lb"])

            if convert:
                answer = solution(numbers, units_from, units_to)
                st.info(answer)

    elif select == "Volume":
        with col1:
            units_from = st.selectbox("From",["m³","cm³","mm³","L","mL","gal"])
            numbers = st.number_input(value=1, label_visibility="collapsed", label="Number")

        with col2:
            st.markdown("<br>" * 2, unsafe_allow_html=True)
            convert = st.button("Convert", key="convert", use_container_width=True)

        with col3:
            units_to = st.selectbox("To",["m³","cm³","mm³","L","mL","gal"])
            
            if convert:
                answer = solution(numbers, units_from, units_to)
                st.info(answer)


if __name__ == "__main__":
    main()