from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)

import pymongo

import gensim

from dotenv import load_dotenv
import os
import time

start = time.time()
model = gensim.models.Word2Vec.load("word2vec.zh.300.model")
end = time.time()
print(f"done,total:{ end - start } s")


load_dotenv()
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRECT = os.environ["CHANNEL_SECRECT"]

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRECT)


@app.route("/ricky", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    
    myclient = pymongo.MongoClient("mongodb+srv://jasonyaya:jasonyaya@class.nwopb5x.mongodb.net/")

    # mongodb+srv://jasonyaya:jasonyaya@class.nwopb5x.mongodb.net/%20?retryWrites=true&w=majority

    mydb = myclient["ptt_movie"]

    mycol = mydb["movie"]

    x = event.message.text.split(" ")

    myquery = { "tfidf": { "$in": x } }

    text = ""

    n = 0
    for match in mycol.find(myquery).limit(50) :
        #print(match["title"])
        text = text + '\n'+ str(n) + ' : ' + match["title"] + '\n' + match["link"]
        n += 1

    if len(text) == 0:
        text = "什麼都找不到...QQ"


    line_bot_api.reply_message(
    event.reply_token,
    TextMessage(text=text),
    )

if __name__ == "__main__":
    app.run()