import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#ファイルを書き込みモードで開く
filename = "linklist.txt"
with open(filename,"w") as f:#fとしてファイルを開く
    #すべてのaタグを検索し、リンクを絶対URLで書き出す
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url,url)
        f.write(element.text + "\n")
        f.write(link_url + "\n")
