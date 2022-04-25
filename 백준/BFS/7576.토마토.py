import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
ans = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j, 0])
while q:
    y, x, cnt = q.popleft()
    directy = [0, 1, 0, -1]
    directx = [1, 0, -1, 0]
    if cnt > ans:
        ans = cnt
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] != 0:
                continue
            arr[dy][dx] = 1
            q.append([dy, dx, cnt+1])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans = -1
print(ans)