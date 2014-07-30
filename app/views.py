from flask import render_template, jsonify, request
from app import app
import tweepy
from mongoengine import *
from models import Tweet
import datetime

connect('test1')#,host='mongodb://heroku:OuchYNmsY66BYCcRMOLEbqZhYf5iWknekhSBZNENGRKd6BoZPSdNbrTrlHF5pUIyYCV1dD3kseANJQMKO4MMNg@kahana.mongohq.com:10012/app27538292')

@app.route('/')
@app.route('/index')
def index():
    ckey='wuWgjIP9ouUWTeo0D3WcF1WZ0'
    csecret='KLjs8izSiuTDkHlOpjlFcrmxaJnQSMTqqckvxvVC2g1RMc5Gwo'
    atoken='615818947-y32PlOKg38iu4hMjcjV42u5fKJzSM1ixbpWoIibb'
    asecret='aDqKj6OlbrwqQ7zAGh8ONgPTn02p0k062zsGppiWJLv3U'

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    public_tweets = api.search('bitcoin')
    #for tweet in public_tweets:
    #	new_tweet = Tweet(text=tweet.text, classification='positive').save()

    user = { 'nickname': 'Ryan' } #fake user
    return render_template("index.html", user=user, tweets=enumerate(public_tweets))

def affin_score(aff_file):
    word_scores={}
    for line in open(aff_file):
        word, score = line.split('\t')
        word_scores[word] = int(score)

    return word_scores

def score_tweet(tweet, word_scores):
  tweet = (tweet)
  score = 0
  try:
    tweet_text = tweet
    for word in tweet_text.split(' '):
      try:
        score += word_scores[word]
      except KeyError:
        pass
    #scored_tweet = Tweet(text=tweet_text, score=score).save()
  except KeyError:
    pass
  return score
#
@app.route('/_classify_tweet')

def classify_tweet():
    file_affin='AFINN-111.txt'
    affin_scores={}
    text = request.args.get('text')
    affin_scores=affin_score(file_affin)
    score_final=score_tweet(text,affin_scores)
    date=str(datetime.datetime.now())
    classification = request.args.get('classification')
    classified_tweet = Tweet(text=text, classification=classification,score=score_final, date=date).save()
    return jsonify(result=1+1)

