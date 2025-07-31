from connect import reddit as r
import pandas as pd
data = []

def gather_information_subreddit(subreddit : str, sort : str, subject : str, limit : int):
    for submission in r.subreddit(subreddit).search(subject,  sort = sort , limit = limit):
        submission.comments.replace_more(limit = 0)
        top_level_comment = submission.comments[:3]
        for comment in top_level_comment:
            data.append({
                "Subreddit" : f"{subreddit}",
                "Submission title" : f"[{submission.title}]",
                "Comment"  : f"[{comment.body}]"
            })

    data_subreddit = pd.DataFrame(data)
    return data_subreddit
def clean_data(df :pd.DataFrame) -> pd.DataFrame:
    return 1