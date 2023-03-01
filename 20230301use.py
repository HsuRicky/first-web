import gensim

import pymongo
import time


def gen():
    model = gensim.models.Word2Vec.load("word2vec.zh.300.model")


    #print(model.wv.vectors.shape)

    #print(model.wv.vectors)


    #print(model.wv.most_similar("數學")) #尋找"關鍵字"最相關前10的詞語

    #words = list(model.wv.index_to_key) #將上面的多list改成一維
    #print(f"總共收錄了 {len(words)} 個詞彙") #印出總共有多少詞彙

    #print("印出 20 個收錄詞彙:")
    #print(words[:10]) #印出前10個收錄詞彙

    '''
    word = "Jason蕭" #尋找"word"這個詞彙是否有被收錄
    try:
        vec = model.wv[word]
    except KeyError as e:
        print(e)
    '''    
    
    #print("Result:")
    #print(model.wv.most_similar("周杰倫", topn=10))

    print("Result:")
    try:
        print(model.wv.similarity("周杰倫", "鄧紫棋")) #尋找兩個"關鍵字"的關聯程度
    except KeyError as e:
        print(e)

gen()