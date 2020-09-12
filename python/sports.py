from bs4 import BeautifulSoup 
import requests 
topSportsNews = []

listSite = "https://timesofindia.indiatimes.com/sports"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = (soup.find(class_ ="top-newslist small").ul.find_all('li'))
for site in listN :
    link = site.find(class_ ="w_tle").a["href"]
    heading = site.find(class_ ="w_tle").text
    news = {
        "href": link,
        "headline": heading
    }
    topSportsNews.append(news)
#print(topSportsNews)

topSportsNews2 = []
listSite = "https://indianexpress.com/section/sports/"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = soup.find(class_ ="nation").find_all(class_ ="articles")
for site in listN:
    link = site.h2.a["href"]
    heading = site.h2.text
    news = {
        "href": link,
        "headline": heading
    }
    print(link)
    topSportsNews2.append(news)