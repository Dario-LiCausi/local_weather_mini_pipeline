import json
import pandas as pd
import geocoder
from datetime import date

class Transform:
    def __init__(self, json_path = "../data/raw_weather_data.json"):
        self.json_path = json_path
        self.df = None
        self.lat = None
        self.lng = None
        self.location = None

    def rename_keys(self):
        with open(self.json_path) as file:
            data = json.load(file)
        
        self.lat = data.get("latitude")
        self.lng = data.get("longitude")

        daily = data["daily"]
        self.df = pd.DataFrame(daily)

        self.df.rename(columns={
            "time": "date",
            "temperature_2m_max": "max_temp",
            "temperature_2m_min": "min_temp",
            "precipitation_sum": "precipitation"
        }, inplace=True)

        self.df["max_temp"] = self.df["max_temp"].round(1)
        self.df["min_temp"] = self.df["min_temp"].round(1)
        self.df["precipitation"] = self.df["precipitation"].round(1)

    def classify_value(self, precip_value):
        if precip_value == 0:
            return "Clear"
        elif precip_value <= 2:
            return "Light Rain"
        elif precip_value <= 10:
            return "Rain"
        else:
            return "Storm"

    def classify_rain(self):
        self.df["precipitation_type"] = self.df["precipitation"].apply(self.classify_value)

    def define_location(self):
        if self.lat is not None and self.lng is not None:
            g = geocoder.osm([self.lat, self.lng], method="reverse")
            self.location = g.city or g.address or "Unknown"
            self.df["location"] = self.location
        else:
            self.df["location"] = "Unknown"

    def load_date(self):
        self.df["load_date"] = date.today().isoformat()

    def summary(self):
        if self.df is None:
            print("[ERROR] No DataFrame to summarize. Run transform() first.")
            return

        rain_types = self.df["precipitation_type"].value_counts()

        print(f"\nLocation: {self.location}")
        print(f"Data Loaded: {date.today().isoformat()}")
        print(f"Total Days of Forecast: {len(self.df)}")
        print("\nWeather Type Breakdown:")
        for condition, count in rain_types.items():
            print(f"  • {condition}: {count} day(s)")

    def transform(self):
        self.rename_keys()
        self.classify_rain()
        self.define_location()
        self.load_date()
        return self.df