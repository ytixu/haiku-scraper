import re
import types
from bs4 import BeautifulSoup, Comment

def replace_with_newlines(element):
	text = ''
	for elem in element.recursiveChildGenerator():
		if isinstance(elem, Comment):
			continue
		if isinstance(elem, types.StringTypes):
			text += elem.strip()
		elif elem.name == 'br':
			text += '\n'
	return text

def clean_char(line):
	# line = line.lower()
	line = re.sub('&nbsp', u' ', line)
	line = re.sub(u'[^0-9a-zA-Z\n\.\' \-\,]+', u' ', line)
	return re.sub(u' {2,}', u' ', line)

def clean(line):
	line = replace_with_newlines(line)
	# line = line.get_text()
	line = clean_char(line)
	lines = [l.strip() for l in line.split('\n') if len(l) > 0]
	if len(lines) < 3:
		return ''

	return u' \\ '.join(lines)

def break_lines(line):
	lines = line.split(u'/')
	lines = [clean_char(l).strip() for l in lines]

	if len(lines) != 3:
		return ''
	return u' \\ '.join(lines)

def filter_haikus(haiku):
	if len(haiku) < 3:
		return False

	return True