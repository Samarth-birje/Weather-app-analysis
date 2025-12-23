import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    if not city:
        return None, "City name cannot be empty"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code != 200:
            return None, "Invalid city name or API error"

        data = response.json()

        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"]
        }

        return weather_data, None

    except requests.exceptions.RequestException:
        return None, "Network Error"


def get_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data["cod"] != "200":
            return None

        forecast_data = []

        for item in data["list"]:
            if "12:00:00" in item["dt_txt"]:
                forecast_data.append({
                    "date": item["dt_txt"].split(" ")[0],
                    "temp": item["main"]["temp"],
                    "condition": item["weather"][0]["main"]
                })

        return forecast_data

    except:
        return None
    
def get_weather_icon(condition):
    icons= {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Haze": "🌫️"
    }
    return icons.get(condition, "🌍")
