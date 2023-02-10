import requests
from bs4 import BeautifulSoup

r = requests.get("https://forum.gamer.com.tw/C.php?bsn=17532&snA=689998&tnum=18")
#print(r.text)


soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
sel = soup.select("div.reply-content span")
print(sel)

#for s in sel:
#    print(s["href"],",", s.text)