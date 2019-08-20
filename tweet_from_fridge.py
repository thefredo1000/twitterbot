#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='YDZFTz5xNSNq3OvGa2P5T1lpd',
consumer_secret='EpMmDqMrS1jCfXX9C2DVMmZTyaTgxZH1yr2rhDsgduRQBJlJp0',
access_token='74551352-ddfAwOVr3v65Oc6AaoihMlvOOYri6W8BqjkXjQ8AR', 
access_token_secret='OrrsINiqk4QtikdtSbxowM4VVArWtkTp9meB5soKs3jte'
)

user = "@guitarsolo4"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	time.sleep(10)
if __name__ == "__main__":
	while 1:
		tweet()