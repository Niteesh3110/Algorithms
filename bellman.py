def bellman(graph, u, v, src):
	vertex_value = [none] * v
	vertex_value[src] = 0
	for i in range(v - 1):
		for j in range(u):
			if vertex_value[graph[j][0]] + graph[j][2] < vertex_value[graph[j][1]]:
				vertex_value[graph[j][1]] = vertex_value[graph[j][0]] + graph[j][2]

	for i in range(u):
		x = graph[i][0]
		y = graph[i][1]
		weight = graph[i][2]
		if vertex_value[x] != none and vertex_value[x] + vertex_value[weight] < vertex_value[y]:
			print("graph contains negative weight cycle")

	print("Vertex distance from source")
	for i in range(v):
		print(i, vertex_value[i])

none = 0
v = 8 #vertices
path = []
graph = [
			[1,2,6],
			[1,3,5],
			[1,4,5],
			[2,5,-1],
			[3,2,-2],
			[3,5,1],
			[4,3,-2],
			[4,6,-1],
			[5,7,3],
			[6,7,3]
					]
graph2 = [[0, 1, -1], [0, 2, 4], [1, 2, 3], 
             [1, 3, 2], [1, 4, 2], [3, 2, 5],
             [3, 1, 1], [4, 3, -3]]
u = len(graph) #edges
bellman(graph, u, v, 0)


