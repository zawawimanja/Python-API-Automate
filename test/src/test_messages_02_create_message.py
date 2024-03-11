import requests
import json

# Message Endpoint URL
url = 'http://localhost:3000/messages'

# headers
headers = {'Content-Type': 'application/json'}

# Define the data to be sent in the POST request
data = {"text": "Hi again, World", "category": "Testinggggg"}  # Corrected the dictionary key

def test_create_message():
    # Send a POST request to create a message
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the status code indicates successful creation (e.g., 201 CREATED)
    assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"

    # Optionally, check the response body to ensure that the created message matches the data you sent
    response_data = response.json()
    assert response_data['text'] == data['text'], "The created message text does not match the expected text"

