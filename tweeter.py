# activate venv by using the following command
# source ./venv/bin/activate
import tweepy
from mykey import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authenticate to Twitter

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# # Create a tweet
# str = "In Illinois, an elderly didn't receive her absentee ballot, so she decided to travel  more than 600 miles round trip to vote.\n"
# str += "Political Leaning: Leaning Left\n"
# str += "Accuracy: Have failed several fact checks from Politifact\n"
# str += "https://www.cnn.com/2020/10/19/politics/elderly-woman-travels-300-miles-to-vote-trnd/index.html?utm_content=2020-10-24T04%3A00%3A06&utm_term=link&utm_source=twCNN&utm_medium=social"
# api.update_status(str)

#retweet for a search string
search1 = "election Trump Biden has:links lang:en"
search2 = "election has:links lang:en"
search3 = "from:realDonaldTrump has:links"
numberOfTweets = 2
get_tweet_success = False

# if not get_tweet_success:
#     for tweet in tweepy.Cursor(api.search,q=search2, tweet_mode='extended',result_type='popular').items(numberOfTweets):

if not get_tweet_success:
    count = 0
    for tweet in api.search(q=search2, tweet_mode='extended', count=10, result_type='recent'):
        try:
            # tweet.retweet()
            get_tweet_success = True
            print('Retweeted the retweet: ', tweet.retweeted_status.full_text)
        except:
            print('retweet: ', tweet.full_text)
        count += 1
    print(count)