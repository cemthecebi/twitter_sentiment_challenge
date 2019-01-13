import tweepy
from textblob import TextBlob
import csv 

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search("Trump")



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

with open("twitter_sentiments.csv" ,"a") as csvFile:
    writer = csv.writer(csvFile)
    for tweet in public_tweets:
        #print(tweet.text)
        #Step 4 Perform Sentiment Analysis on Tweets

        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity < 0:  
            sentiment = " Negative"
        else:
            sentiment = " Positive"
        list_tweet = [tweet.text,sentiment]
        
        writer.writerow(list_tweet)

csvFile.close
