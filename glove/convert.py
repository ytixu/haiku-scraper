import sys
import re
import csv
import argparse
from nltk import word_tokenize

# terminal argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--paired', help='Paired lines', action='store_true')
args = parser.parse_args()


# with open('limericks.csv') as csvfile:
# 	spamreader = csv.reader(csvfile)
# 	for line in spamreader:
# 		# sentence segment
# 		print line[0].strip('\n').replace('\n', ' \\ ')

		# words = word_tokenize(line[0].lower())
		# words = [w for w in words if re.match('.+[a-z].+', w)]
		# print ' '.join(words)

for line in sys.stdin:
	if args.paired:
		# pair up lines
		words = [word_tokenize(l) for l in line.lower().split(' \\ ')]
		words = [[w.strip('-') for w in l if re.match('.*[a-z0-9].*', w)]+['<ENDLINE>'] for l in words]
		for i,_ in enumerate(words[:-1]):
			print ' '.join(words[i] + words[i+1])
	else:
		# just lower case
		words = word_tokenize(line.lower())
		words = [w.strip('-') for w in words if re.match('.+[a-z].+', w)]
		print ' '.join(words)

