from bs4 import BeautifulSoup 
import requests 
from summarize import getSummary
import datetime
def parseTime(time):
    return time

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}
# listSite = "https://www.bbc.com/news"
# baseURL = "https://www.bbc.com"
# page = requests.get(listSite, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')
# listN = soup.find_all(class_ = "nw-c-top-stories__secondary-item") 

# topNews = []
# for site in listN :
#     heading = site.find('a').h3.text
#     heading = heading.replace('\xa0', ' ').encode('utf-8')
#     link = baseURL + site.find('a')["href"]
#     time = site.find('time')["datetime"]
#     time = parseTime(time)
#     news = {
#         "href": link,
#         "headline": heading,
#         "time": time
#     }
#     topNews.append(news)


def indianExpress(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find(class_ = "full-details")
    timeSoup = soup.find(id_ = "storycenterbyline")
    time = timeSoup.span['content']
    imageSoup = soup.find(class_="custom-caption")
    image = imageSoup.img["src"]
    return []
    # incomplete 


    # Object Model:
    # headline
    # time(in datetime format)
    # keywords(returned from summarizer.py)
    # category(from scraping e.g. finance, tech etc.)
    # body(summary returned from summarizer)
    # url(url to the full article)
    # source(name of media channel e.g times of india, indianExpress etc.)
    # image_url(url for article image, if cannot find one then give some boilerplate image from net corresponding to category)
    # randomly generated id for object(mongo creates one on its own, idk about firebase, please see that..)
    # any other field you can think of