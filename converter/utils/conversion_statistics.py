import numpy as np
import corpora

class statistics:

	def __init__(self):
		self.reset()

	def update(self, pairs, topics, tokened_lines, filtered_tokened_lines, corpus):
		self.total_haikus += 1.0
		self.total_entries += len(pairs)

		for i, tps in enumerate(topics):
			n = len(tokened_lines[i])*1.0
			self.lines_length[i] += n
			self.unnormalized_word_topic_ratio += len(tps) / n

			n = len(filtered_tokened_lines[i])*1.0
			self.unnormalized_word_topic_ratio_filtered += len(tps) / n

		corpus_name = corpus.split('_')[0]
		method = [func for name, func in corpora.__dict__.iteritems() if callable(func) and name.startswith('_'+corpus_name)][0]
		for combo in pairs:
			# NEED TO TEST WITH BOTH
			score = np.average([method(combo[inds[0]][0], combo[inds[1]][0]) for inds in [(0,1),(1,2)]])
			# score = method([combo[0][0], combo[1][0]], combo[2][0])
			self.association_score += score

	def print_stats(self, message_list=[]):
		print '\t'.join(message_list + map(str, [self.total_entries/self.total_haikus,
				self.unnormalized_word_topic_ratio/self.total_haikus/3,
				self.unnormalized_word_topic_ratio_filtered/self.total_haikus/3] + \
				[l/self.total_haikus for l in self.lines_length] + \
				[self.association_score/self.total_haikus]))

	def print_header(self, header_list=[]):
		print '\t'.join(header_list + ['Average haiku expansion',
			'Average word-to-topic ratio',
			'Average word-to-topic ratio (stopwords removed)',
			'Average line length (1)',
			'Average line length (2)',
			'Average line length (3)',
			'Average association score'])


	def reset(self):
		self.total_entries = 0.0
		self.total_haikus = 0.0
		self.unnormalized_word_topic_ratio = 0.0
		self.unnormalized_word_topic_ratio_filtered = 0.0
		self.association_score = 0.0

		self.lines_length = [0]*3