from twitter import endpoints
from utils import export 

def get_likes(twitter_username):
    user_id = endpoints.get_user_id(twitter_username)

    all_likes = []
    all_media = []
    all_users = []
    pagination_token = None

    while True:
        likes, media, users, pagination_token = endpoints.get_likes(user_id, pagination_token)
        all_likes.extend(likes)
        all_media.extend(media)
        all_users.extend(users)

        if pagination_token is None:
            break

    for tweet in all_likes:
        # look for matching media
        try:
            media_keys = tweet["attachments"]["media_keys"]

            for media in all_media:
                if media["media_key"] in media_keys:
                    tweet["media"] = media
        except:
            pass
        
        # look for matching user
        author_id = tweet["author_id"]

        for user in all_users:
            if user["id"] == author_id:
                tweet["author"] = user
                
    export.list_to_json(all_likes)