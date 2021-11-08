# Функция для сортировки.
def merge_sort(array):
	if len(array) == 1 or len(array) == 0:
		return array
	left, right = array[:len(array) // 2], array[len(array) // 2:]
	merge_sort(left)
	merge_sort(right)
	n = m = k = 0
	c = [0] * (len(left) + len(right))
	while n < len(left) and m < len(right):
		if left[n].get_quotient() <= right[m].get_quotient():
			c[k] = left[n]
			n += 1
		else:
			c[k] = right[m]
			m += 1
		k += 1
	while n < len(left):
		c[k] = left[n]
		n += 1
		k += 1
	while m < len(right):
		c[k] = right[m]
		m += 1
		k += 1
	for i in range(len(array)):
		array[i] = c[i]
	return array
