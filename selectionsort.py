import random
# the function
def selection_sort(arr):
	unsorted_arr = arr
	sorted_arr = []
	minimum_value = 0
	for i in range(len(arr)):
		minimum_value = min(arr)
		sorted_arr.append(minimum_value)
		arr.remove(minimum_value)
	print(sorted_arr)
	return sorted_arr
# array
arr = [-1,8,3,4,-5,9]
# Creating random number
# for i in range(1,10):
# 	random_number = random.randrange(1,20)
# 	arr.append(random_number)
selection_sort(arr)