import numpy as np
from utils import corpora, utils

CORPORA = {
# 			'glove_twitter_25': 0.8,
# 			'glove_twitter_50':0.7,
# 			'glove_wiki_50':0.6,
# 			'glove_wiki_100':0.5,
			'glove_haiku_50':(0.36, 0.05)}

def expand_topic(tp_list, thr):
	topics = corpora.glove_sim_ranks(tp_list, thr)
	topics = utils.filter_stopwords(topics)
	return np.random.choice(topics, 1)[0]

def expand(input_word, corpus):
	topics = corpora.get_topics(input_word.lower().split(), corpus)
	n = len(topics)
	thr = (CORPORA[corpus][0]+np.sqrt(CORPORA[corpus][1]), CORPORA[corpus][0]-np.sqrt(CORPORA[corpus][1]))
	if n == 2:
		w3 = expand_topic(topics, thr)
		return topics + [w3]

	if n == 1:
		w2 = expand_topic(topics, thr)
		w3 = expand_topic(topics+[w2], thr)
		return topics + [w2, w3]

	return []


if __name__ == '__main__':
	while True:
		input_term = raw_input("\nEnter word(s) (EXIT to break): ")
		if input_term == 'EXIT':
			break
		else:
			print expand(input_term, 'glove_haiku_50')
