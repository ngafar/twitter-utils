from twitter import endpoints
from utils import export 

user_id = endpoints.get_user_id("NawazGafar")

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

export.list_to_json(all_likes)