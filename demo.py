a = "1"
b = "0"
d = "DEAD"
i = 0
j = 0

State = 0

inp = str(input("ENTER THE STRING: "))

list = []
list[:0] = inp

def to_check_string_starts_end_with_ab(list):
	if(list[0] == a and list[1] == b and list[-1] == b and list[-2] == a):
		print("String is accepted by the finite automata")
	else: 
		print('string not accepted')

def to_check_string_contains_ab(list):
	if(a,b in list):
		print("String is accepted by the finite automata")
	else:
		print("String not accepted")

def to_check_string_ends_with_ab(list):
	if(list[-1] == b and list[-2] == a):
		print("String is accepted by the finite automata")
	else:
		print("String not accepted")

def to_check_string_starts_with_ab(list):
	if(list[0] == a and list[1] == b):
		print("String is accepted by the finite automata")
	else:
		print("String not accepted")

def to_check_string_should_contain_pattern_ab(list):
	x = 0
	j = 0
	for i in list:
		while(j < int(len(list))):
			if(j == 0):
				if(list[j] == a):
					j = j + 1
					continue
				else:
					pass
			if(j % 2 == 0):
				if(list[j] == a):
					j = j + 1
				else:
					x = 1
					break

			else:
				if(list[j] == b):
					j = j + 1
				else:
					x = 1
					break
	if x == 1:
		print("String not accepted by finite automata")
	else:
		print("String is accepted by finite automata")


def to_check(list):
	i = 0
	j = 0
	for j in list:
		while i < 5:
			print("String starting with ab")
			to_check_string_starts_with_ab(list)
			i = i + 1
			print("String ending with ab")
			to_check_string_ends_with_ab(list)
			i = i + 1
			print("String contains ab")
			to_check_string_contains_ab(list)
			i = i + 1
			print("String should contain a pattern ab")
			to_check_string_should_contain_pattern_ab(list)
			i = i + 1
			print("String starts and ends with ab")
			to_check_string_starts_end_with_ab(list)
			i = i + 1

to_check(list)




