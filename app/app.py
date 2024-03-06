Here's an example of a Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/loan_application', methods=['POST'])
def process_loan_application():
    data = request.get_json()

    # Document verification process
    required_documents = ['identification', 'proof_of_income', 'credit_history', 'employment_details']
    provided_documents = data.keys()

    missing_documents = list(set(required_documents) - set(provided_documents))
    if missing_documents:
        return jsonify({'error': f'Missing documents: {", ".join(missing_documents)}'}), 400

    for document in provided_documents:
        if not verify_document(data[document]):
            return jsonify({'error': f'Invalid {document} document'}), 400

    # Eligibility assessment
    eligibility_status = assess_eligibility(data)

    # Generate report
    report = generate_report(data, eligibility_status)

    # Notify bank employee
    notify_employee(data['applicant_id'], eligibility_status)

    return jsonify({'report': report})

def verify_document(document):
    # Implement document verification logic here
    # Return True if document is valid, False otherwise
    return True

def assess_eligibility(data):
    # Implement eligibility assessment logic here
    # Return eligibility status (e.g., 'eligible', 'not eligible')
    return 'eligible'

def generate_report(data, eligibility_status):
    # Implement report generation logic here
    # Return report as a dictionary
    return {'applicant_id': data['applicant_id'], 'eligibility_status': eligibility_status}

def notify_employee(applicant_id, eligibility_status):
    # Implement notification logic here
    # Send a notification to the bank employee about the applicant's eligibility status
    pass

if __name__ == '__main__':
    app.run()
```

This code sets up a Flask API with a single endpoint `/loan_application` that accepts a POST request. The endpoint expects a JSON payload containing the applicant's information and documents. The code then verifies the provided documents, assesses the eligibility based on the documents, generates a report, and notifies the bank employee of the eligibility status.

Note that the document verification, eligibility assessment, report generation, and notification logic are all placeholders and need to be implemented according to your specific requirements.