import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.label_city = tk.Label(master, text="Enter City:")
        self.label_city.grid(row=0, column=0, padx=5, pady=5)

        self.entry_city = tk.Entry(master, width=30)
        self.entry_city.grid(row=0, column=1, padx=5, pady=5)

        self.btn_get_weather = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.btn_get_weather.grid(row=0, column=2, padx=5, pady=5)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def get_weather(self):
        city = self.entry_city.get()
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        weather_data = response.json()

        if weather_data['cod'] == 200:
            city_name = weather_data['name']
            weather_desc = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            result_text = f"City: {city_name}\nWeather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        else:
            result_text = "City not found."

        self.label_result.config(text=result_text)

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
