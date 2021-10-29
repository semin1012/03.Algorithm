u = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
s = [
	{ 0, 1, 2, 7 },
	{ 0, 1, 2, 3, 7 },
	{0, 1, 2, 3},
	{1, 2, 3, 4, 6, 7},
	{3, 4, 5, 6},
	{4, 5, 6, 8, 9},
	{3, 4, 5, 6},
	{0, 1, 3, 7},
	{5, 8},
	{5, 9}
]

set_cover = []
while len(u) > 0:	# 커버 안 된 원소가 있는 동안
	# 가장 많은 원소를 커버하는 집합 인덱스 찾기
	max_cover_set = s.index(max(s, key=lambda x: len(u & x)))
	u = u - s[max_cover_set]		# 찾은 집합 원소 제거
	set_cover.append(max_cover_set)	# 찾은 집합 인덱스 저장
	s[max_cover_set] = { -1 }		# dummy 집합으로 교체

print('집합 커버를 위한 부분 집합 리스트:', set_cover)
