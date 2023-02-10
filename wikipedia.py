from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Special:Search?go=Go&search=latest+trending+movies+on+hollywood&ns0=1"

sesh = HTMLSession()

data = []


def getpage(url):
    page = sesh.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_data(soup):
    items = soup.find_all("li", class_="mw-search-result mw-search-result-ns-0")
    print("total Items found=", len(items))
    for item in items:
        name = item.find("div", class_="mw-search-result-heading").find("a").text
        desc = item.find("div", class_="searchresult").text
        link = "https://en.wikipedia.org" + str(
            item.find("div", class_="mw-search-result-heading").find("a")["href"]
        )
        dict = {"name": name, "link": link, "description": desc}
        data.append(dict)
    return


def nextpage(soup):
    nextpg = "https://en.wikipedia.org" + str(
        soup.find("a", class_="mw-nextlink")["href"]
    )
    return nextpg


try:
    while True:
        soup = getpage(url)
        get_data(soup)
        url = nextpage(soup)
        print("scraping page-> ", nextpage(soup))
except:
    print("all pages done")


scraped = pd.DataFrame(data)
print(scraped)
# scraped.to_json("wikipedia-scraping.json")
# scraped.to_csv("wikipedia-scraping.csv", index=False)
