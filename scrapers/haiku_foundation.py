import requests
import bs4
import re
from string import ascii_uppercase

from utils.utils import clean, remove_signatures

LINK_URL_ARCHIVE = 'https://www.thehaikufoundation.org/haikunow-archive/'
LINK_REGISTRY = 'https://www.thehaikufoundation.org/haiku-registry/?Search1='
NAME = 'haiku_foundation'

def scrape():
	response = requests.get(LINK_URL_ARCHIVE)
	soup = bs4.BeautifulSoup(response.text, 'lxml')

	yield [remove_signatures(clean(h)) for h in soup.select('pre')]

	for a in soup.select('div.entry-content ul li a'):
		link = a.get('href')
		# yield link
		response = requests.get(link)
		soup = bs4.BeautifulSoup(response.text, 'lxml')
		yield [remove_signatures(clean(h)) for h in soup.select('article pre')]

	for search in ascii_uppercase:
		response = requests.get(LINK_REGISTRY + search)
		soup = bs4.BeautifulSoup(response.text, 'lxml')

		for a in soup.select('article h4 a'):
			link = a.get('href')
			response = requests.get(link)
			soup = bs4.BeautifulSoup(response.text, 'lxml')
			yield [clean(h) for h in soup.select('article pre')]


if __name__ == '__main__':
	for s in scrape():
		print s
