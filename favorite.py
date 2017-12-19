877718115118968832
881103481716781056

for status in tweepy.Cursor(api.home_timeline).items():
	print (status.user)
	
	

import tweepy
import keys



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
	
	
	
stuff = api.user_timeline(user_id= '877718115118968832',count=100,include_rts=False)

for status in tweepy.Cursor(api.user_timeline,id='877718115118968832').items():

##working script to favorite all of CJThomasNHS's tweets
for tweet in api.user_timeline(screen_name = "CJThomasNHS",count=10,include_rts=False):
	idstrtweet = str(tweet.id_str)
	api.create_favorite(idstrtweet)

	
##end script
	

	


for a in stuff.:
	api.create_favorite(a.id)
