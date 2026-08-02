def find_image(title):

    title = title.lower()


    # Players
    if "welbeck" in title:
        return "https://upload.wikimedia.org/wikipedia/commons/9/9c/Danny_Welbeck_2019.jpg"


    if "mbeumo" in title:
        return "https://upload.wikimedia.org/wikipedia/commons/4/4f/Bryan_Mbeumo_2024.jpg"


    if "infantino" in title:
        return "https://upload.wikimedia.org/wikipedia/commons/1/1d/Gianni_Infantino_2023.jpg"


    # Clubs
    if "real madrid" in title or "madrid" in title:
        return "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"


    if "chelsea" in title:
        return "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"


    if "man utd" in title or "manchester united" in title:
        return "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg"


    # Competitions
    if "fifa" in title or "world cup" in title:
        return "https://upload.wikimedia.org/wikipedia/commons/0/03/FIFA_logo.svg"


    if "uefa" in title or "champions league" in title:
        return "https://upload.wikimedia.org/wikipedia/en/f/f5/UEFA_Champions_League_logo_2.svg"


    # Default
    return "https://upload.wikimedia.org/wikipedia/commons/6/6e/Football_iu_1996.jpg"
