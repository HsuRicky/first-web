import gensim



model = gensim.models.Word2Vec.load("word2vec.zh.300.model")


print(model.wv.vectors.shape)

print(model.wv.vectors)


print(model.wv.most_similar("數學"))

words = list(model.wv.index_to_key)

print(f"總共收錄了 {len(words)} 個詞彙")

print("印出 20 個收錄詞彙:")
print(words[:10])


word = "Jason蕭"

try:
    vec = model.wv[word]
except KeyError as e:
    print(e)
    
    
print(model.wv.most_similar("漫威", topn=10))


print(model.wv.similarity("美國隊長", "漫威"))