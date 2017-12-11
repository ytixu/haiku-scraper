import numpy as np
from utils import corpora, utils

CORPORA = {'glove_poem_pair_50':(0.187357508751, 0.0653636996872, 0.238429212481, 0.056475821579)}

def expand_topic(tp_list, thr):
	topics = corpora.glove_sim_ranks(tp_list, thr)
	topics = utils.filter_stopwords(topics)
	return np.random.choice(topics, 1)[0]

def get_thr(n, corpus, std_level, mean_level):
	std = CORPORA[corpus][n+1]
	bound = std_level*std
	mean = CORPORA[corpus][n] + mean_level*std
	thr = (mean+bound, mean-bound)
	print thr
	return thr


def expand(input_word, corpus, std_level=1, mean_level=0):
	topics = corpora.get_topics(input_word.lower().split(), corpus)
	n = len(topics)

	if n == 2:
		thr = get_thr(2, corpus, std_level, mean_level)
		w3 = expand_topic(topics, thr)
		return topics + [w3]

	if n == 1:
		thr = get_thr(0, corpus, std_level, mean_level)
		w2 = expand_topic(topics, thr)
		thr = get_thr(2, corpus, std_level, mean_level)
		w3 = expand_topic(topics+[w2], thr)
		return topics + [w2, w3]

	return []


if __name__ == '__main__':
	m, s = 0, 1

	input_term = raw_input("\nEnter degree of creativity (between 0 to 10) or press ENTER (default = 9):")
	if input_term != '':
		assert(int(input_term) in range(11))
		m = 9-int(input_term)

	input_term = raw_input("\nEnter degree of variety (between 0 to 10) or press ENTER (default = 0):")
	if input_term != '':
		assert(int(input_term) in range(11))
		s = int(input_term)+1

	print m,s
	while True:
		input_term = raw_input("\nEnter word(s) (EXIT to break): ")
		if input_term == 'EXIT':
			break
		else:
			print expand(input_term, 'glove_poem_pair_50', s, m)
