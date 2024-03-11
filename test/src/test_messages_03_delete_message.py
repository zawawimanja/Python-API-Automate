import requests;
import json;

# Message Endpoint URL
url = 'http://localhost:3000/messages/1';

# headers
headers = {'Content-Type': 'application/json' }


def test_delete_message_valid_id():
    # Send a DELETE request to delete the message with the specified ID
    resp = requests.delete(url, headers=headers)

   # Validate response status code
    assert resp.status_code == 200, f"Expected status code 200, but received {resp.status_code}"

