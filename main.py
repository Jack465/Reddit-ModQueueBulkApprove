import praw

reddit = praw.Reddit(client_id='###',
                client_secret='###',
                user_agent='CatFlier r_RequestABot Request',
                username='CatFlier',
                password='###')

for item in reddit.subreddit('musicbottesting').mod.modqueue(limit=None):
    item.mod.approve()
    print("approved " + str(item))

