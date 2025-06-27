def format_prediction(pred):
    match = pred['match']
    return (
        f"🏉 *{match['home']} vs {match['away']}* ({match['competition']})\n"
        f"⏱ {match['date']} | 🌤 {match['weather']}\n\n"
        f"✅ *AI Prediction*: {pred['prediction']['outcome']} "
        f"(Confidence: {pred['prediction']['confidence']}%)\n"
        f"🎯 *Correct Score*: {pred['correct_score']}\n"
        f"🔔 *BTTS Probability*: {pred['btts_prob']}%\n"
        f"📊 *Book Consensus*: {pred['bookmaker_consensus']}\n\n"
        f"⚕️ *Injuries*: {match['key_injuries']}\n"
        f"👨‍🏫 *Coaching Impact*: {match['coaching_notes']}\n"
        f"🧑‍⚖️ *Referee*: {match['referee']} ({match['ref_tendency']})"
    )
