# Selection Sort
import unsorted

list = unsorted.numbers[:15000]

for a in range(len(list)):
	min = list[a]
	at = a
	for b in range(a + 1, len(list)):
		if min > list[b]:
			min = list[b]
			at = b
	list[a], list[at] = list[at], list[a]

# print(list)
