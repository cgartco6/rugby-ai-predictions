import os
import sys

# Add the parent directory to the path so we can import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

from data_collection.update_daily import update_all_data

from data_collection import update_all_data
from modeling.predict import PredictionEngine
from telegram_bot.bot import send_predictions

def main():
    # Update data sources
    update_all_data()
    
    # Initialize prediction engine
    engine = PredictionEngine()
    
    # Get upcoming matches (next 3 days)
    matches = engine.get_upcoming_matches(days=3)
    
    # Generate predictions
    predictions = [engine.predict(match) for match in matches]
    
    # Filter to BTTS and Win/Draw selections
    filtered = [p for p in predictions if p['btts_prob'] > 0.65 and p['win_draw_confidence'] > 70]
    
    # Send to Telegram
    send_predictions(filtered)

if __name__ == "__main__":
    main()
