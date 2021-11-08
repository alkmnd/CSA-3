from WellOfWisdom import WellOfWisdom


# Класс описывает афоризм.
class Aphorism(WellOfWisdom):
	# Конструктор класса.
	def __init__(self, author, content):
		super().__init__(content)
		self.author = author

	# Получение значения author.
	@property
	def author(self):
		return self.author

	# Присвоение нового значения author.
	@author.setter
	def author(self, value):
		self._author = value

	# Метод для представления афоризма в виде строки.
	def to_string(self):
		return f"This is a aphorism: {self.content}\tAnswer: {self._author}\tValue of the function: {float('{:.3f}'.format(self.get_quotient()))}\n "
