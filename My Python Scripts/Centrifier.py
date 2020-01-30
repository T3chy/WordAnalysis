from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import tweepy
import matplotlib
import re
import json

consumer_key = "wBlchO1ZEiGnv1ly1wmVplNr5"
consumer_secret = "iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"
access_key = "1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"
access_secret = "GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"
numwrong = 0


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
    tweets_for_csv = [[tweet.text, tweet.date/time] for tweet in tweets,]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append([j])

        # Printing the tweets
    print(tmp)
    with open('listfile.txt', 'w') as filehandle:
        for listitem in places:
            filehandle.write('%s\n' % listitem)

bl = Blobber(analyzer=NaiveBayesAnalyzer())
bp = input("use text list? y/n")
if bp == "y":
    with open('listfile.txt') as f:
        tweet1 = f.readline()
else:
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
    try:
        get_tweets(at)
    except Exception as e:
        print("sorry bucko, getting your tweets didn't work out")
        print("The error message is: " + str(e))
    else:
        print("tweets sucessfully gathered! Caching...")
    with open('listfile.txt') as f:
        tweet1 = f.readline()
tweetb = TextBlob(str(tweet1))
print("here's your most recent tweet: " + tweet1)
print('Counting spelling errors, please wait...')
with open('listfile.txt') as f:
        for twt in f:
            tweetb = TextBlob(str(twt))
            if not str(tweetb) == tweetb.correct():
                numwrong = numwrong + 1
if numwrong == 1:
    print("You have about " + str(numwrong) + " spelling error!")
elif numwrong == 0:
    print("You have about " + str(numwrong) + " spelling errors! Congrats!")
else:
    print("You have about " + str(numwrong) + " spelling errors!")
print("Analyzing for polarity...")
polars = []
twtlst = []
with open('listfile.txt') as f:
    for t in f:
        tw = TextBlob(str(t))
        twtlst.append([t.strip('\n'), tw.sentiment.polarity]) #get polarity value added as subitem
        polars.append(tw.sentiment.polarity)
sumnum = 0
for n in polars:
    sumnum = sumnum + n
avgpolar = sumnum / len(polars)
if avgpolar > 0:
    posneg = "positive and "
elif avgpolar < 0:
    posneg = "negative and "
elif avgpolar == 0:
    posneg = "neutral"
if avgpolar == 0:
    polar = ""
elif abs(avgpolar) > 0 and abs(avgpolar) < .2:
    polar = "low!"
elif abs(avgpolar) > .2 and abs(avgpolar) < .4:
    polar = "eh, pretty low!"
elif abs(avgpolar) > .4 and abs(avgpolar) < .6:
    polar = "somewhat high"
elif abs(avgpolar) > .6 and abs(avgpolar) < .8:
    polar = "pretty gosh darn high"
elif abs(avgpolar) > .8:
    polar = "woah there bucko, that's pretty polar"
print("your average polarity is " + posneg + polar)

