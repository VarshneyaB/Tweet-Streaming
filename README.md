# Tweet-Streaming

To use Above APIs one need to install
1. Tweepy to work with twitter
2. pymongo to work with databases

While using API_1 personal access token,access key of twitter are to be given as a file.

# API_1

## usage
1. setStorage -- To set Database's name
2. startStreaming has args
   * query - word to search
   * date1,date2 - dateRange(optional)
   * limit - Number of Tweets

###Example

t = tweetStream()

t.setStorage("xstorage")

t.authKey("authKey")  //file name in which authkey is there

t.startStreaming("#hollywood")


# API_2

## usage
1. setStorage -- To set Database's name
2. showTweets -- Displays tweets.It has three args
    * search : {search : "textTosearch"}
    * filter : {variable : {min : "Val",max : "Val"}}
    * sort : {Variable : 1/0} specifies either ascending/descending
