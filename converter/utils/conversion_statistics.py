class statistics:

	def __init__(self):
		self.reset()

	def update(self, pairs, topics, tokened_lines, filtered_tokened_lines):
		self.total_haikus += 1.0
		self.total_entries += len(pairs)

		for i, tps in enumerate(topics):
			n = len(tokened_lines[i])*1.0
			self.lines_length[i] += n
			self.unnormalized_word_topic_ratio += len(tps) / n

			n = len(filtered_tokened_lines[i])*1.0
			self.unnormalized_word_topic_ratio_filtered += len(tps) / n

	def print_stats(self, message = None):
		print '---'
		if message:
			print message
		print 'Average haiku expansion:', self.total_entries/self.total_haikus
		print 'Average word-to-topic ratio:', self.unnormalized_word_topic_ratio/self.total_haikus/3
		print 'Average word-to-topic ratio (stopwords removed):', self.unnormalized_word_topic_ratio_filtered/self.total_haikus/3
		print 'Average line length:', [l/self.total_haikus for l in self.lines_length]

	def reset(self):
		self.total_entries = 0.0
		self.total_haikus = 0.0
		self.unnormalized_word_topic_ratio = 0.0
		self.unnormalized_word_topic_ratio_filtered = 0.0

		self.lines_length = [0]*3