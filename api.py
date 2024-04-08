from flask import Flask, request, jsonify
import spacy
import streamlit as st

# Initialize Flask app
app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_med7_lg")


@app.route('/status', methods=['GET'])
def status_check():
    return jsonify({"message": "API is running"}), 200


@app.route('/analyze', methods=['PUT'])
def analyze_text():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Process the text
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    return jsonify(entities)


if __name__ == "__main__":
    # Run on a different port if 5000 is used by Streamlit
    st.write("Running on streamlit")
    app.run(debug=False, port=6001)
