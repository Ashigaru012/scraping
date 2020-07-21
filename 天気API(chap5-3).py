import requests
import json

#現在の天気を取得する
url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang = ja & units = metric"
url = url.format(city="kobe,JP",key="80b25d623c385b7a0d55270dd2759e11")

jsondata = requests.get(url).json()
print(jsondata)
