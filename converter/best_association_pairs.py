from glob import glob
import sys

from utils import corpora, utils, conversion_statistics, association
from reader.reader import read_lines
from all_word_pairs import convert as awp_convert

NAME = 'best_words'
# CORPORA = ['wordnet', 'glove_twitter_25', 'glove_twitter_50',  'glove_twitter_100', 'glove_twitter_200',
# 		'glove_wiki_50', 'glove_wiki_100', 'glove_wiki_200', 'glove_wiki_300', 'glove_crawl_300']
CORPORA = ['glove_twitter_25']

def convert(corpus):
	sr = conversion_statistics.record()

	datafiles = glob('data/*.csv')
	for filename in datafiles:

		for combo in awp_convert(corpus, filename, False):
			pair_scores = association.get_avg_associations(combo)
			# best pair
			best_idx = np.argsort(-pair_scores)[0]
			sr.update(pair_scores[best_idx])
			yield combo[best_idx]

		sr.print_stats(corpus, filename)

if __name__ == '__main__':
	for corpus in CORPORA:
		count = 1
		for pairs in convert(corpus):
			print pairs
			# sys.stdout.write("\r%d" % count)
			# sys.stdout.flush()
			count += 1