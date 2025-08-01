from connect import reddit as r
import pandas as pd
data = []
unwanted =["Thank you for posting on /r/Artistlounge, please be sure to check out or Rules on the sidebar and visit our [FAQ](https://www.reddit.com/r/artistlounge/wiki/faq)",
           ""]
def gather_information_subreddit(subreddit : str, sort : str, subject : str, limit : int):
    for submission in r.subreddit(subreddit).search(subject,  sort = sort , limit = limit):
        submission.comments.replace_more(limit = 0)
        top_level_comment = submission.comments[:3]
        for comment in top_level_comment:
            data.append({
                "Comment"  : f"{comment.body}"
            })

    data_subreddit = pd.DataFrame(data)
    return data_subreddit


def is_bot(comment):
    if pd.isna(comment):
        return False
    return "i am a bot" in comment.lower() or "performed automatically" in comment.lower()

def is_useless(comment):
    if pd.isna(comment):
        return False
    return "thank you for posting on" in comment.lower() or "please be sure to check out or Rules on the sidebar" in comment.lower()