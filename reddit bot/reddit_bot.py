#Author @ Pradeep Shetty

import praw

reddit = praw.Reddit(client_id='c1A-fN1h1Oeg1A',
                         client_secret='q3WnOlCW7Y1HqHtTbxZb9aixhkU',
                         password='',
                         user_agent='testscript by /u/vertibrex',
                         username='')

##submission = reddit.submission(url='https://www.reddit.com')
##
##from praw.models import MoreComments
##for top_level_comment in submission.comments:
##    if isinstance(top_level_comment, MoreComments):
##        continue
##    print(top_level_comment.body)

##for submission in reddit.front.hot():
##    print(submission)



subreddit = reddit.subreddit("datascience")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")


input()
