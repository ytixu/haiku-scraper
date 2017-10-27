import requests
import bs4
import re
from utils.utils import clean

LINK_URL = 'http://theheronsnest.com/'
NAME = 'herons_nest'

def scrape():
	response = requests.get(LINK_URL + 'archives.html')
	soup = bs4.BeautifulSoup(response.text, 'lxml')
	other_link = None

	for a in soup.select('article p a'):
		link = a.get('href')
		if 'http' in link:
			other_link = link
			break

		response = requests.get(LINK_URL + link)
		soup = bs4.BeautifulSoup(response.text, 'lxml')
		link = link.split('/')[0]

		for p in soup.select('article nav ul li a'):
			page = p.get('href')
			if 'editors-choices' in page:
				continue

			response = requests.get(LINK_URL + link + '/' + page)
			soup = bs4.BeautifulSoup(response.text, 'lxml')

			haikus = [clean(h) for h in soup.select('p.haiku')]

			yield haikus

	response = requests.get(other_link)
	soup = bs4.BeautifulSoup(response.text, 'lxml')

	for a in soup.select('dir li a'):
		link = a.get('href')

		if len(re.findall(u'h[0-9]+\.html$', link)) == 0:
			continue

		response = requests.get(link)
		soup = bs4.BeautifulSoup(response.text, 'lxml')

		yield [clean(h) for h in soup.select('table tr td table tr td p font')]



if __name__ == '__main__':
	for s in scrape():
		print s