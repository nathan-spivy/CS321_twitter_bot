import tweepy
import time
from search import get_tweet
from os import environ


def tweet():
    """
    About: This function compiles the a tweet containing the bias and accuracy of a source that was
           Tweeted in a popular tweet. It then posts the tweet to the TrueNews twitter account.
    """

    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_token_secret = environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    tweet = get_tweet()
    tweet_contents = "News Source: " + tweet[0] + "\nSource Bias: " + tweet[1] + \
                     "\nSource Accuracy: " + tweet[2] + "\nArticle: " + tweet[3] + ""

    # Create API object
    api = tweepy.API(auth)

    api.update_status(tweet_contents)


# Post every hour
post_interval = 60 * 60

# Post intervals
while True:
    tweet()
    time.sleep(post_interval)
