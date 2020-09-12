from bs4 import BeautifulSoup 
import requests 
from summarize import getSummary

def parseTime(time):
    return time

headers = {
    # "Referer": "https://www.financialexpress.com/",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}
listSite = "https://www.financialexpress.com/economy/"

page = requests.get(listSite, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
listN = soup.find_all(class_ = "listitembx") 

topNews = []
for site in listN :
    heading = site.find('h3').a.text
    heading = heading.replace('\xa0', ' ').encode('utf-8')
    link = site.find('h3').a["href"]
    time = site.find(class_ = "minsago").text
    time = parseTime(time)
    news = {
        "href": link,
        "headline": heading,
        "time": time
    }
    topNews.append(news)

listSite = "https://economictimes.indiatimes.com/news/economy"
mainSite = "https://economictimes.indiatimes.com"
page = requests.get(listSite, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
listN = soup.find(class_ = "list1").find_all('li') 

topNews2 = []
for site in listN :
    heading = site.find('a').text
    heading = heading.replace('\xa0', ' ').encode('utf-8')
    link = mainSite + site.find('a')["href"]
    time = site.find('time')['data-time']
    time = parseTime(time)
    news = {
        "href": link,
        "headline": heading,
        "time": time
    }
    topNews2.append(news)


print(topNews2)
