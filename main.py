import requests, json
from tkinter import *


def addtime():
    yes = entry.get()
    api_key = "d8c4ab6753ff8af8c82c04868f77401f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = yes
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if city_name!="" and x["cod"] != "404":

        y = x["main"]
        frame1 = Frame(frame)
        frame1.configure(background="#FF5733")
        frame1.pack()
        ciudad = Label(frame1, text=city_name,font=("Arial",15))
        current_temperature = Label(frame1, text="Temperature: "+str(round(y["temp"] - 273.15)) + " °C")

        current_pressure = Label(frame1, text="Pressure: "+str(round(y["pressure"])) + " hPa")

        current_humidity = Label(frame1, text="Humidity: "+str(round(y["humidity"])) + " %")
        current_humidity.configure(background="#FF5733")
        current_pressure.configure(background="#FF5733")
        current_temperature.configure(background="#FF5733")
        ciudad.configure(background="#FF5733")
        z = x["weather"]

        weather_description = Label(frame1, text=z[0]["description"])
        weather_description.configure(background="#FF5733")
        ciudad.grid(row=1, column=0,padx=10)
        current_temperature.grid(row=2, column=0,padx=10)
        current_pressure.grid(row=3, column=0,padx=10)
        current_humidity.grid(row=4, column=0,padx=10)
        weather_description.grid(row=5, column=0,padx=10)
        but = Button(frame1, text="x", command=lambda: frame1.pack_forget(),bg="#87CEEB")
        but.grid(row=3, column=1,padx=10)
        space = Label(frame1, text="")
        space.configure(background="#FF5733")
        space.grid(row=6, column=0,padx=10)

    else:
        print("City not found")



root = Tk()
root.title("Weather App")
root.geometry("320x600")
root.configure(background="#6495ED")
frame = Frame(root)
frame.configure(background="#6495ED")
root.iconbitmap("icon.ico")
add = Button(root, text="Add City", command=addtime)
entry = Entry(root, borderwidth=15, relief=FLAT, bg="#87CEEB", fg="black",width=50)
entry.grid(row=0,column=0,pady=10)
add.grid(row=1,column=0,pady=10)
frame.grid(row=2,column=0)
root.mainloop()