from nltk.corpus import wordnet as wn
from nltk.corpus import words

# import nltk
# nltk.download('words')


ENGLISH_VOCAB = set(w.lower() for w in words.words())

def from_wordnet(token):
	# return len(wn.synsets(token)) > 0
	return token in ENGLISH_VOCAB

def get_topics(tokens, corpus_name):
	return [t for t in tokens if globals()['from_'+corpus_name](t)]