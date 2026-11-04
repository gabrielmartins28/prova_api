import openmeteo_requests

import json
import pandas as pd
import requests_cache
from retry_requests import retry
import requests



url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"current": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m", "apparent_temperature"],
	"timezone": "America/Sao_Paulo",
}
resposta = requests.get(url, params = params)

print(resposta.json())
dados = resposta.json()

dados_meterologicos = dados['current_units']

print("\nA temperatura do ar é:", dados_meterologicos['temperature_2m'])
print("A umidade relativa é: ", dados_meterologicos['relative_humidity_2m'], "%")
print("A sensação térmica é de:", dados_meterologicos['apparent_temperature'], "°C")
print("A precipitação é:", dados_meterologicos['precipitation'], "mm")
print("A velocidade do vento é:", dados_meterologicos['wind_speed_10m'], "km/h")






