class Parser:
	def __init__(self, tokens):
		self.tokens = tokens

		self.tree = []

	def start(self):
		while self.tokens:
			top = self.tokens[0]

			if top.type == 'IDENTIFIER':
				self.function()
			else:
				self.tls()

		return self.tree

	def function(self):
		name = self.tokens.pop(0).value
		self.tree.append(["FUNCTION", name, self.take_statement()])

	def tls(self):
		self.tree.append(["TLS", self.statement()])

	def take_statement(self):
		assert self.tokens[0].type == "TAKE", f"Expected TAKE, got {self.tokens[0]}"
		self.tokens.pop(0)
		return self.statement()

	def statement(self):
		stmt = [self.statement_part()]

		while self.tokens[0].type != "EOS":
			if self.tokens[0].type != "COMMA":
				raise Exception(f"EXPECTED COMMA! got {self.tokens[0]}")

			self.tokens.pop(0)
			stmt.append(self.statement_part())
			
		self.tokens.pop(0)

		return stmt

	def statement_part(self):
		if self.tokens[0].type == "SHOW":
			self.tokens.pop(0)
			return ["SHOW"]
		elif self.tokens[0].type in ("ADD", "SUB", "MULTIPLY", "DIVIDE"):
			return self.maths()
		else:
			return self.expression()

	def maths(self):
		op = self.tokens.pop(0)
		if op.type in ("MULTIPLY", "DIVIDE"):
			assert self.tokens[0].type == "BY", f"Expected BY, got {self.tokens[0]}"
			self.tokens.pop(0)

		return [op.type, self.expression()]

	def expression(self):
		if self.tokens[0].type == "NUMBER":
			return ["NUMBER", self.tokens.pop(0).value]
		elif self.tokens[0].type == "IDENTIFIER":
			return ["VARIABLE", self.tokens.pop(0).value]

		elif self.tokens[0].type == "RUN":
			self.tokens.pop(0)
			return ["CALL", self.expression()]
		
		elif self.tokens[0].type == "LOAD":
			self.tokens.pop(0)
			return ["LOAD", self.expression()]