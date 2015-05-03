from tweepy import StreamListener

class TwitterStreamListener(StreamListener):
    '''
    This class overrides tweepy's default StreamListener.
    It defines custom functions to handle incoming stream.
    '''

    def __init__(self, api=None, fprefix='stream'):
        self. self.api  = api or API()
        self.fprefix    = fprefix


    def on_data(self, data):
        print(data)
