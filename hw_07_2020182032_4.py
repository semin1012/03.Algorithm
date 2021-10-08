# Quick Sort #1
from unsorted import numbers

sublist = numbers[:300000]

def quickSort(list, left, right): # right = inclusive
	if left >= right:
		return
	pivot = partition(list, left, right)
	quickSort(list, left, pivot-1)
	quickSort(list, pivot+1, right)

def partition(list, left, right):
	pi = left
	pivot = list[pi]

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