from city import cities
from edge import edges
import visualizer as vis

roots = []
def union(u, v):
	global roots
	uroot = find_root(u)
	vroot = find_root(v)
	roots[vroot] = uroot

def find_root(u):
	global roots
	if u != roots[u]:
		roots[u] = find_root(roots[u])
	return roots[u]

def main():
	vertex_count = len(cities)

	global roots
	roots = [x for x in range(vertex_count)]
	print(roots)

	weight_edges = sorted(edges, key=lambda e: e[2])

	MST = []
	total_cost = 0

	while len(MST) < vertex_count - 1:
		u, v, w = weight_edges.pop(0)
		if find_root(u) == find_root(v):
			continue

		if u > v: u, v = v, uroot

		c1, c2 = cities[u], cities[v]
		total_cost += w

		MST.append((u, v))

		draw_city(c1)
		draw_city(c2)
		vis.draw_edge(c1, c2, w)

		print(c1.name, '->', c2.name, '+'+str(w), '='+str(total_cost))

		union(u, v)

drawn_cities = set()
def draw_city(city):
	global drawn_cities
	if city.name in drawn_cities:
		return
	vis.draw_city(city)
	drawn_cities.add(city.name)

if __name__ == '__main__':
	vis.setup(cities)
	vis.draw_title('Kruscal Algorithm')
	main()
	vis.wait()