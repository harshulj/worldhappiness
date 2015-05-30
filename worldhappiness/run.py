import click
import tweepy

import filters
from authorizers import auth
from workers import TweetBulkSaveWorker
from listeners import TwitterStreamListener


# Following defines the group of commands for click
@click.group()
def cli():
    click.echo(click.style('Starting World Happiness\n', fg='green'))


# Following are the commands available for worldhappiness
# 'collect' command is used to collect sample tweets which are
# then used for supervised learning
@cli.command('collect')
@click.option('--number', default=10000,
        help='Number of tweets to be collected.' )
@click.argument('type', nargs=1)
def collect(number, type):
    '''
    This command collects happy/sad tweets and saves them to redis.
    '''
    click.echo(click.style('Collecting %d Happy Tweets' % number, fg='green'))

    if type == 'happy':
        queue   = 'raw_happy_tweets';   filter  = filters.happy
    elif type == 'sad':
        queue   = 'raw_sad_tweets';     filter  = filters.sad

    api             = tweepy.API(auth)
    tweetBulkSaver  = TweetBulkSaveWorker(queue)
    listen          = TwitterStreamListener(api,tweetBulkSaver,number,'test')
    stream          = tweepy.Stream(auth, listen)

    try:
        stream.filter(track = filter)
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        stream.disconnect()


# 'learn' command takes sample tweets as input and
# creates the index of words which are then used for classifying
# the input tweets.

@cli.command('learn')
def learn():
    '''
    This commands uses the sample collected tweets
    and then creates the index which is then used
    for classifying the incomming tweets.
    '''
    click.echo(click.style('Starting learning', fg='green'))


if __name__ =='__main__':
    print "running"
    collect_happy(100)
