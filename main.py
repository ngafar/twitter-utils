from twitter import endpoints

user_id = endpoints.get_user_id("NawazGafar")

all_likes = []
pagination_token = None

while True:
    likes, pagination_token = endpoints.get_likes(user_id, pagination_token)
    all_likes.extend(likes)

    if pagination_token is None:
        break

print(len(all_likes))