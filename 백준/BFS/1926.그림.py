import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        q = deque()
        cnt = 1
        if arr[i][j] == 1:
            q.append([i,j])
            visit[i][j] = 1
            while q:
                y, x = q.popleft()
                directy = [0, 1, 0, -1]
                directx = [1, 0, -1, 0]
                for k in range(4):
                    dy = y + directy[k]
                    dx = x + directx[k]
                    if 0 <= dy < n and 0 <= dx < m:
                        if visit[dy][dx] == 1:
                            continue
                        if arr[dy][dx] != 0:
                            visit[dy][dx] = 1
                            cnt += 1
                            arr[dy][dx] = cnt
                            q.append([dy, dx])

max_ans = 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans += 1
        if arr[i][j] > max_ans:
            max_ans = arr[i][j]
print(ans)
print(max_ans)
