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


def get_likes(user_id, pagination_token=None):
    endpoint = url + f"/{user_id}/liked_tweets"
    if pagination_token:
        endpoint = endpoint + f"?pagination_token={pagination_token}"

    response = requests.request("GET", endpoint, headers=headers)

    try:
        likes = response.json()["data"]
        next_token = response.json()["meta"].get("next_token")
    except:
        likes = []
        next_token = None

    return likes, next_token


user_id = get_user_id("NawazGafar")

all_likes = []
pagination_token = None

while True:
    likes, pagination_token = get_likes(user_id, pagination_token)
    all_likes.extend(likes)

    if pagination_token is None:
        break

print(len(all_likes))
