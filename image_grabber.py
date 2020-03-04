from bs4 import BeautifulSoup
import requests
url = 'https://www.mozzism.ch'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
image_tags = soup.findAll('script')
# print out image urls
for image_tag in image_tags:
    print(image_tag.get('src'))