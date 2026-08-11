# Handling HTTP Errors
import json
import requests

try:
    url = 'https://api.open-meteo.com/st?latitude=35&longitude=139&hou'
    response = requests.get(url, timeout=5) # ensures the request will only wait 5 seconds before timing out
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')