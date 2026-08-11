# Handling HTTP Errors
import json
import requests

try:
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    response = requests.get(url, timeout=5) # ensures the request will only wait 5 seconds before timing out
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.RequestException as e:
    print(f'An error occured: {e}')