import requests

api_key = "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"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

json_data = {
    "model": "mistralai/mixtral-8x7b-instruct",  # You can try others too!
    "messages": [
        {"role": "user", "content": "Hello! What can you do?"}
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=json_data
)

if response.status_code == 200:
    print("✅ Key is valid.")
    print("AI Response:", response.json()['choices'][0]['message']['content'])
else:
    print("❌ Key failed or error occurred.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
