def decide(action_scores: dict):
    best_action = max(action_scores, key=action_scores.get)
    confidence = action_scores[best_action]

    if confidence >= 0.8:
        return {"action": best_action, "confidence": confidence}
    return {"action": "monitor", "confidence": confidence}
