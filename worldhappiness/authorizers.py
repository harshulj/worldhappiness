#TODO Make a better design
import tweepy

consumer_key        = "2thk9BzFT10uUkwtr68qxyiBB"
consumer_secret     = "bBn52W8c4E4mQN4dq8UTautewS2oC6QoBw0A93mlNuDPafgrmi"
access_token        = "1366749896-5VdOmdkk3K9SrcSZNF64CI6lWPod6Zbsbhd6yej"
access_token_secret = "Tc8RJNsy5iCrPFX74tcBaloW5LZ9vqPWcfG1tof1EI6NW"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

