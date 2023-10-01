from requests import get
from time import sleep
from re import compile

URL = "https://api.dane.gov.pl/1.4/search?page=1&per_page=20&sort=-date&model[terms]=dataset&model[terms]=resource&categories[id][terms]=145&format[terms]=csv&lang=pl"

remove_html = compile(r"<[^>]+>")

next_url = URL

number_of_data = 0

def save_item(item):
    link = item["links"]["self"]
    attributes = item["attributes"]
    id = attributes["slug"]
    title = attributes["title"]
    notes = remove_html.sub("", attributes["notes"])
    file_name = f"{id}.txt"
    tags = ", ".join(attributes["keywords"])
    with open(file_name, "w+") as f:
        f.write("\n\n".join([link, tags, title, notes]))

while True:
    r = get(next_url)
    data = r.json()
    for item in data["data"]:
        save_item(item)
        number_of_data += 1
    print(number_of_data)
    next_url = data["links"]["next"]
    sleep(1)

