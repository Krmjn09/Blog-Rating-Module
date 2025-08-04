#!/usr/bin/env python3

import os
import time
import requests
from textblob import TextBlob
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini = genai.GenerativeModel("gemini-1.5-flash")

# Replace with your actual Django backend URL
BACKEND_API_URL = "http://127.0.0.1:8000/api/blogs/"  # Django REST endpoint

def rate_with_textblob(content):
    """Rate using basic sentiment analysis as fallback."""
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
    """Use Gemini to rate blog based on quality and relevance."""
    prompt = (
        "You are an expert finance content reviewer.\n"
        "Please rate the following blog **only on a scale of 1 to 5**, based on:\n"
        "- Relevance to finance topics (investment, saving, budgeting, etc.)\n"
        "- Depth, clarity, grammar, coherence, and usefulness\n\n"
        "**Only return a single integer (1 to 5)**.\n\n"
        "Content:\n" + content
    )
    try:
        res = gemini.generate_content(prompt)
        return int(res.text.strip())
    except Exception as e:
        print("Gemini rating failed:", e)
        return None

def rate_blog(content):
    """Hybrid rating using Gemini (weighted) and TextBlob."""
    gemini_rating = rate_with_gemini(content)
    if gemini_rating is not None:
        blob_rating = rate_with_textblob(content)
        final_rating = round((gemini_rating * 4 + blob_rating) / 5)
        return max(1, min(5, final_rating))  # Clamp to [1, 5]
    return rate_with_textblob(content)

def fetch_blogs():
    """Fetch all blogs from the backend."""
    try:
        response = requests.get(BACKEND_API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Failed to fetch blogs:", e)
        return []

def update_blog_rating(blog_id, new_rating):
    """Update blog rating via PATCH request."""
    try:
        patch_url = f"{BACKEND_API_URL}{blog_id}/"
        response = requests.patch(patch_url, json={"rating": new_rating})
        response.raise_for_status()
        print(f"✔ Updated blog {blog_id} rating to {new_rating}")
    except Exception as e:
        print(f"✘ Failed to update rating for blog {blog_id}:", e)

def run_rating_pipeline():
    """Fetch blogs, rate them using AI/TextBlob, and update backend."""
    blogs = fetch_blogs()
    for blog in blogs:
        blog_id = blog.get("id")
        content = blog.get("content", "")
        if not blog_id or not content:
            continue
        new_rating = rate_blog(content)
        update_blog_rating(blog_id, new_rating)

# Continuous loop
if __name__ == "__main__":
    print("🚀 AI Rating Engine started. Press Ctrl+C to stop.")
    while True:
        try:
            run_rating_pipeline()
        except Exception as err:
            print("Unexpected error during pipeline:", err)
        print("⏳ Waiting 60 seconds before next run...\n")
        time.sleep(60)
