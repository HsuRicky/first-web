import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
#print(r.text)

soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
#print(soup)
sel = soup.select("div.title a")
#print(sel)

for s in sel:
    print(s["href"],"", s.text)