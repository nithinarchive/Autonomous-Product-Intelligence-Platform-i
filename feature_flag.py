def toggle_feature(feature_name: str, enabled: bool):
    state = "ENABLED" if enabled else "DISABLED"
    print(f"Feature {feature_name} is now {state}")
