import tweepy

from database import connect, source_bias, source_accuracy, source_name
from mykey import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def search_tweets():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    search_term = 'Election OR Trump OR Biden OR Harris'

    tweets = tweepy.Cursor(api.search, count=100, q=search_term, result_type='popular').items()
    linked_tweets = []

    for tweet in tweets:
        if len(tweet._json['entities']['urls']) == 0:
            continue
        linked_tweets.append(tweet)

    return linked_tweets


def get_tweet():
    tweets = search_tweets()
    df = connect()
    for tweet in tweets:
        url = tweet._json['entities']['urls'][0]['expanded_url']
        bias = source_bias(df, url)
        if len(bias) > 0:
            return [source_name(df,url),bias,url,tweet]

