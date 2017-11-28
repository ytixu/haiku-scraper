import numpy as np
from nltk.corpus import wordnet as wn
from nltk.corpus import words

# import nltk
# nltk.download('words')


ENGLISH_VOCAB = set(w.lower() for w in words.words())
GLOVE_WORDS = None

GLOVE_FILE_IDX = 0
GLOVE_FILE_DIM = 0
GLOVE_FILES = ['./corpora/glove.twitter.27B/glove.twitter.27B.DIMd.txt',
				'./corpora/glove.6B/glove.6B.DIMd.txt',
				'./corpora/glove.42B.300d.txt',
				'./corpora/glove.haiku.50d.txt']

def from_wordnet(token):
	# return len(wn.synsets(token)) > 0
	return token in ENGLISH_VOCAB

def get_topics(tokens, corpus_name):
	return [t for t in tokens if globals()['from_'+corpus_name](t)]

def _wordnet_sim_score(ta, tb):
	sa = wn.synsets(ta)
	sb = wn.synsets(tb)
	sims = [ssa.path_similarity(ssb) for ssa in sa for ssb in sb]
	if len(sims) == 0:
		return 0
	return max(map(lambda x: 0 if x is None else x, sims))
	# return np.amax([[
	# 	ssa.path_similarity(ssb),
	# 	# ssa.lch_similarity(ssb),
	# 	# ssa.wup_similarity(ssb),
	# 	# ssa.res_similarity(ssb),
	# 	# ssa.jcn_similarity(ssb),
	# 	# ssa.lin_similarity(ssb)
	# ] for ssa in sa for ssb in sb], axis=0)


# taken form the glove repo

def from_glove(token, file_idx=None, dim=0):
	global GLOVE_WORDS, GLOVE_FILE_IDX, GLOVE_FILES, GLOVE_FILE_DIM
	if GLOVE_FILE_IDX != file_idx or GLOVE_FILE_DIM != dim:
		GLOVE_FILE_IDX = file_idx
		GLOVE_FILE_DIM = dim
		GLOVE_WORDS = None

	if GLOVE_WORDS is None:
		words = []
		vectors = {}
		filename = GLOVE_FILES[GLOVE_FILE_IDX]
		if GLOVE_FILE_DIM > 0:
			filename = filename.replace('DIM', str(GLOVE_FILE_DIM))

		with open(filename, 'r') as f:
			for line in f:
				vals = line.rstrip().split(' ')
				vectors[vals[0]] = [float(x) for x in vals[1:]]
				words.append(vals[0])

		vocab_size = len(words)
		vocab = {w: idx for idx, w in enumerate(words)}
		ivocab = {idx: w for idx, w in enumerate(words)}

		vector_dim = len(vectors[ivocab[0]])
		W = np.zeros((vocab_size, vector_dim))
		for word, v in vectors.items():
			if word == '<unk>':
				continue
			W[vocab[word], :] = v

		# normalize each word vector to unit variance
		W_norm = np.zeros(W.shape)
		d = (np.sum(W ** 2, 1) ** (0.5))
		W_norm = (W.T / d).T
		GLOVE_WORDS = (W_norm, vocab, ivocab)
		return token in vocab

	else:
		return token in GLOVE_WORDS[1]

def glove_random_word(n=1):
	# assume all params are set
	return np.random.choice(GLOVE_WORDS[1].keys(), n)

def from_glove_twitter_25(token):
	return from_glove(token, 0, 25)

def from_glove_twitter_50(token):
	return from_glove(token, 0, 50)

def from_glove_twitter_100(token):
	return from_glove(token, 0, 100)

def from_glove_twitter_200(token):
	return from_glove(token, 0, 200)

def from_glove_wiki_50(token):
	return from_glove(token, 1, 50)

def from_glove_wiki_100(token):
	return from_glove(token, 1, 100)

def from_glove_wiki_200(token):
	return from_glove(token, 1, 200)

def from_glove_wiki_300(token):
	return from_glove(token, 1, 300)

def from_glove_crawl_300(token):
	return from_glove(token, 2)

def from_glove_haiku_50(token):
	return from_glove(token, 3)

def __glove_vector(ta_list, W, vocab, ivocab):
	for idx, term in enumerate(ta_list):
		if term in vocab:
			if idx == 0:
				vec_result = np.copy(W[vocab[term], :])
			else:
				vec_result += W[vocab[term], :]
		else:
			return 0

	vec_norm = np.zeros(vec_result.shape)
	d = (np.sum(vec_result ** 2,) ** (0.5))
	vec_norm = (vec_result.T / d).T

	return vec_norm

def _glove_sim_score(ta_list, tb):
	global GLOVE_WORDS
	W, vocab, ivocab = GLOVE_WORDS

	if type(ta_list) == type('s') or type(ta_list) == type(u's'):
		ta_list = [ta_list]

	if tb not in vocab:
		return 0

	vec_norm = __glove_vector(ta_list, W, vocab, ivocab)
	return np.dot(W[vocab[tb]], vec_norm.T)

def glove_sim_ranks(ta_list, thr):
	global GLOVE_WORDS
	W, vocab, ivocab = GLOVE_WORDS
	vec_norm = __glove_vector(ta_list, W, vocab, ivocab)
	dist = np.dot(W, vec_norm.T)

	for term in ta_list:
		index = vocab[term]
		dist[index] = -np.Inf

	a = np.argsort(-dist)
	max_idx, min_idx = 0, 0
	thr_max, thr_min = thr
	for i, x in enumerate(a):
		if dist[x] > thr_max:
			max_idx  = i+1
		if dist[x] < thr_min:
			min_idx = i-1
			break

	return [ivocab[x] for x in a[max_idx:min_idx]]