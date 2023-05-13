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
    params_expansions = "?expansions=attachments.media_keys,author_id"
    params_media_fields = "&media.fields=alt_text,preview_image_url,type,url,variants"
    params_tweet_fields = "&tweet.fields=created_at,referenced_tweets,source"
    params_user_fields = "&user.fields=id,name,profile_image_url,username"

    endpoint += (
        params_expansions
        + params_media_fields
        + params_tweet_fields
        + params_user_fields
    )
    if pagination_token:
        endpoint = endpoint + f"&pagination_token={pagination_token}"

    print(endpoint)

    response = requests.request("GET", endpoint, headers=headers)

    likes = response.json().get("data", [])
    media = response.json().get("includes", {}).get("media", [])
    users = response.json().get("includes", {}).get("users", [])
    next_token = response.json().get("meta", {}).get("next_token", None)

    return likes, media, users, next_token
