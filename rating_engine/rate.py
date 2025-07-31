def rate_blog(content: str) -> float:
    from .utils import preprocess
    # Dummy logic for rating
    score = len(preprocess(content)) / 100
    return round(min(score, 5.0), 2)
