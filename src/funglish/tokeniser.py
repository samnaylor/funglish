from string import digits, ascii_letters, whitespace
from collections import namedtuple

Token = namedtuple('Token', 'type, value')

def tokenise(source):
	tokens = []

	keywords = {
		'take': 'TAKE',
		'show': 'SHOW',
		'add': 'ADD',
		'subtract': 'SUB',
		'multiply': 'MULTIPLY',
		'divide': 'DIVIDE',
		'by': 'BY',
		'run': 'RUN',
		'load': 'LOAD',
	}

	pos = 0

	identifier = ''
	number = ''

	while pos < len(source):
		if source[pos] in ascii_letters:
			while source[pos] != '\n' and source[pos] in ascii_letters + ' ':
				identifier += source[pos]
				pos += 1
				if identifier in keywords.keys():
					break
			
			tokens.append(Token(keywords.get(identifier, 'IDENTIFIER'), identifier))
			identifier = ''

		elif source[pos] in digits:
			while source[pos] in digits + '_':
				number += source[pos]
				pos += 1
			
			tokens.append(Token('NUMBER', number))
			number = ''

		elif source[pos] == ',':
			tokens.append(Token('COMMA', ','))
			pos += 1
		
		elif source[pos] == '.':
			tokens.append(Token('EOS', '.'))
			pos += 1

		elif source[pos] == '#':
			while source[pos] != '\n' and pos < len(source) -1:
				pos += 1
			pos += 1
		
		elif source[pos] in whitespace:
			pos += 1

	return tokens