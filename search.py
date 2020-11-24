import tweepy
from os import environ
from database import connect, source_bias, source_accuracy, source_name

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

'''
About:
    - This function makes a request for 100 tweets with a certain search criteria. It then returns an iterable object
      that contains the requested tweets.
Return:
    - tweets (Status Iterator) This function returns a tweepy status iterator that contains the requested tweets.
'''
def search_tweets():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    search_term = 'Election AND (Trump OR Biden OR Harris OR Pence)'

    tweets = tweepy.Cursor(api.search, count=100, q=search_term, result_type='mixed').items()

    return tweets


def past_tweets():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.user_timeline).items(10)

    links = []
    for tweet in tweets:
        links.append(tweet._json['entities']['urls'][0]['expanded_url'])
    return links


def get_tweet():
    tweets = search_tweets()
    df = connect()
    found = False

    # Loop until an tweet with an article is found. Searching for more tweets if necessary.
    while not found:
        for tweet in tweets:
            # Making sure tweet contains a url
            if len(tweet._json['entities']['urls']) > 0:
                url = tweet._json['entities']['urls'][0]['expanded_url']

                # Getting tweet bias and accuracy
                bias = source_bias(df, url)
                accuracy = source_accuracy(df, url)

                # Making sure the article isn't posted twice
                if url in past_tweets():
                    continue
                # Checks if Bias is valid
                if len(bias) > 0:
                    return [source_name(df, url), bias, accuracy, url, tweet]
        tweets = search_tweets()
