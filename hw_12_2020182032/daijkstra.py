from city import cities
from edge import edges
import visualizer as vis
from collections import defaultdict
from heapdict import heapdict
from random import randrange

graph = defaultdict(dict)
final_costs = dict()
connects = dict()

def draw_all_edges():
	global graph
	vis.edge_line_color = (0.9, 0.9, 0.9)
	vis.edge_weight_color = (0.8, 0.8, 0.9)
	for beg, end, weight in edges:
		vis.draw_edge(cities[beg], cities[end], weight)
		# vis.edge_line_color = 'green'
		# vis.edge_weight_color = 'blue'

def setup():
	global graph
	for beg, end, weight in edges:
		graph[beg][end] = weight
		graph[end][beg] = weight

def main():
	setup()

	costs = heapdict()
	n_cities = len(cities)
	INF = float('inf')
	for i in range(n_cities):
		costs[i] = INF
			
	global start_index
	costs[start_index] = 0
	connects[start_index] = start_index

	while costs:
		added_city_index, added_city_cost = costs.popitem()
		final_costs[added_city_index] = added_city_cost
		added_city = cities[added_city_index]
		from_index = connects[added_city_index]
		draw_city(from_index, added_city_index, True)
		draw_anno(added_city_index, added_city_cost, True)

		for adj, cost in graph[added_city_index].items():
			if not adj in costs:
				continue
			updated_cost = added_city_cost + cost
			if updated_cost < costs[adj]:
				# print('update:', adj, costs[adj], '->', updated_cost)
				costs[adj] = updated_cost
				connects[adj] = added_city_index
				draw_city(added_city_index, adj)
				draw_anno(adj, '%d - %s' % (updated_cost, added_city.name))

	# print('------')
	# for index in range(n_cities):
	# 	cost = final_costs[index]
	# 	# print(city_path(index))
	# 	vis.draw_edge(cities[index], cities[connects[index]])
	# 	vis.draw_city(cities[index])
	# 	vis.draw_city_annotation(cities[index], 10, -15, cost)

update_counts = defaultdict(int)
def draw_anno(index, text, final = False):
	vis.city_anno_color = 'blue' if final else (0.9, 0.7, 0.7)
	city = cities[index]
	count = update_counts[index]
	if not final: count += 1
	dx, dy = 20, -15 * count
	# print(dx, dy, index, city.name, count, text)
	vis.draw_city_annotation(city, dx, dy, text)
	update_counts[index] = count

def draw_city(from_index, to_index, final = False):
	c1, c2 = cities[from_index], cities[to_index]
	if final:
		vis.city_circle_color = 'gray'
		vis.city_name_color = 'black'
		vis.city_anno_color = 'blue'
		vis.edge_line_color = 'green'
	else:
		vis.city_circle_color = (0.8, 0.8, 0.8)
		vis.city_name_color = (0.7, 0.7, 0.7)
		vis.city_anno_color = (0.9, 0.7, 0.7)
		vis.edge_line_color = (0.7, 0.9, 0.7)
	vis.draw_edge(c1, c2)
	vis.draw_city(c2)

def city_path(index):
	text = str(index)# + '.' + cities[index].name + ' ' + str(final_costs[index])
	origin = connects[index]
	if origin == index: return text
	return city_path(origin) + ' > ' + text

if __name__ == '__main__':
	global start_index
	# start_index = randrange(len(cities))
	start_index = 4
	vis.setup(cities)
	vis.city_anno_color = 'blue'
	vis.draw_title('Daijkstra Algorithm')
	vis.draw_title(cities[start_index].name, -15)
	vis.draw_city(cities[start_index])
	draw_all_edges()
	main()
	vis.wait()