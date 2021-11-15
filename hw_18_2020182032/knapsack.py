from copy import deepcopy

W = [0, 5, 4, 6, 3]
V = [0, 10, 40, 30, 50]

N = len(W)

capacity = 10

K = [[0 for _ in range(capacity + 1)] for _ in range(N)]
P = [[[] for _ in range(capacity + 1)] for _ in range(N)]

# print(K)
print(P)

for i in range(1, N):
	for w in range(1, capacity + 1):
		if W[i] > w:
			K[i][w] = K[i-1][w]
			P[i][w] = P[i-1][w][:]
		else:
			if K[i-1][w] > K[i-1][w-W[i]] + V[i]:
				K[i][w] = K[i-1][w]
				P[i][w] = deepcopy(P[i-1][w])
			else:
				K[i][w] = max(K[i-1][w], K[i-1][w-W[i]] + V[i])
				P[i][w] = deepcopy(P[i-1][w - W[i]])
				P[i][w].append(i)
		print('i=', i, 'w=', w, 'K=', K[i], 'P[i][w]=', P[i][w])
		# print(P)

print(K[N-1][capacity])
print(P[N-1][capacity])