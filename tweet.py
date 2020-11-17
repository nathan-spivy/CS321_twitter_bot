import tweepy
from CS321_twitter_bot.search import get_tweet
from CS321_twitter_bot.mykey import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def tweet():
    tweet = get_tweet()
    tweet_contents = "News Source: " + tweet[0] + "\nSource Bias: " + tweet[1] + "\nArticle: " + tweet[2] + ""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    api.update_status(tweet_contents)

tweet()

