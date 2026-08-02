import json


def export_story(article, score):

    data = {
        "title": article.get("title", ""),
        "link": article.get("link", ""),
        "date": article.get("date", ""),
        "source": article.get("source", ""),
        "verification": article.get("verification", "🔵 TRUSTED"),
        "priority": score,
        "category": article.get("category", ""),
        "image": article.get("image", ""),

        # Use the values created by story_writer.py
        "caption": article.get("caption", ""),
        "why": article.get("why", ""),
        "script": article.get("script", ""),
        "hashtags": article.get("hashtags", "")
    }

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump([data], f, indent=4, ensure_ascii=False)
