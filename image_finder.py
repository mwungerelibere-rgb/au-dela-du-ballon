def find_image(title):

    title = title.lower()


    football_image = "https://images.unsplash.com/photo-1579952363873-27d3bfad9b0c"


    if "fifa" in title or "world cup" in title:
        return football_image


    if "uefa" in title or "champions league" in title:
        return football_image


    if "real madrid" in title or "madrid" in title:
        return football_image


    if "chelsea" in title:
        return football_image


    if "liverpool" in title:
        return football_image


    if "arsenal" in title:
        return football_image


    if "manchester" in title:
        return football_image


    if "salah" in title:
        return football_image


    if "vinicius" in title or "viní" in title:
        return football_image


    return football_image
