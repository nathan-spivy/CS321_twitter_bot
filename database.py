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


def source_name(df, link):
    # Making sure that inputted is valid
    if len(link) < 8:
        return ""
    # Removes the https:// from the link
    link = link[8:]

    # Twitter posts sometimes will include links to the status. Does not mean there is a link in the status
    if 'twitter.com' in link:
        return ""

    if '/' in link:
        link1 = link[0:link.index('/')] + "/"
        temp = link[link.index('/') + 1:len(link)]
        link2 = ''
        if '/' in temp:
            temp = temp[0:temp.index('/') + 1]
            link2 = link1 + temp
    else:
        link1, link2 = link

    # Finds the name for the news source the link corresponds to
    name = df.source_name[df.source_url.str.contains(link1)]

    backup_name = df.source_name[df.source_url.str.contains(link2)]

    if len(name) > 1 and len(backup_name) == 1:
        name = backup_name.iloc[0]
    else:
        name = name.iloc[0]
    return name

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

    # Twitter posts sometimes will include links to the status. Does not mean there is a link in the status
    if 'twitter.com' in link:
        return ""

    if '/' in link:
        link1 = link[0:link.index('/')] + "/"
        temp = link[link.index('/') + 1:len(link)]
        link2 = ''
        if '/' in temp:
            temp = temp[0:temp.index('/') + 1]
            link2 = link1 + temp
    else:
        link1, link2 = link
    # Finds the bias rating for the news source the link corresponds to
    bias = df.media_bias_rating[df.source_url.str.contains(link1)]

    backup_bias = df.media_bias_rating[df.source_url.str.contains(link2)]

    if len(bias) > 1 and len(backup_bias) == 1:
        bias = backup_bias.iloc[0]
    elif len(bias) > 1:
        bias = bias.iloc[0]
    else:
        return ''

    # Checking if database contains news source
    if len(bias) < 100:
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
    # Since over 800 accuracy ratings need to be manually inputed, accuracy has not been put in the database yet
    return "Coming Soon!"

    # Making sure that inputted is valid
    if len(link) < 8:
        return ""
    # Removes the https:// from the link
    link = link[8:]

    # Twitter posts sometimes will include links to the status. Does not mean there is a link in the status
    if 'twitter.com' in link:
        return ""

    if '/' in link:
        link1 = link[0:link.index('/')] + "/"
        temp = link[link.index('/') + 1:len(link)]
        link2 = ''
        if '/' in temp:
            temp = temp[0:temp.index('/') + 1]
            link2 = link1 + temp
    else:
        link1, link2 = link
    # Finds the bias rating for the news source the link corresponds to
    accuracy = df.media_accuracy_rating[df.source_url.str.contains(link1)]

    backup_accuracy = df.media_accuracy_rating[df.source_url.str.contains(link2)]

    if len(accuracy) > 1 and len(backup_accuracy) == 1:
        accuracy = backup_accuracy.iloc[0]
    elif len(accuracy) > 1:
        accuracy = accuracy.iloc[0]
    else:
        return ''

    # Checking if database contains news source
    if len(accuracy) < 100:
        return accuracy
    else:
        return ""
