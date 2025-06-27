import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_fixtures(league, season):
    api_key = os.getenv('SPORTSDAR_API_KEY')
    url = f"https://api.sportradar.com/rugby/{league}/{season}/fixtures?api_key={api_key}"
    response = requests.get(url)
    # Process response and return DataFrame
    return pd.DataFrame()

# Similar functions for other endpoints
