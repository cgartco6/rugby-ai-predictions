from sportsradar_api import update_fixtures, update_team_stats
from weather_api import update_weather_forecasts
from news_scraper import scrape_injury_reports
from data_validation import validate_raw_data
from feature_engineering.feature_store import update_feature_store
from utils.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Starting daily data pipeline")
    
    # Update external data sources
    update_fixtures()
    update_team_stats()
    update_weather_forecasts()
    scrape_injury_reports()
    
    # Validate and process data
    validate_raw_data()
    update_feature_store()
    
    logger.info("Daily data pipeline completed")

if __name__ == "__main__":
    main()
