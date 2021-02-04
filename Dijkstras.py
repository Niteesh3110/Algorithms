inf = float('inf')
start = 'A'
stop = 'D'
graph = {}
graph['A'] = {}
graph['A']['B'] = 2
graph['A']['F'] = 3

graph['B'] = {}
graph['B']['C'] = 7

graph['C'] = {}
graph['C']['D'] = 1

graph['F'] = {}
graph['F']['E'] = 3

graph['E'] = {}
graph['E']['D'] = 5

graph['D'] = {}

costs = {}
parents = {}
for node in graph:
	costs[node] = inf
	parents[node] = {}

costs[start] = 0

def find_cheapest_node(costs, not_checked):
	cheapest_node = None
	lowest_cost = inf
	for node in not_checked:
		if costs[node] <= lowest_cost:
			lowest_cost = costs[node]
			cheapest_node = node
	return cheapest_node

if __name__ == '__main__':
	not_checked = [node for node in costs]
	node = find_cheapest_node(costs, not_checked)
	while not_checked:
		print(f"Not checked: {not_checked}")
		cost = costs[node]
		child_cost = graph[node]
		for c in child_cost:
			if costs[c] > cost + child_cost[c]:
				costs[c] = cost + child_cost[c]
				parents[c] = node

		not_checked.pop(not_checked.index(node))
		node = find_cheapest_node(costs, not_checked)

	print(f"Costs: {costs}")
	print(f"The cost to go from {start} to {stop} is {costs[stop]}!")

	if costs[stop] < inf:
		path = [stop]
		i = 0
		while start not in path:
			path.append(parents[path[i]])
			i += 1

		print(f"The shortest path is: {path[::-1]}")
	else:
		print(f"A path could not be found")