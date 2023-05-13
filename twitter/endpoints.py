import requests
from dotenv import dotenv_values

env = dotenv_values(".env")

url = "https://api.twitter.com/2/users"
headers = {"authorization": f'Bearer {env["TWITTER_BEARER_TOKEN"]}'}


def get_user_id(twitter_username):
    endpoint = url + f"/by?usernames={twitter_username}"
    
    response = requests.request("GET", endpoint, headers=headers)
    user_id = response.json()["data"][0]["id"]

    return user_id


def get_likes(user_id):
    endpoint = url + f"/{user_id}/liked_tweets"

    response = requests.request("GET", endpoint, headers=headers)
    likes = response.json()["data"]

    return likes


user_id = get_user_id("NawazGafar")
likes = get_likes(user_id)
print(likes)
