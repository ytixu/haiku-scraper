from reader.reader import read_lines, get_all_files

if __name__ == '__main__':
	files = get_all_files()
	for haiku_file in files:
		for haiku in read_lines(haiku_file):
			print haiku.strip('\n')