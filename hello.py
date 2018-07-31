import requests
import constants
import json

resp = requests.get(constants.url_weather_api+constants.city_ids.get("Delhi"))

if resp.status_code == 200:
    response = json.loads(resp.text)
    print(response["name"])
    weather = response["weather"]
    print(weather[0]["main"])
    climate = response["main"]
    print(climate["temp"])
    print(climate["humidity"])
else:
    exit(0)
