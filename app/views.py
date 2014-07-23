from flask import render_template, jsonify, request	
from app import app
import tweepy
from mongoengine import *
from models import Tweet

connect('test1',host='mongodb://kahana.mongohq.com:10012/app27538292')

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


@app.route('/_classify_tweet')
def classify_tweet():
	text = request.args.get('text')
 	classification = request.args.get('classification')
 	classified_tweet = Tweet(text=text, classification=classification).save()
 	return jsonify(result=1+1)
