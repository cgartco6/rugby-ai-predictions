# src/data_collection/update_daily.py
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from .sportsradar_api import get_fixtures, get_team_stats, get_player_stats
from .weather_api import get_weather_forecasts
from .news_scraper import get_injury_reports, get_transfer_news
from .data_validation import validate_raw_data
from utils.logger import get_logger
from utils.config_loader import get_env_var, load_config

logger = get_logger(__name__)

def update_all_data():
    """Main function to update all data sources"""
    logger.info("Starting data update process")
    
    # Load configuration
    config = load_config('../config/api_keys.yaml')  # Adjusted path
    
    # Get upcoming matches (next 7 days)
    start_date = datetime.today().strftime('%Y-%m-%d')
    end_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
    
    # Update core data sources
    update_fixtures(start_date, end_date)
    update_team_player_data()
    update_environmental_data()
    update_news_data()
    
    # Validate and process data
    validate_raw_data()
    
    logger.info("Data update completed successfully")

# Rest of the functions remain the same as before...
