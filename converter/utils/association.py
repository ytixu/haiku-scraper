import numpy as np
import corpora


def get_method(corpus_name):
	return [func for name, func in corpora.__dict__.iteritems() if callable(func) and name.startswith('_'+corpus_name)][0]

def average_association(corpus, pairs, mode='avg', get_list=False):
	corpus_name = corpus.split('_')[0]
	method = get_method(corpus_name)
	ass_score = np.zeros(len(pairs))

	for i, combo in enumerate(pairs):
		score = 0
		if mode != 'add':
			score = np.average([method(combo[inds[0]][0], combo[inds[1]][0]) for inds in [(0,1),(1,2)]])

		if mode != 'avg':
			score = np.max([score] + [method([combo[inds[0]][0], combo[inds[1]][0]], combo[inds[2]][0])
						for inds in [(0,1,2), (0,2,1), (1,2,0)]])

		ass_score[i] = score

	if get_list:
		return ass_score

	return np.average(ass_score)

def vector_association(corpus, pairs):
	return average_association(corpus, pairs, 'add')

def get_avg_associations(corpus, pairs):
	return average_association(corpus, pairs, 'avg', True)

def get_vec_associations(corpus, pairs):
	return average_association(corpus, pairs, 'add', True)

def comb_vec_associations(corpus, pairs):
	return average_association(corpus, pairs, 'comb', True)