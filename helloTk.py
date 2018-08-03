import tkinter as tk
import constants
import json
import requests

root = tk.Tk()
root.title("OpenWeather")
root.minsize(360, 360)

# Exit btn
btn_exit = tk.Button(text="Exit", width=15, pady=3, fg="#a9a9a9", command=root.destroy)
btn_exit.pack(side="bottom")


# Radio btn
def print_response(resp):
    place = resp['city']['name'] + ", " + resp['city']['country']
    print(place)
    for item in resp['list']:
        output = item['weather'][0]['description'] + ", temp: %.2f"%(item['main']['temp'] - 273.15) \
                 + ", humidity: %d"%(item['main']['humidity'])
        print output
        print("---")


def get_city_weather():
    url = constants.url_forecast_api + id_city_selected.get()
    req = requests.get(url)
    print(url)
    if req.status_code == 200:
        resp = json.loads(req.text)
        print_response(resp)
    else:
        resp = None


id_city_selected = tk.StringVar()
for key in constants.city_ids.keys():
    radio_button = tk.Radiobutton(text=key, variable=id_city_selected, value=constants.city_ids.get(key),
                                  justify=tk.CENTER, command=get_city_weather, pady=1)
    radio_button.deselect()
    radio_button.pack(side="top", anchor="w", padx=3)

# Display Weather area

# Get Weather btn
root.mainloop()
