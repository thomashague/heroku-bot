# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "pBIfu7T4bewNcQ4NizbRBNP7h"
consumer_secret = "Q9EsbCYdXjJlkWdpluYVA88VHIEFIclXoWyyGZhK7wiFG5OdMg"
access_token = "908923215791247365-lZKnwBo5SEm5IC4cXhbBMhbrKBw7fQU"
access_token_secret = "xRRtVv82b55ZeQskxtH5RI9zvXJb0l0sqcgQIXEyPEJi6"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE