"""This module is created to run the main streamlit application for Final project"""
import spacy
import requests
import streamlit as st
from spacy import displacy


# Load the spaCy model
med7 = spacy.load("en_core_med7_lg")
# Create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119',
                 '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors': col_dict}

# Main app function


def main():
    """Main function for running the application"""
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox(
        "Select a page:", ["Medical NER", "Expose API", "About"])

    if option == "Medical NER":
        show_medical_ner()
    elif option == "Expose API":
        show_expose_api()
    elif option == "About":
        show_about()


def show_medical_ner():
    """This function wistll process the text using MED7 model and give its NE"""
    st.header("Medical Named Entity Recognition (NER)")
    st.write(
        "Enter medical text to visualize named entities recognized by the Med7 model.")
    text = st.text_area("Enter text here:", height=150)
    button = st.button('Analyze Text')

    if button and text:
        doc = med7(text)
        ent_html = displacy.render(doc, style='ent', options=options)
        st.markdown(ent_html, unsafe_allow_html=True)
    elif button:
        st.error("Please enter text to analyze.")


def show_expose_api():
    """This function will expose its relevant API's"""
    st.header("Expose API")
    st.write("Click the button below to start the API if it's not already running.")
    st.success("Click the button below to check if the API is running.")
    if st.button('Check API Status'):
        try:
            # Adjust URL/port as needed
            response = requests.get('http://127.0.0.1:6001/status')
            if response.status_code == 200:
                st.success("API is running!")
            else:
                st.error("API is running but returned a non-200 status code.")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the API: {e}")

    st.markdown("""
    **API Details:**
    - **Framework:** Flask
    - **Endpoint:** `/analyze`
    - **Method:** PUT
    - **Payload:** `{ "text": "Your medical text here" }`
    - **Response:** JSON containing entities recognized in the text.
    """)


def show_about():
    """This function will show its API's"""
    st.header("About This App")
    st.write("This app demonstrates the capabilities of spaCy and the Med7 model for recognizing medical entities in text.")
    st.markdown("""
    - **Developed by:** Ronit Shahu and Utkarsh Nipane
    - **GitHub:** [Link to project repository](#)
    - **Purpose:** Educational demonstration of medical NER.
    """)


if __name__ == "__main__":
    main()
