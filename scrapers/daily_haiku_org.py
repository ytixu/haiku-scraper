import requests
import bs4
from utils.utils import clean

URL = 'http://www.dailyhaiku.org/haiku/?pg='
NAME = 'daily_haiku'

def scrape():
	page_ind = 1
	while(True):
		response = requests.get(URL+str(page_ind))
		page_ind += 1
		soup = bs4.BeautifulSoup(response.text, "lxml")

		haikus = [clean(h) for h in soup.select('p.haiku')]
		if len(haikus) == 0:
			raise StopIteration

		yield haikus

if __name__ == '__main__':
	for s in scrape():
		print s