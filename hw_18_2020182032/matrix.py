d = [10, 20, 5, 15, 30] 	# 입력 행렬

N = len(d) - 1
INF = float('inf')

C = [[ 0 for _ in range(N+1)] for _ in range(N+1)]
P = [[ 0 for _ in range(N+1)] for _ in range(N+1)]
# print(C)

def print_mult(P, i, j):
	if i == j:
		print('A' + str(i), end='')
	else:
		print('(', end='')
		print_mult(P, i, P[i][j])
		print_mult(P, P[i][j] + 1, j)
		print(')', end='')

def print_mat():
	print('-' * 50)
	for i in range(1, N+1):
		for j in range(1, N+1):
			print('%6d' % C[i][j], end='')
		print('\t|\t', end='')
		for j in range(1, N+1):
			print('%6d' % P[i][j], end='')
		print()


for L in range(2, N+1):
	for i in range(1, N-L+2):
		j = i + L - 1
		C[i][j] = INF
		for k in range(i, j):
			temp = C[i][k] + C[k+1][j] + d[i-1] * d[k] * d[j]
			if temp < C[i][j]:
				C[i][j] = temp
				P[i][j] = k
			print_mat()

print_mat()
print(C[1][N])
print_mult(P, 1, N)
print()