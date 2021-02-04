string = 'My name is Niteesh Panchal'

alphabets_frequency = dict()

string1 = list(string.upper().replace(" ",""))
string2 = list()
for i in string1:
	alphabets_frequency[i] = string1.count(i)
	if i not in string2:
		string2.append(i)
	else:
		continue
minimum = sorted(alphabets_frequency.values())
minimum_values = [0]
for i in range(len(minimum)):
	if len(minimum) == len(minimum):
		x = minimum[0] + minimum[1]
		minimum_values.append(x)
		minimum.pop(i)
		minimum.pop(i+1)
	else:
		y = minimum[i]
		z = minimum_values[0] + x
		minimum_values[0] = z
		minimum.pop(i)
	print('i',i)
	print('x',x)
# print(string1)
# print(string2)
# print(alphabets_frequency)
print(minimum)
print(minimum_values)
