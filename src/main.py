import os
import sys

from funglish import FunglishParser, CodeGenerator


if __name__ == "__main__":
	file = open(sys.argv[1]).read()
	tree = FunglishParser.parse(file)
	code = CodeGenerator().generate(tree)

	open("./output.js", "w").write(code)
	os.system("node ./output.js")