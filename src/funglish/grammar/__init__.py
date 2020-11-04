import os.path

from lark import Lark
from .transformer import FunglishTransformer

# something to do with paths and imports and stuff :)

path = os.path.join(
	os.path.dirname(os.path.abspath(__file__)),
	"grammar.lark"
)

FunglishParser = Lark.open(path, transformer = FunglishTransformer(), parser = "lalr")