import re
import types
from bs4 import Comment

special_chars = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''


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

def remove_signatures(lines):
	if len(lines) == 0:
		return lines

	lines = re.sub(u'\-[\-\w ]+$', u'', lines)
	for i in range(3):
		lines = re.sub(u' [A-Z][A-Za-z]*.?$', u'', lines)
		lines = re.sub(' [A-Z][A-Za-z]*.?$', u'', lines)

	if lines[-1] == '\\':
		return lines[:-2]
	return lines

def clean_char(line):
	# line = line.lower()
	line = line.replace(u'\xe2', u'\'').replace(u'\u0027', u'\'').replace(u'\u2019', u'\'').replace(u'\u2018', u'\'')
	line = re.sub('&nbsp', u' ', line)
	line = re.sub(u'[^0-9a-zA-Z\n\.\' \-\,]+', u' ', line)
	return re.sub(u' {2,}', u' ', line)

def format(line):
	line = clean_char(line)
	lines = [l.strip() for l in line.split('\n') if len(l.strip()) > 0]
	if len(lines) < 3:
		return ''

	return u' \\ '.join(lines)

def clean(line):
	line = replace_with_newlines(line)
	# line = line.get_text()
	return format(line)

def special_char_ratio(text):
	if len(text) > 0:
		found_chars = [c for c in text if c in special_chars]
		counted_chars = len(found_chars)
		return counted_chars * 1.0 / len(text)

	return 0

def filter_special_char_line(text):
	return special_char_ratio(text) < 0.3

def filter_tweet(text):
	return '\n'.join([l for l in text.split('\n')
			if u'#' not in l
				and u'https:' not in l
				and u'http:' not in l
				and u'@' not in l
				and filter_special_char_line(l)])

def filter_and_break_lines(text):
	lines = filter_tweet(text)
	lines = re.findall(u'(?=.*[a-zA-Z]).+\n(?=.*[a-zA-Z]).+\n(?=.*[a-zA-Z]).+', lines)
	if len(lines) == 1:
		lines = [clean_char(l).strip() for l in lines[0].split('\n')]

	if len(lines) != 3:
		return ''

	return u' \\ '.join(lines)


def break_lines(line):
	lines = line.split(u'/')
	lines = [clean_char(l).strip() for l in lines]

	if len(lines) != 3:
		return ''
	return u' \\ '.join(lines)

def filter_haikus(haiku):
	if len(haiku.split('\\')) != 3:
		return False

	return True