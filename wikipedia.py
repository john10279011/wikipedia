from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Special:Search?go=Go&search=latest+trending+movies+on+hollywood&ns0=1"

sesh = HTMLSession()

page = BeautifulSoup(sesh.get(url).content, "html.parser")


def getpage(url):
    page = sesh.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_data(soup):
    items = page.find_all("li", class_="mw-search-result mw-search-result-ns-0")
    print("total Items =", len(items))
    for item in items:
        name = item.find("div", class_="mw-search-result-heading").find("a").text
        desc = item.find("div", class_="searchresult").text
        link = "https://en.wikipedia.org" + str(
            item.find("div", class_="mw-search-result-heading").find("a")["href"]
        )

        return name


soup = getpage(url)
print(get_data(soup))
