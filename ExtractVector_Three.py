import nltk
from textblob import TextBlob

#read the disease samples txt
dissamples = open("DiseaseSamples.txt", encoding = 'utf-8').read()
tokens = nltk.word_tokenize(dissamples)

pos_tags = nltk.pos_tag(tokens)

print(pos_tags)


dissamples = open("DiseaseSamples.txt", encoding = 'utf-8').read()
blob = TextBlob(dissamples)
print(blob.noun_phrases)
