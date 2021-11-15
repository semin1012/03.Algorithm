INF = float('inf')

D = [
	[0, 4, 2, 5, INF],
	[INF, 0, 1, INF, 4],
	[1, 3, 0, 1, 2],
	[-2, INF, INF, 0, 2],
	[INF, -3, 3, 1, 0]
]

N = len(D)

pred = [[-1 for _ in range(N)] for _ in range(N)]
# print(pred)
# exit(1)


def print_dist():
	global D, N
	print('-' * 50)
	for i in range(N):
		for j in range(N):
			print('%5s' % str(D[i][j]), end='')
		print('\t|\t', end='')
		for j in range(N):
			if pred[i][j] >= 0:
				print('%5d' % pred[i][j], end='')
			else:
				print(' ' * 5, end='')
		print()

print_dist()

for k in range(N):
	for i in range(N):
		for j in range(N):
			via = D[i][k] + D[k][j]
			if D[i][j] > via:
				D[i][j] = via
				pred[i][j] = k
				print_dist()