# src/feature_engineering/feature_store.py
import pandas as pd
from pathlib import Path
from .feature_pipeline import create_feature_vector  # Fixed import
from utils.logger import get_logger  # Fixed import

logger = get_logger(__name__)

# Rest of the code remains the same...

FEATURE_STORE_PATH = Path('data/processed/features')

def update_feature_store():
    # Load new matches
    matches = pd.read_json('data/raw/fixtures/latest.json')
    
    # Generate features
    features = []
    for _, match in matches.iterrows():
        try:
            feature_vector = create_feature_vector(match)
            features.append(feature_vector)
        except Exception as e:
            logger.error(f"Error processing match {match['id']}: {str(e)}")
    
    # Save to feature store
    feature_df = pd.DataFrame(features)
    date_str = pd.Timestamp.now().strftime('%Y%m%d')
    feature_df.to_parquet(FEATURE_STORE_PATH / f'match_features_{date_str}.parquet')
    
    logger.info(f"Feature store updated with {len(feature_df)} matches")
