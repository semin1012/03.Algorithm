import heapq

mygraph = {
	'A':{'B':8, 'C':1, 'D':2},
	'B':{},
	'C':{'B':5, 'D':2},
	'D':{'E':3, 'F':5},
	'E':{'F':1},
	'F':{'A':5}
}

def dijkstra(graph, start):
	# 초기화
	distances = { node:float('inf') for node in graph}
	distances[start] = 0
	queue = []
	heapq.heappush(queue, [distances[start], start]) # [ 0, 'A' ]

	# 반복문
	while queue:
		cur_route_distance, cur_node = heapq.heappop(queue)

		if distances[cur_node] < cur_route_distance:
			print(cur_node, distances[cur_node], cur_route_distance)
			continue

		for adjacent, weight in graph[cur_node].items():
			distance = cur_route_distance + weight

			if distance < distances[adjacent]:
				distances[adjacent] = distance
				heapq.heappush(queue, [distance, adjacent])

	return distances

print(dijkstra(mygraph, 'A'))