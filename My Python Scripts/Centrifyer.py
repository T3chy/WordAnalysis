from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import tweepy
import re

consumer_key = "wBlchO1ZEiGnv1ly1wmVplNr5"
consumer_secret = "iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"
access_key = "1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"
access_secret = "GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"


# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

        # Printing the tweets
    print(tmp)
bl = Blobber(analyzer=NaiveBayesAnalyzer())
at = input("what's the @?")
print(at)
confirm = input("does this look right? y/n")
while True:
    if confirm == "y":
        print("epic")
        break
    at = input("what's the @?")
    print(at)
    confirm = input("does this look right? y/n")
#get_tweets("realdonaldtrump")
tweet = "ukraine opens inquiry into trump"
tweetb = TextBlob(str(tweet))
print("here's your most recent tweet: " + tweet)
if not str(tweetb) == tweetb.correct():
    print("first of all, let's fix this spelling, shall we?")
    spell = input("y/n")
    if spell == "y":
        corrected = tweetb.correct()
        print("before: " + tweet)
        print("after: " + str(corrected))
        conf = input("does this look right? y/n")
        if conf == "n":
            print("ok, taking the original tweet")
        else:
            tweet = corrected
            tweetb = TextBlob(str(corrected))
    else:
        print("aight lol you do you")
print("lets see how polarizing you are")










