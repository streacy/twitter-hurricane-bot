import os
import tweepy
import requests
from key import *
from time import gmtime, strftime


bot_username = 'HurricaneBot1'
logfile_name = bot_username + ".log"

# ==============================================================


def create_tweet():
    """Create the text of the tweet you want to send."""
    r = requests.get('http://api.wunderground.com/api/1db15a63686c68ec/currenthurricane/view.json')
    json_object = r.json()
    text = str(json_object['currenthurricane'][0]['stormInfo']['stormName'])
    return "storm name: " + text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)