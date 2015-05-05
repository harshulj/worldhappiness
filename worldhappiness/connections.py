# This file defines all the connection related objects.
from redis.connection import Connection, ConnectionPool

import config

def redis_connection_pool(self, maxConnections=10):
    '''
    This function returns redis connection pool
    '''
    connectionPool = ConnectionPool(Connection, maxConnections, **config.redis)
    return connectionPool

