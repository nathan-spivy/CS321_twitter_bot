import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("hqh6IhsgKhsU1jcGYE7mPJcjO", "dFoypiPTvEBD9wOSTris2sbGoeAGy0X1ge7C8mCvkWV6VEkJmE")
auth.set_access_token("1316108593448603649-wVg3Qu9FZtz9fruxOKGPcyjOCP7q97", "vZWaOA9FBiBKhpJLU2cT4NXGX9SnLlXHYqqsVHO21rH1L")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello from team 09")