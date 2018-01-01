import praw
import config
import json
import os
#import getusers
def botLogin():
		redditObj = praw.Reddit(username = config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
						user_agent = config.user_agent)
		return redditObj



def get_comments(author,redditObj):
		commentsList = []
		for comment in redditObj.redditor(author).comments.new(limit=None):
				# print(comment.body)
     			commentsList.append(comment.body)
		# print(commentsList)
		return commentsList


obj = botLogin()
users_already_processed = set(os.listdir('data'))
authors = set(json.load(open('authors.json')).keys())
users_to_process = authors.difference(users_already_processed)
print(len(users_to_process)," users to process")
for author in users_to_process:
		data = {}
		fail = 1
		while fail:
				try:
						print(author)
						commentsList = get_comments(author,obj)
						data["comments"] = (commentsList)
						#data = addUserComments(author,commentsList)
						fail = 0
				except Exception as excpt:
						print(excpt)
						if excpt in ["404 HTTP response", "403 HTTP response"]:
							print("rip user")
							fail = 0
						pass
		with open("./data/"+author,'w+') as f:
			#print(data)
			json.dump(data,f,indent=4)