from WellOfWisdom import WellOfWisdom


class Proverb(WellOfWisdom):
	def __init__(self, country, content):
		super().__init__(content)
		self.country = country

	@property
	def country(self):
		return self.country

	@country.setter
	def country(self, value):
		self._country = value

	def to_string(self):
		return f"This is a proverb: {self.content}\tAnswer: {self._country}\tValue of the function: {float('{:.3f}'.format(self.get_quotient()))}\n"
