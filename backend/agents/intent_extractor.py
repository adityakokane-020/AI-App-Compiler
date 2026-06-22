def extract_intent(prompt: str):

    prompt = prompt.lower()

    features = []

    keywords = [
        "login",
        "dashboard",
        "payment",
        "payments",
        "contact",
        "contacts",
        "analytics"
    ]

    for word in keywords:
        if word in prompt:
            features.append(word)

    return {
        "app_type": "Unknown",
        "features": sorted(list(set(features))),
        "status": "intent_extracted"
    }