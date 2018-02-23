from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
from pymongo.mongo_client import MongoClient
from pprint import pprint
from datetime import datetime, timedelta
from email.utils import parsedate_tz
import requests


ckey = "WAybii2PCWwRgQnso5yaIR1Xk"
csecret = "M7aHF5gGfv2AlMz0us9Bvp8ZchFst9t6AeeXzAD2WdvaLmCe4v"


vars = ["created_at","id_str","user","reply_count","retweet_count","favorite_count"]
user = ["name","location"]




class listener(StreamListener):
    def __init__(self,limit,name,date1,date2):
        super().__init__()
        self.__limit = limit
        self.__dbname = name
        self.__date1 = date1
        self.__date2 = date2
    
    def on_data(self,raw_data):
        obj = json.loads(raw_data)
        self.processTweet(obj)
        print(self.__limit)
        if(self.__limit == None):
            return True
        elif(self.__limit > 0):
            self.__limit -= 1
            return True
        else:
            print("Fetching Done!")
            return False
        


    def on_error(self, status):
        print(status)

    def processTweet(self,obj):
       newobj = {}
       keys = ["text","created_at","favorite_count","retweet_count","reply_count"]
       userdetails = ["id","location","name","screen_name","lang","followers_count","friends_count","verified"]
       entities = ["hashtags","urls","user_mentions"]
       for key in keys:
           if(key == "created_at"):
               newobj["tweet_date"] = self.to_datetime(obj[key])
           else:
               newobj[key] = obj[key]
       for key in userdetails:
           newobj["user_" + key] = obj["user"][key]
       for key in entities:
           newobj[key] = obj["entities"][key]
       
       if self.__date1 != None and self.__date2 != None:
           if newobj["tweet_date"] in self.date_range(self.__date1,self.__date2):
            self.saveTweet(newobj)
       else:
           self.saveTweet(newobj)


    def saveTweet(self,obj):
        conec = MongoClient()
        tweetBase = conec[self.__dbname]
        tweetBase.tweets.insert(obj)

    def to_datetime(self,datestring):
        time_tuple = parsedate_tz(datestring.strip())
        dt = datetime(*time_tuple[:6])
        return dt - timedelta(seconds=time_tuple[-1])

    def date_range(self,start,end):
        current = start
        while (end - current).days >= 0:
            yield current
            current = current + datetime.timedelta(days = 1)

class tweetStream:
    def __init__(self):
        self.__name = ""
        self.__key = ""
        self.__secret = ""
        self.__dbname = "defaultTweetStorage"

    def setAuth(self,filename):
        f = open(filename,"r")
        lines = f.read()
        f.close()
        self.__key,self.__secret = lines.strip().split('\n')
        

    def setStorage(self,value):
        self.__dbname = value

    def startStreaming(self,query,limit = None,date1 = None,date2 = None):
        auth = OAuthHandler(ckey,csecret)
        auth.set_access_token(self.__key, self.__secret)
        if(limit != None):
            limit -= 1
        twitterStream = Stream(auth, listener(limit,self.__dbname,date1,date2))
        twitterStream.filter(track=[query])
        