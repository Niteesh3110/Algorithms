# function printing the matrix
def print_matrix(arr3):
	for i in arr3:
		print(i)
# function to make numm matrix for multipliction
def to_make_null_matrix_for_mul(arr1, arr2):
	global arr4
	n1 = len(arr1)
	m1 = len(arr1[0])
	n2 = len(arr2)
	m2 = len(arr2[0]) 
	arr4 = [0] * n2
	for i in range(n2):
		arr4[i] = [0] * m1
	return arr4
# function to make null matrix
def to_make_null_matrix(arr1, arr2):
	global arr3
	n = len(arr1) 
	m = len(arr1[0])
	arr3 = [0] * n 
	for i in range(n):
		arr3[i] = [0] * m
	return arr3
# function for addtion of matix
def add_matrix(arr1, arr2):
	to_make_null_matrix(arr1, arr2)
	if len(arr1) == len(arr2):
		for i in range(len(arr1)):
			for j in range(len(arr1[0])):
				arr3[i][j] = arr1[i][j] + arr2[i][j] 
	print_matrix(arr3)
 	return arr3
# function for subtraction of matirx
def sub_matrix(arr1, arr2):
	to_make_null_matrix(arr1, arr2)
	if len(arr1) == len(arr2):
		for i in range(len(arr1)):
			for j in range(len(arr1[0])):
				arr3[i][j] = arr1[i][j] - arr2[i][j] 
	print_matrix(arr3)
	return arr3
# function for multiplication of matix
def mul_matrix(arr1, arr2):
	n1 = len(arr1)
	m1 = len(arr1[0])
	n2 = len(arr2)
	m2 = len(arr2[0])
	if n1 == m2:
		to_make_null_matrix_for_mul(arr1, arr2)
		for i in range(n1):
			for j in range(m2):
				for k in range(n2):
					arr4[i][j] += arr2[k][j] * arr1[i][k]
		print_matrix(arr4)
def create_matrix(n,m):
	

arr1 = [[1,2,3,4],
		[2,3,4,5],
		[3,4,2,1]]

arr2 = [[3,4,5,2],
		[2,3,4,5],
		[3,4,2,3]]

matrix1 = [[1, 2, 3],
			[4, 5, 6]]

matrix2 = [[7, 8],
			[9, 10],
			[11, 12]]

print('sub: ')
sub = sub_matrix(arr1, arr2)
print('mul')
mul = mul_matrix(matrix1, matrix2)