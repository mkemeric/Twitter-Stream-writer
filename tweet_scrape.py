#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

#Variables that contains the user credentials to access Twitter API 
rotate = 10
access_token = "21841708-5dh2iiCAQeUtmYWNaEQWPOOZ5BCom9f49RkyilCpR"
access_token_secret = "WQuBN5cTzhoVeyNDyfogIhWkTnSfIDgDsYTdDowLhgPHV"
consumer_key = "nhiJYFEnLvjAjURlrMf8MGCDx"
consumer_secret = "9K3pT7QYI5rqQTVOFlCz399ff4x9zZMrZ4AHEoEAvAFsnmQNR7"
timeout = time.time() + rotate
file_out = open ('twitter_stream.json','w')
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
		global timeout
		global file_out
		if time.time() > timeout :
			file_out.close()
			file_out = open ('twitter_stream'+str(time.time()) +'json' ,'w')
			timeout = time.time() + rotate
		print data[1:34]
		file_out.write(data)
		file_out.flush()
		return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

  #This handles Twitter authetification and the connection to Twitter Streaming API
  l = StdOutListener()
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  stream = Stream(auth, l)

  #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
  stream.filter(track=['python', 'javascript', 'ruby'])
