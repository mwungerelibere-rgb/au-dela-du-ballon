def classify_news(title):

    title = title.lower()

    breaking_words = [
        "official",
        "confirmed",
        "signs",
        "sacked",
        "resigns",
        "announced"
    ]

    rumor_words = [
        "linked",
        "interest",
        "could",
        "possible",
        "sources"
    ]

    for word in breaking_words:
        if word in title:
            return "🚨 CONFIRMED NEWS"

    for word in rumor_words:
        if word in title:
            return "🟡 REPORT / RUMOR"

    return "📰 FOOTBALL UPDATE"

