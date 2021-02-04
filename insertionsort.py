import random
# the function
def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	print(arr)
	return arr

arr = [9.8,1.5,6.8,3.5]
arr2 = [6.7,9.8,7,1,0.1]
# creating random number
# for i in range(1,10):
# 	random_value = random.randrange(float(-10),float(20))
# 	arr.append(random_value)
insertion_sort(arr2)	