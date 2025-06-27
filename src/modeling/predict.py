import joblib
import numpy as np

class PredictionEngine:
    def __init__(self):
        self.models = {
            'outcome': joblib.load('data/models/outcome_model.pkl'),
            'score': joblib.load('data/models/score_model.pkl'),
            'btts': joblib.load('data/models/btts_model.pkl')
        }
        self.feature_builder = FeatureBuilder()
    
    def predict(self, match):
        # Build feature vector
        features = self.feature_builder.build_features(match)
        
        # Make predictions
        outcome_proba = self.models['outcome'].predict_proba([features])[0]
        score_pred = self.models['score'].predict([features])[0]
        btts_prob = self.models['btts'].predict_proba([features])[0][1]
        
        # Decode predictions
        return {
            'match': match,
            'prediction': self._decode_outcome(outcome_proba),
            'correct_score': score_pred,
            'btts_prob': round(btts_prob * 100, 1),
            'bookmaker_consensus': self._get_bookmaker_consensus(match)
        }
    
    def get_upcoming_matches(self, days=3):
        # Retrieve matches from database or API
        pass
