import sys
import csv

def scrape_and_save(converter_class):
	from utils.utils import flatten_and_encode
	for corpus in converter_class.CORPORA:
		print 'Converting', converter_class.NAME, 'with', corpus

		with open('data/converted/'+converter_class.NAME+'-'+corpus+'.csv', 'w') as csvfile:
			spamwriter = csv.writer(csvfile)
			count = 0

			for haikus in converter_class.convert(corpus):
				count += 1
				for haiku in haikus:
					spamwriter.writerow(flatten_and_encode(haiku))

				sys.stdout.write("\r%d" % count)
				sys.stdout.flush()

		print ' Done'

def compute_association_for_gen():
	from utils.conversion_statistics import record
	from utils.corpora import _glove_sim_score, get_topics

	first_pair = record()
	second_pair = record()
	corpus = 'glove_poem_pair_50'
	get_topics([''], corpus)

	with open('data/converted/best_words-%s.csv' % (corpus)) as csv_file:
		spamreader = csv.reader(csv_file)
		for count, row in enumerate(spamreader):
			first_pair.update(_glove_sim_score(row[0], row[2]))
			second_pair.update(_glove_sim_score([row[0], row[2]], row[4]))
			sys.stdout.write("\r%d" % count)
			sys.stdout.flush()

	first_pair.print_stats()
	second_pair.print_stats()

if __name__ == '__main__':
	import all_word_pairs
	import best_association_pairs
	# scrape_and_save(all_word_pairs)
	# scrape_and_save(best_association_pairs)
	compute_association_for_gen()