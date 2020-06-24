import csv
from Tweet import make_tweet
import glob
import os
import joblib


class Database_manager(object):

    db = None
    cur = None

    def __init__(self):
        """
         If you want to recover tweets from a mysql db set the config.py:
         for example  mysql = {
         'host': 'yourhost',
         'user': 'yourmysqluser',
         'passwd': 'yourpassword',
         'db': 'dbname'}
        """

    def return_tweets(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """
        tweets = self.return_tweets_training()+self.return_tweets_test()

        print(len(tweets))
        return tweets

    def return_tweets_training(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """

        if os.path.isfile('..........'):
            tweets= joblib.load('..........')
            return tweets

        tweets = []

        filelist = sorted(glob.glob("........."))


        for file in filelist:
            first = True

            csvfile=open(file, newline='')
            spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
            for tweet in spamreader:

                if not first:

                        id = tweet[0]
                        text = tweet[1]
                        # language = file.split(".")[1]
                        # topic = tweet[4]
                        label = tweet[2]

                        """
                        Create a new instance of a Tweet object
                        """
                        this_tweet = make_tweet(id, text, label)

                        tweets.append(this_tweet)

                first = False

        joblib.dump(tweets, '..........')

        return tweets

    def return_vector_space(self):
        """Return an array containing vectorspace.
        """
        """
         You could recover tweets from db or csv file
        """

        if os.path.isfile('..........pkl'):
            vector_space = joblib.load('...........pkl')
            return vector_space

        vector_space = []

        filelist = sorted(glob.glob(".........."))


        for file in filelist:
            first = True

            csvfile=open(file, newline='')
            spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
            for tweet in spamreader:

                if not first:

                        id = tweet[0]
                        text = tweet[1]
                        # language = file.split(".")[3]
                        # topic = tweet[4]
                        label = tweet[2]

                        """
                        Create a new instance of a Tweet object
                        """
                        this_tweet = make_tweet(id, text, label)

                        tweets.append(this_tweet)

                first = False

        joblib.dump(X, '..........')

        return vector_space


    def return_tweets_test(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """
        if os.path.isfile('spanish_tweets_test.pkl'):
            tweets= joblib.load('spanish_tweets_test.pkl')
            return tweets

        tweets=[]

        filelist = sorted(glob.glob(".........."))

        for file in filelist:
            first = True

            csvfile = open(file, newline='')
            spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
            for tweet in spamreader:
                if not first:

                    id = tweet[0]
                    text = tweet[1]
                    # language = file.split(".")[3]
                    # topic = tweet[2]
                    label = tweet[2]

                    """
                    Create a new instance of a Tweet object
                    """
                    this_tweet = make_tweet(id, text, label)

                    tweets.append(this_tweet)

                first = False

        joblib.dump(tweets, '..........')

        return tweets


def make_database_manager():
    database_manager = Database_manager()

    return database_manager


if __name__== "__main__":
    database_manager = Database_manager()

    tweets = database_manager.return_tweets_training()
    print("Tweets train")
    for tweet in tweets:
        print(tweet.id, tweet.text, tweet.label)

    tweets = database_manager.return_tweets_test()
    print("Tweets test")
    for tweet in tweets:
        print(tweet.id, tweet.text, tweet.label)

    tweets = database_manager.return_tweets()
    print("Tweets")
    for tweet in tweets:
        print(tweet.id, tweet.text, tweet.label)
