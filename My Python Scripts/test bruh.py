from textblob import TextBlob
import nltk
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import re
bl = Blobber(analyzer=NaiveBayesAnalyzer())
input = TextBlob(input("prompt"))
sentiment = input.sentiment

