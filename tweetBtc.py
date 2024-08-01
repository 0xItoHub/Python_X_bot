import tweepy
import requests
import schedule
import time

# Twitter APIの認証情報を設定
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# 認証
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# BTCの価格を取得する関数
def get_btc_price():
    url = '<https://api.coindesk.com/v1/bpi/currentprice/JPY.json>'
    response = requests.get(url)
    data = response.json()
    price_jpy = data['bpi']['JPY']['rate']
    return price_jpy

# 毎日9:00にツイートする関数
def tweet_btc_price():
    price = get_btc_price()
    tweet = f"現在のBTCの価格は {price} JPY です。 #Bitcoin #BTC"
    api.update_status(tweet)
    print(f"ツイートしました: {tweet}")

# スケジュール設定
schedule.every().day.at("09:00").do(tweet_btc_price)

# 無限ループでスケジュールを実行
while True:
    schedule.run_pending()
    time.sleep(1)
