import praw
import pandas as pd
import datetime as dt


def main():
    client_id = ''
    client_secret = ''
    user_agent = 'infoSender'
    username = ''
    password = ''

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password
    )


if __name__ == '__main__':
    main()
