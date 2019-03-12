import json
import requests
from bs4 import BeautifulSoup
import functions

with open('input.json', 'r') as file_handle:
    data = json.load(file_handle)


def remove_invalid_links(url, links):
    valid_links = set()
    for link in links:
        is_link = not (link.__contains__("javascript:") or link.startswith("#"))
        is_the_same_domain = link.startswith(url) or link.startswith("/")

        # is_not_file = (not link.__contains__(".")) or link.__contains__(".html") or link.__contains__(".php")
        if is_link and is_the_same_domain and link != url:
            valid_links.add(link)
    return valid_links


def find_links(soup):
    links = []
    for link in soup.findAll('a'):
        try:
            links.append(link["href"])
        except KeyError:
            None
    return links


def get_text_and_links_from(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for script in soup(["script", "style", "header", "footer"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()
    links = find_links(soup)
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text, links


for url in data:
    text, links = get_text_and_links_from(url)
    links = remove_invalid_links(url, links)

    sites = {}
    index = {}
    i = 1
    for link in links:
        print("download site: " + str(i) + "/" + str(len(links)) + " " + link)
        text, _ = get_text_and_links_from(link)
        text = functions.leave_only_words(text)
        sites[link] = text
        index[i] = link
        i += 1

    i = 1
    for link, site in sites.items():
        print("write to file: " + str(i) + "/" + str(len(sites)) + " " + link)
        f = open("sites/" + str(i), 'w+')
        f.write(site)
        f.close()
        i += 1

    f = open("sites/index.json", "w+")
    json.dump(index, f, indent=2)
    f.close()



