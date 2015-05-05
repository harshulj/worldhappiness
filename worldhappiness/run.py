import tweepy

import filters
from listeners import TwitterStreamListener
from authorizers import auth

api      = tweepy.API(auth)

def main( mode = 1 ):
    follow = []

    listen = TwitterStreamListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    try:
        stream.filter(track = filters.happy, follow = follow)
        #stream.sample()
    except Exception as e:
        print "error!"
        print e
        stream.disconnect()

if __name__ == '__main__':
    main()
