import requests
import constants
import json

req = requests.get(constants.url_weather_api + constants.city_ids.get("Delhi"))

if req.status_code == 200:
    resp = json.loads(req.text)
    print(resp["name"])
    print(resp["weather"][0]["main"])
    print(resp["main"]["temp"])
    print(resp["main"]["humidity"])
else:
    exit(0)
