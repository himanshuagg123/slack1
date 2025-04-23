import requests

token = ""  # paste token here

url = "" #  paste url here

channel = "" # paste channel id here 

message = "hi annant"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

payload = {
    "channel": channel,
    "text": message,
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200 and response.json().get("ok"):
    print("Message sent successfully!")
else:
    print(f"Error: {response.json().get('error')}")
