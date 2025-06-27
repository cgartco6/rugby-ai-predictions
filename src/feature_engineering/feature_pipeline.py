from .team_features import build_team_features
from .player_features import build_player_features
from .environmental import build_environmental_features

def create_feature_vector(match):
    team_features = build_team_features(match)
    player_features = build_player_features(match)
    env_features = build_environmental_features(match)
    return {**team_features, **player_features, **env_features}
