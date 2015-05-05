import json

from redis import StrictRedis

import config
from connections import redis_connection_pool

class BaseRedisWorker(StrictRedis):
    '''
    This defines the base functionality of a Redis worker.
    In Redis a queues is represented by just a name. Hence each worker will
    be provided just the queue name. Each worker will know its task. Whether to
    pop or push from queue.
    '''

    def __init__(self, queue):
        self.queue = queue
        self.connectionPool = redis_connection_pool(1)
        super(BaseRedisWorker, self).__init__(connection_pool=self.connectionPool)

    def run(self):
        raise NotImplementedError('All base classes should over ride run')


class TweetBulkSaveWorker(BaseRedisWorker):
    '''
    This worker gets tweets from the stream and adds them to the queue.
    '''
    def __init__(self, queue):
        super(TweetBulkSaveWorker, self).__init__(queue)

    def run(self, data):
        '''
        This function takes an array of tweets and pushes them to the queue.
        '''
        self.lpush(self.queue, *data)
