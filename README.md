
# PII Detection API

This is a Python Flask application that provides an API endpoint to identify Personally Identifiable Information (PII) in text using spaCy. It categorizes and extracts PII entities such as names, organizations, locations, dates, times, monetary values, quantities, percentages, and identification numbers.

## Getting Started

Follow these instructions to set up and run the API locally.

### Prerequisites

- Python 3.x
- Flask
- spaCy (with the "en_core_web_sm" model)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pii-detection-api.git
   cd pii-detection-api
   ```

2. Install the required Python packages:

   ```bash
   pip install flask spacy
   python -m spacy download en_core_web_sm
   ```

### Usage

To start the API server, run the following command:

```bash
python app.py
```

The API will be available at `http://localhost:5000/api/identify-pii` by default.

#### Endpoint

- **POST /api/identify-pii**: Identify PII in text.

  - Request Body:
    ```json
    {
      "body": "Text to analyze for PII detection."
    }
    ```

  - Response:
    ```json
    {
      "pii_detected": ["John Doe", "Company Inc.", "New York", "2023-01-15", ...],
      "error": "nil"
    }
    ```

### Example

You can use tools like `curl` or Postman to send POST requests to the API endpoint.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"body": "John Doe was born on 2000-05-15 in New York."}' http://localhost:5000/api/identify-pii
```

### PII Categories

The API identifies the following PII categories:
- PERSON
- ORGANIZATION
- GPE (Geopolitical Entity)
- DATE
- TIME
- MONEY
- QUANTITY
- PERCENT
- ID (Identification Number)

## Contributing

We welcome contributions to improve this project. If you find any issues or have suggestions for enhancements, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- The code uses spaCy for natural language processing.
- This project was inspired by the need for PII detection in text.

---

Feel free to modify this template according to your specific needs and provide more detailed information about your project if necessary.
