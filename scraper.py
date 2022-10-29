from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import praw

user_agent = "Scraper 1.0 by __DEADPOOP__"
reddit = praw.Reddit(
    client_id= "u51-K4hFXTKEaTTc9dNP1Q",
    client_secret= "d_6eMwdS9qahhIEjtXbxbOHtsO8-7A",
    user_agent= user_agent
)

headlines = set()
for submission in reddit.subreddit('canada').hot(limit=45):
    print(submission.score)
    headlines.add(submission.score)
print(len(headlines))


df = pd.DataFrame(headlines)
df.head()

df.to_csv('C:/Users/csmen/Documents/Pers-Project/voteCounts.csv', header=False, index=False)
