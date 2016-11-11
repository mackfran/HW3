# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References: Amanda McLeod, Colleen's twitter code
#             Internet sources (listed above the code for the part they were used for)

# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# Sources:
	## http://stackoverflow.com/questions/19337672/post-tweet-with-tweepy
	## http://docs.tweepy.org/en/v3.5.0/api.html

import tweepy

# unique code from Twitter
access_token = "241344659-yFB9FvxHwPSj9sgCY68l6E97wLxC2yGf1Pw0Ukl0"
access_token_secret = "woXcePujVFtkLKdkmUm4Dt1L1roxIhOGHFxeyR7BLlXlM"
consumer_key = "tfJePQmvQLvhV7FYoKgM91AdO"
consumer_secret = "cjzeadvaqAZqQoQrjZxJvJiGTUR95aN9scw76pEE08vEYcamha"

# boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# now we can create tweets
api = tweepy.API(auth)

try:
	# updates Twitter status with text and an image
	api.update_with_media(filename='UofM.jpg', status='#UMSI-206 #Proj3')
	print("Success!")
except:
	print("Error")