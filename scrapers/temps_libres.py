import requests
import bs4
import re
from langdetect import detect
from utils.utils import clean
from langdetect.lang_detect_exception import LangDetectException

LINK_URL = 'http://www.tempslibres.org/tl/tlphp/'
NAME = 'temps_libres'

def scrape():
	response = requests.get(LINK_URL + 'dbauteursl.php?lang=en&lg=e')
	soup = bs4.BeautifulSoup(response.text, 'lxml')

	for a in soup.select('article table tr td a'):
		link = a.get('href')
		if link:
			response = requests.get(LINK_URL + link)
			soup = bs4.BeautifulSoup(response.text, 'lxml')
			link = link.split('/')[0]

			haikus = []

			for h in soup.select('article div p.haiku'):
				haiku = clean(h).split('\\')
				en_haiku = None

				for i in range(0, len(haiku), 3):
					en_haiku = '\\'.join(haiku[i:i+3])

					try:
						if detect(en_haiku) == 'en':
							haikus.append(en_haiku.strip())

					except LangDetectException:
						pass

			yield haikus


if __name__ == '__main__':
	for s in scrape():
		print s