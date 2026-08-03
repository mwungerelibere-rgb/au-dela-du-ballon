import json
import os


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
        "caption": article.get("caption", ""),
        "why": article.get("why", ""),
        "script": article.get("script", ""),
        "hashtags": article.get("hashtags", "")
    }

    news = []

    if os.path.exists("news.json"):
        try:
            with open("news.json", "r", encoding="utf-8") as f:
                news = json.load(f)
        except Exception:
            news = []

    if not any(item.get("title") == data["title"] for item in news):
        news.insert(0, data)

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(news, f, indent=4, ensure_ascii=False)
