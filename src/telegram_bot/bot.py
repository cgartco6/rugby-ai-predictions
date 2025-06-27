# src/telegram_bot/bot.py
import requests
import json
from .message_formatter import format_prediction  # Fixed import
from utils.config_loader import get_env_var  # Fixed import
from utils.logger import get_logger

logger = get_logger(__name__)

def send_predictions(predictions):
    bot_token = get_env_var('TELEGRAM_BOT_TOKEN')
    chat_id = get_env_var('TELEGRAM_CHAT_ID')
    
    if not bot_token or not chat_id:
        logger.error("Telegram credentials not configured")
        return
    
    message = "🏉 *AI RUGBY PREDICTIONS - WEEKEND MATCHES*\n\n"
    
    for pred in predictions:
        message += format_prediction(pred) + "\n\n"
    
    message += "⚠️ _Disclaimer: Predictions for informational purposes only_"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info("Predictions sent to Telegram successfully")
    except Exception as e:
        logger.error(f"Failed to send to Telegram: {str(e)}")
