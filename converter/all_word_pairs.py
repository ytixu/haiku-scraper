from glob import glob

from utils import corpora, utils, conversion_statistics
from reader.reader import read_lines

NAME = 'all_words'
CORPORA = ['wordnet']

def convert(corpus):
	cst = conversion_statistics.statistics()

	datafiles = glob('data/*.csv')
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
			cst.update(combos, topics, tokened_lines, tokens)

			yield combos

		cst.print_stats(filename)

if __name__ == '__main__':
	for pairs in convert():
		print pairs