from writer import create_news
from export_news import export_story
from ranking import rank_stories
from newsroom import group_stories
from news_collector import collect_news
from verify import verify
from category import get_category
from story_writer import create_story
from archive_manager import archive_news


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
        "athletics",
        "boxing",
        "rugby",
        "horse racing",
        "tennis"
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
        "world cup",
        "goal",
        "striker",
        "midfielder",
        "defender",
        "goalkeeper",
        "arsenal",
        "chelsea",
        "liverpool",
        "manchester",
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


    posted = load_posted_news()


    for item in ranked_news[:5]:

        score = item["score"]

        article = item["group"][0]


        article = verify(article)


        article["category"] = get_category(
            article["title"]
        )


        article = create_story(article)


        title = article["title"]


        print("\n⭐ PRIORITY:", score)

        print(
            "🏷 CATEGORY:",
            article["category"]
        )


        print(
            "CHECK:",
            title,
            is_football_news(title),
            title in posted
        )


        if title not in posted and is_football_news(title):


            print("\n🌍 BEYOND THE BALL")
            print("-------------------")


            print(article["category"])

            print(article["verification"])


            # SAVE TO NEWS.JSON
            export_story(
                article,
                score
            )


            create_news(
                [article]
            )


            archive_news(
                [article]
            )


            save_posted_news(
                title
            )
