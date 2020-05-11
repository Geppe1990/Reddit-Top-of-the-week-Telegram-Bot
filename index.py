import praw
import pandas as pd
import datetime as dt


def main():
    data = {}
    with open("data.txt") as f:
        for line in f:
            key, value = line.strip().split(':')
            data[key] = value

    reddit = praw.Reddit(
        client_id=data["client_id"],
        client_secret=data["client_secret"],
        user_agent=data["user_agent"],
        username=data["username"],
        password=data["password"]
    )


if __name__ == '__main__':
    main()
