import tweepy, csv
from time import sleep
from config import CONFIG

# twitter key 
CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

# Tweepy auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Tweepy create instance
api = tweepy.API(auth)

# ツイート取得
tweet_lst = []
tweets = tweepy.Cursor(api.user_timeline, screen_name="yoskmr", exclude_replies=True)

for tweet in tweets.items():
    try:
        tweet_lst.append([
            tweet.id, # id
            tweet.created_at, # ツイート日時
            tweet.text.replace('\n',''), # ツイートした内容
            tweet.favorite_count, # いいね数
            tweet.retweet_count # RT数
        ])
    except Exception as e:
        sleep(15) # ツイートを取得できなかった場合は15秒プログラムを停止する

# 取得したツイートをCSVに書き込む
with open('yoskmr.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","like","rt"]) # １行目に書く
    writer.writerows(tweet_lst)
