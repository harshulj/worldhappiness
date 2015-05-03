from listeners import TwitterStreamListener
import time, tweepy, sys

## auth.
## TK: Edit the username and password fields to authenticate from Twitter.
#username = ''
#password = ''
#auth     = tweepy.auth.BasicAuthHandler(username, password)
#api      = tweepy.API(auth)

# Eventually you'll need to use OAuth. Here's the code for it here.
# You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key        = "2thk9BzFT10uUkwtr68qxyiBB"
consumer_secret     = "bBn52W8c4E4mQN4dq8UTautewS2oC6QoBw0A93mlNuDPafgrmi"
access_token        = "1366749896-5VdOmdkk3K9SrcSZNF64CI6lWPod6Zbsbhd6yej"
access_token_secret = "Tc8RJNsy5iCrPFX74tcBaloW5LZ9vqPWcfG1tof1EI6NW"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api      = tweepy.API(auth)

def main( mode = 1 ):
    track  = ['cricket', 'worldcup', 'wc2015', 'aus', 'australia', 'kiwi', 'newzealand', 'ausvsnz', 'cricketworldcup', 'cricketwc2015', 'finals', 'wcfinals2015']
    follow = []

    listen = TwitterStreamListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try:
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
