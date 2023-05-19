import sys
from dotenv import dotenv_values
from workflows import get_likes

env = dotenv_values(".env")
twitter_username = env["TWITTER_USERNAME"]

if __name__ == "__main__":
    arg = sys.argv[1].lower()
    
    if arg == "get_likes":
        get_likes.get_likes(twitter_username)