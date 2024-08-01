# BTC価格自動ツイートボット

このリポジトリは、毎日朝9:00にBTC（ビットコイン）の価格を円建てでツイートするボットのPythonスクリプトを含んでいます。

## 機能

- Twitter APIを使用して、指定したアカウントで自動的にツイートを投稿
- 外部APIから取得した最新のBTC価格を円建てでツイート
- 毎日決まった時間にツイートをスケジュール

## 必要なもの

- Python 3.6+
- Twitter Developerアカウント
- [Tweepy](https://www.tweepy.org/)
- [requests](https://docs.python-requests.org/en/latest/)

## インストール

1. 必要なライブラリをインストールします。
    
    ```bash
    pip install tweepy requests schedule
    
    ```
    
2. `bot.py`スクリプトをクローンまたはダウンロードします。
    
    ```bash
    git clone <https://github.com/your-username/btc-twitter-bot.git>
    cd btc-twitter-bot
    
    ```
    
3. `bot.py`の認証情報を設定します。
    
    ```python
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    
    ```
    
4. スクリプトを実行します。
    
    ```bash
    python bot.py
    
    ```
    

## 使い方

1. スクリプトを実行すると、毎日朝9:00にBTCの価格がツイートされます。
2. 他の時間にツイートしたい場合は、`schedule.every().day.at("09:00").do(tweet_btc_price)`の部分を変更してください。

## 注意事項

- Twitter APIキーとトークンは安全に保管してください。外部に公開しないように注意してください。
- 外部APIの利用規約を確認し、リクエスト制限に注意してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細についてはLICENSEファイルを参照してください。
