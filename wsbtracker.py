import praw 
from WriteToCSV import WriteToCSV
import threading

# IDEA: Scrape from new and scrape from top of day
# Scrape from new: Run it 30 min before the market starts, and run it until the market closes. 
# Scrape from top day once every hour. Also scrape the comments and upvote ratio and upvote count.

user_agent = "Scraper 1.0 by /u/justtrustmeplease"

#stock_ticker_mention_count = 0
#stock_ticker = input("What stock do you want to SCRAPE?: ")

reddit = praw.Reddit(
    client_id = "TNqEttEQXgGGIZ03AE6DpA",
    client_secret = "37Z18Netzke2pqZuejRkgfNKTsv5cQ",
    user_agent = user_agent
)

def newPosts(): 
    threading.Timer(5.0,newPosts).start()
    with open('wsbnew.csv', 'r') as f:
        for line in f:
            pass
        last_line = line
    previous_submission_title = last_line

    print(previous_submission_title)

    headlines = set()
    for submission in reddit.subreddit('wallstreetbets').new(limit=None):
        #print(submission.title)
        #print(submission.id)
        #print(submission.author)
        #print(submission.created_utc)
        #print(submission.score)
        #print(submission.upvote_ratio)
        #print(submission.url)
        #break
        print(submission.title)
        headlines.add(submission.title)

    # Don't need this in new but do it for hot and top
    # the_submission = reddit.submission(submission.id)
    # the_submission.comments.replace_more(limit=None)
    # for comment in the_submission.comments.list():
    #     print(comment.body)

    #submission_title = submission.title
    print(submission.title)
    #print(submission_title)

    PleaseWriteToCSV = WriteToCSV()

    #filename = 'wsbnew.csv'S

    if(submission.title != previous_submission_title):
        PleaseWriteToCSV.append_to_csv(submission.title)

newPosts()

# TO DO LATER: Go into the post and scrape the comments too. 