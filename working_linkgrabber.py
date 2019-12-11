import requests
from bs4 import BeautifulSoup

url = "https://www.brack.ch/amewi-flugzeug-am38-rtf-979823"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0)'}

html_content = requests.get(url, headers).text
soup = BeautifulSoup(html_content, "lxml")

names = soup.find('title').text
prices = soup.find_all('p', attrs={'class':'productStage__offeredPrice'})

itemList = []
for price in prices:
    itemPrice = price.find('em')['content']
    #itemName = name.find('h1')
    itemList.append((itemPrice))


#<h1 itemprop="name">
print(names + ' ; ' + str(itemList[0]))

print(prices)