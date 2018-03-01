# Tweet-Streaming

To use Above APIs one need to install
1. Tweepy to work with twitter
2. pymongo to work with databases


# API_1

_To use this API you need to have a twitter account.
And,you need to set you access key and access Token in a file,each per line and give it to tweetStream.setAuth()_
## usage
1. tweetStream - class need to be imported from API_1
2. setStorage - To set Database's name
3. startStreaming has args
   * query - word to search
   * date1,date2 - dateRange(optional)
   * limit - Number of Tweets(optional)

### Example

```
from API_1 import tweetStream

t = tweetStream()
t.setStorage("xstorage")
t.setAuth("authKey")    #file name in which authkey is there
t.startStreaming(query = "#hollywood",limit = 10)
```


# API_2

_This is to fetch tweets that were stored in database_

## usage
1. setStorage -- To set Database's name
2. showTweets -- Displays tweets. It has three args
    * search - "textTosearch" (optional)
    * filter - {variable : {"min" : "Val","max" : "Val"}} (optional)
    * sortBy - list of Tuples (Variable,direction)  direction = 1/0 denoting ascending or descending.  (optional)

### Example

```
from API_2 import tweetReader
from pprint import pprint  #imported only to print out objects
t = tweetReader()
t.setStorage("xstorage")
tweets = t.showTweets(
    search = "Josh",
    filter = {"user_followers_count" : { "min" : 2500}},
    sortBy = [("user_friends_count",1)]
)

for tweet in tweets:
    pprint(tweet["user_friends_count"])
```
# API_3

_This is to export the data from database into a desired file._

## usage

1. setColumns - to select the columns we want to export
2. export - arguements are explained below
    *   filename - Choose filename of the exported file
    *   tweets - set of tweetobjects we want to export
    *   mode - mode in which we wanna save the file
        *   "a" - append mode
        *   "w" - write mode
    *   sep - separator by which columns have to be seperated  (optional)

### Example

```
from API_2 import tweetReader
from API_3 import export

t = tweetReader()
t.setStorage("xstorage")
tweets = t.showTweets()
exp = export()
exp.setColumns("user_name","user_screen_name","user_friends_count")
exp.export("data.csv",tweets,"a",sep = "###")
```
