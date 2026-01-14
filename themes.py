import re

THEMES = {
    "Comfort": {"light", "heavy", "fit", "wearable"},
    "Durability": {"broke", "strong", "quality", "fragile"},
    "Appearance": {"shiny", "dull", "design", "polish"}
}

def detect_themes(review_text: str):
    words = set(re.findall(r'\b\w+\b', review_text.lower()))
    detected = []

    for theme, keywords in THEMES.items():
        if words.intersection(keywords):
            detected.append(theme)

    return detected
