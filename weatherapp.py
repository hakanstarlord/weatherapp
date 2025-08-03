import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

API_KEY = "d519faed89e4ddabb5a7dc3c6a9212cf"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city or city == "Enter city name...":
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "lang": "tr",
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            result = (
                f"📍 {data['name']}, {data['sys']['country']}\n"
                f"🌡 Sıcaklık: {data['main']['temp']}°C\n"
                f"💧 Nem: {data['main']['humidity']}%\n"
                f"🌬 Rüzgar Hızı: {data['wind']['speed']} m/s\n"
                f"🌥 Durum: {data['weather'][0]['description']}"
            )
        else:
            result = "❌ Şehir bulunamadı veya API hatası."

    except Exception as e:
        result = f"⚠️ Hata oluştu:\n{str(e)}"

    result_label.config(text=result)


# Arayüz Ayarları
window = tk.Tk()
window.title("Weather App")
window.geometry("400x380")
window.configure(bg="#e0f7fa")



# Simge Ekleme
try:
    window.iconbitmap("weather.ico")  # .ico uzantılı yeni hava durumu simgen burada olmalı
except:
    pass

# Başlık
title_label = tk.Label(window, text="Weather App", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#0288d1")
title_label.pack(pady=10)

# Giriş
city_entry = tk.Entry(window, font=("Arial", 14), width=30, justify="center", fg="gray")
city_entry.insert(0, "Enter city name...")

def clear_placeholder(event):
    if city_entry.get() == "Enter city name...":
        city_entry.delete(0, tk.END)
        city_entry.config(fg="black")

city_entry.bind("<FocusIn>", clear_placeholder)
city_entry.pack(pady=10)

# Buton
search_button = tk.Button(window, text="Get Weather", font=("Arial", 12), bg="#0288d1", fg="white", command=get_weather)
search_button.pack(pady=5)

# Sonuç
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#e0f7fa", justify="left", wraplength=350)
result_label.pack(pady=20)

window.mainloop()
