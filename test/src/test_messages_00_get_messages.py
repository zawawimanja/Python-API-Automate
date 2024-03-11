import requests;
import json;

# Message Endpoint URL
url = 'http://localhost:3000/messages';

# headers
headers = {'Content-Type': 'application/json' }


import requests

# Define the URL for retrieving messages
url = 'http://localhost:3000/messages'

# Define the headers
headers = {'Content-Type': 'application/json'}

def test_get_messages_no_filter():
    # Send a GET request to retrieve messages
    resp = requests.get(url, headers=headers)

    # Validate response status code
    assert resp.status_code == 200, f"Expected status code 200, but received {resp.status_code}"

    # Parse the response body as JSON
    resp_body = resp.json()

    # Validate the structure of the response
    assert isinstance(resp_body, list), "Response body is not a list of messages"

    # Validate the number of messages returned
    expected_message_count = 2  # Update this to the expected number of messages
    assert len(resp_body) == expected_message_count, f"Expected {expected_message_count} messages, but received {len(resp_body)}"

    # Optionally, validate the content of each message
    for message in resp_body:
        assert 'id' in message, "Message ID is missing"
        assert 'text' in message, "Message text is missing"
        assert 'category' in message, "Message category is missing"

    # Print the response body for debugging purposes
    print(resp.text)
