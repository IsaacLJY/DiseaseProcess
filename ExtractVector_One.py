
import jieba
import jieba.analyse
import jieba.posseg
from collections import Counter
import tools

#read the disease samples and contrast txt
dissamples = open("DiseaseSamples.txt", encoding = 'utf-8').read()
consamples = open("ContrastSamples.txt", encoding = 'utf-8').read()

#load user dict
jieba.load_userdict("all_dict.txt")

#use jieba to separate the words into sets
discut = set(jieba.lcut(dissamples))
concut = set(jieba.lcut(consamples))

#get disease features from set difference
res = discut.difference(concut)

result = set()
#remove numbers
for item in res:
    if tools.is_number(item):
       continue
    else:
        result.add(item)

print(result)

#use tf-idf
result = jieba.analyse.extract_tags(dissamples, 100)
print(result)

#vocabulary type tag
words = jieba.posseg.cut(dissamples)
for w in words:
    print(w.word, w.flag)


# cut = jieba.cut(dissamples)
# c = Counter(cut).most_common(2000)
#
# print(c)
# print(len(cut))
# ad = jieba.lcut(s)
# print(ad)
#
# #difference() 计算2个集合的差集
# dreamers = {'ljl','wc','xy','zb','lsy'}
# girls = {'mmf','lsy','syj'}
# result = dreamers.difference(girls)# result = a + b
# print(result)
