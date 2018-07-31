import tkinter as tk
import constants


root = tk.Tk()
root.title("OpenWeather")
root.minsize(360, 360)


# Exit btn
btn_exit = tk.Button(text="Exit", width=15, pady=3, fg="#a9a9a9", command=root.destroy)
btn_exit.pack(side="bottom")
# Radio btn


def get_city_weather():
    print(constants.url_forecast_api+id_city_selected.get())


id_city_selected = tk.StringVar()
for key in constants.city_ids.keys():
    radio_button = tk.Radiobutton(text=key, variable=id_city_selected, value=constants.city_ids.get(key),
                                  justify=tk.CENTER, command=get_city_weather, pady=1)
    radio_button.deselect()
    radio_button.pack(side="top", anchor="w", padx=3)

# Display Weather area

#Get Weather btn
root.mainloop()
