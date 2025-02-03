import requests
import json
api_key = "xai-fwKoJuoBgkDQe7BNqj6EAsu8NfzhW1KT0CgUPoJ4baVgBKV9lomLNCDLsWZ3DZtELwkKjzXP6MjcDi4F"
endpoint = "https://api.x.ai/v1/chat/completions"

input_text = "The concept of artificial intelligence is complex."

# data = {"api_key": api_key, "text": input_text}
# response = requests.post(endpoint, json=data)
# explained_text = response.json()["explained_text"]
# print(explained_text)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the data payload for the request
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are a test assistant."
        },
        {
            "role": "user",
            "content": "Testing. Just say hi and hello world and nothing else."
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}

# Make the POST request to the API
response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    print(response_data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)