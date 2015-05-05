import tweepy

import filters
from authorizers import auth
from workers import TweetBulkSaveWorker
from listeners import TwitterStreamListener


def main( mode = 1 ):
    follow = []
    api  = tweepy.API(auth)
    tweetBulkSaver = TweetBulkSaveWorker('bulk_raw_tweets')
    listen = TwitterStreamListener(api, tweetBulkSaver, r'test')
    stream = tweepy.Stream(auth, listen)

    try:
        stream.filter(track = filters.happy, follow = follow)
        #stream.sample()
    except Exception as e:
        print e
        stream.disconnect()

if __name__ == '__main__':
    main()
