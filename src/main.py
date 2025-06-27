# src/main.py
from data_collection.update_daily import update_all_data
from modeling.predict import PredictionEngine
from telegram_bot.bot import send_predictions
from utils.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

def main():
    # Run on Thursday/Friday only
    today = pd.Timestamp.today()
    if today.dayofweek not in [3, 4]:  # 3=Thursday, 4=Friday
        logger.info("Not a prediction day (Thursday/Friday). Exiting.")
        return
    
    logger.info("Starting prediction workflow")
    
    # Ensure we have fresh data
    try:
        logger.info("Updating data sources")
        update_all_data()
    except Exception as e:
        logger.error(f"Data update failed: {str(e)}")
        # Continue with existing data if update fails
    
    # Initialize prediction engine
    engine = PredictionEngine()
    
    # Get upcoming weekend matches
    saturday = today + pd.Timedelta(days=(5 - today.dayofweek) % 7)
    sunday = saturday + pd.Timedelta(days=1)
    
    matches = engine.get_upcoming_matches(
        start_date=saturday.strftime('%Y-%m-%d'),
        end_date=sunday.strftime('%Y-%m-%d')
    )
    
    if not matches:
        logger.warning("No upcoming matches found")
        return
    
    # Generate predictions
    predictions = []
    for match in matches:
        try:
            prediction = engine.predict(match)
            predictions.append(prediction)
        except Exception as e:
            logger.error(f"Prediction failed for {match['home']} vs {match['away']}: {str(e)}")
    
    # Filter to high-confidence BTTS and Win/Draw selections
    filtered = [
        p for p in predictions 
        if p['btts_prob'] > 0.65 and p['win_draw_confidence'] > 70
    ][:16]  # Limit to 16 games
    
    # Send to Telegram
    if filtered:
        send_predictions(filtered)
        logger.info(f"Sent {len(filtered)} predictions to Telegram")
    else:
        logger.warning("No qualified predictions to send")
    
    logger.info("Prediction workflow completed")

if __name__ == "__main__":
    main()
