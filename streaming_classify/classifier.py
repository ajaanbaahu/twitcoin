from mongoengine import *
import re, cPickle
import datetime
from models import Tweet
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
from text.classifiers import NaiveBayesClassifier
#from sklearn import metrics
#from operator import itemgetter
#from sklearn.metrics import classification_report
import codecs, csv
#import nltk, string, os
#from nltk.corpus import stopwords
#from sklearn import naive_bayes

connect('twitter_db',host='127.0.0.1')


f = open('/home/ubuntu/Projects/twitcoin/streaming_classify/fast_classifier.pickle')
NV_classifier =cPickle.load(f)
f.close()
file="/home/ubuntu/Projects/twitcoin/streaming_classify/data.txt"
result_set={}
for lines in open(file):
    tag=NV_classifier.classify(lines)
    Tweet(text=lines,classification=tag,date=str(datetime.datetime.now())).save()
