import nltk

#read the disease samples txt
dissamples = open("DiseaseSamples.txt", encoding = 'utf-8').read()
tokens = nltk.word_tokenize(dissamples)

pos_tags = nltk.pos_tag(tokens)

print(pos_tags)