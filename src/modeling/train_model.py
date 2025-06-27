import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_outcome_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    model = RandomForestClassifier(n_estimators=500)
    model.fit(X_train, y_train)
    joblib.dump(model, 'data/models/outcome_model.pkl')
