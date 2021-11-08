from WellOfWisdom import WellOfWisdom


class Puzzle(WellOfWisdom):
	def __init__(self, answer, content):
		super().__init__(content)
		self.answer = answer

	@property
	def answer(self):
		return self.answer

	@answer.setter
	def answer(self, value):
		self._answer = value

	def to_string(self):
		return f"This is a puzzle: {self.content}\tAnswer: {self._answer}\tValue of the function: {float('{:.3f}'.format(self.get_quotient()))}\n"

