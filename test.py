from pymongo.mongo_client import MongoClient
from pprint import pprint
conec = MongoClient()
base = conec['twitterData']
base.tweets.insert_one({"name" : "Modi","twitter" : "Lakaka"})
x = base.docs.find_one({"name" : "Modi"})
pprint(base)
pprint(x)