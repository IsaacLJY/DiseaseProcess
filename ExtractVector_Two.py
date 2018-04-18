import jieba
from collections import Counter
import tools


#read the disease samples
samples = open("DiseaseSamples.txt", encoding = 'utf-8').read()

#discard certain words, for example, the punctuation



#load user dict
jieba.load_userdict("all_dict.txt")

#use jieba to separate the words
cut = jieba.lcut(samples)







c = Counter(cut).most_common(100)




print(c)