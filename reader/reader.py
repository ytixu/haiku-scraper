import csv

def read(filename):
	with open('data/'+filename+'.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print row[0].decode('utf-8')


if __name__ == '__main__':
	read('twitter_haiku')