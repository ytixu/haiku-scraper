import csv
import glob

def read(filename):
	with open('data/'+filename+'.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			print row[0].decode('utf-8')

def get_all_files():
	files = glob.glob('data/*.csv')
	files.extend(glob.glob('data/*.txt'))
	return files

def get_all_outputs():
	return glob.glob('output/*.txt')

def read_lines(filename):
	with open(filename, 'r') as fileobj:
		if filename.split('.')[-1] == 'csv':
			spamreader = csv.reader(fileobj)
			for row in spamreader:
				yield row[0].decode('utf-8')
		else:
			for row in fileobj.readlines():
				yield row.decode('utf-8')

if __name__ == '__main__':
	read('twitter_haiku')