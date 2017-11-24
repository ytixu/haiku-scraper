import sys
import csv

from utils.utils import flatten_and_encode
import all_word_pairs
import best_association_pairs

def scrape_and_save(converter_class):
	for corpus in converter_class.CORPORA:
		print 'Converting', converter_class.NAME, 'with', corpus

		with open('data/converted/'+converter_class.NAME+'-'+corpus+'.csv', 'w') as csvfile:
			spamwriter = csv.writer(csvfile)
			count = 0

			for haikus in converter_class.convert(corpus):
				count += 1
				for haiku in haikus:
					spamwriter.writerow(flatten_and_encode(haiku))

				# sys.stdout.write("\r%d" % count)
				# sys.stdout.flush()

		print ' Done'

if __name__ == '__main__':
	# scrape_and_save(all_word_pairs)
	scrape_and_save(best_association_pairs)