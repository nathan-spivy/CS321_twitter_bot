import pymongo
import pandas as pd

databasename = 'TwitterBot'
cluster = 'cluster0'


def connect():
    # Establishing connection to mongodb
    client = pymongo.MongoClient("mongodb+srv://production_user:group9project@" + cluster +
                                 ".yiatl.mongodb.net/" + databasename + "?retryWrites=true&w=majority")
    # Transforming database data from json/dictionary format into a pandas dataframe
    df = pd.DataFrame.from_dict(client.TwitterBot.newsSources.find_one()['allsides_media_bias_ratings'])
    return df


"""
About:
    - This function searches the database for the news source that corresponds to the inputted link and returns
      the bias
Arguments:
    - link (String) : A string containing the direct link to the news article taken from a tweet
Return:
    - bias (String) : A string containing the bias rating for the inputted news source
"""


def source_bias(df, link):
    # Making sure that inputted is valid
    if len(link) < 8:
        return ""
    # Removes the https:// from the link
    link = link[8:]

    # Finds the core portion of the link
    link = link[0:link.index('/')]

    # Twitter posts sometimes will include links to the status. Does not mean there is a link in the status
    if 'twitter.com' in link:
        return ""

    # Finds the bias rating for the news source the link corresponds to
    bias = df.media_bias_rating[df.source_url.str.contains(link)]

    # Checking if database contains news source
    if len(bias) > 0:
        return bias
    else:
        return ""


"""
    About:
        - This function searches the database for the news source that corresponds to the inputted link and returns
          the accuracy
    Arguments:
        - link (String) : A string containing the direct link to the news article taken from a tweet
    Return:
        - accuracy (String) : A string containing the accuracy rating for the inputted news source
    """


def source_accuracy(df, link):
    # Making sure that inputted is valid
    if len(link) < 8:
        return ""
    # Removes the https:// from the link
    link = link[8:]

    # Finds the core portion of the link
    link = link[0:link.index('/')]

    # Twitter posts sometimes will include links to the status. Does not mean there is a link in the status
    if 'twitter.com' in link:
        return ""

    # Finds the accuracy rating for the news source the link corresponds to
    accuracy = df.media_accuracy_rating[df.source_url.str.contains(link)]

    # Checking if database contains news source
    if len(accuracy) > 0:
        return accuracy
    else:
        return ""
