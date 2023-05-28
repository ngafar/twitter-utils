def matching_tweet_finder(all_likes, all_media, all_users):
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
                
    return all_likes