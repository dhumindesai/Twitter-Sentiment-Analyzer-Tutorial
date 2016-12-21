"""
import sentiment_mod as s

print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(s.sentiment("sucks the movie"))
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


ckey="74wbDBcm0fjvg0ud1Tea6olaM"
csecret="cShpWb9NFQAxHcT5UtoYGfoYrOetkXGDREoUuYsKMdv5X5Zxcl"
atoken="148612813-NEbIraBKDVqyJNJsH5sdtT0d7eDmf3uICmCx6NDF"
asecret="LwMDmUUxmnQ1natqAfYyCxARYZpgiIeAg3Dvh0fGSOOUn"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        print tweet
        sentiment_value, confidence = s.sentiment(tweet)
        print tweet, sentiment_value, confidence 

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])

