import requests
import geocoder
import json
import os

class Extract_from_API:

    def __init__(self):
        self.lat, self.lng = self.user_location()
        self.weather_data = None

    # define user's location and pass it to api url
    def user_location(self):
        g = geocoder.ip('me')
        return g.lat, g.lng

    # estracts local weather raw data from API
    def get_weather_data(self):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.lat}&longitude={self.lng}"
            f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
            f"&timezone=auto"
        )
        response = requests.get(url)
        self.weather_data = response.json()

    # writes a json file with raw data from API
    def write_json(self, path="data/raw_weather_data.json"):
        if self.weather_data is not None:
            with open(path, "w") as f:
                json.dump(self.weather_data, f, indent=2)
            print("\nLocal weather data extracted from API and saved in raw data\n")
        else:
            print("\n[ERROR] Cannot find any weather data related to your location.\n")
    
    # runs the class
    def run(self):
        self.get_weather_data()
        self.write_json()