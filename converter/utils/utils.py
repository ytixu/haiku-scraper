from nltk import word_tokenize
from nltk.corpus import stopwords
import itertools
import copy

# import nltk
# nltk.download('stopwords')


NLTK_STOPWORDS = set(stopwords.words('english'))
NLTK_STOPWORDS.update(['\'', '\"', ',', '.', '-', '!', '?', ':', ';',
	'\'s', '\'ll', '\'re', '\'d', '\'ve', '\'t'])

def tokenize(line):
	return word_tokenize(line)

def filter_stopwords(tokens):
	return [t for t in tokens if t not in NLTK_STOPWORDS]

def filter_punctuations(tokens):
	# filter the words ending with -
	return [t.strip('-') for t in tokens]

def parse(haiku):
	haiku = haiku.lower().replace('-', ' ')
	lines = haiku.split(' \\ ')
	tokened_lines = [filter_punctuations(tokenize(l)) for l in lines]
	return lines, tokened_lines, [filter_stopwords(l) for l in tokened_lines]

def make_combos(topics, lines, combos=[[]], words=[[]]):
	if len(topics) == 0:
		return combos

	new_combos = []
	new_words = []
	for i, combo in enumerate(combos):
		for topic in topics[0]:
			if topic not in words:
				new_combos.append(copy.copy(combo) + [(topic,lines[0])])
				new_words.append(copy.copy(words[i]) + [topic])

	return make_combos(topics[1:], lines[1:], new_combos, new_words)


def flatten_and_encode(pairs):
	return [x.encode('utf-8') for x in list(itertools.chain(*pairs))]
