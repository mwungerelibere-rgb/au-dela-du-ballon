import feedparser
from datetime import datetime, timezone
from image_finder import find_image


SOURCES = [
    {
        "name": "ESPN FC",
        "url": "https://www.espn.com/espn/rss/soccer/news",
        "status": "trusted"
    },
    {
        "name": "BBC Sport Football",
        "url": "https://feeds.bbci.co.uk/sport/football/rss.xml",
        "status": "trusted"
    }
]


def extract_image(item):

    image = ""

    try:
        if hasattr(item, "media_content"):
            image = item.media_content[0].get("url", "")

        elif hasattr(item, "media_thumbnail"):
            image = item.media_thumbnail[0].get("url", "")

        elif hasattr(item, "enclosures") and item.enclosures:
            image = item.enclosures[0].get("href", "")

    except Exception:
        image = ""

    return image


def collect_news():

    articles = []

    for source in SOURCES:

        try:
            feed = feedparser.parse(
                source["url"],
                agent="BeyondTheBall/1.0"
            )

        except Exception as e:
            print("RSS error:", source["name"], e)
            continue

        for item in feed.entries[:5]:

            published = getattr(item, "published_parsed", None)

            if published:

                article_date = datetime(
                    *published[:6],
                    tzinfo=timezone.utc
                )

                age = datetime.now(timezone.utc) - article_date

                if age.days > 2:
                    continue

            image = extract_image(item)

            if not image:
                try:
                    image = find_image(item.title)
                except Exception:
                    image = ""

            articles.append({
                "title": getattr(item, "title", ""),
                "link": getattr(item, "link", ""),
                "date": getattr(item, "published", ""),
                "source": source["name"],
                "status": source["status"],
                "image": image
            })

    return articles
