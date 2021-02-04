# to register meeting schedule and to adjust new meeting in between free time
meetings = [[]]
def add_meeting():
	i = 0
	j = 0
	flag = True
	while(flag == True):
		start_time = input("Enter the start time: ")
		end_time = input("Enter the end time: ")
		meetings[0][0].append(start_time)
		j += 1
		meetings[i][j].append(end_time)
		i += 1
		j -= 1
		print(meetings)

add_meeting()

