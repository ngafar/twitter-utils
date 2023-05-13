import requests
from dotenv import dotenv_values

env = dotenv_values(".env")


def get_user_id(twitter_username):
    url = f"https://api.twitter.com/2/users/by?usernames={twitter_username}"

    headers = {"authorization": f'Bearer {env["TWITTER_BEARER_TOKEN"]}'}

    response = requests.request("GET", url, headers=headers)
    user_id = response.json()["data"][0]["id"]

    return user_id

user_id = get_user_id("NawazGafar")
print(user_id)