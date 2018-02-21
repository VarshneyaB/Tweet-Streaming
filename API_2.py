from pymongo.mongo_client import MongoClient
from pymongo import ASCENDING,DESCENDING,IndexModel,TEXT
from pprint import pprint
import pymongo
    # pymongo library is used to access MONGODB Database

class tweetReader:
    '''Class that reads tweets from the database'''
    def __init__(self):
        self.__dbname = "defaultTweetStorage"

        '''If setStorage() is not called,Then default storage is mentioned Above'''
    
    def setStorage(self,val):
        '''Sets the storage to look at for tweets'''
        self.__dbname = val

    def showTweets(self,search = None,sortBy = None,filter = None):
        '''
            Used to display the tweets
            arg "search": 
                     Type = string
                To be passed if we need to search in text or user_name

            arg "sortBy":
                     Type = list of tuples
                To be passed if we need to sort the results

            arg "filter":
                    Type = dic
                To be passed if we need to filter the results 
        '''
        conec = MongoClient()
        tweetBase = conec[self.__dbname]
        searchobj = {}
        if(search != None):    
            index1 = IndexModel([("user_name",TEXT),("text",TEXT)],name = "U")
            tweetBase.tweets.create_indexes([index1])
            searchobj['$text'] = {'$search' :  search }
            '''If Arguement "search" is passed The following Code is executed:
            Explaination:
                1 : index1 = IndexModel([("user_name",TEXT),("text",TEXT)],name = "U")
                2: tweetBase.tweets.create_indexes([index1])

                Indexed as per the "user_name" and "text" keys which allows
                us to search the text in tweets in the values of those keys

                3:searchobj['$text'] = {'$search' :  search }

                Task to be done is noted
                It will be executed in the later part of the code'''


        if(filter != None):
            ints = ["tweet_date","favorite_count","retweet_count","user_id","user_followers_count","user_friends_count"]

            #args supporting "Min" and "Max"
            for key in filter: 
                if key in ints:
                    this = filter[key]
                    this2 = {}
                    if "min" in this:
                        this2["$gte"] = this["min"]
                    if "max" in this:
                        this2["$lte"] = this["max"]
                    searchobj[key] = this2
                else:
                    searchobj[key] = filter[key]

        searched = tweetBase.tweets.find(filter = searchobj)
        """If Arguement "filter" is passed The following Code is executed:
        Explaination:
        filter[key] has code required for the required filter
        1 : searchobj[key] = filter[key]    (in for loop)
                
        Task to be done is noted which will be executed in the later part

        2 : searched = tweetBase.tweets.find(filter = searchobj)

        All the tasks that were noted above,are executed here
        "searchobj" specifies text search and filters
        find applies filters and search for text
        if searchobj is null,it simply returns all the values(MongoDB)
        """
    

                

        if(sortBy != None):
            sortedobj = searched.sort(sortBy)
        else:
            sortedobj = searched

        """ If Arguement "sortBy" is passed The following Code is executed:
            Explaination:
                1 : sortedobj = searched.sort(sortBy)
                
                if sortBy is not None,then sort is applied
                
                2: sortedobj = searched

                if sortBy is None,no sort is applied
        """

        return sortedobj #final result is returned