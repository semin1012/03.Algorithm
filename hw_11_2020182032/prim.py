from city import cities
from edge import edges
import mkedge as draw_util
from collections import defaultdict
from random import randrange
import visualizer as vis

from heapdict import heapdict
# pip install heapdict

graph = defaultdict(dict)
costs = heapdict()
connects = dict()
total_cost = 0

def setup():
	global graph
	for beg, end, weight in edges:
		graph[beg][end] = weight
		graph[end][beg] = weight
	print(graph)

def main():
	setup()

	MST = []
	n_cities = len(cities)
	global start_index
	print('start_index:', start_index)
	
	inf = float('inf')
	start_edges = graph[start_index]
	for i in range(n_cities):
		if i in start_edges:
			costs[i] = start_edges[i]
			connects[i] = start_index
		else:
			costs[i] = inf
			connects[i] = None

	# print('graph:', graph)
	# print('costs:', costs)
	# print('connects:', connects)

	vis.draw_city(cities[start_index])

	global total_cost
	while costs:
		v_nearest, cost = costs.popitem()
		# print('v_nearest:', v_nearest, 'costs:', cost)
		v_in_mst = connects[v_nearest]

		MST.append((v_in_mst, v_nearest, cost))
		total_cost += cost

		c1 = cities[v_in_mst]
		c2 = cities[v_nearest]
		w = graph[v_in_mst][v_nearest]
		print(c1.name, '->', c2.name, '+'+str(cost), '='+str(total_cost))
		vis.draw_city(c2)
		vis.draw_edge(c1, c2, w)

		for v_adj, adj_cost in graph[v_nearest].items():
			if v_adj in costs and adj_cost < costs[v_adj]:
				costs[v_adj] = adj_cost
				connects[v_adj] = v_nearest

if __name__ == '__main__':
	global start_index
	start_index = randrange(len(cities))
	vis.setup(cities)
	vis.draw_title('Prim Algorithm')
	vis.draw_title(cities[start_index].name, -15)
	main()
	vis.draw_title('Cost: ' + str(total_cost), -30)
	vis.wait()