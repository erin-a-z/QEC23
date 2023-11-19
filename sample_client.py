import requests

url = 'http://127.0.0.1:5000/api/1/1/1/1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
