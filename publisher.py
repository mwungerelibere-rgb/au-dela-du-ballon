import json


def load_news():

    with open("news.json", "r", encoding="utf-8") as file:
        return json.load(file)


def create_post(article):

    post = f"""
🌍 BEYOND THE BALL

🔥 {article['title']}

🏷 {article['category']}

🔵 {article['verification']}

📰 Source: {article['source']}

📝 {article['caption']}

📊 Why it matters:
{article['why']}

🎬 Reel Script:
{article['script']}

{article['hashtags']}
"""

    return post


def publish():

    news = load_news()

    for article in news:

        post = create_post(article)

        print("-------------------")
        print(post)


if __name__ == "__main__":
    publish()
