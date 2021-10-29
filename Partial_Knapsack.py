N = 4
CAPACITY = 40
weight = [10, 15, 25, 50]	# 각 항목의 무게
unit_value = [60, 50, 4, 1]	# 이미 단위 무게 당 가치(천원)로 정렬됨
# item 0 = 백금, item 1 = 금, item 2 = 은, item 3 = 주석

value = 0 	# 배낭에 담긴 항목들의 가치의 합
weight_sum = 0 	# 배낭에 담긴 항목들의 무게의 합
item = 0
while CAPACITY >= weight_sum + weight[item]:
	weight_sum += weight[item]
	value += (weight[item] * unit_value[item])
	item += 1

partial = CAPACITY - weight_sum	# 배낭에 부분적으로 담을 수 있는 무게
if partial > 0:
	value += (partial * unit_value[item])

print('배낭에 담은 항목의 가치는 %d 만원이다.' % (value // 10))
print('배낭에 담긴 항목 리스트:', end=' [')
for j in range(item):
	print('항목 %d' % j, end=' ')
if partial > 0:
	print(']\n단, 항목 %d는 %dg만 배낭에 담겼음' % (item, partial))
