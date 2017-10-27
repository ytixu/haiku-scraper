import time
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import praw

from utils.utils import break_lines
import utils.oauth

SUBREDDIT = 'haiku'
NAME = 'reddit_haiku'

def scrape():
	import praw
	reddit = praw.Reddit(user_agent='Haiku-Scraper',
						client_id=utils.oauth.REDDIT_CLIENT_ID, 
						client_secret=utils.oauth.REDDIT_CLIENT_SECRET)
	skipped = []

	for submission in reddit.subreddit(SUBREDDIT).submissions(946684800, int(time.time())):
		haiku = break_lines(submission.title)

		if len(haiku) > 0:
			try:
				if detect(haiku) == 'en':
					yield [haiku]
					
			except LangDetectException:
				pass

		else:
			skipped.append(submission.id)
	
	print ' Skipped ', len(skipped), skipped
	raise StopIteration

if __name__ == '__main__':
	for s in scrape():
		print s