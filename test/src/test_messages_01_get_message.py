import requests;
import json;

# Message Endpoint URL
url = 'http://localhost:3000/messages/1';

# Headers
headers = {'Content-Type': 'application/json'}

def test_get_message_valid_id():
    # Send a GET request to retrieve the message
    resp = requests.get(url, headers=headers)

    # Validate response status code
    assert resp.status_code == 200, f"Expected status code 200, but received {resp.status_code}"

    # Print the response body for debugging purposes
    print(resp.text)