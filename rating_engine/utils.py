def preprocess(text: str) -> str:
    return text.lower().replace('\n', ' ').strip()
