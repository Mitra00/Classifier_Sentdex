from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'MRVHBh8Bax10kJkXv1H6akvtq'
csecret = 'oAopusEeleL6wZOWRTbB5hOcaXnmbYS6Kx55E8jZc6FjIKVUUl'
atoken = '70659001-eNl6EBYM0hbuYmKXFFuUf1xY8mIyHXTHqU7Td8AQ3'
asecret = 'ZN3QdCLXAoisFKTLBqQRv4Pn1Ax251AEqEC8SCGyCFN94'


class listener(StreamListener):

    def on_data(self,data):
        try:
            
           lang = data.split('","lang":"')[1].split('","')
           lang = lang[0][0:2]
           if(lang  == "en"):
            
              print (data)
              saveFile = open('Apple.6.23.2015.CSV','a')
              saveFile.write(data)
              saveFile.write('\n')
              saveFile.close()
              return True
            
        except BaseException as e:
            print ('failed ondata,',str(e))
            time.sleep(5)


    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Apple"])
        
