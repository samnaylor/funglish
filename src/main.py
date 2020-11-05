import os
import sys

from funglish import CodeGenerator

from funglish import tokenise
from funglish import Parser

from pprint import pprint

if __name__ == "__main__":
	file = open(sys.argv[1]).read()

	tokens = tokenise(file)
	# pprint(tokens)
	tree = Parser(tokens).start()

	# pprint(tree)

	# tree = FunglishParser.parse(file)
	# pprint(tree)
	code = CodeGenerator().generate(tree)

	open("./output.js", "w").write(code)
	os.system("node ./output.js")