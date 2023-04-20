import requests

url = "http://localhost:8000/classify_bots"

payload = {
    "screen_name": "Hayko Cepkin",
    "description": "Rock'n roll.",
    "location": "Turkey",
    "verified": False
}

response = requests.get(url, params=payload)

print(response.json())