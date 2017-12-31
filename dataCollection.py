import praw
import config
import json
#import getusers


data = {}

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
     			commentsList.append(comment.body.encode('ascii','ignore').split('\n', 1))
		return commentsList


obj = botLogin()
#print(get_comments('flaminggandu',obj))
try:
	authorsData = json.load(open('authors.json'))
	for author in authorsData:
			print author
			commentsList = get_comments(author,obj)
			#data.[author] 
			data[author] = (commentsList)
			#data = addUserComments(author,commentsList)
except:
	pass
with open("data.json",'w+') as f:
	#print(data)
	json.dump(data,f,indent=4)