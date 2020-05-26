#code for streaming tweets
import tweepy
import couchdb
import json
from urllib3.exceptions import ProtocolError
### TWITTER CREDENTIALS ###
access_key = 'ijcwMgXJquxCq6TJPbdofkYcd'
access_secret = 'xkiQYXxnL4Xke1kDFiMj9RfYHtqIjM1mH9bf7dFHrUFrawSmD7'

access_token = '1257319847970484227-4KAwk5Bjq5bfZPffRkgjMfqGkbgCz4'
access_token_secret = 'rIH9RSZQKmvW9wlhcn7PgxAPAbdZdCNlc3LXHRkDU4YGg'

auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#Code for CouchDB 
db_tweet = 'tweet'
db_address = "http://group26:group26@172.26.133.189:5984/"
db_server = couchdb.Server(db_address)

if db_tweet in db_server:
    db_tweet = db_server[db_tweet]
else:
    db_tweet = db_server.create(db_tweet)
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        tweet = json.loads(data)
        tweet_id = tweet["id_str"]
        if tweet_id not in db_tweet:
            db_tweet[tweet_id] = {"tweet": tweet}
            print("new tweet: "+tweet_id)
        return True

    def on_error(self, status):
        print(status)

    def on_exception(self, exception):
        print(exception)
        return

### TWITTER STREAM LISTENER ###
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("hello")

while True:
    try:
        myStream.filter(locations=[113.338953078, -43.6345972634, 153.569469029, -10.6681857235])
    except ProtocolError:
        continue
