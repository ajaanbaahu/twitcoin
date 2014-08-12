import pymongo
from pymongo import Connection
import numpy as np
import re, cPickle

#from sklearn.naive_bayes import MultinomialNB
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
from text.classifiers import NaiveBayesClassifier
#from sklearn import metrics
#from operator import itemgetter
#from sklearn.metrics import classification_report
import codecs, csv
import nltk, string, os
from nltk.corpus import stopwords
#from sklearn import naive_bayes


f = open('/home/ajaanbaahu/Documents/Projects/fast_classifier.pickle')
NV_classifier =cPickle.load(f)
f.close()
file="/home/ajaanbaahu/Documents/Projects/data.txt"
result_set={}
for lines in open(file):
    tag=NV_classifier.classify(lines)
    if tag not in result_set:	
    	result_set[tag]=1
    result_set[tag]+=1 	

file= open("/home/ajaanbaahu/Documents/Projects/data_result.txt",'a')

#file.write(result_set)

for keys, values in result_set.iteritems():
    file.write("{},{}".format(keys,values)+'\n')
   # keys, values
