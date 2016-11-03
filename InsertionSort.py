import random
my_array=random.sample(xrange(0,10000),100)
print my_array
def selection_sort(array=[]):
	for count in range(1,len(array)):
		position = count 
		number = array[position]
		

		while position > 0 and array[position-1] > number:
			array[position] = array[position-1]
			position = position - 1
			array[position] = number

			


		

selection_sort(my_array)
print my_array
