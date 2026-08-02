import json
import os


ARCHIVE_FILE = "archive.json"


def load_archive():

    if not os.path.exists(ARCHIVE_FILE):
        return []

    with open(ARCHIVE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)



def save_archive(story):

    archive = load_archive()

    titles = [
        item["title"]
        for item in archive
    ]


    if story["title"] not in titles:

        archive.append(story)


    with open(
        ARCHIVE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            archive,
            file,
            indent=4,
            ensure_ascii=False
        )



def archive_news(news):

    for story in news:
        save_archive(story)
