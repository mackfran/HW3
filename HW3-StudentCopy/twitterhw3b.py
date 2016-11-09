# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

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

public_tweets = api.search("Donald Trump")

subjectivity = []
polarity = []

for tweet in public_tweets:
	print(tweet.text, '\n')
	analysis = TextBlob(tweet.text)
	subjectivity.append(analysis.sentiment.subjectivity)
	polarity.append(analysis.sentiment.polarity)

sub_avg = sum(subjectivity)/len(subjectivity)
pol_avg = sum(polarity)/len(polarity)

print("Average subjectivity is " + str(sub_avg))
print("Average polarity is " + str(pol_avg))