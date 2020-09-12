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
topNews = []
listSite = "https://indianexpress.com/section/technology/"
page = requests.get(listSite, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser') 

# print(soup)
listN = soup.find(class_ = "top-article").ul.find_all('li')

for site in listN:
    link = site.h3.a["href"]
    heading = site.h3.a.text
    news = {
        "href": link,
        "headline": heading
    }
    # print(link)
    topNews.append(news)

print(topNews)