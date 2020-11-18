import tweepy
from search import get_tweet
from mykey import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

'''
About: This function compiles the a tweet containing the bias and accuracy of a source that was
       Tweeted in a popular tweet. It then posts the tweet to the TrueNews twitter account.
'''
def tweet():
    tweet = get_tweet()
    tweet_contents = "News Source: " + tweet[0] + "\nSource Bias: " + tweet[1] + "\nArticle: " + tweet[2] + ""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    api.update_status(tweet_contents)



