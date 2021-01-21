import os
import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup
import re




def get_html_text(url):
    try:
        #kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "crawl error"


if __name__ == '__main__':
    url = "http://www.go4go.net/go/games/record_request"
    new_url = url + '/' + '94668'
    html = get_html_text(new_url)
    soup = BeautifulSoup(html, 'html.parser')

    reg = re.compile('DT')
    tag = soup.find_all(text=reg)
    print(tag)






