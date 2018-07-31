import requests
import constants

resp = requests.get(constants.url_forecast_api+constants.city_ids.get("Delhi"))

if resp.status_code == 200:
    print resp.json()
else:
    exit(0)
