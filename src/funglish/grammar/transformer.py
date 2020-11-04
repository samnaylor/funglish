from lark import Transformer

class FunglishTransformer(Transformer):

    # track variable / function name usage here, multi use => let, single use => const

    def start(self, node):
        return node

    def mode(self, node):
        return ["MODE", node[0]]

    def toplevel(self, node):
        return node[0]

    def function(self, node):
        return ["FUNCTION", node[0].value, node[1]]

    def tls(self, node):
        return ["TLS", node[0]]

    def take_statement(self, node):
        return node[0]

    def statement(self, node):
        return node

    def show(self, node):
        return ["SHOW"]

    def statement_part(self, node):
        return node[0]

    def add(self, node):
        return ["ADD", node[0]]

    def sub(self, node):
        return ["SUB", node[0]]

    def mul(self, node):
        return ["MUL", node[0]]

    def div(self, node):
        return ["DIVIDE", node[0]]

    def number(self, node):
        return ["NUMBER", node[0].value]

    def variable(self, node):
        return ["VARIABLE", node[0].value]

    def call(self, node):
        return ["CALL", node[0]]

    def callnoargs(self, node):
        return ["LOAD", node[0]]