import requests
import json
import tkinter as tk

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def display_weather(weather_data):
    location = weather_data['location']['name']
    country = weather_data['location']['country']
    temp_c = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']

    result_label.config(text=f"Weather in {location}, {country}:\nTemperature: {temp_c}°C\nCondition: {condition}")

def get_weather_button_clicked():
    api_key = "98d50c3070ac43f7baf73720232705"
    city = city_entry.get()

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

# Tkinter arayüzü oluşturma
window = tk.Tk()
window.title("Weather App")
window.minsize(height=400, width=400)

# Şehir giriş kutusu
city_label = tk.Label(window, text="City:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

# Hava durumu bilgisini gösteren sonuç etiketi
result_label = tk.Label(window, text="")
result_label.pack()

# Hava durumu bilgisini almak için düğme
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack()

window.mainloop()