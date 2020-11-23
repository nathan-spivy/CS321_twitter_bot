import tweepy
import time
from search import get_tweet
from mykey import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def tweet():
    """
    About: This function compiles the a tweet containing the bias and accuracy of a source that was
           Tweeted in a popular tweet. It then posts the tweet to the TrueNews twitter account.
    """

    tweet = get_tweet()
    tweet_contents = "News Source: " + tweet[0] + "\nSource Bias: " + tweet[1] + \
                     "\nSource Accuracy: " + tweet[2] + "\nArticle: " + tweet[3] + ""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    api.update_status(tweet_contents)


# Post every hour
post_interval = 60 * 60

# Post intervals
while True:
    tweet()
    time.sleep(post_interval)
