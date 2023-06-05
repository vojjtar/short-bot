import reddit_module


class Bot:
    """ Main class for the bot """

    def __init__(self):
        self.subreddit_name = 'AskReddit'
        self.reddit = reddit_module.RedditModule(self.subreddit_name)

    def start(self):
        """ Main function for the bot """
        submission = self.reddit.get_top_submission_from_subreddit()
        comments = self.reddit.get_top_comments_from_submission(submission)
        print(comments)

if __name__ == "__main__":
    bot = Bot()
    bot.start()
