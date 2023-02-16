import requests
from bs4 import BeautifulSoup
import sys
import pymongo

article = []
error = []
last_page_link = ""
time = 0

if int(sys.argv[1]) > 5000 :
    time = 5000
else :
    time = int(sys.argv[1])

def capData() :
    r = requests.get("https://www.ptt.cc/bbs/Steam/index.html")
    
    global time
    while time > 0:
        
        soup = BeautifulSoup(r.text,"html.parser")
        index_soup = soup.select("div.title a")

        last_page_soup = soup.select("a.btn")


        for l in last_page_soup:
            if "‹ 上頁" == l.text:
                last_page_link = l["href"]
                

        try:
            for i in index_soup:
                r = requests.get("https://www.ptt.cc"+i["href"])
                
                soup = BeautifulSoup(r.text,"html.parser")
                #print(soup)
                article_soup = soup.select("div#main-content")

                article.append({ "html" : str(article_soup), "link" : i["href"] })
                #print(article_soup)
        except:
            error.append("https://www.ptt.cc"+i["href"])


        r = requests.get("https://www.ptt.cc"+last_page_link)
        time -= 1
        print(time)
        #print(len(article_link))

def saveToDB() :
    myclient = pymongo.MongoClient("mongodb+srv://jasonyaya:jasonyaya@cluster0.rjbp5vy.mongodb.net")

    mydb = myclient["ptt_Ricky"]

    mycol = mydb["steam"]
    
    mycol.insert_many(article)

def main() :
    capData()
    saveToDB()
    print(error)
    print("Total article : " + str(len(article)))
    
if __name__ == '__main__':
    main()
