# Merge Sort #1
from unsorted import numbers

sublist = numbers[:300000]

def mergeSort(list):
	size = len(list)
	if size <= 1: return list

	mid = size // 2
	left = mergeSort(list[:mid])
	right = mergeSort(list[mid:])
	merged = merge(left, right)
	# print(merged)
	return merged

def merge(list1, list2):
	merged = []
	while len(list1) > 0 and len(list2) > 0:
		if list1[0] <= list2[0]:
			merged.append(list1.pop(0))
		else:
			merged.append(list2.pop(0))
	if len(list1) > 0:
		merged += list1
	if len(list2) > 0:
		merged += list2
	return merged

#print(sublist)
sorted = mergeSort(sublist)
#print(sorted)