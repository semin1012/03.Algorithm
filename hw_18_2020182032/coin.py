from copy import deepcopy

coins = [16, 10, 5, 1] 	# 동전 세트
N = 20 	# 거스름 돈

INF = float('inf')
num_coins = [INF for _ in range(N+2)]
used_coins = [[] for _ in range(N+2)]

num_coins[0] = 0
# print(num_coins)

for j in range(1, N+1):
	used_coins[j] = []
	for i in range(len(coins)):
		if coins[i] <= j and num_coins[j - coins[i]] + 1 < num_coins[j]:
			num_coins[j] = num_coins[j - coins[i]] + 1
			used_coins[j] = deepcopy(used_coins[j - coins[i]])
			used_coins[j].append(coins[i])
			print(j, num_coins, used_coins[j])

print(num_coins)
print(used_coins[N])