# The requests library (HTTP for Humans)
import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
response = requests.get(url)
print(response.status_code)

print(response.headers)
print(response.text)
data = response.json()
print(data['hourly']['temperature_2m']) # temperature values as a list