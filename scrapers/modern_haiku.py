import requests
import bs4
import re

from utils.utils import clean

LINK_URL = 'http://www.modernhaiku.org/'
NAME = 'modern_haiku'

def try_links(baselink, attempt_endpoint):
	response = requests.get(LINK_URL + attempt_endpoint)
	soup = bs4.BeautifulSoup(response.text, 'lxml')
	return [clean(h) for h in soup.select('table table table p')]

def scrape():
	response = requests.get(LINK_URL + 'previousissue.html')
	soup = bs4.BeautifulSoup(response.text, 'lxml')

	for a in soup.select('table table td p a'):
		link = a.get('href')
		if link is None:
			continue

		if 'MH-Archive' in link:
			break

		yield try_links(LINK_URL, link.replace('index', 'haiku'))
		issue = '-'.join(re.findall('[\d]+', link))
		yield try_links(LINK_URL, link.replace('index', 'haiku'+issue))


if __name__ == '__main__':
	for s in scrape():
		print s
