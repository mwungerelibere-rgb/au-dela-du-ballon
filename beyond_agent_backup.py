from writer import create_news
from export_news import export_stories
from ranking import rank_stories
from newsroom import group_stories
from news_collector import collect_news
from verify import verify


def load_posted_news():
    try:
        with open("posted_news.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_posted_news(news):
    with open("posted_news.txt", "a") as file:
        file.write(news + "\n")


def is_football_news(title):

    title = title.lower()

    blocked = [
        "800m",
        "athletics",
        "boxing",
        "rugby",
        "horse racing",
        "goodwood",
        "commonwealth games"
    ]

    for word in blocked:
        if word in title:
            return False

    keywords = [
        "football",
        "soccer",
        "fifa",
        "uefa",
        "transfer",
        "premier league",
        "champions league",
        "europa league",
        "world cup",
        "goal",
        "striker",
        "midfielder",
        "defender",
        "goalkeeper",
        "arsenal",
        "chelsea",
        "liverpool",
        "manchester united",
        "manchester city",
        "barcelona",
        "real madrid",
        "psg"
    ]

    for word in keywords:
        if word in title:
            return True

    return False


if __name__ == "__main__":

    news = collect_news()

    news_groups = group_stories(news)

    ranked_news = rank_stories(news_groups)

    print("Collected:", len(news))
    print("Groups:", len(news_groups))


    # Export top 5 stories
    stories_to_export = []

    for item in ranked_news[:5]:

        article = verify(item["group"][0])

        stories_to_export.append(
            (
                article,
                item["score"]
            )
        )

    export_stories(stories_to_export)


    posted = load_posted_news()


    for item in ranked_news[:5]:

        score = item["score"]

        print("\n⭐ PRIORITY:", score)

        article = verify(item["group"][0])

        title = article["title"]

        print(
            "CHECK:",
            title,
            is_football_news(title),
            title in posted
        )


        if title not in posted and is_football_news(title):

            print("\n🌍 BEYOND THE BALL")
            print("-------------------")

            print(article["verification"])

            create_news(item["group"])

            save_posted_news(title)
