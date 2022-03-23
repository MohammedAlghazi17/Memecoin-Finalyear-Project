from csv import writer
import csv
from sched import scheduler
from typing import Collection
import tweepy 
import configparser
import pandas as pd
import requests
import schedule
import time
from datetime import date

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#user tweets
#user = '@cex_io'
#limit=1000

#tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
csvheader =['User','Tweet']
#search tweets
keywords = 'dogelon'
limit=1000
tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)



# create DataFrame
columns = ['Date', 'User', 'Tweet']
data = []
today = str(date.today())
for tweet in tweets:
    # Get today#s date
    
     data.append([today, tweet.user.screen_name, tweet.full_text])

   # data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
#with open('twitter-doge-shib-data.csv','w',encoding='UTF8', newline='') as f:
 #   writer = csv.writer(f)
  #  writer.writerow(csvheader)
   # writer.writerows(tweets)


print(df)
df.to_csv('elon' + today + '.csv')
df.to_csv('data-clensing.csv', mode='a', header=False)
#df.to_csv('elon.csv')