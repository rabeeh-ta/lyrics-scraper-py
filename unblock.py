"""
this file is for testing the proxy setup and user-agent faking 
"""

import bs4
import re
import requests
from lxml.html import fromstring
from itertools import cycle
from random import choice


# this function will go to the feeproxylist website and scrape the latest available proxies and put them in a list
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = list()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.append(proxy)
    return proxies


proxies = ['1.10.189.126:57959', '81.90.224.248:3128', '118.99.104.13:8080',
           '188.72.82.108:8888', '36.91.41.246:3128', '167.179.4.142:55443']  # get_proxies()
# randomly choosing one proxy from the proxies that we got
proxy = choice(proxies)


url = 'https://www.azlyrics.com/lyrics/justinbieber/holy.html'
lyrics = ''
res = requests.get(url, proxies={"http": proxy, "https": proxy})
soup = bs4.BeautifulSoup(res.text, "lxml")
for lyrics_divs in soup.find_all("div", {"class": None}):
    if len(lyrics_divs.text) == 0:
        print(f"not found ")
        pass
    else:
        lyrics = lyrics + lyrics_divs.text
        print(f"found ")
print("---------------------------------------------------------------")
print(lyrics)
