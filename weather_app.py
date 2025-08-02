import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text=f"Error: {data['message']}")
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"🌍 City: {city.title()}\n"
            f"🌡️ Temperature: {temp} °C\n"
            f"☁️ Weather: {weather}\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind} m/s"
        )

        result_label.config(text=result)
    except Exception as e:
        result_label.config(text=f"❌ Error: {e}")

# GUI setup
root = tk.Tk()
root.title("🌤️ Real-Time Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
