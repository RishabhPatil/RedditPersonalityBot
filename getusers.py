# -*- coding: utf-8 -*-
"""
Created on 8 August 2017
@author: Rishabh Patil
"""

import praw
import sys
import operator
import json

with open("config.json","r") as f:
	config = json.load(f)

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

print(reddit.user.me())

subreddit = reddit.subreddit('mbti')

print(subreddit.display_name)
print(subreddit.title)

with open("authors.json","r") as f:
	authors=json.load(f)

def add_author(name,text_flair,css_flair):
	global authors
	if name not in authors:
		authors[name] = (text_flair,css_flair)

count = 0

for submission in subreddit.submissions():
	count+=1
	sys.stdout.write("\r{0} {1}".format(count,len(authors)))
	sys.stdout.flush()
	fail = 1
	while fail:
		try:
			submission.comments.replace_more(limit=None)
			add_author(str(submission.author),submission.author_flair_text,submission.author_flair_css_class)
			for comment in submission.comments.list():
			    add_author(str(comment.author),comment.author_flair_text,comment.author_flair_css_class)
			fail = 0
		except:
			continue

with open("authors.json",'w+') as f:
	# print(authors)
	json.dump(authors,f,indent=4)

# config["timelast"] = timelast + (timestep*steps)
# with open("config.json",'w') as f:
# 	json.dump(config,f)