from city import cities
import random
import math
from functools import cmp_to_key
import visualizer as vis

def main():

	print('Edge maker')
	edge_set = set()

	max_dist = min(vis.diff_x, vis.diff_y) / 4

	n_cities = len(cities)
	for c in range(n_cities):
		city = cities[c]

		n, nn, count = 0, 0, random.randint(2, 4)
		while n < count:
			t = random.randrange(n_cities)
			nn += 1
			if nn > 100:
				print('Too many tries on', c, city.name)
				break
			if t == c : continue
			c1, c2 = (c, t) if c < t else (t, c)
			dist = distance(city, cities[t])
			# print(dist)
			if dist > max_dist: continue
			edge_set.add((c1, c2))
			n += 1

	edge_list = list(edge_set)
	edge_list.sort(key=cmp_to_key(edge_compare))
	# print(edge_list, len(edge_list))
	edges = []
	for c, t in edge_list:
		dist = distance(cities[c], cities[t])
		int_dist = int(dist * random.uniform(0.5, 1.5) / 100 )
		edges.append((c, t, int_dist))

	# print(edges, len(edges))

	for city in cities:
		vis.draw_city(city)

	for c,t,dist in edges:
		vis.draw_edge(cities[c], cities[t], dist)
		print(' ' + str((c, t, dist)) + ',')


def distance(c, t):
	dx, dy = c.x - t.x, c.y - t.y
	dist_sq = dx ** 2 + dy ** 2
	return math.sqrt(dist_sq)

def edge_compare(a, b):
	if a[0] == b[0]: return a[1] - b[1]
	return a[0] - b[0]

if __name__ == '__main__':
	vis.setup(cities)
	random.seed('KPU Game 2021')
	main()
	vis.wait()