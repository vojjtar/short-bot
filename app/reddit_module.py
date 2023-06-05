import praw


class RedditModule:
    """ Reddit module. """

    def __init__(self, subreddit_name: str):
        self.subreddit_name = subreddit_name
        self.reddit = praw.Reddit(
            client_id="",
            client_secret="",
            user_agent="",
        )

    def get_top_submission_from_subreddit(self):
        """" Gets top submission from subreddit. """
        subreddit = self.reddit.subreddit(self.subreddit_name)
        top_submission = next(subreddit.top(limit=1, time_filter="day"))

        return top_submission

    def get_top_comments_from_submission(self, top_submission):
        """ Gets the top 10 comments from provided submission. """
        top_submission.comment_sort = 'top'
        top_submission.comments.replace_more(limit=0)
        top_comments = top_submission.comments[:10]

        return top_comments
