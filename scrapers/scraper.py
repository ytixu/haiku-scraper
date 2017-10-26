import csv
import sys
import daily_haiku_org

def scrape_and_save(scraper_class):
	print 'Scraping ', scraper_class.NAME

	with open('data/'+scraper_class.NAME+'.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile)
		count = 0

		for haikus in scraper_class.scrape():
			count += 1
			for haiku in haikus:

				spamwriter.writerow([haiku.encode('utf-8')])
			
			sys.stdout.write("\r%d" % count)
			sys.stdout.flush()

if __name__ == '__main__':
	scrape_and_save(daily_haiku_org)