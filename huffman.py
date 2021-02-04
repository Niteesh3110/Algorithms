string1 = 'My name is Niteesh Panchal'
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# const_frequency = dict{}
frequency = []
main_heap = []
min_heap = []
min_heap2 = []
alphabets_in_string = []
const_frequency = []
alphabets_frequency = dict()

def to_remove_multipe_occurance(arr1):
	for i in arr1:
		if i not in const_frequency:
			const_frequency.append(i)
		else:
			pass

	print('cf:',const_frequency)

def alphabetsInString(string):
	x = string.replace(" ","")
	list1 = list(x.upper())
	for i in list1:
		if i not in alphabets_in_string:
			alphabets_in_string.append(i)
		else:
			pass
	print(alphabets_in_string)
	print(len(alphabets_in_string))

def find_frequency(string):
	x = string.replace(" ","")
	list1 = list(x.upper())
	for i in alphabets:
		if i in list1:
			frequency.append(list1.count(i))
	print(frequency)
	print('len(frequency):',len(frequency))
	to_remove_multipe_occurance(frequency)

def huffman(string):
	find_frequency(string)
	frequency.sort()
	summition = frequency[0] + frequency[1]
	if summition < frequency[-1]:
		min_heap.append(summition)
		frequency.pop(0)
		frequency.pop(1)
		frequency.insert(1, summition)
	elif len(frequency) == 1:
		pass
	else:
		pass
	print(min_heap)
	print(min_heap2)
	print(frequency)
alphabetsInString(string1)
find_frequency(string1)
# huffman(string1)

