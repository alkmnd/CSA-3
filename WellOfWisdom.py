import string


class WellOfWisdom:
	def __init__(self, content):
		self.content = content

	@property
	def content(self):
		return self._content

	def get_quotient(self):
		counter = 0
		for i in range(0, len(self.content)):
			if self.content[i] in string.punctuation:
				counter = counter + 1
		return counter / len(self.content)

	@content.setter
	def content(self, value):
		self._content = value
