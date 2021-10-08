from unsorted import numbers
# from sorted import numbers
from random import randint

def pratition(arr, left, right):
	pi = randint(left, right)
	if pi != left:
		arr[pi], arr[left] = arr[left], arr[pi]

	p = left + 1
	q = right
	while True:
		while p < right and arr[p] < arr[left]:
			p += 1
		while q > left and arr[q] > arr[left]:
			q -= 1
		if p <= q:
			break
		arr[p], arr[q] = arr[q], arr[p]
		p += 1
		q -= 1

	arr[left], arr[q] = arr[q], arr[left]
	return q

def selection(arr, left, right, k):
	pivot = pratition(arr, left, right)
	sgs = pivot - left # 스몰그룹 사이즈
	if k < sgs:
		return selection(arr, left, pivot-1, k)
	elif k == sgs:
		return arr[sgs]
	else: # pivot < k
		return selection(arr, pivot+1, right, k-sgs-1)

sublist = numbers[:10]
print(sorted(sublist))
k = 6 # 1-based
value = selection(sublist, 0, len(sublist)-1, k - 1)
print("{:2}번째 작은 수는 {:2} 이다.".format(k, value))
