from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from firstlesson.first import get_unconverted_bags
from collections import Counter
from math import log

lemmatizer = WordNetLemmatizer()

STOPWORDS = set(stopwords.words('english'))
'''
 Extra object(calculate unigran and bigram)
'''
class Document(object):

    def __init__(self, words, text, *args, **kwargs):
        super(Document, self).__init__()
        lemmatized_words = map(lambda x: lemmatizer.lemmatize(x), words)
        self.words = lemmatized_words
        self.text = text
        self.id = kwargs.get('id', None)

    def unigram(self,):
        self.unigram_counted_words = dict(Counter(self.words))
        self.unigram_count = sum(self.unigram_counted_words.values())

    def calculate_uniqram_counted_words(self,):
        self.unigram()
        return self.unigram_counted_words

    def calculate_uniq_equals(self, string):
        self.text = string
        counted_words, _string = self.get_filtered_counted_words(string, self.unigram_counted_words)
        self.log = reduce(lambda n, x: n + log(x[1] / float(self.unigram_count)), counted_words.items(), float(0))
        return self.log

    def bigram(self,):
        bigram_words = {}
        words = self.words
        for i in range(0, len(self.words) - 1):
            count = bigram_words.get(words[i], {}).get(words[i+1], 0) + 1
            if bigram_words.has_key(words[i]):
                bigram_words.get(words[i]).update({words[i+1]: count})
            else:
                bigram_words.update({words[i] : {words[i+1] : 1}})
        return bigram_words

    def calculate_bigram_counted_words(self,):
        self.bigram_words = self.bigram()
        return self.bigram_words

    def calculate_bigram_equals(self, string):
        self.text = string
        counted_words, _string = self.get_filtered_counted_words(string, self.bigram_words)
        self.log = 0
        for i in range(len(_string) - 1):
            try:
                getter = counted_words.get(_string[i])
                self.log += log(getter.get(_string[i+1]) / float(sum(getter.values())))
            except:
                pass
        return self.log

    def get_filtered_counted_words(self, string, counted_words):
        string = filter(lambda y : y not in STOPWORDS, map(lambda x: lemmatizer.lemmatize(x) ,string.split(' ')))
        return dict(filter(lambda x: x[0] in string, counted_words.items())), string

    def repr_equals(self, obj, string, text = 'UNIGRAM', function_name = 'calculate_uniq_equals'):
        getattr(self, function_name)(string)
        getattr(obj, function_name)(string)
        print '{}\nDocument id:{} \n   Text : \"{}\" - log : {} '.format(text, self.id, self.text, self.log)
        print 'Document id:{} \n   Text : \"{}\" - log : {} \n'.format(obj.id, obj.text, obj.log)

if __name__ == '__main__':
    texts, words = get_unconverted_bags()
    texts_words = zip(texts, words)

    documents = map(lambda x, id: Document(words = x[1], text = x[0], **{'id': id}), texts_words, range(len(texts)))

    counted_words = map(lambda x:  x.calculate_uniqram_counted_words(), documents)
    counted_bigram = map(lambda x: x.calculate_bigram_counted_words(), documents)

    documents[0].repr_equals(documents[1], 'computing with data')
    documents[0].repr_equals(documents[1],'computing with data', '\nBIGRAM', 'calculate_bigram_equals')

