# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# Sources:
	## http://stackoverflow.com/questions/19337672/post-tweet-with-tweepy
	## http://docs.tweepy.org/en/v3.5.0/api.html

import tweepy

# Unique code from Twitter
access_token = "241344659-yFB9FvxHwPSj9sgCY68l6E97wLxC2yGf1Pw0Ukl0"
access_token_secret = "woXcePujVFtkLKdkmUm4Dt1L1roxIhOGHFxeyR7BLlXlM"
consumer_key = "tfJePQmvQLvhV7FYoKgM91AdO"
consumer_secret = "cjzeadvaqAZqQoQrjZxJvJiGTUR95aN9scw76pEE08vEYcamha"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

try:
	api.update_with_media(filename='UofM.jpg', status='#UMSI-206 #Proj3')
	print("Success!")
except:
	print("Error")