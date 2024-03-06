Here is a sample code for a Python Flask API to implement the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive loan application documents
@app.route('/loan/application', methods=['POST'])
def receive_loan_application():
    # Get the applicant's identification, proof of income, credit history, and employment details from the request
    identification = request.json.get('identification')
    proof_of_income = request.json.get('proof_of_income')
    credit_history = request.json.get('credit_history')
    employment_details = request.json.get('employment_details')
    
    # Perform document verification and eligibility assessment logic here
    # ...
    # ...
    
    # Generate a report indicating the eligibility status
    report = {
        'identification': identification,
        'proof_of_income': proof_of_income,
        'credit_history': credit_history,
        'employment_details': employment_details,
        'eligibility_status': 'eligible'  # Replace with actual eligibility status
    }
    
    # Notify the bank employee of the eligibility status
    # ...
    # ...
    
    # Return the report as a response
    return jsonify(report), 200

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have defined a Flask route `/loan/application` to receive loan application documents as a POST request. The applicant's identification, proof of income, credit history, and employment details are extracted from the request JSON. You can implement the logic for document verification and eligibility assessment based on these details.

After performing the assessment, a report is generated with the applicant's details and eligibility status. This report is then returned as a JSON response.

Note: This is a basic structure for the Flask API code. You would need to add appropriate validations, error handling, and integrate it with your existing system as per your requirements.