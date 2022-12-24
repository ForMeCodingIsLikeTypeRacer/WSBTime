import json
import praw 
from WriteToTXT import WriteToTxt
import threading

# TODO: Idea is to scrape all the titles and upvotes for each title and make some calculation to buy or ignore/sell a stock
# TODO: change csv file to txt file

user_agent = "Scraper 1.0 by /u/Constant-Yam531"

#stock_ticker_mention_count = 0
#stock_ticker = input("What stock do you want to SCRAPE?: ")

credentials = 'client_secrets.json'

with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(
    client_id = creds['client_id'],
    client_secret = creds['client_secret'],
    user_agent = creds['user_agent'],
    redirect_uri = creds['redirect_uri']
)

def newPosts(): 
    threading.Timer(5.0,newPosts).start()
    with open('wsbnew.csv', 'r') as f:
        for line in f:
            pass
        last_line = line
    previous_submission_title = last_line

    #print(previous_submission_title)

    headlines = set()
    for submission in reddit.subreddit('wallstreetbets').new(limit=1):
        #print(submission.title)
        #print(submission.id)
        #print(submission.author)
        #print(submission.created_utc)
        #print(submission.score)
        #print(submission.upvote_ratio)
        #print(submission.url)
        #break
        #print(submission.title)
        headlines.add(submission.title)

    # Don't need this in new but do it for hot and top
    # the_submission = reddit.submission(submission.id)
    # the_submission.comments.replace_more(limit=None)
    # for comment in the_submission.comments.list():
    #     print(comment.body)

    #submission_title = submission.title
    #print(submission.title)
    #print(submission_title)
    print(submission.title)
    PleaseWriteToTXT = WriteToTxt()

    #filename = 'wsbnew.csv'S

    if(submission.title != previous_submission_title):
        PleaseWriteToTXT.append_to_csv(submission.title)

def topPosts(): 
    threading.Timer(5.0,topPosts).start()
    with open('wsbnew.csv', 'r') as f:
        for line in f:
            pass
        last_line = line
    previous_submission_title = last_line

    headlines = set()
    for submission in reddit.subreddit('wallstreetbets').top(limit=1):
        headlines.add(submission.title)

    print(submission.title)
    PleaseWriteToCSV = WriteToTxt()

    #filename = 'wsbnew.csv'S

    if(submission.title != previous_submission_title):
        PleaseWriteToCSV.append_to_csv(submission.title)

def hotPosts(): 
    threading.Timer(5.0,hotPosts).start()
    with open('wsbnew.csv', 'r') as f:
        for line in f:
            pass
        last_line = line
    previous_submission_title = last_line

    #headlines = set()
    headlines = {

    }

    count = 0
    for submission in reddit.subreddit('wallstreetbets').hot(limit=100):
        #headlines[submission.title] = submission.score
        headlines[count] = [submission.title,submission.score]
        count = count + 1
        #headlines.add(submission.title)

    #print(submission.title)
    #print(list(headlines)[10])
    #print(headlines)
    PleaseWriteToTXT = WriteToTxt()

    #filename = 'wsbnew.csv'S
    print(headlines[0][1])
    count = 0
    while(count < 100):
        PleaseWriteToTXT.append_to_txt(headlines[count][0])
        count = count + 1
    

hotPosts()
#topPosts()
# newPosts()

# TO DO LATER: Go into the post and scrape the comments too. 
