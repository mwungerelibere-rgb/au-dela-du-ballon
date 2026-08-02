def normalize_title(title):

    words = title.lower().replace(":", "").split()

    ignore = [
        "the", "a", "an",
        "fifa", "fc",
        "football", "sport"
    ]

    return set(
        word for word in words
        if word not in ignore
    )


def similar_story(title1, title2):

    words1 = normalize_title(title1)
    words2 = normalize_title(title2)

    if not words1 or not words2:
        return False

    score = len(words1.intersection(words2)) / len(words1.union(words2))

    return score >= 0.35


def group_stories(articles):

    groups = []

    for article in articles:

        found = False

        for group in groups:

            if similar_story(
                article["title"],
                group[0]["title"]
            ):
                group.append(article)
                found = True
                break

        if not found:
            groups.append([article])

    return groups
