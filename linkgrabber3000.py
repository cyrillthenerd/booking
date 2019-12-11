import requests
from bs4 import BeautifulSoup

url = "https://www.brack.ch/baumarkt-hobby/rc-modellbau/rc-flugzeuge/rc-flugzeug?redirected=1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0)'}

html_content = requests.get(url, headers).text
soup = BeautifulSoup(html_content, "lxml")

names = soup.find('span', attrs={'class': 'productList__itemTitle'}).text

#prices = soup.find_all('em', attrs={'class':'js-currentPriceValue specialOffer'})

#itemList = []
#for item in soup:
#    itemPrice = price.find('span', attrs={'class': 'productList__itemTitle'}.text
    #itemName = name.find('h1')
#    itemList.append((itemPrice))

#itemList = []
#for name in names:
#   itemList.append((name))


#<h1 itemprop="name">
print(names)

