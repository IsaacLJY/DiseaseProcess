import jieba
import jieba.posseg
import jieba.analyse
from collections import Counter
import re

def vocaFre(input):
    """
    method 1
    use vocabulary frequency
    :param input: string, sentences to cut
    :return: list, words
    """
    cut = jieba.lcut(input)
    counter = Counter(cut)
    num = len(counter)
    clow = counter.most_common(int(num/3))
    chigh = counter.most_common(int(num*2/3))
    result = []
    for w in chigh:
        if w not in clow:
            result.append(w[0])
    print("vocabulary frequency: ", result)
    return result

def vocaType(input):
    """
    method 2
    use vocabulary type
    only noun is usefull
    :param input: string, sentences to cut
    :return: list, words
    """

    result = []
    words = jieba.posseg.lcut(input)
    for word in words:
        if word.flag == 'n':
            result.append(word.word)
    print("vocabulary type: ", result)
    return result

def diffTxt(input):
    """
    method 3
    use difference of different txt
    :param input: string, sentences to cut
    :return: list, words
    """

    consamples = open("ContrastSamples.txt", encoding='utf-8').read()

    # use jieba to separate the words into sets
    discut = set(jieba.lcut(input))
    concut = set(jieba.lcut(consamples))

    # get disease features from set difference
    res = discut.difference(concut)

    result = list(res)
    print("difference of different txt: ", result)
    return result


def tfidf(input):
    """
    method 4
    use tf-idf
    :param input: string, sentences to cut
    :return: list, words
    """
    cut = jieba.lcut(input)
    counter = Counter(cut)
    num = len(counter)
    result = jieba.analyse.extract_tags(input, int(num/3))
    print("tf-idf results: ",result)
    return result

def removeNumAlphaSingle(words):
    """
    remove all words which contains number and alpha;
    remove all single word
    :param words:
    :return:
    """
    result = []
    for w in words:
        if not (hasNum(w) or hasAlpha(w) or isSingle(w)):
            result.append(w)

    return result


def hasNum(word):
    """
    whether word contains a number
    :param word: sting
    :return: bool
    """
    return bool(re.search(r'\d', word))

def hasAlpha(word):
    """
    whether word contains an alpha
    :param word: string
    :return: bool
    """
    if bool(re.search(r'[a-z]+', word)) or bool(re.search(r'[A-Z]+', word)):
        return True
    else:
        return False

def isSingle(word):
    if len(word) == 1:
        return True
    else:
        return False

def addFeatures(features, extra):
    """
    extend features with necessary vocabulary
    :param features: list, old features
    :param extra: list, extra features
    :return: list, features + extra
    """
    return features + extra



#read the disease samples and get target string
targetStr = ""
with open("DiseaseSamples.txt", encoding = 'utf-8') as f:
    for line in f:
        if "现病史" in line:
            line.replace("现病史", "")
            targetStr += line


#load user dict
jieba.load_userdict("all_dict.txt")

freFactor = 1
wordsFre = removeNumAlphaSingle(vocaFre(targetStr))
typeFactor = 3
wordsType = removeNumAlphaSingle(vocaType(targetStr))
txtFactor = 1
wordsTxt = removeNumAlphaSingle(diffTxt(targetStr))
tfidfFactor = 1
wordstfidf = removeNumAlphaSingle(tfidf(targetStr))

roughFeatures = dict()

for w in wordsFre:
    if w not in roughFeatures:
        roughFeatures[w] = 0
    roughFeatures[w] = roughFeatures[w] + freFactor
for w in wordsType:
    if w not in roughFeatures:
        roughFeatures[w] = 0
    roughFeatures[w] = roughFeatures[w] + typeFactor
for w in wordsTxt:
    if w not in roughFeatures:
        roughFeatures[w] = 0
    roughFeatures[w] = roughFeatures[w] + txtFactor
for w in wordstfidf:
    if w not in roughFeatures:
        roughFeatures[w] = 0
    roughFeatures[w] = roughFeatures[w] + tfidfFactor

#form the final features
filter_cluster = open("all_dict_utf8.txt", encoding="utf-8").read()
filter_abandon = open("filter_abandon.txt", encoding="utf-8").read()
features = []
for w in roughFeatures:
    if roughFeatures[w] > 3 and w in filter_cluster and w not in filter_abandon:
        features.append(w)
print(features)

