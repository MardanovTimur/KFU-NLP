#coding=utf-8
import io, os, json
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold

import numpy as np
import pandas as pd

classifyer = GaussianNB()
vectorizer = TfidfVectorizer(ngram_range=(0,1))

ALL = 500
TRAIN= (ALL/100) * 80
TEST = ALL - TRAIN

K_cross = 5

precision = recall = fmera = 0

_path = os.path.dirname(__file__)
FILENAME= 'reviews.txt'

def read_pd(file_name=os.path.join(_path, FILENAME)):
    print 'OPEN: {} dataset'.format(file_name)
    return pd.read_json(file_name, lines=True)

if __name__ == '__main__':
    dataset = read_pd()[:ALL]
    #shuffle dataframe
    dataset = dataset.sample(frac=1).reset_index(drop=True)
    DATA = np.array(vectorizer.fit_transform(dataset.text).toarray())

    #Cross validation
    kf = KFold(n_splits=5)
    for train, test in kf.split(dataset):
        classifyer = GaussianNB()
        train_data = dataset.loc[train].copy()
        train_data_data = DATA[train]

        test_data = dataset.loc[test].copy()
        test_data_data = DATA[test]

        classifyer.fit(train_data_data, train_data.positive )
        predicted_data = classifyer.predict(test_data_data)
        TP = sum(map(lambda x, y: 1 if x==y and x else 0, predicted_data, test_data.positive))
        TP_FP = sum(predicted_data)
        TP_FN = sum(test_data.positive)

        precision += TP/float(TP_FP)
        recall += TP/float(TP_FN)
        fmera += 2*precision*recall/(precision + recall)

    #  classifyer.fit(dataset[:TRAIN].data, dataset[:TRAIN].positive)
    #  predicted_data = classifyer.predict(dataset[:-TEST].positive)
    #  TP = sum(map(lambda x, y: 1 if x==y and x else 0, predicted_data, dataset.target[-TEST:]))
    #  TP_FP = sum(predicted_data)
    #  TP_FN = sum(dataset.target[-TEST:])

    #  precision =TP/float(TP_FP)
    #  recall = TP/float(TP_FN)

    print '\bPrecision data: {}'.format(precision/K_cross)
    print '\nRecall data: {}'.format(recall/K_cross)
    print '\nF-mera: {}'.format(fmera/K_cross)

