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

def update_fixtures(start_date, end_date):
    """Update match fixtures data"""
    logger.info(f"Updating fixtures from {start_date} to {end_date}")
    fixtures = get_fixtures(start_date, end_date)
    
    # Save raw data
    fixtures_file = f"data/raw/fixtures/fixtures_{datetime.today().strftime('%Y%m%d')}.json"
    with open(fixtures_file, 'w') as f:
        json.dump(fixtures, f)
    
    logger.info(f"Saved {len(fixtures)} fixtures to {fixtures_file}")

def update_team_player_data():
    """Update team and player statistics"""
    logger.info("Updating team and player data")
    
    # Get all teams
    teams = pd.read_csv('data/processed/teams.csv')['team_id'].tolist()
    
    for team_id in teams:
        # Team stats
        team_stats = get_team_stats(team_id)
        team_file = f"data/raw/teams/{team_id}_{datetime.today().strftime('%Y%m%d')}.json"
        with open(team_file, 'w') as f:
            json.dump(team_stats, f)
        
        # Player stats
        player_stats = get_player_stats(team_id)
        player_file = f"data/raw/players/{team_id}_players_{datetime.today().strftime('%Y%m%d')}.json"
        with open(player_file, 'w') as f:
            json.dump(player_stats, f)
    
    logger.info(f"Updated stats for {len(teams)} teams")

def update_environmental_data():
    """Update weather and venue data"""
    logger.info("Updating environmental data")
    
    # Get venues with upcoming matches
    venues = pd.read_csv('data/processed/venues.csv')
    
    for _, venue in venues.iterrows():
        # Weather forecast
        weather = get_weather_forecasts(venue['city'], venue['country'])
        weather_file = f"data/raw/weather/{venue['venue_id']}_{datetime.today().strftime('%Y%m%d')}.json"
        with open(weather_file, 'w') as f:
            json.dump(weather, f)
        
        # Pitch condition (simulated)
        pitch_condition = {
            'venue_id': venue['venue_id'],
            'condition': 'Good',  # Would come from groundskeeper API
            'last_maintenance': '2023-10-10',
            'hardness': 75  # Scale 1-100
        }
        pitch_file = f"data/raw/venues/{venue['venue_id']}_pitch.json"
        with open(pitch_file, 'w') as f:
            json.dump(pitch_condition, f)
    
    logger.info(f"Updated environmental data for {len(venues)} venues")

def update_news_data():
    """Update injury reports and transfer news"""
    logger.info("Updating news data")
    
    # Get injury reports
    injuries = get_injury_reports()
    injury_file = f"data/raw/injuries/injuries_{datetime.today().strftime('%Y%m%d')}.json"
    with open(injury_file, 'w') as f:
        json.dump(injuries, f)
    
    # Get transfer news
    transfers = get_transfer_news()
    transfer_file = f"data/raw/transfers/transfers_{datetime.today().strftime('%Y%m%d')}.json"
    with open(transfer_file, 'w') as f:
        json.dump(transfers, f)
    
    logger.info(f"Updated {len(injuries)} injury reports and {len(transfers)} transfer news items")

if __name__ == "__main__":
    update_all_data()
