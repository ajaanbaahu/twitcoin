import pymongo
import mongoengine
from pymongo import Connection
from collections import Counter
import pandas as pd
from collections import OrderedDict
import pandas as pd
from operator import itemgetter
from generate_time_series import generate_series
server = 'localhost'
port = 27017
dbs = 'twitter_db'
collection = 'tweet'
conn = Connection(server)
db = conn[dbs]
poling = db.tweet.find().limit(10000)
file = open('time_data.txt', 'a')
collect_tweet = {}


def pre_process(query):
    result = []
    for items in query:
        data = items['date'].split(' ')
        text = items['classification']
        day = data[0]
        time = data[1].split(':')[0]
        result.append('{0} {1} {2}'.format(day, time, text))

    return result



def flatten(d):
    series = []
    for (k, v,) in sorted(d.items(), key=itemgetter(0)):
        if isinstance(v, dict):
            for (key, val,) in sorted(v.items(), key=itemgetter(0)):
                series.append([k, key, val])


    return series


for line in pre_process(poling):
    (date, time, tag,) = line.split()
    if date not in collect_tweet:
        collect_tweet[date] = {}
    if time not in collect_tweet[date]:
        collect_tweet[date][time] = {}
    if tag not in collect_tweet[date][time]:
        collect_tweet[date][time][tag] = 1
    else:
        collect_tweet[date][time][tag] += 1

dict_data = flatten(collect_tweet)
conn.close()

mongoengine.Connection('testSeries')

for keys in dict_data:
    generate_series(Day=keys[0],hour=keys[1],counts=keys[2]).save()
    


