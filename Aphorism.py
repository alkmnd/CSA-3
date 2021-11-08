from WellOfWisdom import WellOfWisdom


class Aphorism(WellOfWisdom):
	def __init__(self, author, content):
		super().__init__(content)
		self.author = author

	@property
	def author(self):
		return self.author

	@author.setter
	def author(self, value):
		self._author = value

	def to_string(self):
		return f"This is a aphorism: {self.content}\tAnswer: {self._author}\tValue of the function: {float('{:.3f}'.format(self.get_quotient()))}\n"
