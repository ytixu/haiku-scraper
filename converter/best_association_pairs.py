import sys
import numpy as np

from utils import corpora, utils, conversion_statistics, association
from reader.reader import get_all_files
from all_word_pairs import convert as awp_convert

NAME = 'best_words'
# CORPORA = ['wordnet', 'glove_twitter_25', 'glove_twitter_50',  'glove_twitter_100', 'glove_twitter_200',
# 		'glove_wiki_50', 'glove_wiki_100', 'glove_wiki_200', 'glove_wiki_300', 'glove_crawl_300', 'glove_haiku_50']
# CORPORA = ['glove_haiku_50', 'glove_twitter_25', 'glove_twitter_50', 'glove_wiki_50', 'glove_wiki_100']
CORPORA = [
# 'glove_twitter_25', 'glove_twitter_50', 'glove_wiki_50', 'glove_wiki_100',
		# 'glove_haiku_50', 'glove_haiku_pair_50', 'glove_poem_50',
		'glove_poem_pair_50']

def convert(corpus):
	sr = conversion_statistics.record()

	datafiles = get_all_files()
	for filename in datafiles:

		for combo in awp_convert(corpus, filename, False):
			if len(combo) < 1:
				continue

			pair_scores = association.comb_vec_associations(corpus, combo)
			# best pair
			best_idx = np.argsort(-pair_scores)[:min(len(combo), 3)]

			for i in best_idx:
				sr.update(pair_scores[i])

			yield [combo[i] for i in best_idx]

		sr.print_stats(corpus, filename)
		sr.reset()

if __name__ == '__main__':
	for corpus in CORPORA:
		count = 1
		for pairs in convert(corpus):
			# print pairs
			sys.stdout.write("\r%d" % count)
			sys.stdout.flush()
			count += 1