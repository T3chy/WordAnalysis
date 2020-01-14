from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import twitter
import re
api = twitter.Api(consumer_key=["wBlchO1ZEiGnv1ly1wmVplNr5"],
                  consumer_secret=["iyHcmJITDblWRf4Zj46r19UVbngnU8DoXkBoXCtchZpZ7kF6HT"],
                  access_token_key=["1214224530341629952-RpXwF26MvZ0KEBJTcYzwEhKHgE4vQx"],
                  access_token_secret=["GTa4it7WQ4pXnvu1klWlFnbMFfUSVVBw8gvu0sipWGeD7"])
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
tweet = "standd in statement"
tweetb = TextBlob(str(tweet))
print(tweetb)
print("first of all, let's fix this spelling, shall we?")
spell = input("y/n")
if spell == "y":
    corrected = tweetb.correct()
    print("before: " + tweet)
print("after: " + str(corrected))



