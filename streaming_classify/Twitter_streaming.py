import time, tweepy, sys,json,re

## authentication
ckey='wuWgjIP9ouUWTeo0D3WcF1WZ0'
csecret='KLjs8izSiuTDkHlOpjlFcrmxaJnQSMTqqckvxvVC2g1RMc5Gwo'
atoken='615818947-y32PlOKg38iu4hMjcjV42u5fKJzSM1ixbpWoIibb'
asecret='aDqKj6OlbrwqQ7zAGh8ONgPTn02p0k062zsGppiWJLv3U'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api= tweepy.API(auth)

public_tweets = api.search('bitcoin',count=1000)

file=open("/home/ajaanbaahu/Documents/Projects/data.txt",'w')
for tuples in public_tweets:
        body=''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tuples.text))
	file.write(body+'\n')


