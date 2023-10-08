from flask import Flask, request, jsonify
import spacy


app = Flask(__name__)


def identify_pii(text):
  """
  Identifies PII in text using spaCy.

  Args:
    text: A string containing the text to be analyzed.

  Returns:
    A list of strings containing the PII found in the text.
  """

  nlp = spacy.load("en_core_web_sm")
  doc = nlp(text)
  pii = []
  for ent in doc.ents:
    if ent.label_ == "PERSON":
      pii.append(ent.text)
    elif ent.label_ == "ORG":
      pii.append(ent.text)
    elif ent.label_ == "GPE":
      pii.append(ent.text)
    elif ent.label_ == "DATE":
      pii.append(ent.text)
    elif ent.label_ == "TIME":
      pii.append(ent.text)
    elif ent.label_ == "MONEY":
      pii.append(ent.text)
    elif ent.label_ == "QUANTITY":
      pii.append(ent.text)
    elif ent.label_ == "PERCENT":
      pii.append(ent.text)
    elif ent.label_ == "ID":
      pii.append(ent.text)
  return pii


@app.route("/api/identify-pii", methods=["POST"])
def identify_pii_api():
  """
  API endpoint to identify PII in text.

  Returns:
    A JSON response containing an array of PII found in the text.
  """

  text = request.json["body"]
  pii = identify_pii(text)

  response = {
    "pii_detected": pii,
    "error": "nil"
  }

  return jsonify(response), 200



if __name__ == "__main__":
  app.run(debug=True)
