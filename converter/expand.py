import numpy as np
from utils import corpora, utils

CORPORA = {
'glove_haiku_50':(0.172623282374,0.0861122072487,0.195189285837,0.0806755023293),
'glove_haiku_pair_50':(0.122414439778,0.0834738573092,0.176147607884,0.069845982223),
'glove_poem_50':(0.245128032712,0.0607993903255,0.281071056951,0.0583519094113),
'glove_poem_pair_50':(0.187357508751, 0.0653636996872, 0.238429212481, 0.056475821579)}

def expand_topic(tp_list, thr):
	topics = corpora.glove_sim_ranks(tp_list, thr)
	topics = utils.filter_stopwords(topics)
	if len(topics) == 0:
		return None
	return np.random.choice(topics, 1)[0]

def get_thr(n, corpus, std_level, mean_level):
	std = np.sqrt(CORPORA[corpus][n+1])
	bound = std_level*std
	mean = CORPORA[corpus][n] + mean_level*std
	thr = (mean+bound, mean-bound)
	# print thr, bound
	return thr


def expand(input_word, corpus, std_level=1, mean_level=0):
	topics = corpora.get_topics(input_word.lower().split(), corpus)
	n = len(topics)

	if n == 2:
		thr = get_thr(2, corpus, std_level, mean_level)
		w3 = expand_topic(topics, thr)
		if w3 is None:
			return
		return topics + [w3]

	if n == 1:
		thr = get_thr(0, corpus, std_level, mean_level)
		w2 = expand_topic(topics, thr)
		if w2 is None:
			return
		thr = get_thr(2, corpus, std_level, mean_level)
		w3 = expand_topic(topics+[w2], thr)
		if w3 is None:
			return
		return topics + [w2, w3]

	return []


if __name__ == '__main__':
	m, s = 0, 1

	input_term = raw_input("\nEnter degree of creativity (between 0 to 10) or press ENTER (default = 9):")
	if input_term != '':
		assert(int(input_term) in range(11))
		m = (9-int(input_term))*0.3

	input_term = raw_input("\nEnter degree of variety (between 0 to 10) or press ENTER (default = 0):")
	if input_term != '':
		assert(int(input_term) in range(11))
		s = (int(input_term)+1)*0.2

	print m,s
	while True:
		input_term = raw_input("\nEnter word(s) (EXIT to break): ")
		if input_term == 'EXIT':
			break
		else:
			print expand(input_term, 'glove_poem_pair_50', s, m)


	# for c in CORPORA:
	# 	print c
	# 	for input_term in ['sun', 'autumn', 'street', 'play', 'wind freeze', 'window leaves']:
	# 		for m in range(11):
	# 			for s in range(1, 11):
	# 				mm = (9-m)*0.3
	# 				ss = s*0.1
	# 				print mm, ss, expand(input_term, c, ss, mm)