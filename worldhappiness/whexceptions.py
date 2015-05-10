# This file defines all the exceptions.

class StreamingFinished(Exception):
    def __init__(self, *args, **kwargs):
        super(StreamingFinished, self).__init__(*args, **kwargs)
