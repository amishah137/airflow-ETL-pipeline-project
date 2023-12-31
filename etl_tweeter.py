import yaml
import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs 

def run_etl():
    credentials = {}
    credentials["consumer_key"] = ""
    credentials["consumer_secret"] = ""
    credentials["access_token"] = ""
    credentials["access_token_secret"] = ""
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    api = tweepy.API(auth)

    # Retrieve authenticated user's account settings

    users = ['@elonmusk', '@ElvishYadav','@FabrizioRomano']
    new_user_info = []
    for user in users:
        try:
            user_info = api.get_user(id = user)
        except:
            pass
        refined_user_info = {
            "id": user_info._json["id"],
            "name": user_info._json["name"],
            "description": user_info._json["description"],
            'followers_count' : user_info._json["followers_count"],
            'friends_count' : user_info._json["friends_count"],
            }

        new_user_info.append(refined_user_info)

    df = pd.DataFrame(new_user_info)
    df.to_csv('s3://ami-airflow-etl-test/refined_user_info.csv')
    #df.to_csv('refined_user_info.csv')
