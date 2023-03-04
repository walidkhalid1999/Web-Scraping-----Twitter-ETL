import pandas as pd
import tweepy
import s3fs
import json
from datetime import datetime


def run_twitter_etl():

    access_key= "  "
    access_secret= "  "
    consumer_key= "   "
    consumer_secret= "   "
    
    #step1: make a connection between a code and the twitter APIs
    #twitter authentication
    auth=tweepy.OAuthhandler(access_key , access_secret)
    auth.set_access_token(consumer_key , consumer_secret)  
    
    #create an API object
    api=tweepy.API(auth)
    
    
    #to get information about partical user
    tweets =api.user_timeline(
        screen_name='@profile_name',
        #number of tweets you want to extract
        count=200,
        #necessary to keep full text 
        #otherwise only the first 140 words are extended
        tweet_mode='extended'
        )
    
    
    #make a looping on each tweet and extracting data from it 
    tweet_list=[]
    for tweet in tweets:
        text = tweet.__json["full_text"]
        refined_tweet= {
            "user" : tweet.user.screen_name,
            "text" : text,
            "favourite_count" : tweet.favourite_count,
            "retweet_count" : tweet.retweet_count,
            "created_at" : tweet.created_at
             }
        tweet_list.append(refined_tweet)
        
    #make a DataFrame
    df=pd.DataFrame(tweet_list)
    df.to_csv("elonmusk_twitter_data.csv")



























