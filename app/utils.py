def validate_text(text):
    if not text:
        return "No text provided"
    if len(text.strip()) < 30:
        return "Text too short for processing"
    return None
