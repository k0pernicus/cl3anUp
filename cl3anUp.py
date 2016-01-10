import sys
import tweepy
from time import sleep

consumer_key = "TO_REPLACE!"
consumer_secret = "TO_REPLACE!"
access_token = "TO_REPLACE!"
token_secret = "TO_REPLACE!"

def t_auth():
    """
    Return a Twitter authentification
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    return tweepy.API(auth)

def get_tweets(api):
    """
    Get the 20 first tweets in your timeline
    """
    return api.user_timeline()

def get_direct_messages(api):
    """
    Get direct messages
    """
    return api.direct_messages()

def get_favorites(api):
    return api.favorites()

def destroy_tweets(api):
    i = 1
    print("Currently destroy your status...")
    while True:
        tweet_note = "tweet"
        tweets = get_tweets(api)
        if len(tweets) == 0:
            tweets = get_favorites(api)
            tweet_note = "favorite"
            if len(tweets) == 0:
                break
        for tweet in tweets:
            tweet_id = tweet.id
            tweet_date = tweet.created_at
            if tweet_note == "tweet":
                print("\t{0} Destroy status {1}, from {2}".format(i, tweet_id, tweet_date))
                api.destroy_status(tweet_id)
            else:
                print("\t{0} Destroy favorite {1}, from {2}".format(i, tweet_id, tweet_date))
                api.destroy_favorite(tweet_id)
            i += 1
        sleep(0.5)
    print("Tweets are destroyed! Your user timeline is empty :-)")

def destroy_direct_messages(api):
    i = 1
    print("Currently destroy your direct messages...")
    while True:
        tweets = get_direct_messages(api)
        if len(tweets) == 0:
            break
        for tweet in tweets:
            tweet_id = tweet.id
            tweet_date = tweet.created_at
            print("\t{0} Destroy direct message {1}, from {2}".format(i, tweet_id, tweet_date))
            api.destroy_direct_message(tweet_id)
            i += 1
        sleep(0.5)
    print("Direct messages are destroyed! Your message timeline is empty :-)")

def destroy():
    try:
        api = t_auth()
        print("You've been authentified!")
    except:
        print("Oops...")
        sys.exit()
    destroy_tweets(api)
    destroy_direct_messages(api)

if __name__ == '__main__':
    destroy()
