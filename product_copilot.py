def explain_insight(insight: dict):
    return (
        f"Retention dropped due to {insight['cause']}. "
        f"Recommended action: {insight['recommended_action']}. "
        f"Confidence: {insight['confidence']}"
    )
