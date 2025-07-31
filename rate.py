# rate_blog.py

import os
from textblob import TextBlob
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini = genai.GenerativeModel("gemini-2.5-flash")

def rate_with_textblob(content):
    polarity = TextBlob(content).sentiment.polarity
    if polarity <= -0.6:
        return 1
    elif polarity <= -0.2:
        return 2
    elif polarity <= 0.2:
        return 3
    elif polarity <= 0.6:
        return 4
    else:
        return 5

def rate_with_gemini(content):
    prompt = f"""Rate this blog on a scale of 1 to 5 based on content quality, coherence, relevance, and engagement.
Only return the number. Content:\n{content}"""
    try:
        res = gemini.generate_content(prompt)
        return int(res.text.strip())
    except Exception as e:
        print("Gemini failed:", e)
        return None

def rate_blog(content):
    gemini_rating = rate_with_gemini(content)
    if gemini_rating is not None:
        blob_rating = rate_with_textblob(content)
        return round((gemini_rating*4 + blob_rating) / 5)
    return rate_with_textblob(content)

# Test
if __name__ == "__main__":
    blog = "The article was insightful, though a bit verbose. It discussed AI trends well."
    print("Hybrid Rating:", rate_blog(blog))
