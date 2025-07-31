import requests
import geocoder
import json
import os

# define user's location and pass it to api
def user_location():
    g = geocoder.ip('me')
    return g.lat, g.lng

# estracts local weather raw data from API
def get_weather_data(lat, lng):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lng}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=auto"
    )
    response = requests.get(url)
    return response.json()

# writes a json file with raw data from API
def write_json(data):
    with open("data/raw_weather_data.json", "w") as f:
        json.dump(data, f, indent=2)

lat, lng = user_location()
weather = get_weather_data(lat, lng)
write_json(weather)
print("Local weather data extracted from API and saved in raw data")

