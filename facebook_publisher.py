import requests
import json
import os


PAGE_ID = "YOUR_PAGE_ID"
ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"


def publish_to_facebook(article):

    message = f"""
🔥 {article['title']}

🏷 {article.get('category','Football News')}

📰 Source: {article['source']}

📝 {article.get('caption','')}

📊 Why it matters:
{article.get('why','')}

🎬 Reel Script:
{article.get('script','')}

{article.get('hashtags','')}
"""


    url = f"https://graph.facebook.com/{PAGE_ID}/feed"


    data = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }


    response = requests.post(url, data=data)


    return response.json()



if __name__ == "__main__":

    with open("news.json", "r") as file:
        news = json.load(file)


    if news:

        result = publish_to_facebook(news[0])

        print(result)
