import praw
import datetime as dt
import botogram


def main():
    data = {}

    with open("data.txt") as f:
        for line in f:
            key, value = line.strip().split(': ')
            data[key] = value

    reddit = praw.Reddit(
        client_id=data["reddit_client_id"].strip(),
        client_secret=data["reddit_client_secret"].strip(),
        user_agent=data["reddit_user_agent"].strip(),
        username=data["reddit_username"].strip(),
        password=data["reddit_password"].strip()
    )

    bot = botogram.create(data["telegram_token"])

    hot_limit = 5
    subreddit_list = ['redditdev', 'Nootropics']
    for sr in subreddit_list:
        subreddit = reddit.subreddit(sr)
        message = "<b>"+sr.upper()+"</b>\n\n"
        # Mi ricavo i post hot che non sono stickied
        top_ten = [p for p in subreddit.hot(limit=100) if not p.stickied][:hot_limit]

        for post in top_ten:
            message += "<a href='"+post.url+"'>"+post.title+"</a>\n<i>"+str(dt.datetime.fromtimestamp(post.created))+"</i>\n\n"

        bot.chat(data["telegram_id"]).send(message, preview=False)


if __name__ == '__main__':
    main()
