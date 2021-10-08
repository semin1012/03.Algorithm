# Quick Sort #2
from random import randint
from sorted import numbers

sublist = numbers[:300000]

def quickSort(list, left, right): # right = inclusive
	if left >= right: return
	pivot = partition(list, left, right)
	quickSort(list, left, pivot-1)
	quickSort(list, pivot+1, right)

def partition(list, left, right):
	v1 = list[left]
	v2 = list[(left + right) // 2]
	v3 = list[right]

	pi = left
	if v1 <= v2 and v2 <= v3:
		pi = (left+right) // 2
	elif v1 <= v3 and v3 <= v1:
		pi = right 

	# pi = left # randint(left, right)
	pivot = list[pi]
	# print(v1, v2, v3, left, right, pi, pivot)

	list[left], list[pi] = list[pi], list[left]

	p, q = left + 1, right
	while p < q:
		while p < right and list[p] <= pivot:
			p += 1
		while left < q and list[q] >= pivot:
			q -= 1
		if p < q:
			list[p], list[q] = list[q], list[p]
			p += 1
			q -= 1
	list[left], list[q] = list[q], list[left]
	# print(q, list)
	return q

# print(sublist)
quickSort(sublist, 0, len(sublist) - 1)
# print(sublist)