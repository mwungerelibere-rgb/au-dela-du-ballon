brand = "BEYOND THE BALL"


brand = "BEYOND THE BALL"


def create_news(group):

    article = group[0]

    title = article["title"]

    sources = []

    for item in group:
        sources.append(item["source"])

    print("\n🌍", brand)
    print("━━━━━━━━━━━━━━━━━━")

    print("🔥 BREAKING:")
    print(title)

    print("\n📰 Sources:")
    for source in sources:
        print("-", source)

    print("\n📝 Caption:")
    print(
        f"{title}\n\n"
        "Stay updated with football stories beyond the ball.\n"
        "We bring you the facts, analysis, and stories behind the game."
    )

    print("\n📊 Why it matters:")

    why = "This development could influence the football world."

    lower = title.lower()

    if "transfer" in lower or "madrid" in lower or "arsenal" in lower:
        why = (
            "This transfer story could reshape club plans "
            "and influence the transfer market."
        )

    elif "fifa" in lower or "world cup" in lower:
        why = (
            "This FIFA decision could have a major impact on "
            "international football and future competitions."
        )

    elif "injury" in lower or "doping" in lower or "mudryk" in lower:
        why = (
            "This news could affect team selection and "
            "upcoming matches."
        )

    print(why)

    print("\n🎬 Reel Script:")
    print(
        "Breaking football news! "
        "Here is what happened and why it matters. "
        "Follow BEYOND THE BALL for more football updates."
    )

    print("\n#Hashtags:")
    print(
        "#BeyondTheBall #FootballNews "
        "#BreakingNews #Football"
    )


if __name__ == "__main__":

    test_article = {
        "title": "Real Madrid open to Vinicius Jr exit"
    }

    create_news(group)
