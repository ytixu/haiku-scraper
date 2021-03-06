import sys

from utils import corpora, utils, conversion_statistics
from reader.reader import read_lines, get_all_files

NAME = 'all_words'
# CORPORA = ['wordnet', 'glove_twitter_25', 'glove_twitter_50',  'glove_twitter_100', 'glove_twitter_200',
# 		'glove_wiki_50', 'glove_wiki_100', 'glove_wiki_200', 'glove_wiki_300', 'glove_crawl_300']
CORPORA = ['glove_poem_pair_50']

def convert(corpus, data_file=None, get_stats=True):
	if get_stats:
		cst = conversion_statistics.statistics()
		cst.print_header(['haiku corpus', 'dictionary'])

	if not data_file:
		datafiles = get_all_files()
	else:
		datafiles = [data_file]

	for filename in datafiles:
		for haiku in read_lines(filename):
			lines, tokened_lines, tokens = utils.parse(haiku)

			try:
				assert len(tokens) == 3
				for tks in tokens:
					assert len(tks) > 0
			except(AssertionError):
				# print 'AssertionError: not 3-lined', haiku
				continue

			topics = [[]]*3

			for i, line_tokens in enumerate(tokens):
				topics[i] = corpora.get_topics(line_tokens, corpus)

			combos = utils.make_combos(topics, lines)

			if get_stats:
				cst.update(combos, topics, tokened_lines, tokens, corpus)

			yield combos

		if get_stats:
			cst.print_stats([filename, corpus])
			cst.reset()

if __name__ == '__main__':
	for corpus in CORPORA:
		count = 1
		for pairs in convert(corpus, 'data/best_haikus.txt'):
			print pairs
			# sys.stdout.write("\r%d" % count)
			# sys.stdout.flush()
			count += 1