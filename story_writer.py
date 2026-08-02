def create_story(article):

    title = article.get("title", "")
    category = article.get("category", "⚽ Football News")

    if "FIFA" in category or "UEFA" in category:

        caption = (
            f"{title}\n\n"
            "More than football. The stories behind the game."
        )

        why = (
            "This story could affect FIFA, UEFA, international football and future World Cup decisions."
        )

        script = (
            f"Breaking FIFA and UEFA news! {title}. Here's what happened and why football fans around the world are watching closely."
        )

    elif "Transfer" in category:

        caption = (
            f"{title}\n\n"
            "More than football. The stories behind the game."
        )

        why = (
            "This transfer could strengthen the squad and influence the club's ambitions this season."
        )

        script = (
            f"Transfer update! {title}. Here's everything you need to know."
        )

    elif "Match" in category:

        caption = (
            f"{title}\n\n"
            "More than football. The stories behind the game."
        )

        why = (
            "The result could affect league standings, team confidence and upcoming fixtures."
        )

        script = (
            f"Match report! {title}. Let's look at the key moments and what they mean."
        )

    else:

        caption = (
            f"{title}\n\n"
            "More than football. The stories behind the game."
        )

        why = (
            "This development is important for football supporters around the world."
        )

        script = (
            f"Breaking football news! {title}. Here's what happened and why it matters."
        )

    hashtags = (
        "#BeyondTheBall "
        "#FootballNews "
        "#BreakingNews "
        "#Football"
    )

    article["caption"] = caption
    article["why"] = why
    article["script"] = script
    article["hashtags"] = hashtags

    return article
