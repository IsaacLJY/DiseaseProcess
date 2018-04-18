


#encoding=utf-8

import jieba.posseg

a = '我'
b = "我"
print(len(a))
print(len(b))

c = "，dj.d,@"
print(jieba.posseg.lcut(c))