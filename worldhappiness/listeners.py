import json
from tweepy import StreamListener

class TwitterStreamListener(StreamListener):
    '''
    This class overrides tweepy's default StreamListener.
    It defines custom functions to handle incoming stream.
    '''

    def __init__(self, api, worker, fprefix='stream'):
        self.api        = api
        self.fprefix    = fprefix
        self.count      = 0
        self.data       = []
        self.worker     = worker
        self.bulk_limit = 1


    def on_data(self, data):
        self.count += 1
        self.data.append(data)
        if self.count == self.bulk_limit:
            self.worker.run(self.data)
            self.data = []
            self.count = 0
