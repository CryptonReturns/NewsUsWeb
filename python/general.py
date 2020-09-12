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
listSite = "https://timesofindia.indiatimes.com"
baseURL = "https://timesofindia.indiatimes.com"
page = requests.get(listSite, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
listN = soup.find(class_ = "list9").find_all('li') 

topNews = []
for site in listN :
    print(site)
    try:
        heading = site.find('a').text
        heading = heading.replace('\xa0', ' ').encode('utf-8')
        link = baseURL + site.a["href"]
        news = {
            "href": link,
            "headline": heading,
            # "time": time
        }
        topNews.append(news)
    except:
        print("Non list item ")

print(topNews)