import requests
import bs4
import re
from utils.utils import format, clean


URL = 'https://allpoetry.com/poems/read_by/Matsuo%20Basho?page='
NAME = 'basho'

def scrape():
	page_ind = 1
	while(True):
		response = requests.get(URL+str(page_ind))
		page_ind += 1
		soup = bs4.BeautifulSoup(response.text, "lxml")

		for h_ele in soup.select('div.poem_body'):
			haikus = re.sub(u'[\r\t\xa0]', '', h_ele.get_text())
			haikus = haikus.split('Compiled and')[0]
			haikus = haikus.split('Translated by')[0]
			haikus = haikus.split(u'\xc9 by owner')[0]
			haikus = haikus.split('\n\n\n')
			haikus = [format(h) for h in haikus]
			if len(haikus) == 1 and len(haikus[0]) == 0:
				haikus = clean(h_ele).split(' by owner')[0].split(' \\ ')
				if len(haikus) % 3 == 0:
					yield [' \\ '.join(haikus[i:i+3]) for i in range(0,len(haikus), 3)]

			yield haikus

		if len(haikus) == 0:
			raise StopIteration

if __name__ == '__main__':
	for s in scrape():
		print s
