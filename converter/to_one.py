from reader.reader import read_lines, get_all_files
import re

if __name__ == '__main__':
	files = get_all_files()
	for haiku_file in files:
		for haiku in read_lines(haiku_file):
			haiku = haiku.replace(u'\xe2', u'\'').replace(u'\u0027', u'\'').replace(u'\u2019', u'\'').replace(u'\u2018', u'\'')
			haiku = re.sub('&nbsp', u' ', haiku)
			lines = haiku.split('\\')
			haiku = '\\'.join([re.sub(u'[^0-9a-zA-Z\n\.\' \-\,]+', u' ', l) for l in lines])
			print haiku.strip('\n')