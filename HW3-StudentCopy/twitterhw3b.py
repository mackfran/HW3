# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References: Amanda McLeod, Colleen's twitter and sentiments code

# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# unique code from Twitter
access_token = "241344659-yFB9FvxHwPSj9sgCY68l6E97wLxC2yGf1Pw0Ukl0"
access_token_secret = "woXcePujVFtkLKdkmUm4Dt1L1roxIhOGHFxeyR7BLlXlM"
consumer_key = "tfJePQmvQLvhV7FYoKgM91AdO"
consumer_secret = "cjzeadvaqAZqQoQrjZxJvJiGTUR95aN9scw76pEE08vEYcamha"

# boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# now we can print and analyze tweets
api = tweepy.API(auth)

# searches for public tweets containing a specified search term
public_tweets = api.search("Barack Obama")

# creates empty lists for the subjectivity and polarity values of these tweets
subjectivity = []
polarity = []

# parses through the public tweets containing the specified search term
for tweet in public_tweets:
	# prints the tweet
	print(tweet.text, '\n')
	analysis = TextBlob(tweet.text)
	# analyzes the tweet and appends its subjectivity and polarity scores to their respective lists
	subjectivity.append(analysis.sentiment.subjectivity)
	polarity.append(analysis.sentiment.polarity)

# calculates the average subjectivity and polarity scores of the results
sub_avg = sum(subjectivity)/len(subjectivity)
pol_avg = sum(polarity)/len(polarity)

# prints these average scores
print("Average subjectivity is " + str(sub_avg))
print("Average polarity is " + str(pol_avg))