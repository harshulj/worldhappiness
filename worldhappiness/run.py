import click
import tweepy

import filters
from authorizers import auth
from workers import TweetBulkSaveWorker
from listeners import TwitterStreamListener


def main( mode = 1 ):
    api  = tweepy.API(auth)
    tweetBulkSaver = TweetBulkSaveWorker('bulk_raw_tweets')
    listen = TwitterStreamListener(api, tweetBulkSaver, r'test')
    stream = tweepy.Stream(auth, listen)

    try:
        stream.filter(track = filters.happy)
    except Exception as e:
        print e
        stream.disconnect()


# Following defines the group of commands for click
@click.group()
def cli():
    click.echo(click.style('Starting World Happiness\n', fg='green'))


# Following are the commands available for worldhappiness
@cli.command('collect_happy')
@click.option('--number', default=10000,
        help='Number of tweets to be collected.' )
def collect_happy(number):
    '''
    This command collects happy tweets and saves them to redis.
    '''
    click.echo(click.style('Collecting %d Happy Tweets' % number, fg='green'))
    api             = tweepy.API(auth)
    tweetBulkSaver  = TweetBulkSaveWorker('raw_happy_tweets')
    listen          = TwitterStreamListener(
                            api,
                            tweetBulkSaver,
                            number,
                            r'test'
                        )
    stream          = tweepy.Stream(auth, listen)

    try:
        stream.filter(track = filters.happy)
    except Exception as e:
        print e
        stream.disconnect()


if __name__ =='__main__':
    print "running"
    collect_happy(100)
