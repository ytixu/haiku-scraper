import time
import re
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import twitter

from utils.utils import filter_and_break_lines
import utils.oauth

hashtage = 'haiku'
NAME = 'twitter_haiku'

def is_retweet(text):
	return len(re.findall('RT @[0-9a-zA-Z_]+: ', text))

def scrape():
	api = twitter.Api(consumer_key=utils.oauth.TWITTER_API_KEY,
					consumer_secret=utils.oauth.TWITTER_API_SECRET,
					access_token_key=utils.oauth.TWITTER_ACCESS_TK,
					access_token_secret=utils.oauth.TWITTER_ACCESS_TK_SECRET)

	results = api.GetSearch(raw_query="l=en&q=%23haiku&result_type=mixed&count=100")
	retweet = ''

	while len(results) > 0:
		for tweet in results:
			haiku = tweet.text
			
			if is_retweet(haiku):
				continue

			if len(haiku) > 0:
				try:
					if detect(haiku) == 'en':
						haiku = filter_and_break_lines(haiku)

						if len(haiku) > 0 and haiku != retweet:
							retweet = haiku
							yield [haiku]

				except LangDetectException:
					pass
		
		time.sleep(5)
		results = api.GetSearch(raw_query="max_id="+str(int(results[-1].id)-1)+"&l=en&q=%23haiku&result_type=mixed&count=100")	
		

if __name__ == '__main__':
	for s in scrape():
		print s