import pymongo
import pandas as pd

databasename = 'TwitterBot'
cluster = 'cluster0'


class Database:
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://production_user:group9project@" + cluster +
                                     ".yiatl.mongodb.net/" + databasename + "?retryWrites=true&w=majority")
        self.sources_df = pd.DataFrame.from_dict(client.TwitterBot.newsSources.find_one()['allsides_media_bias_ratings'])

    def source_bias(self, link):
        if len(link) < 8:
            return ""
        link = link[8:]
        link = link[0:link.index('/')]
        bias = self.sources_df.media_bias_rating[self.sources_df.source_url.str.contains(link)]
        if len(bias) > 0:
            return bias
        else:
            return ""

    def source_accuracy(self, link):
        if len(link) < 8:
            return ""
        link = link[8:]
        link = link[0:link.index('/')]
        bias = self.sources_df.media_accuracy_rating[self.sources_df.source_url.str.contains(link)]
        if len(bias) > 0:
            return bias
        else:
            return ""