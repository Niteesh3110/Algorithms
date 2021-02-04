def relaxation(x):
	for i in range(len(graph)):
		if graph[x][i] > 0:
			adj_vertex = graph[x].index(graph[x][i])
			if dist[adj_vertex] == 0 or dist[adj_vertex] > graph[x][i]:
				dist[adj_vertex] = graph[x][i]
				key.append(graph[x][i])
				print("Edge value",graph[x][i])
				print('adj_vertex',adj_vertex)
				print(dist)

def min_node():
	minimum = min(key)
	print('min',minimum)
	mstset.append(dist.index(minimum))


def print_mstset():
	print(mstset)

def prims(graph):
	parent[0] = -1
	dist[0] = 0
	mstset[0] = 0
	for i in range(vertices):
		print('i',i) 
		if i != 0:
			u = dist[i] #value of the node
			print(dist,' ',u)
			v = dist.index(u) #index of the node
			print('v', v)
			next_node = mstset[-1]
			if v not in mstset or v == next_node:
				relaxation(i)
				min_node()
				print('mstset',mstset)
			else:
				continue
		else:
			print('FIRST')
			relaxation(i)
			min_node()
	print(dist)
	print_mstset()






graph = [
			[0,4,0,0,0,0,0,8,0],
			[4,0,8,0,0,0,0,11,0],
			[0,8,7,0,0,0,0,0,2],
			[0,0,7,0,9,14,0,0,0],
			[0,0,0,9,0,10,0,0,0],
			[0,0,4,14,10,0,2,0,0],
			[0,0,0,0,0,2,0,1,6],
			[8,11,0,0,0,0,1,0,7],
			[0,0,2,0,0,0,6,7,0]
		]
vertices = len(graph)
mstset = [0]
dist = [0] * vertices
parent = [0]
key = []
prims(graph)
