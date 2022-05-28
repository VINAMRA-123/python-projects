import tweepy
import time

consumer_key = 'AnoT59dptdzC5EfmP7pKNEOig'
consumer_secret = 'KdJUnRGWPxzrOuirwNruOFgQlXwbCIOJzodlOnbiKsmhJcEWsS'
key = '447938059-Z2owpm4FQOXBGGoKXQfC8kCUt4akBk8vde5TOZvZ'
secret = 'sbp4FCt0okPyeZR64PvTJTLFXcmvWhBPjucBOBZWxFF1e'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

File_name = 'last_seen.txt'

def read_last_seen_file(File_name):                     #function used for seeing last id
    read_file = open(File_name,'w')
    last_seen_id = int(read_file.read().strip())
    read_file.close()
    return last_seen_id
    
def store_last_seen(File_name,last_seen_id):              #function used to store last id
    store_file = open(File_name, 'r')
    store_last_seen_id = str(store_file.write())
    store_file.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen_file(File_name),tweet_mode = 'extended')
    for tweet in reversed(tweets):                 # here reversed is used to reply the oldest tweet first
        if '#randomtweet' in tweet.full_text.lower():
            api.update_status('@ '+ tweet.user.screen_name + '#100 days of code!' ,tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            print(str(tweet.id)+ - + tweet.text)
            read_last_seen_file(File_name,tweet.id)

while True:
    reply()
    time.sleep(60)
    
# for retweet to a particular hashtag
hashtags = "#100 days of code"
tweet_number = 3 

tweets = tweepy.Cursor(api.search,hashtags).items(tweet_number)

for tweet in tweets:
    tweet.retweet()