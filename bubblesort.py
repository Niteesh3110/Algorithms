def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(1,len(arr)):
			if arr[i] > arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			elif arr.sort():
				break
			else:
				continue
	print(arr)
	return arr

arr = [1,5,4,7,2]

bubble_sort(arr)


