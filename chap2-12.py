import requests
from pathlib import Path

#保存用フォルダを作る
#現在のディレクトリに作られる
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

image_url = "http://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

#URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1]

#download(フォルダ)にアクセスするためにjoinpath()を使う
out_path = out_folder.joinpath(filename)

#画像なのでバイナリーモードでファイルに書き出す
with open(out_path,"wb") as f:
    f.write(imgdata.content)
