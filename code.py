ckey="WAybii2PCWwRgQnso5yaIR1Xk"
csecret="M7aHF5gGfv2AlMz0us9Bvp8ZchFst9t6AeeXzAD2WdvaLmCe4v"
from pprint import pprint

from API_1 import tweetStream
t = tweetStream()
t.setStorage("ex1")
t.setAuth(ckey,csecret)
t.startStreaming("modi",25)