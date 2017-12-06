import numpy as np
from utils import corpora, utils

CORPORA = {'glove_poem_pair_50':(0.4613325043, 0.0311938)}

def expand_topic(tp_list, thr):
	topics = corpora.glove_sim_ranks(tp_list, thr)
	topics = utils.filter_stopwords(topics)
	return np.random.choice(topics, 1)[0]

def expand(input_word, corpus, std_level=1, mean_level=0):
	topics = corpora.get_topics(input_word.lower().split(), corpus)
	n = len(topics)
	std = np.sqrt(CORPORA[corpus][1])
	bound = std_level*std
	mean = CORPORA[corpus][0] + mean_level*std
	thr = (mean+bound, mean-bound)
	if n == 2:
		w3 = expand_topic(topics, thr)
		return topics + [w3]

	if n == 1:
		w2 = expand_topic(topics, thr)
		w3 = expand_topic(topics+[w2], thr)
		return topics + [w2, w3]

	return []


if __name__ == '__main__':
	m, s = 0, 1
	input_term = raw_input("\nEnter degree of creativity (between 0 to 2) or press ENTER (default = 1):")
	if input_term != '':
		assert(int(input_term) in range(3))
		m = 1-int(input_term)

	input_term = raw_input("\nEnter degree of variety (between 1 to 10) or press ENTER (default = 1):")
	if input_term != '':
		assert(int(input_term) in range(1, 11))
		s = int(input_term)

	while True:
		input_term = raw_input("\nEnter word(s) (EXIT to break): ")
		if input_term == 'EXIT':
			break
		else:
			print expand(input_term, 'glove_poem_pair_50', s, m)
