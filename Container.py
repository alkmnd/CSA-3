import random

from Aphorism import Aphorism
from Proverb import Proverb
from Puzzle import Puzzle

# генерация рандомной строки.
def get_random_string(is_content=True):
	if is_content:
		letters = "qwertyuiopasdfghjklzxcvbnm1234567890.,!?:"
	else:
		letters = "qwertyuiopasdfghjklzxcvbnm"
	length = random.randint(1, 20)
	rand_string = ''.join(random.choice(letters) for _ in range(length))
	return rand_string

# Класс описывает контейнер.
class Container:
	container = []
	MAX_SIZE = 10000

	def __init__(self):
		self._size = 0

	# Получение размера контейнера.
	@property
	def size(self):
		return self._size

	# Рандомное заполнение контейнера.
	def fill_randomly(self, count):
		for i in range(0, count):
			type_of_object = random.randint(0, 2)
			well_of_wisdom = None
			if type_of_object == 0:
				well_of_wisdom = Aphorism(get_random_string(False), get_random_string(True))
			elif type_of_object == 1:
				well_of_wisdom = Proverb(get_random_string(False), get_random_string(True))
			elif type_of_object == 2:
				well_of_wisdom = Puzzle(get_random_string(False), get_random_string(True))
			if self.size < Container.MAX_SIZE:
				self.container.append(well_of_wisdom)
				self.size += 1

	# Запись содержимого контейнера в файл.
	def write(self, output_file):
		for i in range(0, self.size):
			output_file.write(f"{i + 1}. {self.container[i].to_string()}")

	# Считывания данных для заполнения контейнера.
	def read(self, input_file):
		count = 0
		try:
			count = int(input_file.readline())
		except ValueError:
			return
		for i in range(0, count):
			type_of_object = input_file.readline()
			content = input_file.readline()
			type_content = input_file.readline()
			if len(content) == 0:
				raise ValueError()
			well_of_wisdom = None
			if int(type_of_object) == 0:
				well_of_wisdom = Aphorism(type_content, content)
			elif int(type_of_object) == 1:
				well_of_wisdom = Proverb(type_content, content)
			elif int(type_of_object) == 2:
				well_of_wisdom = Puzzle(type_content, content)
			else:
				raise ValueError()
			if self.size < Container.MAX_SIZE:
				self.container.append(well_of_wisdom)
				self.size += 1

	# Изменение значения размера.
	@size.setter
	def size(self, value):
		self._size = value
