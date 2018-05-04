import json
from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy



with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)


    
class FileWriteListener(StreamListener):
    
     # Returns a StreamListener object
    def __init__(self):
        # Refers to "FileWriteListener" class implicitly
        super().__init__()
        # writes tweets to 'tweets.json' with append
        self.save_file = open('tweets.json','a')
        self.tweets = []

    def on_data(self, tweet):
        self.tweets.append(json.loads(tweet))
        self.save_file.write(str(tweet))

    def on_error(self, status):
        print(status)
        return True
    
      
if __name__ == '__main__':
    listener = FileWriteListener()
    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
      
   
    stream = Stream(auth, listener)
    stream.filter(track=['programming'])
    

