import sys
def floyd(graph, vertex):
	intermediate = 0
	while vertex != intermediate:
		for i in range(len(graph)):
			for j in range(len(graph)):
				if i == j:
					graph[i][j] = 0
				elif i == intermediate or j == intermediate:
					pass
				elif graph[i][j] < graph[i][intermediate] + graph[intermediate][j]:
					graph[i][j] = graph[i][j]
				elif graph[i][j] > graph[i][intermediate] + graph[intermediate][j]:
					graph[i][j] = graph[i][intermediate] + graph[intermediate][j]
				else:
					pass
		intermediate += 1
	for i in range(len(graph)):
		print(graph[i])
		
vertex = 4
inf = sys.maxsize
graph = [
			[0,3,inf,7],
			[8,0,2,inf],
			[5,inf,0,1],
			[2,inf,inf,0]
				]
floyd(graph, vertex)
