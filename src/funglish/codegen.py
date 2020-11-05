class CodeGenerator:
    # if ident is assigned to multiple times, only use let on the first one

    def __init__(self):
        self.js = ""

        self.stack = []
        self.functions = {}

    def emit(self, line):
        self.js += f"{line}\n\n"

    def unknown_node(self, node):
        raise Exception(f"Unknown node type {node[0]}")

    def _generate(self, node):
        return getattr(self, node[0], self.unknown_node)(node)

    def generate(self, tree):
        for node in tree:
            self._generate(node)

        while self.stack:
            self.emit(self.stack.pop(0) + ";")

        return self.js.strip()

    def FUNCTION(self, node):
        fnameParts = node[1].split(" ")
        fname = fnameParts.pop(0) + "".join(
            list(map(lambda e: e.capitalize(), fnameParts))
        )

        for sub in node[2]:
            self._generate(sub)

        sig = f"var {fname} = (theInput) => {self.stack.pop()};"
        self.emit(sig)

    def VARIABLE(self, node):
        fnameParts = node[1].split(" ")
        fname = fnameParts.pop(0) + "".join(
            list(map(lambda e: e.capitalize(), fnameParts))
        )
        self.stack.append(fname)

    def ADD(self, node):
        self._generate(node[1])
        a, b = self.stack[-2:]
        del self.stack[-2:]
        self.stack.append(f"({a} + {b})")

    def SUB(self, node):
        self._generate(node[1])
        a, b = self.stack[-2:]
        del self.stack[-2:]
        self.stack.append(f"({a} - {b})")

    def MULTIPLY(self, node):
        self._generate(node[1])
        a, b = self.stack[-2:]
        del self.stack[-2:]
        self.stack.append(f"({a} * {b})")

    def DIVIDE(self, node):
        self._generate(node[1])
        a, b = self.stack[-2:]
        del self.stack[-2:]
        self.stack.append(f"Math.round({a} / {b})")

    def NUMBER(self, node):
        self.stack.append(node[1])

    def LOAD(self, node):
        self._generate(node[1])
        self.stack.append(
            f"{self.stack.pop()}()"
        )

    def CALL(self, node):
        self._generate(node[1])
        self.stack.append(
            f"{self.stack.pop()}({self.stack.pop() if self.stack else ''})"
        )

    def SHOW(self, node):
        self.stack.append(f"console.log({self.stack.pop()})")

    def TLS(self, node):
        for each in node[1]:
            self._generate(each)

        self.emit(self.stack.pop())
