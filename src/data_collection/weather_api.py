import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather_forecast(location, date):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/future.json?key={api_key}&q={location}&dt={date}"
    response = requests.get(url)
    # Extract relevant weather data
    return {}
