import tkinter as tk
import requests

# 🔑 PASTE YOUR API KEY HERE
API_KEY = "74c305faaca97d5e154d062bd6b1cf6e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text="City not found ❌")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        result_label.config(
            text=f"🌡 Temperature: {temp}°C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"☁ Condition: {condition}"
        )

    except Exception as e:
        result_label.config(text="Error fetching weather data.")

root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.resizable(False, False)

title = tk.Label(root, text="🌦️ Weather App", font=("Arial", 18, "bold"))
title.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

get_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(root, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
