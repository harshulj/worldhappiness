'''
 This file implements the algorithm for learning
 using sample tweets. Following are the tasks/steps
 involved in this algorithm
 1. Take tweets and clean them.
 2. Then using cleaned tweet extract features from that tweet.
 3. Dont forget to remove stop words.
 4. Add that to the features list.
 5. Use NLTK to create training set
 6. Save the training set on redis for later use.
'''

class WHTrainer:
    '''
    This class does the job of training. It takes the raw tweets and
    returns a training set and saves it on redis.
    #TODO Currently all the functions are specific to tweet and
    # are located in this class. Make it modular and more generic.
    '''
    def __init__(self):
        self.features       = []
        self.trainingSet    = []
        self.stopWords      = []

        # Load all stop words
        self._loadStopWords()

    def _loadStopWords(self):
        '''
        This function loads all the stop words into memory.
        '''
        pass

    def _getRawTweet(self, tweet):
        '''
        This function fetches a raw tweet from redis.
        '''
        pass

    def _parseRawTweet(self, tweet):
        '''
        This function parses a raw tweets string and fetches all the
        required information for the tweet.
        '''
        pass

    def _cleanTweet(self, tweet):
        '''
        This function cleans the tweet text according to parsing rules
        so that a good feature list can be created.
        '''
        pass

    def _getTweetFeatures(self, tweet):
        '''
        This function takes cleaned tweet text and converts it into a
        feature vector.
        '''
        pass


    def run(self):

