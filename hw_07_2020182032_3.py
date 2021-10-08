# Merge Sort #2
from unsorted import numbers

sublist = numbers[:300000]

def mergeSort(list, p, q): # q=inclusive
	if p >= q: return
	mid = (p + q) // 2
	mergeSort(list, p, mid)
	mergeSort(list, mid + 1, q)
	merge(list, p, mid + 1, q)

def merge(list, left, right, end):
	merged = []
	l, r = left, right
	while l < right and r <= end:
		if list[l] <= list[r]:
			merged.append(list[l])
			l += 1
		else:
			merged.append(list[r])
			r += 1
	while l < right:
		merged.append(list[l])
		l += 1
	while r <= end:
		merged.append(list[r])
		r += 1

	l = left
	for n in merged:
		list[l] = n
		l += 1

# print(sublist)
mergeSort(sublist, 0, len(sublist) - 1)
# print(sublist)