import csv
import sys

from utils.utils import filter_haikus
import daily_haiku_org
import the_herons_nest
import temps_libres

def scrape_and_save(scraper_class):
	print 'Scraping', scraper_class.NAME

	with open('data/'+scraper_class.NAME+'.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile)
		count = 0

		for haikus in scraper_class.scrape():
			count += 1
			for haiku in haikus:
				if filter_haikus(haiku):
					spamwriter.writerow([haiku.encode('utf-8')])
			
			sys.stdout.write("\r%d" % count)
			sys.stdout.flush()

	print ' Done'

if __name__ == '__main__':
	scrape_and_save(daily_haiku_org)
	scrape_and_save(the_herons_nest)
	scrape_and_save(temps_libres)