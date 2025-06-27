import schedule
import time

def daily_data_job():
    # Run data collection and feature update
    pass

def prediction_job():
    # Run main prediction and send to Telegram
    pass

if __name__ == "__main__":
    schedule.every().day.at("03:00").do(daily_data_job)
    schedule.every().thursday.at("18:00").do(prediction_job)
    schedule.every().friday.at("18:00").do(prediction_job)
    
    while True:
        schedule.run_pending()
        time.sleep(60)
