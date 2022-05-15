import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N-1)]
q = deque([1])
result = [0] * (N+1)
result[1] = 1
dic = {}
for i in range(1, N+1):
    dic[i] = []
for j in range(N-1):
    a, b = arr[j][0], arr[j][1]
    dic[a].append(b)
    dic[b].append(a)
while q:
    now = q.popleft()
    for k in dic[now]:
        if result[k] == 0:
            result[k] = now
            q.append(k)
for l in range(2, N+1):
    print(result[l])