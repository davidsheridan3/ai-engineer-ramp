# The requests library (HTTP for Humans)
import requests
import httpx

url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
response = requests.get(url)
print(response.status_code)

print(response.headers)
print(response.text)
data = response.json()
print(data['hourly']['temperature_2m']) # temperature values as a list

r = httpx.get(url)
print(r.status_code)
print(r.json())

# httpx mirror the simplicity of requests, while adding additional capabilities such as asynchronous requests, built in connection pooling, and http 2 support