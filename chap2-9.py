#指定したページからURL一覧を取得するプログラム
import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")

    #相対パスを絶対パスに変換する
    link_url = urllib.parse.urljoin(load_url,url)
    print(link_url)
