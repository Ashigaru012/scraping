import requests
from bs4 import BeautifulSoup
import urllib
import time
from pathlib import Path

load_url = "http://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")
#href属性は
for element in soup.find_all("img"):
    src = element.get("src")#src属性はHTMLに埋め込むファイルのパス情報

    image_url = urllib.parse.urljoin(load_url,src)
    filename = image_url.split("/")[-1]
    print(image_url,">>",filename)
