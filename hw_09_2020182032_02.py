import math
from city import cities

for i in range(len(cities)):
	cities[i].o = i

dist_call = 0

def distance(c1, c2, md = False):
	global dist_call
	dist_call += 1
	dx = c1.x - c2.x
	if dx < 0 : dx = -dx
	if md and dx > md : return dx
	dy = c1.y - c2.y
	if dy < 0: dy = -dy
	if md and dy > md : return dy
	return math.sqrt(dx ** 2 + dy ** 2)

def distance_sq(c1, c2):
	global dist_call
	dist_call += 1
	dx = c1.x - c2.x
	dy = c1.y - c2.y
	return (dx ** 2 + dy ** 2)

def brute_force(cities, left, right):
	min_dist = float('inf')	# 무한대
	min_c1 = 0
	min_c2 = 1
	# n_cities = len(cities)
	for a in range(left, right + 1):
		c1 = cities[a]
		for b in range(a + 1, right + 1):
			c2 = cities[b]
			dist = distance(c1, c2, min_dist)
			if min_dist > dist:
				min_c1 = a
				min_c2 = b
				min_dist = dist

	return min_c1, min_c2, min_dist


def closest_pair(arr, left, right):
	size = right - left + 1
	if size <= 1:
		return -1, -1, 0
	if size == 2:
		return left, right, distance(arr[left], arr[right])
	if size == 3:
		return brute_force(arr, left, right)

	mid = size // 2 + left - 1 	# 왼쪽 그룹의 맨 오른쪽 점이므로 1을 뺀다

	ls, le, ld = closest_pair(arr, left, mid)
	rs, re, rd = closest_pair(arr, mid + 1, right)

	s, e, d = (ls, le, ld) if ld <= rd else (rs, re, rd)
	cx1 = arr[mid].x - d
	cx2 = arr[mid].x + d

	# mid_area = [c for c in arr if c.x >= cx1 and c.x <= cx2]
	# mid_area.sort()

	index1 = min(c.index for c in x_aligned if c.x >= cx1 )
	index2 = max(c.index for c in x_aligned if c.x <= cx2 )

	strip = [ c for c in y_aligned if c.index >= index1 and c.index <= index2 ]
	# O(n) search

	global dist_call

	n_strip = len(strip)
	for s1 in range(n_strip):
		c1 = strip[s1]
		for s2 in range(s1 + 1, n_strip):
			c2 = strip[s2]
			dy = c1.y - c2.y
			if dy < 0: dy = -dy
			if dy > d: break
			dx = c1.x - c2.x
			if dx > d: continue
			dist_call += 1
			dist = math.sqrt(dx**2 + dy**2)
			if d > dist:
				d = dist
				s, e = c1.index, c2.index

	return s, e, d
	# min_d = min(ld, rd)

	# 중간 단계도 확인


cities = cities[:20] # cities[:100]
x_aligned = sorted(cities, key=lambda c:c.x)
for i in range(len(x_aligned)):
	x_aligned[i].index = i
y_aligned = sorted(cities, key=lambda c:c.y)

(s, e, dist) = closest_pair(x_aligned, 0, len(x_aligned) - 1)
# s, e, dist = brute_force(cities, 0, len(cities) - 1)

print('Closest: ', 'dist=', dist, ' dist_call:', dist_call)
if s >= 0:
	print(cities[s])
	print(cities[e])
else:
	print('No pair found')