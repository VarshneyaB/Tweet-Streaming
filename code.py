from API_1 import tweetStream

t = tweetStream()
t.setStorage("thisStorage")
t.setAuth("authKey");
t.startStreaming("modi",5)