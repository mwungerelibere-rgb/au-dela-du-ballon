TRUSTED = [
    "FIFA",
    "UEFA",
    "BBC Sport Football",
    "ESPN FC",
    "Sky Sports Football",
    "The Athletic",
    "Goal",
    "MARCA",
    "L'Équipe",
    "Transfermarkt"
]

OFFICIAL = [
    "FIFA",
    "UEFA"
]


def verify(article):

    source = article["source"]

    if source in OFFICIAL:
        article["verification"] = "🟢 OFFICIAL"

    elif source in TRUSTED:
        article["verification"] = "🔵 TRUSTED"

    else:
        article["verification"] = "🟡 REPORTED"

    return article
