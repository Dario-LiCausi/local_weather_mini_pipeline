import pandas as pd

def extract(json_path="../data/raw_weather_data.json"):
    
    weather_data = pd.read_json(json_path)
    return weather_data