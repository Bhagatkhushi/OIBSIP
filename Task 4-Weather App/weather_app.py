import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "1664eea894aa91c37c8d777d25e206a0"


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="City not found or API inactive")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result = (
            f"📍 City: {city}\n\n"
            f"🌡 Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind} m/s\n"
            f"📊 Pressure: {pressure} hPa\n"
            f"☁ Condition: {condition}"
        )

        result_label.config(text=result)

    except:
        result_label.config(text="Error fetching weather data")


# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x500")
root.config(bg="#87CEEB")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="☁ Weather App",
    font=("Arial", 24, "bold"),
    bg="#87CEEB",
    fg="white"
)
heading.pack(pady=20)

# Input Box
city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    justify="center",
    bd=3
)
city_entry.pack(pady=15)

# Button
search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="#1E90FF",
    fg="white",
    padx=15,
    pady=5,
    command=get_weather
)
search_btn.pack(pady=10)

# Result Box
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="white",
    fg="black",
    width=30,
    height=10,
    relief="ridge",
    bd=3,
    justify="left",
    anchor="nw",
    padx=10,
    pady=10
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Made with Python",
    font=("Arial", 10),
    bg="#87CEEB",
    fg="white"
)
footer.pack(side="bottom", pady=10)

root.mainloop()