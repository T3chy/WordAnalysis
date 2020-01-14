from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import re
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
tweetb = TextBlob(str("peepee poopoo"))
print(tweetb)
print("first of all, let's fix this spelling, shall we?")
spell = input("y/n")
if spell == "y":
    corrected = tweetb.correct()
    print("before: " + tweet)
print("after: " + corrected)



