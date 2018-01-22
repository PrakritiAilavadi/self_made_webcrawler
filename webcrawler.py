#Topic: Creating a Web Crawler 
#TL;DC: 
#Use:   
import requests
from bs4 import BeautifulSoup
import urllib.request
import random

def down_web(url):
    name = random.randrange(1,1000000)
    full_name = str(name) + ".jpg" 
    urllib.request.urlretrieve(url, full_name)

def trade_spider():
    url = 'https://www.shutterstock.com/search?searchterm=mobile&search_source=base_search_form&language=en&page=1&sort=popular&image_type=all&measurement=px&safe=true'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup_of_site = BeautifulSoup(plain_text, 'html5lib')  #changing from "html5lib"
        
    for link in soup_of_site.find_all('a',{'class':'js_related-item a'}):
        all_links = "https://www.shutterstock.com" + link.get('href')
        print(all_links)
        get_single_item_data(all_links)

def get_single_item_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup_of_item = BeautifulSoup(plain_text, 'html5lib')  #changing from "html5lib"
    for item_name in soup_of_item.find_all('img', {'class': 'img'}):
        all_links = "http:" + item_name.get('src')        
        print(all_links)
        down_web(all_links)
trade_spider()
        





#Downloading images from Unsplash
import requests
from bs4 import BeautifulSoup
import urllib.request
import random

def down_web(url):
    name = random.randrange(1,1000000)
    full_name = str(name) + ".jpg" 
    urllib.request.urlretrieve(url, full_name)

#https://source.unsplash.com/collection/{COLLECTION ID}
#for i in range(50):
#    down_web("https://source.unsplash.com/collection/524823")
#    down_web("https://source.unsplash.com/collection/488437")
    
for i in range(100):
    down_web("https://source.unsplash.com/collection/1044444")







