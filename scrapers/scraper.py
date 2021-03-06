import csv
import sys

from utils.utils import filter_haikus
import daily_haiku_org
import the_herons_nest
import temps_libres
import reddit_haiku
import twitter_haiku
import modern_haiku
import haiku_foundation
import all_poetry_basho

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

# run from root folder, not form scrapers folder!
if __name__ == '__main__':
	# scrape_and_save(daily_haiku_org)
	# scrape_and_save(the_herons_nest)
	# scrape_and_save(temps_libres)
	# scrape_and_save(reddit_haiku)
	# scrape_and_save(twitter_haiku)
	# scrape_and_save(modern_haiku)
	# scrape_and_save(haiku_foundation)
	# scrape_and_save(all_poetry_basho)
	pass

