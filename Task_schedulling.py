job = [[0, 2], [1, 6], [1, 5], [3, 7], [5, 9], [6, 8], [7,8]]
m = [[0]]
for i in range(len(job)):
	j = 0
	allocated = False
	while not allocated and j < len(m):
		if job[i][0] >= m[j][0]:
			m[j].append(i)
			m[j][0] = job[i][1]
			allocated = True
		j+=1
	if not allocated:
		m.append([0])
		m[j].append(i)
		m[j][0] = job[i][1]

last_job = max(job, key=lambda arr: arr[1])
print('모든 작업의 최종 종료 시간 = %d ' % last_job[1])

for k in range(len(m)):
	print('기계 %d:' % k, end='')
	for i in range(1, len(m[k])):
		print(' 작업 %d ' % m[k][i], job[m[k][i]], ' ', end='')
	print()
