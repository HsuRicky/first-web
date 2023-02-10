import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
#print(r.text)


soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
sel = soup.select("div.meta a")
print(sel)

for s in sel:
    print(s["href"]," : ", s.text)