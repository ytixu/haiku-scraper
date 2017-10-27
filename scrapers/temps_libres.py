import requests
import bs4
import re
from utils.utils import clean

LINK_URL = 'http://www.tempslibres.org/tl/tlphp/'
NAME = 'temps_libres'

def scrape():
	response = requests.get(LINK_URL + 'dbauteursl.php?lang=en&lg=e')
	soup = bs4.BeautifulSoup(response.text, 'lxml')

	for a in soup.select('article table tr td a'):
		link = a.get('href')
		if link:
			print link
			response = requests.get(LINK_URL + link)
			soup = bs4.BeautifulSoup(response.text, 'lxml')
			link = link.split('/')[0]

			haikus = []
			for h in soup.select('article div p.haiku'):
				haiku = clean(h).split('\\')
				haikus.append('\\'.join(haiku[:len(haiku)/2]))

			yield haikus


if __name__ == '__main__':
	for s in scrape():
		print s