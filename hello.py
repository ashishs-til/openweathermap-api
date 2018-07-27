import requests
import constants

resp = requests.get(constants.api_url)

if resp.status_code == 200:
    print resp.json()
else:
    exit(0)