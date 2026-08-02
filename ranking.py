def calculate_score(title):

    title = title.lower()

    score = 0 
    title = title.lower()
        # Major football organizations
    if "fifa" in title:
        score += 5

    if "uefa" in title:
        score += 5

    if "world cup" in title:
        score += 5

    if "transfer" in title:
        score += 4

    clubs = [
        "real madrid",
        "barcelona",
        "arsenal",
        "chelsea",
        "liverpool",
        "manchester city",
        "manchester united",
        "bayern",
        "psg",
        "juventus",
        "milan",
        "inter"
    ]

    for club in clubs:
        if club in title:
            score += 3

    players = [
        "mbappe",
        "vinicius",
        "haaland",
        "bellingham",
        "yamal",
        "messi",
        "ronaldo",
        "mudryk"
    ]

    for player in players:
        if player in title:
            score += 2

    high_priority = [
        "breaking",
        "transfer",
        "injury",
        "sacked",
        "resign",
        "final",
        "world cup",
        "champions league"
    ]

    medium_priority = [
        "match",
        "goal",
        "player",
        "coach",
        "manager"
    ]

    for word in high_priority:
        if word in title:
            score += 3

    for word in medium_priority:
        if word in title:
            score += 1

    return score



def rank_stories(groups):

    ranked = []

    for group in groups:

        title = group[0]["title"]

        score = calculate_score(title)

        ranked.append({
            "group": group,
            "score": score
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked
