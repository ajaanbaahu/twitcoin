import pymongo
from pymongo import Connection
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from text.classifiers import NaiveBayesClassifier
from sklearn import metrics
from operator import itemgetter
from sklearn.metrics import classification_report
import codecs, csv
import nltk, string, os
from nltk.corpus import stopwords
from sklearn import naive_bayes

from collections import Counter

server="localhost"
port = 27017
#Establish a connection with mongo instance.
conn = Connection(server,port)
db=conn['test1']

result= db.tweet.find()
data=[]
for tuples in result:
    data.append(((unicode(tuples['text']), unicode(tuples['classification']))))

cl=NaiveBayesClassifier(data)
str='terrible'


print cl.classify(str)



# print(cl.classify(test)) # "pos"
# print(cl.classify("don't take that medicine."))
