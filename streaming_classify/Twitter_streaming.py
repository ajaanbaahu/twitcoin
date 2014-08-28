import time, tweepy, sys,json,re

### authentication
ckey=''
csecret=''
atoken=''
asecret=''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api= tweepy.API(auth)

public_tweets = api.search('bitcoin',count=1000)

file=open("/home/ubuntu/Projects/twitcoin/streaming_classify/data.txt",'w')
for tuples in public_tweets:
        body=''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tuples.text))
	file.write(body+'\n')


