from urllib import urlopen
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, Text, RegexpTokenizer, TextCollection
from bs4 import BeautifulSoup
import math

URLS = [
    "https://en.wikipedia.org/wiki/Data_science",
    'https://en.wikipedia.org/wiki/Machine_learning',
]

STOPWORDS = set(stopwords.words('english'))

TF= []
IDF=[]
TF_IDF= []

def get_tf(words):
    atu = {}
    len_words = len(words)
    map(lambda x: atu.update({x: atu.get(x, 0) + 1}), words)
    atu = dict(map(lambda x: (x[0], x[1]/float(len_words)), atu.items()))
    return sorted(atu.items(), key=lambda x: x[0], reverse=True)

contains = lambda word, texts: sum(map(lambda text: 1 if word in text else 0 ,texts))

def get_idf(_words_, texts, N):
    atu = {}
    map(lambda x: atu.update({x: math.log10(N/float(contains(x, texts)))}) , _words_)
    return sorted(atu.items(), key=lambda x: x[0], reverse=True)


remove_stopwords = lambda words : filter(lambda x: x not in STOPWORDS, words)
lower_case = lambda words : map(lambda x : x.lower(),words)

def get_unconverted_bags():
    toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    toker1 = RegexpTokenizer(r'\W+', gaps=True)
    tetxs_untokenized = map(lambda x: toker.tokenize(BeautifulSoup(urlopen(x).read().decode('utf-8')).get_text()), URLS)
    new_texts = map(lambda e : reduce(lambda x, y: x+y , e).lower(), tetxs_untokenized)
    tetxs_untokenized = map(lambda s : toker1.tokenize(s), new_texts)
    tetxs_untokenized = map(lambda x: remove_stopwords(x), tetxs_untokenized)
    return new_texts, tetxs_untokenized



if __name__ == '__main__':
    texts, words = get_unconverted_bags()
    N = len(URLS)
    TF =  map(lambda x: get_tf(x), words)
    IDF = map(lambda x: get_idf(x, texts, N), words)
    print TF
    print '------------------------------\n--------------\n'
    print IDF
    TF_IDF = map(lambda x,y: map(lambda x1, y1:(x1[0],x1[1]*y1[1]) ,x,y) ,TF,IDF)
    print '----------------------------\n-------------------\n'
    print sorted(TF_IDF[0], key=lambda x : x[1], reverse=True)

