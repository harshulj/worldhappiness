import json
from tweepy import StreamListener

class TwitterStreamListener(StreamListener):
    '''
    This class overrides tweepy's default StreamListener.
    It defines custom functions to handle incoming stream.
    '''

    def __init__(self, worker, api=None, fprefix='stream'):
        self.api  = api or API()
        self.fprefix    = fprefix
        self.count = 0
        self.data = []


    def on_data(self, data):
        self.count += 1
        data = json.loads(data)
        print data['lang']
        self.data.append(data['text'])
        print type(data)
        if self.count == 10:
            print(self.data)
            worker.run(self.data)
            self.data = []
            self.count = 0
